from contextlib import suppress

import allure

import pytest

from pythonProject.Repository_3.restapi_lesson.class_object.user_data_class import User
from pythonProject.Repository_3.restapi_lesson.class_object.color_class import Color

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def create_driver(request):
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id(),
                                         is_headless=ReadConfig.get_headless_mod())
    driver.get('https://reqres.in')
    driver.maximize_window()
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()

@pytest.fixture
def create_user():
    return User("lindsay.ferguson@reqres.in", "Lindsay", "Ferguson")


@pytest.fixture
def create_color():
    return Color(2, "fuchsia rose", 2001, "#C74375", "17-2031")
