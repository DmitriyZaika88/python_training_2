

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def fill_group_name(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)

    def fill_group_header(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)

    def fill_group_footer(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_name(group)
        self.fill_group_header(group)
        self.fill_group_footer(group)
        self.submit_group_creation()
        self.return_to_groups_page()

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # edit selected group
        wd.find_element_by_name("edit").click()
        self.fill_group_name(group)
        wd.find_element_by_name("group_header").clear()
        self.fill_group_header(group)
        wd.find_element_by_name("group_footer").clear()
        self.fill_group_footer(group)
        self.update_group_confirmation()
        self.return_to_groups_page()

    def update_group_confirmation(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
