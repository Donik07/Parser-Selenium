from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Lmarkt():
    def __init__(self, driver, name, id):
        self.driver = driver
        self.name = name
        self.id = id

    def parse(self):
        self.go_to_page()
        self.go_parse()

    def go_to_page(self):
        self.driver.get("http://www.lmarkt.com")
        search = self.driver.find_element_by_name("search")
        search.send_keys(self.name)
        search.send_keys(Keys.RETURN)
        slide_elems = self.driver.find_elements_by_class_name("prod_list_t")
        result = []

        for elem in slide_elems:
            result.append(elem.find_element_by_tag_name('a'))

        return result[self.id].click()

    def go_parse(self):
        price = self.driver.find_element_by_class_name("prod_price").text
        company = self.driver.find_element_by_class_name("prod_param_r").text
        print(price, company)

def main():
    driver = webdriver.Chrome()
    # ВПИШИТЕ ЗАПРОС НА САЙТЕ И ID НУЖНОЙ КАРТОЧКИ
    # НАПРИМЕР:
        # "СКРИПКА", 0
        # "ГИТАРА", 2
    parser = Lmarkt(driver, "Гитара", 1)
    parser.parse()

if __name__ == "__main__":
    main()
