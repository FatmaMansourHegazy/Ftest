from ui_testing.testcases.base_test import BaseTest
from ui_testing.pages.login_page import Login
from ui_testing.pages.article_page import Article
from ui_testing.pages.testplan_page import TstPlan
from ui_testing.pages.order_page import Order
from parameterized import parameterized
import re


class ArticlesTestCases(BaseTest):
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

    @parameterized.expand(['save', 'cancel'])
    def test002_cancel_button_edit_no(self, save):
        """
        New: Article: Save/Cancel button: After I edit no field then press on cancel button,
        a pop up will appear that the data will be

        LIMS-3586
        LIMS-3576
        :return:
        """
        self.article_page.get_random_article()
        article_url = self.base_selenium.get_url()
        self.base_selenium.LOGGER.info(' + article_url : {}'.format(article_url))
        current_no = self.article_page.get_no()
        new_no = self.generate_random_string()
        self.article_page.set_no(new_no)
        if 'save' == save:
            self.article_page.save()
        else:
            self.article_page.cancel(force=True)

        self.base_selenium.get(url=article_url, sleep=self.base_selenium.TIME_MEDIUM)

        article_no = self.article_page.get_no()
        if 'save' == save:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (new_no) == {} (article_no)'.format(new_no, article_no))
            self.assertEqual(new_no, article_no)
        else:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (current_no) == {} (article_no)'.format(current_no, article_no))
            self.assertEqual(current_no, article_no)

    @parameterized.expand(['save', 'cancel'])
    def test003_cancel_button_edit_name(self, save):
        """
        New: Article: Save/Cancel button: After I edit name then press on cancel button,
        a pop up will appear that the data will be

        LIMS-3586
        LIMS-3576
        :return:
        """
        self.article_page.get_random_article()
        article_url = self.base_selenium.get_url()
        self.base_selenium.LOGGER.info(' + article_url : {}'.format(article_url))
        current_name = self.article_page.get_name()
        new_name = self.generate_random_string()
        self.article_page.set_name(new_name)

        if 'save' == save:
            self.article_page.save()
        else:
            self.article_page.cancel(force=True)

        self.base_selenium.get(url=article_url, sleep=self.base_selenium.TIME_MEDIUM)

        article_name = self.article_page.get_name()
        if 'save' == save:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (new_name) == {} (article_name)'.format(new_name, article_name))
            self.assertEqual(new_name, article_name)
        else:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (current_name) == {} (article_name)'.format(current_name, article_name))
            self.assertEqual(current_name, article_name)

    @parameterized.expand(['save', 'cancel'])
    def test004_cancel_button_edit_comment(self, save):
        """
        New: Article: Save/Cancel button: After I edit comment then press on cancel button,
        a pop up will appear that the data will be

        LIMS-3586
        LIMS-3576
        :return:
        """
        self.article_page.get_random_article()
        article_url = self.base_selenium.get_url()
        self.base_selenium.LOGGER.info(' + article_url : {}'.format(article_url))
        current_comment = self.article_page.get_comment()
        new_comment = self.generate_random_string()
        self.article_page.set_comment(new_comment)
        if 'save' == save:
            self.article_page.save()
        else:
            self.article_page.cancel(force=True)

        self.base_selenium.get(url=article_url, sleep=self.base_selenium.TIME_MEDIUM)

        article_comment = self.article_page.get_comment()
        if 'save' == save:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (new_comment) == {} (article_comment)'.format(new_comment, article_comment))
            self.assertEqual(new_comment, article_comment)
        else:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (current_comment) == {} (article_comment)'.format(current_comment, article_comment))
            self.assertEqual(current_comment, article_comment)

    @parameterized.expand(['save', 'cancel'])
    def test005_cancel_button_edit_material_type(self, save):
        """
        New: Article: Save/Cancel button: After I edit material_type then press on cancel button,
        a pop up will appear that the data will be

        LIMS-3586
        LIMS-3576
        :return:
        """
        self.article_page.get_random_article()
        article_url = self.base_selenium.get_url()
        self.base_selenium.LOGGER.info(' + article_url : {}'.format(article_url))
        current_material_type = self.article_page.get_material_type()
        self.article_page.set_material_type(random=True)
        new_material_type = self.article_page.get_material_type()
        if 'save' == save:
            self.article_page.save()
        else:
            self.article_page.cancel(force=True)

        self.base_selenium.get(url=article_url, sleep=5)

        article_material = self.article_page.get_material_type()
        if 'save' == save:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (new_material_type) == {} (article_material_type)'.format(new_material_type,
                                                                                        article_material))
            self.assertEqual(new_material_type, self.article_page.get_material_type())
        else:
            self.base_selenium.LOGGER.info(
                ' + Assert {} (current_material_type) == {} (article_material_type)'.format(current_material_type,
                                                                                            article_material))
            self.assertEqual(current_material_type, self.article_page.get_material_type())

    def test006_archived_articles_shoudnt_dispaly_in_test_plan(self):
        """
        New: Article: In case I archived any article this article shouldn't display in the test plan module when
         I create test plan or edit it

         LIMS-3668
        :return:
        """
        self.base_selenium.LOGGER.info(' + Create new article with Raw Material.')
        self.article_page.create_new_article(material_type='Raw Material')
        self.base_selenium.LOGGER.info(' + Archive the article.')
        self.article_page.archive_article(name=self.article_page.article_name)
        self.test_plan.get_test_plans_page()
        self.base_selenium.LOGGER.info(' + Create test plan with the same material type.')
        self.test_plan.click_create_test_plan_button()
        self.test_plan.set_material_type(material_type=self.article_page.article_material_type)
        self.article_page.sleep_tiny()
        self.base_selenium.LOGGER.info(' + Assert article is not existing in the list.')
        self.assertFalse(self.test_plan.is_article_existing(article=self.article_page.article_name))

    def test007_archived_articles_shoudnt_dispaly_in_order(self):
        """
        New: Article: Archived any article this article shouldn't display in the order module

         LIMS-3668
        :return:
        """
        self.article_page.create_new_article(material_type='Raw Material')
        self.article_page.archive_article(name=self.article_page.article_name)
        self.order.get_orders_page()
        self.order.click_create_order_button()
        self.order.set_new_order()
        self.order.set_material_type(material_type=self.article_page.article_material_type)
        self.article_page.sleep_tiny()
        self.assertFalse(self.order.is_article_existing(article=self.article_page.article_name))

    def test008_created_article_appear_in_test_plan(self):
        """
            New: Article/Test plan: Any article I created should appear in the test plan according to the materiel type.

            LIMS-3581
        :return:
        """
        self.article_page.create_new_article(material_type='Raw Material')
        self.test_plan.get_test_plans_page()
        self.test_plan.click_create_test_plan_button()
        self.test_plan.set_material_type(material_type=self.article_page.article_material_type)
        self.article_page.sleep_tiny()
        self.assertTrue(self.test_plan.is_article_existing(article=self.article_page.article_name))

    def test009_create_article_with_test_plan_search_by_test_plan(self):
        """
        In case I create test plan with the article that I created, this test plan should display in the table view

        LIMS-3583
        :return:
        """
        self.article_page.create_new_article(material_type='Raw Material')
        self.test_plan.get_test_plans_page()
        self.test_plan.create_new_test_plan(material_type=self.article_page.article_material_type,
                                            article=self.article_page.article_name)
        self.article_page.get_article_page()
        self.article_page.sleep_small()
        article = self.article_page.search(value=self.test_plan.test_plan_name)[0]
        self.assertIn(self.test_plan.test_plan_name, article.text)

        self.test_plan.get_test_plans_page()
        self.test_plan.get_test_plan_edit_page(name=self.test_plan.test_plan_name)

        self.test_plan.clear_article()
        self.test_plan.set_article(article='All')
        self.test_plan.save()
        self.article_page.get_article_page()
        article = self.article_page.search(self.article_page.article_name)[0]
        self.assertNotIn(self.test_plan.test_plan_name, article.text)

    def test010_create_article_with_test_plan_filter_by_test_plan(self):
        """
        In case I create test plan with the article that I created, user could filter with test plan

        LIMS-3583
        :return:
        """
        self.article_page.create_new_article(material_type='Raw Material')
        self.test_plan.get_test_plans_page()
        self.test_plan.create_new_test_plan(material_type=self.article_page.article_material_type,
                                            article=self.article_page.article_name)
        self.article_page.get_article_page()
        self.article_page.sleep_small()

        self.article_page.filter_by_test_plan(filter_text=self.test_plan.test_plan_name)
        article = self.article_page.filter_result()[0]
        self.assertIn(self.test_plan.test_plan_name, article.text)

    def test011_archive_articles(self):
        """
        New: Article: Archive Approach: I can archive/restore any article successfully

        LIMS-3587
        :return:
        """
        selected_articles_data, _ = self.article_page.select_random_multiple_table_rows()
        self.article_page.archive_selected_articles()
        self.article_page.get_archived_articles()
        for article in selected_articles_data:
            article_name = article['Article Name']
            self.base_selenium.LOGGER.info(' + {} article should be activated.'.format(article_name))
            self.assertTrue(self.article_page.is_article_archived(value=article_name))

    def test012_restore_articles(self):
        """
        New: Article: Restore Approach: I can archive/restore any article successfully

        LIMS-3587
        :return:
        """
        article_names = []
        self.article_page.get_archived_articles()
        selected_articles_data, _ = self.article_page.select_random_multiple_table_rows()
        for article in selected_articles_data:
            article_names.append(article['Article Name'])

        self.article_page.restore_selected_articles()
        self.article_page.get_active_articles()
        for article_name in article_names:
            self.assertTrue(self.article_page.is_article_archived(value=article_name))

    def test013_create_new_material_type(self):
        """
        Article: Materiel type Approach: make sure you can create new materiel type & this materiel type displayed correct according to this article.

        LIMS-3582
        :return:
        """
        material_type = self.generate_random_string()
        self.article_page.create_new_article(material_type=material_type)
        self.test_plan.get_test_plans_page()
        self.test_plan.click_create_test_plan_button()
        self.test_plan.set_material_type(material_type=self.article_page.article_material_type)
        self.article_page.sleep_tiny()
        self.assertTrue(self.test_plan.is_article_existing(article=self.article_page.article_name))

    def test014_article_search(self):
        """
        New: Articles: Search Approach: I can search by any field in the table view

        LIMS-3594
        :return:
        """
        row = self.article_page.get_random_article_row()
        row_data = self.base_selenium.get_row_cells_dict_related_to_header(row=row)
        for column in row_data:
            if re.findall(r'\d{1,}.\d{1,}.\d{4}', row_data[column]) or row_data[column] == '':
                continue
            self.base_selenium.LOGGER.info(' + search for {} : {}'.format(column, row_data[column]))
            search_results = self.article_page.search(row_data[column])
            self.assertGreater(len(search_results), 1, " * There is no search results for it, Report a bug.")
            for search_result in search_results:
                search_data = self.base_selenium.get_row_cells_dict_related_to_header(search_result)
                if search_data[column] == row_data[column]:
                    break
            self.assertEqual(row_data[column], search_data[column])

    def test015_green_border(self):
        """
        New: All modules: Creation Approach: Green border displayed when I create new record

        LIMS-3597
        :return:
        """
        self.article_page.create_new_article(sleep=False, material_type='Raw Material')
        self.assertEqual(self.base_selenium.get_text(element='articles:alert_confirmation'), 'Successfully created')

    def test016_create_full_options_article(self):
        """
        New: Articles: Creation Approach: I can create new article successfully

        LIMS-3575
        :return:
        """
        self.article_page.create_new_article(full_options=True, material_type='Raw Material')
        article_text = self.article_page.search(value=self.article_page.article_name)[0].text
        self.assertIn(self.article_page.article_unit, article_text)
        self.assertIn(self.article_page.article_comment, article_text)
        self.assertIn(self.article_page.article_material_type, article_text)

    def test017_delete_article_with_test_plan(self):
        """
        New: Articles: Delete Approach; I can't delete any article if this article related to some data

        LIMS-3577
        :return:
        """
        self.article_page.create_new_article(material_type='Raw Material')
        self.test_plan.get_test_plans_page()
        self.test_plan.create_new_test_plan(material_type=self.article_page.article_material_type,
                                            article=self.article_page.article_name)
        self.article_page.get_article_page()
        self.article_page.sleep_small()
        article = self.article_page.search(value=self.test_plan.test_plan_name)[0]

        self.article_page.click_check_box(source=article)
        self.article_page.archive_selected_articles()

        self.article_page.get_archived_articles()
        archived_article = self.article_page.search(value=self.test_plan.test_plan_name)[0]
        self.article_page.click_check_box(source=archived_article)
        self.assertFalse(self.article_page.delete_selected_article())

    def test018_delete_article_with_order(self):
        """
        New: Articles: Delete Approach; I can't delete any article if this article related to some data

        LIMS-3577
        :return:
        """
        self.base_selenium.LOGGER.info(' + Create new article with Raw Material.')
        self.article_page.create_new_article(material_type='Raw Material')
        self.test_plan.get_test_plans_page()
        self.base_selenium.LOGGER.info(
            ' + Create new test plan with {} article.'.format(self.article_page.article_name))
        self.test_plan.create_new_test_plan(material_type=self.article_page.article_material_type,
                                            article=self.article_page.article_name,
                                            test_unit='Qualitative')
        self.order.get_orders_page()
        self.order.click_create_order_button()
        self.base_selenium.LOGGER.info(
            ' + Create new order with {} article.'.format(self.article_page.article_name))
        self.order.create_new_order(article=self.article_page.article_name,
                                    material_type=self.article_page.article_material_type,
                                    test_plan=self.test_plan.test_plan_name)

        self.article_page.get_article_page()
        self.article_page.sleep_small()
        self.base_selenium.LOGGER.info(
            ' + Search for active article with {} test plan.'.format(self.test_plan.test_plan_name))
        search_results = self.article_page.search(value=self.test_plan.test_plan_name)
        self.assertGreater(len(search_results), 1, " * There is no search results for it, Report a bug.")
        for search_result in search_results:
            search_data = self.base_selenium.get_row_cells_dict_related_to_header(search_result)
            if self.test_plan.test_plan_name in search_data['Test Plans']:
                break
            self.base_selenium.LOGGER.debug(' Article test plan : {} '.format(search_data['Test Plans']))
        else:
            raise ValueError(" There is no active article with {} test plan".format(self.test_plan.test_plan_name))
        self.base_selenium.LOGGER.info(' + Archive this article.')
        self.article_page.click_check_box(source=search_result)
        self.article_page.archive_selected_articles()

        self.article_page.get_archived_articles()
        self.base_selenium.LOGGER.info(
            ' + Search for archived article with {} test plan.'.format(self.test_plan.test_plan_name))
        search_results = self.article_page.search(value=self.test_plan.test_plan_name)
        self.assertGreater(len(search_results), 1, " * There is no search results for it, Report a bug.")
        for search_result in search_results:
            search_data = self.base_selenium.get_row_cells_dict_related_to_header(search_result)
            if self.test_plan.test_plan_name in search_data['Test Plans']:
                break
            self.base_selenium.LOGGER.debug(' Article test plan : {} '.format(search_data['Test Plans']))
        else:
            raise ValueError(" There is no archived article with {} test plan".format(self.test_plan.test_plan_name))

        self.base_selenium.LOGGER.info(' + Delete this article, should fail.')
        self.article_page.click_check_box(source=search_result)
        self.assertFalse(self.article_page.delete_selected_article())

    def test019_download_article_sheet(self):
        """
        New: Articles: XSLX File: I can download all the data in the table view in the excel sheet

        LIMS:3589
        :return:
        """
        self.base_selenium.LOGGER.info(' * Download XSLX sheet')
        self.article_page.download_xslx_sheet()
        rows_data = self.article_page.get_articles_rows_data()
        for index in range(len(rows_data)):
            self.base_selenium.LOGGER.info(' * Comparing the article no. {} '.format(index))
            fixed_row_data = self.fix_data_format(rows_data[index].split('\n'))
            values = self.article_page.article_sheet.iloc[index].values
            fixed_sheet_row_data = self.fix_data_format(values)
            for item in fixed_row_data:
                self.assertIn(item, fixed_sheet_row_data)
