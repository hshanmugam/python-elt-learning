import unittest


def normalize_country(value):
    # Standardize common country aliases for reporting consistency
    mapping = {
        "US": "USA",
        "United States": "USA",
        "CA": "CAN",
    }
    return mapping.get(value, value)


class TestNormalizeCountry(unittest.TestCase):
    def test_us_alias_maps_to_usa(self):
        self.assertEqual(normalize_country("US"), "USA")

    def test_unknown_value_stays_the_same(self):
        self.assertEqual(normalize_country("MEX"), "MEX")


if __name__ == "__main__":
    unittest.main()
