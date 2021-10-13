#!/usr/bin/env python3.8

import argparse
import logging
import re


def parse_args():
    """function to parse arguments from the CLI
    """

    epilog = """
    Exemples:
    
        blablabla
    
      Enjoy!
    """

    parser = argparse.ArgumentParser(epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-l", "--loglevel", type=str, help="The log level for the program",
            choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="DISABLE")
    
    subparser = parser.add_subparsers(dest='command')

    list_metadata = subparser.add_parser('list')
    list_metadata.description = "description"

    list_metadata.add_argument("-i", "--input", type=str, required=True, help="help")

    add_metadata  = subparser.add_parser('edit')
    add_metadata.description = "description"

    add_metadata.add_argument("-i", "--input", type=str, required=True, help="help")
    add_metadata.add_argument("-m", "--metadata", type=str, required=True, help="help", nargs='+')

    return parser.parse_args()


class Class():
    """Class template
    """

    def __init__(self):
        pass

    def function(self):
        pass
        
    

def main():
    """main function
    """
    
    # ARGPARSE
    args = parse_args()


    # LOGGING
    disable_logging = False
    
    if args.loglevel == "DEBUG":
        p_level = logging.DEBUG
    elif args.loglevel == "INFO":
        p_level = logging.INFO
    elif args.loglevel == "WARNING":
        p_level = logging.WARNING
    elif args.loglevel == "ERROR":
        p_level = logging.ERROR
    elif args.loglevel == "CRITICAL":
        p_level = logging.CRITICAL
    elif args.loglevel == "DISABLE":
        p_level = logging.CRITICAL
        disable_logging = True
    else:
        p_level = logging.WARNING

    logging.basicConfig(level=p_level, format='%(asctime)s - %(levelname)s - %(message)s')
    if disable_logging:
        logging.disable(level=logging.CRITICAL)


    # ACTION
    if args.command == "":
        pass
    elif args.command == "":
        pass
    elif args.command == "":
        pass
    else:
        print("nothing to do.")


if __name__ == "__main__":
    """Entrypoint of the script
    """

    main()