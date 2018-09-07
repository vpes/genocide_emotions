import sys
import os
from django.db import models
import geoip2.database
import requests
import random
import jsonfield

geoip_reader = geoip2.database.Reader(os.path.join(sys.path[0],'data','GeoLite2-City','GeoLite2-City.mmdb'))
class Country(models.Model):
    name = models.CharField('Name', max_length=80,db_index=True,unique=True)
    alpha2 = models.CharField('Alpha-2', max_length=2,db_index=True,unique=True)
    code = models.CharField('Country Code', max_length=3,db_index=True,unique=True)
    region = models.CharField('Region', max_length=50,db_index=True,null=True)
    subregion = models.CharField('Sub Region', max_length=80,db_index=True,null=True)
    intermregion = models.CharField('Intermediate Region', max_length=80,db_index=True,null=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __unicode__(self):
        return self.name

class VisitorQuery(models.Model):
    keywords = models.CharField(max_length=255,blank=False)
    created = models.DateTimeField(auto_now=True)
    name = models.CharField('Name', max_length=255,blank=False)
    ip = models.CharField('IP', max_length=15,null=True,blank=True)
    country = models.ForeignKey('Country',on_delete=models.SET_NULL,null=True)
    complete_region = models.TextField(max_length=1000,null=True)
    processed = models.DateTimeField(null=True)
    result_count = models.PositiveSmallIntegerField("Result Count",null=True)
    max_proximity = models.FloatField("MaxProximity",null=True)

    class Meta:
        verbose_name = 'VisitorQuery'
        verbose_name_plural = 'VisitorQueries'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.country_id is None:
            self.get_country_by_ip()
        super(VisitorQuery, self).save(force_insert,force_update,using,update_fields)

    def do_search(self):
        query = "toulouse pink city"

        r = requests.get("https://api.qwant.com/api/search/images",
                         params={
                             'count': 50,
                             'q': query,
                             't': 'images',
                             'safesearch': 1,
                             'locale': 'en_US'
                         },
                         headers={
                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                         }
                         )

        response = r.json().get('data').get('result').get('items')
        urls = [r.get('media') for r in response]
        print(random.choice(urls))

    def get_country_by_ip(self):
        try:
            geoip_record = geoip_reader.city(self.ip)
            self.country_id = Country.objects.filter(alpha2=geoip_record.country.iso_code).values_list('id',flat=True).first()
            self.complete_region = '{0}, {3}, lat {1}, lon {2}'.format(geoip_record.city.name or '',
                                                       geoip_record.location.latitude,
                                                       geoip_record.location.longitude,
                                                       geoip_record.country.name)

        except:
            print('Unknown location')


class VisitorQueryResult(models.Model):
    query = models.ForeignKey("VisitorQuery",on_delete=models.CASCADE)
    title = models.CharField("Title",max_length=255)
    url = models.CharField("url",max_length=512)
    media_url = models.CharField("Media url",max_length=512)
    image_path = models.CharField('Image', max_length=255)
    face_rect = models.CharField('Face', max_length=255)
    emotions = jsonfield.JSONField('Emotions')
    proximity = models.FloatField("Proximity",null=True)

    class Meta:
        verbose_name = 'Visitor Query Result'
        verbose_name_plural = 'Visitor Query Results'

