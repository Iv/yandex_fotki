#!/bin/python
import requests
from pelican import signals, logger

API_URL = 'https://api-fotki.yandex.ru'
ACCEPT = 'application/json'


def build_album_url(user, album, url=API_URL):
    return "%s/api/users/%s/album/%s/" % (url, user, album)


def build_album_photos_url(user, album, url=API_URL):
    return "%s/api/users/%s/album/%s/photos/manual/" % (url, user, album)


def get_photos(user, album):
    headers = dict(accept=ACCEPT)
    response = requests.get(build_album_photos_url(user, album), headers=headers)
    j = response.json()
    return j.get('entries', [])


def get_album(user, album):
    headers = dict(accept=ACCEPT)
    response = requests.get(build_album_url(user, album), headers=headers)
    j = response.json()
    return j


def get_cover(user, album):
    a = get_album(user, album)
    cover_url = a['links']['cover']
    headers = dict(accept=ACCEPT)
    response = requests.get(cover_url, headers=headers)
    cover = response.json()
    cover['album_title'] = a['title']
    return cover


def choose_large_image(image):
    for size in ['XXXL', 'XXL', 'XL', 'L', 'M', 'S']:
        if size in image['img']:
            image['img']['large'] = image['img'][size]
            break
    return image


def add_gallery_post(generator):
    USER = generator.settings.get('YANDEX_FOTKI_USER')
    for article in generator.articles:
        if 'yandex_gallery' in article.metadata.keys():
            album = article.metadata.get('yandex_gallery')

            article.yandex_album = album
            article.album = album
            article.galleryimages = map(choose_large_image, get_photos(USER, album))
            article.cover = choose_large_image(get_cover(USER, album))

def add_gallery_page(generator):
    USER = generator.settings.get('YANDEX_FOTKI_USER')
    for page in generator.pages:
        if 'yandex_gallery' in page.metadata.keys():
            album = page.metadata.get('yandex_gallery')

            page.yandex_album = album
            page.album = album
            page.galleryimages = map(choose_large_image, get_photos(USER, album))
            page.cover = choose_large_image(get_cover(USER, album))


def register():
    signals.article_generator_finalized.connect(add_gallery_post)
    signals.page_generator_finalized.connect(add_gallery_page)
