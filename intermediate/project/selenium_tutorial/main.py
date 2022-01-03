import time

from selenium import webdriver
import requests
from decouple import config


# 웹드라이버 생성
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)


# https://www.instagram.com/seokj1012/ 접속
time.sleep(1)
driver.get('https://www.instagram.com/seokj1012/')


# 로그인 버튼 클릭
time.sleep(1.5)
driver.find_element_by_class_name('ENC4C').click()
# ID 입력
time.sleep(1.5)
driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input').send_keys(config('USER_ID'))
# 비밀번호 입력
time.sleep(1.5)
driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input').send_keys(config('USER_PW'))
# 로그인
time.sleep(1.5)
driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3)').click()
# 웹브라우저에 로그인 정보 저장 안하기
time.sleep(1.5)
driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button').click()

# 웹 페이지 가장 밑으로 스크롤
# scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight 까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # scrollHeight 비교
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
time.sleep(1.5)


# 이미지 다운로드
n = 1
for elt in driver.find_elements_by_class_name('FFVAD'):
    # 'style'이라는 속성에서 이미지 url (이미지 주소) 추출
    img_url = elt.get_attribute('src')
    # 이미지 저장할 경로 정의
    img_path = f'./my_images/{n}.jpg'
    # requests 패키지 써서 이미지 다운로드
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(img_path, 'wb+') as f:
            f.write(response.content)
    n += 1

# 게시글은 52개인데 사진 다운은 31개
# 위에 게시글 사진이 다운로드 안됨
# 해결 방법 찾아야 함