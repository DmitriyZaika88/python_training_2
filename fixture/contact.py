

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def name_fields(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

    def personal_information_fields(self, contact):
        wd = self.app.wd
        # photo field not used - doesn't work
        # wd.find_element_by_name('photo').send_keys(os.getcwd() + '/testy.jpg')
        # contact information
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)

    def methods_of_contact_fields(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

    def birthday_fields(self, contact):
        wd = self.app.wd
        # date of birth field
        wd.find_element_by_name("bday").send_keys(contact.day_of_birth)
        wd.find_element_by_name("bmonth").send_keys(contact.month_of_birth)
        wd.find_element_by_name("byear").send_keys(contact.year_of_birth)
        # anniversary field
        wd.find_element_by_name("aday").send_keys(contact.anniversary_day)
        wd.find_element_by_name("amonth").send_keys(contact.anniversary_month)
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("theform").click()

    def add_personal_information(self, contact):
        self.open_contact_creation_page()
        # form block edition begins
        self.name_fields(contact)
        self.personal_information_fields(contact)
        self.methods_of_contact_fields(contact)
        self.birthday_fields(contact)
        # form block edition end
        self.sumbit_contact_creation()
        self.return_to_home_page()

    def sumbit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first checkbox contact
        wd.find_element_by_name("selected[]").click()
        # delete first checkbox contact
        wd.find_element_by_css_selector("input[value='Delete']").click()

    def open_contact_edition_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_edition_page()
        # clear personal_information_fields
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("fax").clear()
        self.personal_information_fields(contact)
        # clear methods_of_contact_fields
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("homepage").clear()
        self.methods_of_contact_fields(contact)
        self.update_contact_confirmation()
        self.return_to_home_page()

    def update_contact_confirmation(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
