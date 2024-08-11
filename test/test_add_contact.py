# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_personal_information(Contact(first_name="alex",
                                         middle_name="wellington",
                                         last_name="Andressen",
                                         nickname="Andy",
                                         title="test",
                                         company="wb",
                                         address="SPb",
                                         home="home",
                                         mobile="secret",
                                         work="QA",
                                         fax="none_none",
                                         email_1="dmitriydzd@gmail.com",
                                         email_2="dmitriydzk@gmail.com",
                                         email_3="dmitrosnachos@gmail.com",
                                         homepage="yandex.ru",
                                         day_of_birth="30",
                                         month_of_birth="June",
                                         year_of_birth="1997",
                                         anniversary_day="30",
                                         anniversary_month="June",
                                         anniversary_year="2027"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_personal_information(Contact(first_name="",
                                         middle_name="",
                                         last_name="",
                                         nickname="",
                                         title="",
                                         company="",
                                         address="",
                                         home="",
                                         mobile="",
                                         work="",
                                         fax="",
                                         email_1="",
                                         email_2="",
                                         email_3="",
                                         homepage="",
                                         day_of_birth="",
                                         month_of_birth="",
                                         year_of_birth="",
                                         anniversary_day="",
                                         anniversary_month="",
                                         anniversary_year=""))
    app.logout()
