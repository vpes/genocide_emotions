import cv2
from emotion_processing.em_model import EMR

# initialize the cascade
cascade_classifier = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_default.xml')
# Initialize object of EMR class
network = EMR()
network.build_network()


def format_image(image):
    """
    Function to format frame
    """
    if len(image.shape) > 2 and image.shape[2] == 3:
        # determine whether the image is color
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        # Image read from buffer
        image = cv2.imdecode(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)

    faces = cascade_classifier.detectMultiScale(image,scaleFactor = 1.3 ,minNeighbors = 5)

    if not len(faces) > 0:
        return None

    # initialize the first face as having maximum area, then find the one with max_area
    max_area_face = faces[0]
    for face in faces:
        if face[2] * face[3] > max_area_face[2] * max_area_face[3]:
            max_area_face = face
    face = max_area_face

    # extract ROI of face
    image = image[face[1]:(face[1] + face[2]), face[0]:(face[0] + face[3])]

    try:
        # resize the image so that it can be passed to the neural network
        image = cv2.resize(image, (48,48), interpolation = cv2.INTER_CUBIC) / 255.
    except Exception:
        print("----->Problem during resize")
        return None

    return image

EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']

def find_face(frame):
    facecasc = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray, 1.3, 5)
    # compute softmax probabilities
    result = network.predict(format_image(frame))
    return result,faces

def process_file(file):
    img = cv2.imread(file, cv2.IMREAD_COLOR)
    result, faces = find_face(img)
    if len(faces) > 0:
        emotions = {}
        for index, emotion in enumerate(EMOTIONS):
            emotions[emotion] = result[0][index] * 100.0
        max_area_face = faces[0]
        for face in faces:
            if face[2] * face[3] > max_area_face[2] * max_area_face[3]:
                max_area_face = face
        face = max_area_face
        return face, emotions
    return None,None