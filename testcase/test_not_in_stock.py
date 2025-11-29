import time
import logging

from page_objects.productdetailpom.productdetailpage import ProductDetailPage
from setup.basetest import BaseTest


class TestCaseNotInStock(BaseTest):
    def test_not_in_stock(self):
        product_obj=ProductDetailPage(self.driver)

        # self.open_url('https://jeevee.com/products/technic-glow-setter-setting-spray-51840')
        self.open_url("https://jeevee.com/products/dr-jk-sunscreen-lotion-s-p-f-50-200-ml-8978")
        time.sleep(3)
        stock_info=product_obj.stock_info()
        logging.info(stock_info)
        is_enabled=product_obj.identify_enabled_status()
        logging.info(is_enabled)

        if "Out of Stock" in stock_info:
            assert not is_enabled, f"Expected button disabled for Out of Stock, but got enabled"
        elif "In Stock" in stock_info:
            assert is_enabled, f"Expected button enabled for In Stock, but got disabled"
