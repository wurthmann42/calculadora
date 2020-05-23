from behave import given, when, then
from Calculator.calculator import Calculador


@given("I have entered {number1:d} into the calculator")
def enter_number1(context, number1):
    context.number1 = number1


@given("I have also entered {number2:d} into the calculator")
def enter_number2(context, number2):
    context.number2 = number2


@when("I press soma")
def press_add(context):
    context.calculator = Calculador()
    context.result = context.calculator.soma(context.number1, context.number2)


@then("the sum should be {result:d}")
def check_result(context, result):
    assert context.result == result


@given("I have entered {number1:d} into the calculator")
def enter_number1(context, number1):
    context.number1 = number1


@given("I have also entered {number2:d} into the calculator")
def enter_number2(context, number2):
    context.number2 = number2


@when("I press subtrai")
def press_subtrai(context):
    context.calculator = Calculador()
    context.result = context.calculator.subtrai(context.number1, context.number2)


@then("the sum should be {result:d}")
def check_result(context, result):
    assert context.result == result


@given("I have entered {number1:d} into the calculator")
def enter_number1(context, number1):
    context.number1 = number1


@given("I have also entered {number2:d} into the calculator")
def enter_number2(context, number2):
    context.number2 = number2


@when("I press multiplica")
def press_subtrai(context):
    context.calculator = Calculador()
    context.result = context.calculator.multiplica(context.number1, context.number2)


@then("the sum should be {result:d}")
def check_result(context, result):
    assert context.result == result


@given("I have entered {number1:d} into the calculator")
def enter_number1(context, number1):
    context.number1 = number1


@given("I have also entered {number2:d} into the calculator")
def enter_number2(context, number2):
    context.number2 = number2


@when("I press divide")
def press_subtrai(context):
    context.calculator = Calculador()
    context.result = context.calculator.divide(context.number1, context.number2)


@then("the sum should be {result:d}")
def check_result(context, result):
    assert context.result == result
