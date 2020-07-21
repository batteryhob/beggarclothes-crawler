
import time
from libs.driverGetter import getDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#config 가져오기
#config.read('/app/config.ini', encoding='utf-8')
#config['NAVER']['ID']
#config['NAVER']['PW']

# 테스트 용
# TEST_URL = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'
# driver = getDriver()
# driver.get(TEST_URL)
# pageString = driver.page_source
# print(pageString)
# driver.quit()

# 네이버 로그인
# driver = getDriver()
# loginUrl = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
# driver.get(loginUrl)
# time.sleep(5)

# 아이디 비번 입력 후 클릭
# WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "id"))).click()
# pyperclip.copy("")
# WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "id"))).send_keys(Keys.CONTROL, 'v')
# time.sleep(5)

# WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "pw"))).click()
# pyperclip.copy("")
# WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "pw"))).send_keys(Keys.CONTROL, 'v')
# time.sleep(5)

# WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "log.login"))).click()

# 카페 검색 결과
targetCafe = "https://cafe.naver.com/dieselmania"

driver = getDriver()
driver.get(targetCafe)

# 카페 검색어
targetDesigner = "마르지엘라"

WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'topLayerQueryInput'))).send_keys(targetDesigner)
time.sleep(5)
WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cafe-search"]/form/button'))).click()
time.sleep(5)

driver.switch_to_frame('cafe_main')
main = driver.find_element_by_id('main-area')
print(main.text)