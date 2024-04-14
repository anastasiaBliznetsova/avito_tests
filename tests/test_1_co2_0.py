from modify_json import modify_json


def test_1_co2_0(page):
    page.route("**/ecoImpact/init", lambda route: route.fulfill(json=modify_json("co2", "0")))
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E").screenshot(path='output/1_co2_0.png')
