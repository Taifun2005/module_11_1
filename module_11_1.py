import requests
import pprint
from PIL import Image, ImageFilter
import time


response = requests.get("https://api.github.com/")
response_json = response.json()
# pprint.pprint(response_json)
print(response_json['public_gists_url'])
print('________')
print(response.headers)
print(response.request.headers)

user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get('https://api.github.com/', headers=user_agent)
print(response.request.headers)



# print('TEST')
dir_ = 'images/'
img = Image.open(dir_ + '3_400x300.jpg')
print(img.size)
print(img.mode)
print(img.format)
print(img.histogram)
# print(p1.info)
img.show()
time.sleep(2)
r_img = img.rotate(180)
r_img.save(dir_ + 'r_img.jpg')
r_img.show()
r_img.save(dir_ + 'r_img.jpg')
r_img.show()
time.sleep(4)
img1 = Image.open(dir_ + '1_400x300.jpg')
img1.show()
time.sleep(2)

blur_img = img1.filter(ImageFilter.BLUR)
blur_img.save(dir_ + 'blur_img.jpg')
blur_img.show()

time.sleep(4)
img2 = Image.open(dir_ + 'r_img.jpg')

blur_img = img2.filter(ImageFilter.CONTOUR)
blur_img.save(dir_ + 'CONTOUR_blur_img.jpg')
blur_img.show()






