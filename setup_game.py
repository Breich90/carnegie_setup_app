from copy import deepcopy
from enum import Enum
from random import randint, sample, shuffle
from tkinter import W
from turtle import circle

BASE_SETUP = 'base'
EXPANSION_SETUP = 'expansion'

DEPARTMENT_COUNT = {
    2: 16,
    3: 24, 
    4: 28
}

PLAYER_COLORS = ['Black', 'Blue', 'Yellow', 'White']
class city(Enum):
    CHICAGO = 'CHICAGO'
    NEW_ORLEANS = 'NEW ORLEANS'
    SAN_FRANCISCO = 'SAN FRANCISCO'
    PORTLAND = 'PORTLAND'
    SEATTLE = 'SEATTLE'
    HELENA = 'HELENA'
    BOISE = 'BOISE'
    RENO = 'RENO'
    SALT_LAKE_CITY = 'SALT LAKE CITY'
    SANTA_FE = 'SANTA FE'
    LOS_ANGELES = 'LOS ANGELES'
    PHOENIX = 'PHOENIX'
    EL_PASO = 'EL_PASO'
    DENVER = 'DENVER'
    SAN_ANTONIO = 'SAN ANTONIO'
    HOUSTON = 'HOUSTON'
    DALLAS = 'DALLAS'
    MEMPHIS = 'MEMPHIS'
    ATLANTA = 'ATLANTA'
    CHARLESTON = 'CHARLESTON'
    FARGO = 'FARGO'
    DULUTH = 'DULUTH'
    ST_PAUL = 'ST. PAUL'
    OMAHA = 'OMAHA'
    ST_LOUIS = 'ST. LOUIS IS BORING'
    KANSAS_CITY = 'KANSAS CITY'
    CINCINNATI = 'CINCINNATI'
    WASHINGTON = 'WASHINGTON'
    PITTSBURGH = 'PITTSBURGH'
    NEW_YORK = 'NEW YORK'
    ALBANY = 'ALBANY'
    BOSTON = 'BOSTON'

class donation(Enum):
    EDUCATION_1 = 1
    EDUCATION_2 = 2
    EDUCATION_3 = 3
    EDUCATION_4 = 4
    EDUCATION_5 = 5

    HUMAN_RIGHTS_1 = 6
    HUMAN_RIGHTS_2 = 7
    HUMAN_RIGHTS_3 = 8
    HUMAN_RIGHTS_4 = 9
    HUMAN_RIGHTS_5 = 10

    WELFARE_1 = 11
    WELFARE_2 = 12
    WELFARE_3 = 13
    WELFARE_4 = 14
    WELFARE_5 = 15

    HEALTH_1 = 16
    HEALTH_2 = 17
    HEALTH_3 = 18
    HEALTH_4 = 19
    HEALTH_5 = 20


CARDS = [
    [donation.WELFARE_3, city.SAN_ANTONIO, city.MEMPHIS, city.DALLAS],
    [donation.HEALTH_2, city.SAN_FRANCISCO, city.SANTA_FE],
    [donation.HUMAN_RIGHTS_5, city.CHICAGO, city.OMAHA],
    [donation.HEALTH_2, city.SAN_FRANCISCO, city.SANTA_FE],
    [donation.EDUCATION_3, city.BOSTON, city.WASHINGTON],
    [donation.HUMAN_RIGHTS_2, city.ALBANY, city.NEW_YORK, city.WASHINGTON, city.PITTSBURGH],
    [donation.WELFARE_1, city.FARGO, city.ST_PAUL],
    [donation.WELFARE_1, city.FARGO, city.ST_PAUL],
    [donation.HEALTH_1, city.PITTSBURGH, city.BOSTON, city.ALBANY],
    [donation.EDUCATION_4, city.NEW_ORLEANS, city.HOUSTON],
    [donation.EDUCATION_1, city.SALT_LAKE_CITY, city.RENO],
    [donation.EDUCATION_1, city.SALT_LAKE_CITY, city.RENO],
    [donation.WELFARE_5, city.NEW_YORK, city.CHICAGO, city.NEW_ORLEANS, city.SAN_FRANCISCO],
    [donation.EDUCATION_4, city.NEW_ORLEANS, city.HOUSTON],
    [donation.EDUCATION_2, city.ST_LOUIS, city.CHICAGO],
    [donation.WELFARE_4, city.PORTLAND, city.BOISE, city.DENVER, city.LOS_ANGELES],
    [donation.HUMAN_RIGHTS_3, city.NEW_ORLEANS, city.ATLANTA],
    [donation.HEALTH_4, city.SAN_FRANCISCO, city.DENVER],
    [donation.WELFARE_5, city.NEW_YORK, city.CHICAGO, city.NEW_ORLEANS, city.SAN_FRANCISCO],
    [donation.HUMAN_RIGHTS_1, city.CINCINNATI, city.DULUTH, city.ST_LOUIS, city.KANSAS_CITY],
    [donation.EDUCATION_5, city.SAN_FRANCISCO, city.LOS_ANGELES],
    [donation.EDUCATION_2, city.ST_LOUIS, city.CHICAGO],
    [donation.HEALTH_5, city.KANSAS_CITY, city.CHICAGO],
    [donation.HEALTH_1, city.PITTSBURGH, city.BOSTON, city.ALBANY],
    [donation.HEALTH_3, city.NEW_ORLEANS, city.ATLANTA, city.HOUSTON, city.CHARLESTON],
    [donation.EDUCATION_3, city.BOSTON, city.WASHINGTON],
    [donation.HUMAN_RIGHTS_4, city.BOSTON, city.NEW_YORK],
    [donation.HUMAN_RIGHTS_2, city.ALBANY, city.NEW_YORK, city.WASHINGTON, city.PITTSBURGH],
    [donation.HUMAN_RIGHTS_4, city.BOSTON, city.NEW_YORK],
    [donation.HUMAN_RIGHTS_1, city.CINCINNATI, city.DULUTH, city.ST_LOUIS, city.KANSAS_CITY],
    [donation.WELFARE_2, city.PITTSBURGH, city.NEW_YORK],
    [donation.EDUCATION_5, city.SAN_FRANCISCO, city.LOS_ANGELES],
    [donation.HUMAN_RIGHTS_5, city.CHICAGO, city.OMAHA],
    [donation.WELFARE_3, city.SAN_ANTONIO, city.MEMPHIS, city.DALLAS],
    [donation.HEALTH_5, city.KANSAS_CITY, city.CHICAGO],
    [donation.HUMAN_RIGHTS_3, city.NEW_ORLEANS, city.ATLANTA],
    [donation.HEALTH_4, city.SAN_FRANCISCO, city.DENVER],
    [donation.HEALTH_3, city.NEW_ORLEANS, city.ATLANTA, city.HOUSTON, city.CHARLESTON],
    [donation.WELFARE_2, city.PITTSBURGH, city.NEW_YORK],
    [donation.WELFARE_4, city.PORTLAND, city.BOISE, city.DENVER, city.LOS_ANGELES]
]

BLOCKING_MARKERS_COUNT = {
    2: 18, 
    3: 9, 
    4: 0
}
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

    # format the player order
    output['player_order'] = sample(PLAYER_COLORS, len(PLAYER_COLORS))

    # format the blocked discs

    donations_list = []
    cities_list = []

    shuffle(CARDS)
    count = 0
    target_count = BLOCKING_MARKERS_COUNT[num_players]
    for card in CARDS:
        if count < target_count:
            if card[0] not in donations_list:
                donations_list.append(card[0].name)
                count += 1
                if count == target_count:
                    break
            for city in card[1:]:
                if city not in cities_list:
                    cities_list.append(city.value)
                    count += 1
                    if count == target_count:
                        break
            if count == target_count:
                break
        else:
            break

    output['blocked_discs'] = {
        'donations': donations_list,
        'cities': cities_list
    }

    return output