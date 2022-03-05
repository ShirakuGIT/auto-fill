from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

option.binary_location = "/usr/bin/brave-browser"


browser = webdriver.Chrome(executable_path='/home/shiraku/chromedriver', options=option)

browser.get("https://forms.gle/DYfTu4urf7RPAuM17")


radiobox = option.find_elements(by="docssharedWizToggleLabeledContainer ajBQVb")

#print(radiobox)