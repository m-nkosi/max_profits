import unittest


def max_profit(prices: list[int]) -> int:
    """getting the maximum profit from a list of profits(the profit is for each day)"""
    max_profit_ = 0
    number_of_days = len(prices)
    for i in range(number_of_days):
        for j in range(i + 1, number_of_days):
            difference = prices[j] - prices[i]
            if difference > max_profit_:
                max_profit_ = difference
    return max_profit_


class Test(unittest.TestCase):
    def test_max_profit_case_one(self):
        """test when the maximum profit greater than zero"""
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)

    def test_max_profit_case_two(self):
        """tests when the maximum profit is 0"""
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)


if __name__ == '__main__':
    unittest.main()
