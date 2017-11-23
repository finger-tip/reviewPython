from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
browser = webdriver.Chrome()
#设置等待时间，因为可能要经常使用，就赋值变量
wait = WebDriverWait(browser,10)
def search():
    #可能会因为网络的原因报时间等待的异常，使用t异常处理


    try:
        browser.get('https://www.suning.com')
        # 等待这么长时间在响应
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#searchKeywords'))
        )
        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#searchSubmit'))
        )
        input.send_keys('手机')
        submit.click()

        total = EC.presence_of_element_located((By.CSS_SELECTOR,'#bottom_pager > div > span.TV-page-move'))
        # print(total)
        # print(type(total))
        # return total.string
        return 50
    except TimeoutException:
        return search()
#进入下一页，在输入框中输入数字进入
def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#bottomPage'))
        )
        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#bottom_pager > div > a.page-more.ensure'))
        )
        input.clear()
        input.send_keys(page_number)
        # browser.get(url) 使用get能够通过a标签进入下个页面
        submit.get('https://search.suning.com/emall/searchProductList.do?keyword=%E6%89%8B%E6%9C%BA&ci=20006&pg=01&cp=7&il=0&st=0&iy=0&adNumber=4&isDoufu=1&n=1&sesab=ABA&id=IDENTIFYING&cc=010&h=h')
        #判定选择器中的内容和传的内容是否相同
        #获取元素中的文字
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#bottom_pager > div > a.cur',str(page_number))))
    except TimeoutException:
        next_page(page_number)

def main():
    total = search()
    #如果能够成功返回文本的话，就使用正则将里面是数字提取出来
    print(total)

    for i in range(2,total+1):
        next_page(i)

if __name__ == '__main__':
    main()

