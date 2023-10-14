import sys
import unittest

sys.path.append("../first")

from first import site_to_ip, ip_to_site


class TestSiteToIP(unittest.TestCase):
    def test_4digit_site(self):
        test_assertions = (
            ("1234", "11.12.34.0"),
            ("3456", "11.34.56.0"),
            ("1010", "11.10.10.0"),
        )
        for test_site, test_network_address in test_assertions:
            self.assertEqual(site_to_ip(test_site), test_network_address)

    def test_4digit_site_with_leading_zeroes(self):
        # hint for making this test case pass:
        # if you cast a string like "000001" to an integer like this:
        # int("000001") then the result will just be 1
        # you can then use the str() function to cast the result back to a string
        # for concatenation
        # string_int = str(int("000000000001"))
        # string_result == "1"  # true
        test_assertions = (("0001", "11.0.1.0"),)
        for test_site, test_network_address in test_assertions:
            self.assertEqual(site_to_ip(test_site), test_network_address)


class TestIpToSite(unittest.TestCase):
    def test_4digit_ip_to_site(self):
        self.assertEqual(ip_to_site("11.12.34.0"), "1234")


if __name__ == "__main__":
    unittest.main()
