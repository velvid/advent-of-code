import os
import argparse
import datetime


def create_subfolders(year, days_start, days_end):
    # open boilerplate file
    try:
        with open("./sample_boilerplate.py", "r") as boilerplate_file:
            base_boilerplate = boilerplate_file.read()
    except FileNotFoundError:
        raise FileNotFoundError("sample_boilerplate.py not found")

    # create dayX folder for 30 days
    for day in range(days_start, days_end + 1):

        # skip subfolders with existing days, otherwise create subfolder
        path = f"../{year}{os.sep}day{day:02d}"
        if os.path.exists(path):
            continue
        os.makedirs(path)

        # create sample test input file in folder
        try:
            with open(f"{path}{os.sep}test.txt", "w") as file:
                file.write("sample input text")
        except FileNotFoundError:
            raise FileNotFoundError(f"{path}{os.sep}test.txt failed to create")

        # copy sample_boilerplate.py to folder
        header = f"# programming challenge from https://adventofcode.com/{year}/day/{day}\n"
        boilerplate = header + base_boilerplate
        try:
            with open(f"{path}{os.sep}solution.py", "w") as file:
                file.write(boilerplate)
        except FileNotFoundError:
            raise FileNotFoundError(f"{path}{os.sep}solution.py failed to create")


if __name__ == '__main__':
    # create argument parser
    parser = argparse.ArgumentParser()

    # current year as subfolder
    current_year = datetime.datetime.now().year
    parser.add_argument("--year", "-y", type=int, default=current_year, \
        help="Year of challenge. Default is current year on your system.")

    # get range of days, 2 arguments for start and end
    parser.add_argument("--days", "-d", type=int, nargs=2, default=[1,25], \
        help="Range of days, specifiying start and beginning. Default is 1 to 25.")

    args = parser.parse_args()
    create_subfolders(args.year, args.days[0], args.days[1])
