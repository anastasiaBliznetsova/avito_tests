from modify_json import modify_json


def test_9_energy_1000(page):
    page.route("**/ecoImpact/init", lambda route: route.fulfill(json=modify_json("energy", "1000")))
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E").screenshot(path='output/9_energy_1000.png')
