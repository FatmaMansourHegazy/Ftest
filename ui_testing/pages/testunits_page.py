from ui_testing.pages.base_pages import BasePages
from random import randint


class TestUnits(BasePages):
    def __init__(self):
        super().__init__()
        self.test_Units_url = "{}testUnits".format(self.base_selenium.url)

    def get_test_units_page(self):
        self.base_selenium.get(url=self.test_Units_url)
        self.sleep_small()

    def get_random_test_units(self):
        row = self.base_selenium.get_table_rows(element='test_plans:test_plans_table')
        self.get_random_x(row=row)

    def click_create_test_plan_button(self):
        self.base_selenium.click(element='test_plans:new_test_plan')
        self.sleep_small()

    def get_test_plan_edit_page(self, name):
        test_plan = self.search(value=name)[0]
        self.get_random_x(row=test_plan)
