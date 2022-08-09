from random import random
import unittest

from setup_game import (
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

    def test_random_generator_2_player_base(self):
        result = _random_generator({}, 0, DEPARTMENT_COUNT[2], BASE_SETUP)
        count = 0
        for k, v in result.items():
            if v < 0 or v > 2 or k < 1 or k > 16:
                self.fail()
            count = count + v
        self.assertTrue(count == 16)
    
    def test_random_generator_3_player_base(self):
        result = _random_generator({}, 0, DEPARTMENT_COUNT[3], BASE_SETUP)
        count = 0
        for k, v in result.items():
            if v < 0 or v > 2 or k < 1 or k > 16:
                self.fail()
            count = count + v
        self.assertTrue(count == 24)

    def test_random_generator_4_player_base(self):
        result = _random_generator({}, 0, DEPARTMENT_COUNT[4], BASE_SETUP)
        count = 0
        for k, v in result.items():
            if v < 0 or v > 2 or k < 1 or k > 16:
                self.fail()
            count = count + v
        self.assertTrue(count == 28)

    def test_random_generator_2_player_expansion(self):
        result = _random_generator({}, 0, DEPARTMENT_COUNT[2], EXPANSION_SETUP)
        count = 0
        for k, v in result.items():
            if v < 0 or v > 2 or k < 1 or k > 32:
                self.fail()
            count = count + v
        self.assertTrue(count == 16)
    
    def test_random_generator_3_player_expansion(self):
        result = _random_generator({}, 0, DEPARTMENT_COUNT[3], EXPANSION_SETUP)
        count = 0
        for k, v in result.items():
            if v < 0 or v > 2 or k < 1 or k > 32:
                self.fail()
            count = count + v
        self.assertTrue(count == 24)

    def test_random_generator_4_player_expansion(self):
        result = _random_generator({}, 0, DEPARTMENT_COUNT[4], EXPANSION_SETUP)
        count = 0
        for k, v in result.items():
            if v < 0 or v > 2 or k < 1 or k > 32:
                self.fail()
            count = count + v
        self.assertTrue(count == 28)

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