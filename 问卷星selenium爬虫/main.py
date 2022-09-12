from concurrent.futures.thread import ThreadPoolExecutor
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


option = Options()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)

# # 设置无头浏览器
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# # 滑块防止检测
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# driver_path = 'C:\Program Files\Google\Chrome\Application\chromedriver'
# driver_path = ''
head = '(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))'
# proxy_list = proxy_util.update_proxy()

# 每个问题选项（-1表示该题为简答题）
option_nums = [3, 4, 4, 4, 3, 3, 4, 1, 3, 4]  # 10
# 0表示单选，1表示多选
multiple_choice = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


    # 打开问卷星网址
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Edge()
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
driver.get('https://ks.wjx.top/vm/e04tGAQ.aspx')


    # driver.maximize_window()
    # 每个问题的选项
    
text_input = driver.find_element(By.XPATH, f'//*[@id="q1"]')
text_input.clear()
text = "陈波"
text_input.send_keys(text)

q_select = driver.find_element(By.XPATH, f'//*[@id="div2"]/div[2]/div[1]')
q_select.click()
# //*[@id="div2"]
# //*[@id="div2"]/div[2]/div[1]

for i in range(2, 12):
        # 单选题
    q_select = driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[2]/div[{option_nums[i-2]}]')
    q_select.click()
    time.sleep(0.1)

    # 多选题
q_select = driver.find_element(By.XPATH, f'//*[@id="div13"]/div[2]/div[{2}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div13"]/div[2]/div[{4}]')
q_select.click()

# //*[@id="div13"]/div[2]/div[1]
q_select = driver.find_element(By.XPATH, f'//*[@id="div14"]/div[2]/div[{2}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div14"]/div[2]/div[{4}]')
q_select.click()

q_select = driver.find_element(By.XPATH, f'//*[@id="div15"]/div[2]/div[{2}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div15"]/div[2]/div[{3}]')
q_select.click()

q_select = driver.find_element(By.XPATH, f'//*[@id="div16"]/div[2]/div[{2}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div16"]/div[2]/div[{4}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div17"]/div[2]/div[{3}]')
q_select.click()

q_select = driver.find_element(By.XPATH, f'//*[@id="div17"]/div[2]/div[{4}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div18"]/div[2]/div[{1}]')
q_select.click()

q_select = driver.find_element(By.XPATH, f'//*[@id="div18"]/div[2]/div[{3}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div18"]/div[2]/div[{4}]')
q_select.click()

q_select = driver.find_element(By.XPATH, f'//*[@id="div19"]/div[2]/div[{1}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div19"]/div[2]/div[{4}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div20"]/div[2]/div[{2}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div20"]/div[2]/div[{3}]')
q_select.click()

q_select = driver.find_element(By.XPATH, f'//*[@id="div21"]/div[2]/div[{1}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div21"]/div[2]/div[{2}]')
q_select.click()

q_select = driver.find_element(By.XPATH, f'//*[@id="div22"]/div[2]/div[{1}]')
q_select.click()
q_select = driver.find_element(By.XPATH, f'//*[@id="div22"]/div[2]/div[{3}]')
q_select.click()

submit_button = driver.find_element(By.XPATH, '//*[@id="ctlNext"]')
submit_button.click()
time.sleep(10)
# confirm = driver.find_element(By.XPATH, '//*[@id="alert_box"]/div[2]/div[2]/button')
# confirm.click()
# validation = driver.find_element(By.XPATH, '//*[@id="rectMask"]')
# validation.click()
# time.sleep(2.5)

# res = driver.find_element(By.XPATH, '//*[@id="SM_TXT_1"]')

# # 滑块验证
# try:
#     slider = driver.find_element(By.XPATH, '//*[@id="nc_1__scale_text"]/span')

#     print('[' + eval(head) + f']: ', slider.text, cnt)
#     if str(slider.text).startswith("请按住滑块"):
#         width = slider.size.get('width')
#         ActionChains(driver).drag_and_drop_by_offset(slider, width, 0).perform()

# except selenium.common.exceptions.NoSuchElementException:
#     pass

# time.sleep(1)
# print('[' + eval(head) + f']: ', res.text, cnt)
# driver.close()


# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(max_workers=1)
#     current_time = int(time.time())
#     last_time = current_time
#     for i in range(1000000):
#         pool.submit(solve, i+1)

#         current_time = int(time.time())
#         gap = current_time - last_time
#         # 8分钟更新一次代理
#         if gap >= 480:
#             proxy_list = proxy_util.update_proxy()
#             print('[' + eval(head) + ']: 更新代理列表')
#             last_time = current_time

