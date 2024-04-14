from modify_json import modify_json


def test_3_co2_1000(page):
    page.route("**/ecoImpact/init", lambda route: route.fulfill(json=modify_json("co2", "1000")))
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E").screenshot(path='output/3_co2_1000.png')
