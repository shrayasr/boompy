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
import os
import json

FILE_LOCATION="boompy.json"
BOOMPY = {}

def list_buckets_and_counts():
    buckets = BOOMPY["metadata"]["buckets"]

    if len(buckets) == 0:
        print "No buckets created"

    else:
        for bucket in buckets:
            bucket_keys = BOOMPY["data"][bucket]["keys"]
            print "%s (%s)" % (bucket, len(bucket_keys))

def parse_and_do_job(args):

    if len(args) == 0:
        print "Shows available lists with the number of keys in them"
        return

    cmd = args[0].lower()

    if cmd == "all":
        list_buckets_and_counts()

    elif cmd == "delete":
        if len(args) == 2 or len(args) == 3:
            list_to_del = args[1].lower()
            if len(args) == 3:
                key_to_del = args[2].lower()
                print "Delete key `%s` in `%s`" % (key_to_del, list_to_del)
            else:
                print "Delete list `%s` and all its keys" % list_to_del
        else:
            print "Delete what?"

    else:
        list_to_use = cmd

        if len(args) == 1:
            print "Creates the list `%s`" % list_to_use

        elif len(args) == 2:
            key_to_fetch = args[1].lower()
            print "prints out the value for key `%s` under `%s`" % (
                    key_to_fetch, list_to_use)

        elif len(args) == 3:
            key_to_create = args[1].lower()
            value_to_assoc = args[2].lower()
            print "Creates the key `%s` under the list `%s` with value `%s`" % (
                    key_to_create, list_to_use, value_to_assoc)

def load_file():

    global BOOMPY

    if not os.path.isfile(FILE_LOCATION):
        base_boompy_template = {
                "metadata": { "buckets": [] },
                "data": {}
                }
        with open(FILE_LOCATION, "w") as w:
            w.write(json.dumps(base_boompy_template))

    with open(FILE_LOCATION) as r:
        BOOMPY = json.loads(r.read())

if __name__ == "__main__":
    args = sys.argv[1:]
    load_file()
    parse_and_do_job(args)
