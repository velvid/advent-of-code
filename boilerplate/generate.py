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
    dir = os.path.dirname(os.path.realpath(__file__))

    # read and store boilerplate code
    # sample_boilerplate.py should be in the same folder as this file
    sample_boilerplate_file_path = os.path.join(dir, "sample.py")
    boilerplate = read_file(sample_boilerplate_file_path)

    # go up one level to create subfolders
    dir = os.path.dirname(dir)

    # create dayX folder for specified range of days
    for day in range(days_start, days_end+1):

        # skip subfolders with existing days, otherwise create subfolder
        subdir = os.path.join(dir, f"{year}", f"day{day:02d}")
        if os.path.exists(subdir):
            if verbose:
                print(f"{subdir} already exists, skipping")
            continue

        if not dry_run:
            os.makedirs(subdir)

        # create sample test input file in folder
        test_file_path = os.path.join(subdir, "test.txt")

        # protected by try/except
        if not dry_run:
            write_file(test_file_path, "sample input text")

        # copy sample_boilerplate.py to folder
        boilerplate_file_path = os.path.join(subdir, "solution.py")
        header = f"# programming challenge from https://adventofcode.com/{year}/day/{day}\n"

        # protected by try/except
        if not dry_run:
            write_file(boilerplate_file_path, header + boilerplate)

        if verbose:
            print(f"Wrote files in {subdir}")


if __name__ == '__main__':
    # create argument parser
    parser = argparse.ArgumentParser(
        add_help=False,
        description='Generates subfolders for Advent of Code days, and '
                    'will create a sample test.txt file and a boilerplate solution.py file. '
                    'Can be run from any directory, but will create subfolders '
                    'in the parent directory of the directory containing this file. '
                    'If a subfolder already exists, it will be skipped. '
    )

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

    if args.verbose:
        print("args:", args)

    if args.days is None:
        args.days = [args.day, args.day]

    create_subfolders(args.verbose, args.dry_run,
                      args.year, args.days[0], args.days[1])
