from selenium import webdriver

with open("sample.txt","r") as reader:
    content=reader.readlines()
    with open("sample.txt","w") as writer:
        for file in reversed(content):
            writer.writelines(file)


#assert
#try
#Except
driver=webdriver.Chrome(executable_path="F:\Crome\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
driver.close()