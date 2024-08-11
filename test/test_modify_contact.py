from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="",
                                             middle_name="",
                                             last_name="",
                                             nickname="",
                                             title="new_test",
                                             company="market",
                                             address="Saint-Petersburg",
                                             home="new_home",
                                             mobile="secret",
                                             work="QA",
                                             fax="new_fax",
                                             email_1="modified_email@gmail.com",
                                             email_2="modified_email2@gmail.com",
                                             email_3="modified_email3@gmail.com",
                                             homepage="",
                                             day_of_birth="",
                                             month_of_birth="",
                                             year_of_birth="",
                                             anniversary_day="",
                                             anniversary_month="",
                                             anniversary_year=""))
    app.session.logout()
