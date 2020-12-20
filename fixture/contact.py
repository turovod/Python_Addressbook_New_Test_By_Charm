from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.fnd_element_by_name(field_name).send_keys(text)

    contacts = []

    def get_contact_list(self):
        driver = self.app.driver
        self.app.open_home_page()
        for row in driver.find_elements_by_name("entry"):
            cell = row.ind_elements_by_tag_name("td")
            firstname = cell[1].text
            lastname = cell[2].text
            id = cell[0].find_element_by_name("input").get_attribute("value")
            self.contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return self.contacts

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

