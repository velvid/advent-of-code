import os
import argparse
import datetime


# helper function to read file
def read_file(file_path):
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path} not found")
    return data


# helper function to write file
def write_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            file.write(data)
    except:
        raise Exception(f"Failed to create {file_path}")


# function to create directory
def create_subfolders(year, days_start, days_end, verbose):
    # path of this file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # read and store boilerplate code
    # sample_boilerplate.py should be in the same folder as this file
    sample_boilerplate_file_path = os.path.join(dir_path, "sample_boilerplate.py")
    boilerplate = read_file(sample_boilerplate_file_path)

    # go up one level to create subfolders
    dir_path = os.path.dirname(dir_path)

    # create dayX folder for specified range of days
    for day in range(days_start, days_end+1):

        # skip subfolders with existing days, otherwise create subfolder
        day_path = os.path.join(dir_path, f"{year}", f"day{day:02d}")
        if os.path.exists(day_path):
            if verbose:
                print(f"{day_path} already exists, skipping")
            continue
        os.makedirs(day_path)

        # create sample test input file in folder
        test_file_path = os.path.join(day_path, "test.txt")
        write_file(test_file_path, "sample input text") # protected by try/except

        # copy sample_boilerplate.py to folder
        boilerplate_file_path = os.path.join(day_path, "solution.py")
        header = f"# programming challenge from https://adventofcode.com/{year}/day/{day}\n"
        write_file(boilerplate_file_path, header + boilerplate) # protected by try/except

        if verbose:
            print(f"Wrote files in {day_path}")


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

    # set verbosity level
    parser.add_argument("--verbose", "-v", action="store_true", \
        help="Print more information.")

    args = parser.parse_args()
    create_subfolders(args.year, args.days[0], args.days[1], args.verbose)
