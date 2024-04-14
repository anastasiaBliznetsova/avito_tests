from modify_json import modify_json


def test_5_water_999(page):
    page.route("**/ecoImpact/init", lambda route: route.fulfill(json=modify_json("water", "999")))
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E").screenshot(path='output/5_water_999.png')
