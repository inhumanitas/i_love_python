# encoding utf-8
"""
This small script will remove all directories under 'build' recursively
"""

import os
import datetime
import argparse
import fnmatch
import shutil
from collections import Iterable


RM_FOLDER_PATTERN = '*/build'


def is_older_than(path, days):
    """Checks if path modification time
    is older than days count
    :rtype: bool
    """
    def modification_date(filename):
        t = os.path.getmtime(filename)
        return datetime.datetime.fromtimestamp(t)

    p_datetime = modification_date(path)
    today = datetime.datetime.now()
    delta = today - p_datetime
    older = False
    if delta.days > days:
        older = True
    return older


def path_for_delete(cur_path, **params):
    """Checks the current path for requirements for removal
    :rtype: bool
    """
    result = False
    if fnmatch.fnmatch(cur_path, RM_FOLDER_PATTERN):
        days = params.get('days', 0)
        if days and is_older_than(cur_path, days):
            result = True
    return result


def find_folder_older_than(root_path, days):
    """Finds all paths under root_path that
    older than days
    :rtype: list
    """
    assert isinstance(days, int), 'wrong input param'

    if not os.path.isdir(root_path):
        print 'wrong file path: ', root_path
        return []

    found_paths = []
    for root, dirs, files in os.walk(root_path, topdown=False):
        for dir_name in dirs:
            cur_path = os.path.join(root, dir_name)
            if path_for_delete(cur_path, days=days):
                found_paths.append(cur_path)
    return found_paths


def rm_paths(paths):
    """Removes all files\folder under each path in paths"""
    assert isinstance(paths, Iterable)
    map(shutil.rmtree, paths)


def parse_opts():
    parser = argparse.ArgumentParser(
        description="Delete all folders under [root_path] "
        "that older than days_count")
    parser.add_argument(
        "-d", "--days", dest="days", type=int, required=True,
        help="specify days count")
    parser.add_argument(
        "-p", "--path", dest="path", default='.',
        type=str, help="root path to start searching")
    parser.add_argument(
        "-v", "--verbose", dest="log", action="store_true", default=False,
        help="Display progress information")

    return parser.parse_args()


if __name__ == '__main__':
    arguments = parse_opts()
    p_list = find_folder_older_than(arguments.path, arguments.days)

    if arguments.log:
        if p_list:
            print 'Directories for delete:'
        else:
            print 'Directories for delete not found'

        for p in p_list:
            print ' - ', p

    rm_paths(p_list)
