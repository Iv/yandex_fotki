Yandex-Fotki
============


Pelican plugin to use [fotki.yandex.ru](https://fotki.yandex.ru/) as fast photo gallery CDN for free.

It is proof of concept but works well for me.

The plugin gets images through JSON API and put lists to article object.
Sample templates are in **/tmplates/includes/** folder.

fotki.yandex.ru api description [here](https://tech.yandex.ru/fotki/).



### HOWTO use


 1. Add to plugins: PLUGINS = […, 'yandex_fotki', …]
 2. Add **YANDEX_FOTKI_USER** settings to the pelicanconf.py  
    ```
    YANDEX_FOTKI_USER = 'sky7club'
    ```
 3. Change templates to use **article.galleryimages** list and cover image **article.cover** dict.
 4. Add metadata to article:    
    ```
    yandex_gallery: 532270
    ```

    where 532270 is gallery id.



### Example

Works here [sky7club.ru](https://sky7club.ru/annonce/invintation-chegem-2017-05.html)


Sample HTML:
```html

<p class="galleria">
        <span itemscope itemtype="http://schema.org/ImageObject">
        <a class="531011 cboxElement"
               href="https://img-fotki.yandex.ru/get/52656/429009185.11/0_1ebfb6_b848e55_XXXL"
               title="Параплан ASA Тайран 5, Чегем" itemprop="contentUrl"
               ><img src="https://img-fotki.yandex.ru/get/52656/429009185.11/0_1ebfb6_b848e55_L" alt="Параплан ASA Тайран 5, Чегем"></a>
        <meta itemprop="caption" content="Параплан ASA Тайран 5, Чегем">
        </span>
        <span itemscope itemtype="http://schema.org/ImageObject">
        <a class="531011 cboxElement"
               href="https://img-fotki.yandex.ru/get/197923/429009185.11/0_1ebfb4_31e386af_XXXL"
               title="Парадром Чегем, вид на Прирамиду" itemprop="contentUrl"
               ><img src="https://img-fotki.yandex.ru/get/197923/429009185.11/0_1ebfb4_31e386af_L" alt="Парадром Чегем, вид на Прирамиду"></a>
        <meta itemprop="caption" content="Парадром Чегем, вид на Прирамиду">
        </span>
</p>
```