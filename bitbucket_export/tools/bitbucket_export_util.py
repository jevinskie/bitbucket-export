#!/usr/bin/env python3

import argparse
import getpass
import os
from pathlib import Path

import bitbucket_export_util


def real_main(args):
    user = os.getenv("BITBUCKET_EXPORT_USER")
    if user is None:
        user = input("Bitbucket username: ")
    password = os.getenv("BITBUCKET_EXPORT_PASSWORD")
    if password is None:
        password = getpass.getpass("Bitbucket password: ")
    bitbucket_export_util.export_to(args.directory, user, password)


def main():
    parser = argparse.ArgumentParser(description="bitbucket-export")
    parser.add_argument(
        "-d",
        "--dir",
        required=True,
        dest="directory",
        type=Path,
        help="Directory to export repos to.",
    )
    args = parser.parse_args()
    real_main(args)


if __name__ == "__main__":
    main()
