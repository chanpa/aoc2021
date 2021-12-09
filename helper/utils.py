import sys
from time import perf_counter_ns
from typing import List, Dict
from locale import atof, atoi, setlocale, LC_NUMERIC
from collections import defaultdict
from pathlib import Path


setlocale(LC_NUMERIC, "en_US.UTF-8")
NS_TO_MILLI = 1_000_000
NS_TO_MICRO = 1_000


def time_function(fn):
    def wrap(*args, **kwargs):
        start = perf_counter_ns()
        res = fn(*args, **kwargs)
        elapsed_time = perf_counter_ns() - start
        print(f"{fn.__name__}:")
        if "part" in fn.__name__:
            print(f"Answer is: {res}")
        print(f"Took: {(elapsed_time / NS_TO_MICRO):_.3f} µs\n")
        return res

    return wrap


def parse_file_rows_to_list(day: int, test=False, split_row_on=None) -> List:
    if test:
        filename = f"{Path(__file__).parents[1].resolve()}/inputs_test/{day}.data"
    else:
        filename = f"{Path(__file__).parents[1].resolve()}/inputs/{day}.data"
    rows = []
    with open(filename) as f:
        for row in f:
            row = row.strip()
            if split_row_on:
                row = [e.strip() for e in row.split(split_row_on) if e]
            rows.append(row)
    return rows


def list_str_to_list_number(data, out_type=int):
    new_data = []
    for element in data:
        if out_type == int:
            num = atoi(element)
        else:
            num = atof(element)
        new_data.append(num)
    return new_data


def group_on_empty_line(rows: List[str]) -> Dict[int, str]:
    groups = defaultdict(list)
    group = 0
    for e in rows:
        if not e:
            group += 1
            continue
        groups[group].append(e)
    return groups


def liststr_to_listlist(group: List[str]) -> List[List]:
    new_vals = []
    for value in group:
        if not type(value) == str:
            print(f"Encountered {value} that is not a str")
            sys.exit(1)
        new_vals.append(list(value))
    return new_vals


def neighbours(point, kernel):
    x, y = point
    return [(x + dx, y + dy) for dx, dy in kernel]
