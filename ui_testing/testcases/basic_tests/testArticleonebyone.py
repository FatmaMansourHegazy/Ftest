from ui_testing.testcases.base_test import BaseTest
from ui_testing.pages.login_page import Login
from ui_testing.pages.article_page import Article
from ui_testing.pages.testplan_page import TstPlan
from ui_testing.pages.order_page import Order
from parameterized import parameterized
import re


class ArticlesTestCasesTrial(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = Login()
        self.article_page = Article()
        self.test_plan = TstPlan()
        self.order = Order()
        self.login_page.login(username=self.base_selenium.username, password=self.base_selenium.password)
        self.base_selenium.wait_until_page_url_has(text='dashboard')
        self.article_page.get_article_page()

    @parameterized.expand(['save', 'cancel'])
    def test001_cancel_button_edit_unit(self, save):
        """
        New: Article: Save/Cancel button: After I edit unit field then press on cancel button,
        a pop up will appear that the data will be

        LIMS-3586
        LIMS-3576
        :return:
        """
        self.article_page.get_random_article()
        article_url = self.base_selenium.get_url()
        self.base_selenium.LOGGER.info(' + article_url : {}'.format(article_url))
        current_unit = self.article_page.get_unit()
        new_unit = self.generate_random_string()
        self.article_page.set_unit(new_unit)
        if 'save' == save:
            self.article_page.save()
        else:
            self.article_page.cancel(force=True)

        self.base_selenium.get(url=article_url, sleep=self.base_selenium.TIME_MEDIUM)

        article_unit = self.article_page.get_unit()
        if 'save' == save:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (new_unit) == {} (article_unit)'.format(new_unit, article_unit))
            self.assertEqual(new_unit, article_unit)
        else:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (current_unit) == {} (article_unit)'.format(current_unit, article_unit))
            self.assertEqual(current_unit, article_unit)
