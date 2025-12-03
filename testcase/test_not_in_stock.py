import time
import logging

from page_objects.productdetailpom.productdetailpage import ProductDetailPage
from setup.basetest import BaseTest


class TestCaseNotInStock(BaseTest):
    def test_not_in_stock(self):
        product_obj=ProductDetailPage(self.driver)

        product_url=self.creds['product_detail_page_url']
        self.open_url(product_url)
        logging.info('Product page opened ')
        time.sleep(3)
        stock_info=product_obj.stock_info()
        logging.info("Stock Information Extracted")
        logging.info(stock_info)
        is_enabled=product_obj.identify_enabled_status()
        logging.info("Status of ADD TO CART button checked")
        logging.info(f'On status: {is_enabled}')
        if "Out of Stock" in stock_info:
            assert not is_enabled, f"Expected button disabled for Out of Stock, but got enabled"
        elif "In Stock" in stock_info:
            assert is_enabled, f"Expected button enabled for In Stock, but got disabled"
