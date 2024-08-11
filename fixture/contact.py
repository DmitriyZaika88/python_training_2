

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def add_personal_information(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # name fields
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
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
        # email fields
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # date of birth field
        wd.find_element_by_name("bday").send_keys(contact.day_of_birth)
        wd.find_element_by_name("bmonth").send_keys(contact.month_of_birth)
        wd.find_element_by_name("byear").send_keys(contact.year_of_birth)
        # anniversary field
        wd.find_element_by_name("aday").send_keys(contact.anniversary_day)
        wd.find_element_by_name("amonth").send_keys(contact.anniversary_month)
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("theform").click()
        self.sumbit_contact_creation()
        self.return_to_home_page()

    def sumbit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
