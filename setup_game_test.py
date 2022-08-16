import math
from random import random
import unittest

from parameterized import parameterized

from src.carnegie_setup.utils.setup_game import (
    _random_generator,
    BASE_SETUP,
    BLOCKING_MARKERS_COUNT,
    Department,
    DEPARTMENT_COUNT,
    EXPANSION_SETUP,
    setup_game
)

class SetupGameTest(unittest.TestCase):

    def test_department_enum_str(self):
        self.assertEqual('Training And Partnerships', str(Department(1)))
        self.assertEqual('Sales', str(Department(6)))

    @parameterized.expand([
        (2, BASE_SETUP),
        (3, BASE_SETUP),
        (4, BASE_SETUP),
        (2, EXPANSION_SETUP),
        (3, EXPANSION_SETUP),
        (4, EXPANSION_SETUP),
    ])
    def test_random_generator(self, player_count, setup_type):
        result = _random_generator({}, 0, DEPARTMENT_COUNT[player_count], setup_type)
        count = 0
        dep_counts = [0,0,0,0,0]
        for k, v in result.items():
            check = k
            if check > 16: 
                check = check - 16
            dep_counts[math.ceil(check/4)] += 1
            if v < 0 or v > 2 or k < 1 or k > 32:
                self.fail()
            count = count + v
        for x in dep_counts:
            if x > 4:
                self.fail()
        self.assertTrue(count == 16)

    def test_formatted_output_2_player_base(self):
        output = setup_game(BASE_SETUP, 2)
        department_count = 0
        for department_type, value in output['departments'].items():
            for department, value in value.items():
                self.assertTrue(Department(value['department_id']).department_type() == department_type)
                department_count += value['count']
        self.assertEqual(department_count, DEPARTMENT_COUNT[2])
        pass

    def test_formatted_output_3_player_base(self):
        output = setup_game(BASE_SETUP, 3)
        department_count = 0
        for department_type, value in output['departments'].items():
            for department, value in value.items():
                self.assertTrue(Department(value['department_id']).department_type() == department_type)
                department_count += value['count']
        self.assertEqual(department_count, DEPARTMENT_COUNT[3])
        pass

    def test_formatted_output_4_player_base(self):
        output = setup_game(BASE_SETUP, 4)
        department_count = 0
        for department_type, value in output['departments'].items():
            for department, value in value.items():
                self.assertTrue(Department(value['department_id']).department_type() == department_type)
                department_count += value['count']
        self.assertEqual(department_count, DEPARTMENT_COUNT[4])
        pass

    def test_formatted_output_2_player_expansion(self):
        output = setup_game(EXPANSION_SETUP, 2)
        department_count = 0
        for department_type, value in output['departments'].items():
            for department, value in value.items():
                self.assertTrue(Department(value['department_id']).department_type() == department_type)
                department_count += value['count']
        self.assertEqual(department_count, DEPARTMENT_COUNT[2])
        pass

    def test_formatted_output_3_player_expansion(self):
        output = setup_game(EXPANSION_SETUP, 3)
        department_count = 0
        for department_type, value in output['departments'].items():
            for department, value in value.items():
                self.assertTrue(Department(value['department_id']).department_type() == department_type)
                department_count += value['count']
        self.assertEqual(department_count, DEPARTMENT_COUNT[3])
        pass

    def test_formatted_output_4_player_expansion(self):
        output = setup_game(EXPANSION_SETUP, 4)
        department_count = 0
        for department_type, value in output['departments'].items():
            for department, value in value.items():
                self.assertTrue(Department(value['department_id']).department_type() == department_type)
                department_count += value['count']
        self.assertEqual(department_count, DEPARTMENT_COUNT[4])
        pass

    def test_blocked_cities_2_player(self):
        for x in range (1,100):
            output = setup_game(BASE_SETUP, 2)
            blocked_donation_count = len(set(output['blocked_discs']['donations']))
            blocked_cities_count = len(set(output['blocked_discs']['cities']))
            self.assertEqual(blocked_donation_count+blocked_cities_count, BLOCKING_MARKERS_COUNT[2])

if __name__ == '__main__':
    unittest.main()