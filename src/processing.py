from typing import Dict, List

dict_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_dicts_by_state(dict_list: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """a function that accepts a list of dictionaries and the value for the state key as input"""
    return [dict_ for dict_ in dict_list if dict_.get("state") == state]


def sort_dicts_by_date(dict_list: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """sorts the list of dictionaries in descending order of date"""
    return sorted(dict_list, key=lambda x: x["date"], reverse=reverse)
