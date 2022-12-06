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
def create_subfolders(verbose, dry_run, year, days_start, days_end):
    if dry_run:
        print("Dry run, no files will be created.")

    # path of this file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # read and store boilerplate code
    # sample_boilerplate.py should be in the same folder as this file
    sample_boilerplate_file_path = os.path.join(dir_path, "sample.py")
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

        if not dry_run:
            os.makedirs(day_path)

        # create sample test input file in folder
        test_file_path = os.path.join(day_path, "test.txt")

        # protected by try/except
        if not dry_run:
            write_file(test_file_path, "sample input text")

        # copy sample_boilerplate.py to folder
        boilerplate_file_path = os.path.join(day_path, "solution.py")
        header = f"# programming challenge from https://adventofcode.com/{year}/day/{day}\n"

        # protected by try/except
        if not dry_run:
            write_file(boilerplate_file_path, header + boilerplate)

        if verbose:
            print(f"Wrote files in {day_path}")


if __name__ == '__main__':
    # create argument parser
    parser = argparse.ArgumentParser(add_help=False)

    # change the default help argument
    parser.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')

    # current year as subfolder
    parser.add_argument("--year", "-y", type=int, default=datetime.datetime.now().year,
                        help="Year of challenge. Default is current year on your system.")

    day_parser = parser.add_mutually_exclusive_group()

    # if only one argument is given, assume it's the current day
    day_parser.add_argument("--day", "-d", type=int, default=datetime.datetime.now().day,
                            help="Single day to create subfolder for. Default is current day on your system.")

    # get range of days, 2 arguments for start and end
    day_parser.add_argument("--days", "-D", type=int, nargs=2,
                            help="Range of days, specifiying start and end. If not specified, only one day (current day) is created.")

    # set verbosity
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Print more information.")

    # dry run
    parser.add_argument("--dry-run", "-n", action="store_true",
                        help="Don't actually create any files.")

    args = parser.parse_args()

    if args.help:
        exit(0)

    if args.verbose:
        print("args:", args)

    if args.days is None:
        args.days = [args.day, args.day]

    create_subfolders(args.verbose, args.dry_run,
                      args.year, args.days[0], args.days[1])
