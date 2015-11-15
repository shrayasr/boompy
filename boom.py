#!/usr/bin/env python

"""
Data structure: json
{
    "metadata": {
        buckets: [
            "foo",
            "bar"
        ]
    },
    "data":{
        "foo": {
            "keys": ["foo1"],
            "values": {
                "foo1": "http://www.google.com"
            }
        }
    }
}
"""

"""
Commands:

    $ boom
        Shows available lists with the number of keys in them
    $ boom <list>
        Creates the list <list>
    $ boom <list> <key> <value>
        Creates the <key> under the list <list> with value <value>
    $ boom <list> <key>
        prints out the <value>
    $ boom delete <list>
        Delete list <list> and all its keys
    $ boom delete <list> <key>
        Delete key <key> in <list>
    $ boom all
        List everything
"""

import sys
import json

FILE_LOCATION="boompy.json"

def parse_and_do_job(args):

    if len(args) == 0:
        print "Shows available lists with the number of keys in them"
        return

    cmd = args[0].lower()

    if cmd == "all":
        print "List everything"
        return

    if cmd == "delete":
        if len(args) == 2 or len(args) == 3:
            list_to_del = args[1].lower()
            if len(args) == 3:
                key_to_del = args[2].lower()
                print "Delete key `%s` in `%s`" % (key_to_del, list_to_del)
            else:
                print "Delete list `%s` and all its keys" % list_to_del
        else:
            print "Delete what?"
        return

    if len(args) == 1:
        list_to_create = args[0].lower()
        print "Creates the list `%s`" % list_to_create

    elif len(args) == 2:
        list_to_use = args[0].lower()
        key_to_fetch = args[1].lower()
        print "prints out the value for key `%s` under `%s`" % (
                key_to_fetch, list_to_use)

    elif len(args) == 3:
        list_to_use = args[0].lower()
        key_to_create = args[1].lower()
        value_to_assoc = args[2].lower()
        print "Creates the key `%s` under the list `%s` with value `%s`" % (
                key_to_create, list_to_use, value_to_assoc)


if __name__ == "__main__":
    args = sys.argv[1:]
    parse_and_do_job(args)
