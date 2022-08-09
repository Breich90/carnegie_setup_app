from copy import deepcopy
from enum import Enum
from random import randint, sample

BASE_SETUP = 'base'
EXPANSION_SETUP = 'expansion'

DEPARTMENT_COUNT = {
    2: 16,
    3: 24, 
    4: 28
}

PLAYER_COLORS = ['Black', 'Blue', 'Yellow', 'White']

class Department(Enum):
    TRAINING_AND_PARTNERSHIPS = 1
    RECRUITING = 2
    SAFETY_AND_QUALITY = 3
    NEW_LOBBY = 4
    PURCHASING = 5
    SALES = 6
    LOGISTICS = 7
    PROPERTY_MANAGEMENT = 8
    CONSTRUCTION = 9
    CONSTRUCTION_SOURCING = 10
    SUPPLY_CHAIN = 11
    COMMUNICATIONS = 12
    ADVANCED_RESEARCH = 13
    ADVANCED_DESIGN = 14
    CHARITABLE_GIVING = 15
    TELEGRAPH_OPERATORS = 16
    HUMAN_RESOURCES_ADMINISTRATION = 17
    LOCAL_PARTNERS = 18
    CORPORATE_COMMUNICATION = 19
    GREEN_SPACES = 20
    ACCOUNTING = 21
    BRANDING = 22
    PAYROLL_MANAGEMENT = 23
    PUBLIC_RELATIONS = 24
    PRODUCTION_LINES = 25
    RENOVATION = 26
    POLITICAL_LOBBYING = 27
    POST_OFFICE = 28
    RD_COORDINATION = 29
    KNOWLEDGE_SHARING = 30
    ARCHIVES = 31
    NETWORK_OF_LIBRARIES = 32

    def __str__(self):
        return self.name.replace('_', ' ').title()

    def department_type(self):
        if self.value in [1,2,3,4,17,18,19,20]:
            return 'Human Resources'
        elif self.value in [5,6,7,8,21,22,23,24]:
            return 'Management'
        elif self.value in [9,10,11,12,25,26,27,28]:
            return 'Construction'
        elif self.value in [13,14,15,16,29,30,31,32]:
            return 'Research & Development'
        else:
            raise ValueError

def _random_generator(output: dict, current_count: int, target_count: int, setup_type: str) -> dict:
    local_output = deepcopy(output)
    local_count = current_count
    if current_count > target_count:
        raise ValueError
    elif current_count == target_count:
        return output
    else:
        if setup_type == BASE_SETUP:
            random_value = randint(1,16)
        else:
            random_value = randint(1,32)
        if random_value in output:
            if local_output[random_value] > 2:
                pass
            elif local_output[random_value] is 1:
                local_output[random_value] += 1
                local_count += 1         
        else: 
            local_output[random_value] = 1
            local_count += 1
        return _random_generator(local_output, local_count, target_count, setup_type)

def setup_game(setup_type: str, num_players: int) -> dict:
    output = {
        'departments': None
    }
    if setup_type == BASE_SETUP:
        output['departments'] = _random_generator({}, 0, DEPARTMENT_COUNT[num_players], BASE_SETUP)
    elif setup_type == EXPANSION_SETUP:
        output['departments'] = _random_generator({}, 0, DEPARTMENT_COUNT[num_players], EXPANSION_SETUP)
    else:
        raise ValueError

    # format the output of the departments dict
    formatted_departments = {
        'Human Resources': {},
        'Management': {},
        'Construction': {},
        'Research & Development': {}
    }
    for department_id, count in output['departments'].items():
        department_type = Department(department_id).department_type()
        formatted_departments[department_type][str(Department(department_id))] = {
            'department_id': department_id,
            'count': count
        }
    output['departments'] = formatted_departments
    output['player_order'] = sample(PLAYER_COLORS, len(PLAYER_COLORS))

    return output


