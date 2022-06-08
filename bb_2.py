from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl

driver = webdriver.Chrome()
driver.get("https://www.bigbasket.com/pc/beauty-hygiene/health-medicine/ayurveda")
driver.maximize_window()

time.sleep(3)  

product_name = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[1]/a ')
product_mrp = driver.find_elements(by=By.XPATH, value='/html/body/div[1]/div[3]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[1]/h4/span[2]')
product_d_mrp = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[1]/h4/span[1]')
product_delivery = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[4]/div[3]/div/div[3]/span/div/p/span[2]')
discount_percent = driver.find_elements(by=By.XPATH, value='//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div/product-template/div/div[2]/div[2]/div/div')
product_is_veg = driver.find_elements(by=By.XPATH, value="//*[@id='dynamicDirective']/product-deck/section/div[2]/div[4]/div[1]/div/div/div[2]/div/div[1]/product-template/div/div[3]/span")

time.sleep(3)

name, mrp, d_mrp, delivery, percent, is_veg = [],[],[],[],[],[]

for a in product_name:
    name.append(a.text)
time.sleep(2)
for b in product_mrp:
    mrp.append(b.text)
time.sleep(2)   
for c in product_d_mrp:
    d_mrp.append(c.text)
time.sleep(2)
for d in product_delivery:
    delivery.append(d.text)
time.sleep(2)
for e in discount_percent:
    percent.append(e.text)
time.sleep(2)
for f in product_is_veg:
    is_veg.append(e.text)
time.sleep(3)

final_sheet = zip(name, mrp, d_mrp, delivery, percent, is_veg)

#print(final_sheet)

wb = openpyxl.Workbook()
sheet = wb.active
for i in list(final_sheet):
    sheet.append(i)
    wb.save("Ayurved_Data.csv")

driver.quit()


'''
//span[@class="discnt-price"]
//span[@class="mp-price ng-scope"]
//span[@class="veg-icon ng-scope"]
'''
