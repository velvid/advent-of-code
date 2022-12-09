# My Advent of Code Solutions

## About

This is my collection of solutions for [Advent of Code](https://adventofcode.com/), an Advent calendar of small programming puzzles. I used `Python 3.10.x` for most of my solutions.

## Project Structure

Since the Advent is a yearly event, the puzzles are grouped by the year and subsequent day number.

```
advent-of-code
├───2015
├───2016
.
.
.
├───2022
│   ├───day01
│   ├───day02
.   .
.   .
.   .
│   └───day25
└───boilerplate
```

The [boilerplate](/boilerplate/) folder contains a script to generate boilerplate code, along with the sample boilerplate to copy.

## Generating Boilerplate

A [script](/boilerplate/generate.py) was created to make directories following the project structure, and write [boilerplate](/boilerplate/sample.py) files inside them.

See usage with:
```bash
cd path/to/this/repo # just to make sure you're in the directory :)
python ./boilerplate/generate.py --help
```