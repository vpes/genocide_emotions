import datetime
import cv2
import os
from urllib.parse import quote_plus
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from django.db import transaction
from emotions_website1.models import VisitorQuery, VisitorQueryResult
from emotion_processing.process_emotion_singleface import process_file
import requests


@transaction.atomic
def do_process_query(query_id):
    vq = VisitorQuery.objects.get(pk=query_id)
    items = search_keywords(vq.keywords)
    index = 1
    max_proximity = 0.0
    for item in items:
        try:
            if index > 10:
                break
            original_path = download_image(query_id,item.get('media'))
            face, emotions = process_image(original_path)
            proximity = 1.0
            if proximity > max_proximity:
                max_proximity = proximity
            VisitorQueryResult.objects.create(query=vq,
                                               title=item.get('title'),
                                                url=item.get('url'),
                                                media_url=item.get('media'),
                                                image_path=original_path,
                                                face_rect=str(face),
                                                emotions=emotions,
                                                proximity = proximity)
            index += 1
        except Exception as ex:
            print(ex)
    vq.processed = datetime.datetime.now()
    vq.result_count = index
    vq.max_proximity = max_proximity
    vq.save()

def search_keywords(query):
    r = requests.get("https://api.qwant.com/api/search/images",
                     params={
                         'count': 30,
                         'q': quote_plus(query),
                         't': 'images',
                         'safesearch': 1,
                         'locale': 'en_US',
                         'uiv': 4
                     },
                     headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                     }
                     )

    return r.json().get('data').get('result').get('items')

def download_image(query_id,url):
    r = requests.get(url)
    if r.status_code == 200:
        return save_file(query_id,url.split('/')[-1], r.content)
    else:
        raise Exception('Request error {}: {}'.format(r.status_code,r.reason))


def save_file(folder,name,bytes):
    dir = os.path.join('static','files',str(folder))
    if not os.path.isdir(dir):
        os.makedirs(dir)
    file_name=os.path.join(dir,name)
    with open(file_name, 'wb') as f:
        f.write(bytes)
    return file_name

def get_emotion_text(value):
    return {'angry': 'enojo', 'disgusted': 'disgusto', 'fearful': 'temor',
         'happy': 'felicidad', 'sad': 'tristeza', 'surprised': 'sorpresa',
         'neutral': 'neutro'}.get(value,value)

def draw_values(img, face, d):
    (x, y, w, h) = face
    pimg = Image.fromarray(img).convert("RGBA")
    values_rect = (x + w + 380,y + h + 10)
    if (pimg.size[0] < values_rect[0]) or (pimg.size[1] <  values_rect[1]):
        new_im = Image.new("RGBA", (max(pimg.size[0], values_rect[0]), max(pimg.size[1], values_rect[1])))
        new_im.paste(pimg, (0, 0))
        pimg = new_im
    tmp = Image.new('RGBA', pimg.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(tmp)
    draw.rectangle(((x, y), (x + w, y + h + 10)), outline=(0, 255, 255, 180))
    draw.rectangle(((x + w + 20, y), (x + w + 380, y + h + 10)), fill=(0, 0, 0, 127))
    txt_height = min(int((h -10)/len(d)),30)
    font_size = int(txt_height*2/3)
    font = ImageFont.truetype("arial",font_size)
    y_start = y
    x_start = x + w + 30
    index = 0
    for k, v in d.items():
        draw.text((x_start, index * txt_height + 22 + y_start), get_emotion_text(k).upper(),font=font,fill=(0, 255, 255, 200))
        draw.rectangle(((x_start + 130, index * txt_height + 20 + y_start),
                      (x_start + 130 + (int(v)*2), index * txt_height + 20 + font_size + y_start)),
                       fill=(0, 255, 255, 200))
        draw.text((x_start + 140 + (int(v)*2), index * txt_height + 22 + y_start), '{:.2f}%'.format(v),font=font,fill=(0, 255, 255, 200))
        index += 1
    pimg = Image.alpha_composite(pimg, tmp)
    img = np.asarray(pimg)
    return img

def process_image(path):
    face, emotions = process_file(path)
    if face is None:
        os.remove(path)
        raise Exception('No face found error : {}'.format(path))
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = draw_values(img, face, emotions)
    cv2.imwrite(path, img)

    return face, emotions