import argparse
import logging


def main(args):
    """
    Main entry point for the program, takes in a string of arguments
    and defines the arguments to be taken
    """
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description="Converts pictures to ASCII")
    parser.add_argument("picture", action="store", type=str)

    results = parser.parse_args(args)
