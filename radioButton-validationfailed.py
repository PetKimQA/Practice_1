from selenium import webdriver

driver = webdriver.Chrome("C:/Users/PetruKim/Desktop/Automation/chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

#locators
maleRadioIndv = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input')
femaleRadioIndv = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[2]/input')
maleRadioGrp = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[1]/input')
femaleRadioGrp = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[2]/input')
ageGrp1 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[1]/input')
ageGrp2 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[2]/input')
ageGrp3 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[3]/input')
getCheckedButton = driver.find_element_by_xpath('//*[@id="buttoncheck"]')
getValueButton = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button')
getCheckedText = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]')
getValueText = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]')

#text expected result
maleIndvExpTxt = "Radio button 'Male' is checked"
femaleIndvExpTxt = "Radio button 'female' is checked"
maleGrpExpTxt1 = "Sex : Male" + "\n" + "Age group: 0 - 5"
maleGrpExpTxt2 = "Sex : Male" + "\n" + "Age group: 5 - 15"
maleGrpExpTxt3 = "Sex : Male" + "\n" + "Age group: 15 - 50"
femaleGrpExpTxt1 = "Sex : Female" + "\n" + "Age group: 0 - 5"
femaleGrpExpTxt2 = "Sex : Female" + "\n" + "Age group: 5 - 15"
femaleGrpExpTxt3 = "Sex : Female" + "\n" + "Age group: 15 - 50"
#age05Txt = "Age group: 0 - 5"
#age515Txt = "Age group: 5 - 15"
#age1550Txt = "Age group: 15 - 50"
expectedResultArry = [maleIndvExpTxt,
                      femaleIndvExpTxt,
                      maleGrpExpTxt1,
                      maleGrpExpTxt2,
                      maleGrpExpTxt3,
                      femaleGrpExpTxt1,
                      femaleGrpExpTxt2,
                      femaleGrpExpTxt3]

#default verification
driver.implicitly_wait(3)
if maleRadioIndv.is_selected() or femaleRadioIndv.is_selected() or maleRadioGrp.is_selected() or femaleRadioGrp.is_selected() or ageGrp1.is_selected() or ageGrp2.is_selected() or ageGrp3.is_selected():
    print("Default status failed")

#individual check
maleRadioIndv.click()
getCheckedButton.click()
#print(getCheckedText.text)
maleIndvAcText = getCheckedText.text

femaleRadioIndv.click()
getCheckedButton.click()
#print(getCheckedText.text)
femaleIndvAcText = getCheckedText.text

#Group check
a = [ageGrp1, ageGrp2, ageGrp3]
maleRadioGrp.click()
maleRadioGrpAcText = []
femaleRadioGrpAcText = []
for i in a:
    i.click()
    getValueButton.click()
    #print(getValueText.text)
    maleRadioGrpAcText.append(getValueText.text)

femaleRadioGrp.click()
for i in a:
    i.click()
    getValueButton.click()
    #print(getValueText.text)
    femaleRadioGrpAcText.append(getValueText.text)

#Better way must be for Array in array(GrpAcText)
testActualResult = [maleIndvAcText,
                    femaleIndvAcText,
                    maleRadioGrpAcText[0],
                    maleRadioGrpAcText[1],
                    maleRadioGrpAcText[2],
                    femaleRadioGrpAcText[0],
                    femaleRadioGrpAcText[1],
                    femaleRadioGrpAcText[2]]

print(testActualResult)
print(expectedResultArry)

#Validation failed!!!!!!!!!!!
i = 0
while i <= len(testActualResult):
    if testActualResult[i] == expectedResultArry[i]:
        i = i + 1
        print("Pass")
    else:
        print("Fail")


#if numpy.array_equal(expectedResultArry, testActualResult):
 #   print("All variations are verified- Test Pass")
#else:
 #   print("Test failed")
driver.quit()

