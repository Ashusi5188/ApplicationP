from time import sleep

from behave import *
import autoit

use_step_matcher("re")


@given("user opens calculator application")
def step_impl(context):
    autoit.run("C:\Windows\System32\calc.exe")
    autoit.win_wait_active("Calculator")


@when("User enter first number")
def step_impl(context):
    sleep(3)
    autoit.mouse_click("", 440, 518, 1, 0)


@step("User enter plus operator")
def step_impl(context):
    sleep(3)
    autoit.mouse_click("", 663, 614, 1, 0)


@step("User enters second number")
def step_impl(context):
    sleep(2)
    autoit.mouse_click("", 599, 521, 1, 0)


@then("User gets result")
def step_impl(context):
    sleep(2)
    autoit.mouse_click("", 675, 693, 1, 0)
    sleep(3)
    autoit.mouse_click("", 675, 184, 1, 0);
