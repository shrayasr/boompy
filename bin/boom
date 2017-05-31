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
        Creates the list <list> if it doesn't exist or lists out the
        contents of it if it does.
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
import pyperclip
import webbrowser
from time import sleep
from contextlib import contextmanager

FILE_LOCATION="boompy.json"
BOOMPY = {}

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

def list_buckets_and_counts():
    buckets = BOOMPY["metadata"]["buckets"]

    if len(buckets) == 0:
        print "No buckets created"

    else:
        for bucket in buckets:
            bucket_keys = BOOMPY["data"][bucket]["keys"]
            print "%s (%s)" % (bucket, len(bucket_keys))

def create_list_or_print_contents(l):

    global BOOMPY

    if l in BOOMPY["metadata"]["buckets"]:
        for key in BOOMPY["data"][l]["keys"]:
            val = BOOMPY["data"][l]["values"][key]
            print "%s\t%s" % (key, val)

    else:
        BOOMPY["metadata"]["buckets"].append(l)
        BOOMPY["data"][l] = {
                "keys": [],
                "values": {}
                }

        write_db()

def add_kv_to_list(l, k, v):

    global BOOMPY

    if l not in BOOMPY["metadata"]["buckets"]:
        print "List doesn't exist, create it first"
        return

    BOOMPY["data"][l]["values"][k] = v

    if k not in BOOMPY["data"][l]["keys"]:
        BOOMPY["data"][l]["keys"].append(k)

    write_db()

def fetch_value(l, k):

    if l not in BOOMPY["metadata"]["buckets"]:
        print "List doesn't exist, create it first"
        return

    if k not in BOOMPY["data"][l]["keys"]:
        print "Key doesn't exist in list"
        return

    value = BOOMPY["data"][l]["values"][k]
    print "Copied %s to your clipboard!" % value
    pyperclip.copy(value)

def list_everything():
    for bucket in BOOMPY["metadata"]["buckets"]:
        print bucket
        for key in BOOMPY["data"][bucket]["keys"]:
            val = BOOMPY["data"][bucket]["values"][key]
            print "  %s\t%s" % (key, val)

def delete_key(l, k):

    global BOOMPY

    if l not in BOOMPY["metadata"]["buckets"]:
        print "List doesn't exist, create it first"
        return

    if k not in BOOMPY["data"][l]["keys"]:
        print "Key doesn't exist in list"
        return

    keys_idx = BOOMPY["data"][l]["keys"].index(k)

    del BOOMPY["data"][l]["values"][k]
    del BOOMPY["data"][l]["keys"][keys_idx]

    write_db()

def delete_list(l):

    global BOOMPY

    if l not in BOOMPY["metadata"]["buckets"]:
        print "List doesn't exist, create it first"
        return

    bucket_idx = BOOMPY["metadata"]["buckets"].index(l)

    del BOOMPY["data"][l]
    del BOOMPY["metadata"]["buckets"][bucket_idx]

    write_db()

def open_list(l):

    global BOOMPY
    urls_to_open = []

    with suppress_stdout():
        if l in BOOMPY["metadata"]["buckets"]:
            for key in BOOMPY["data"][l]["keys"]:
                val = BOOMPY["data"][l]["values"][key]
                urls_to_open.append(val)
            webbrowser.open(urls_to_open[0])
            sleep(1)
            for url in urls_to_open[1:]:
                webbrowser.open_new_tab(url)
            print "URLs have been opened."

        else:
            print "List doesn't exist, create it first"

def open_key(l, k):

    if l not in BOOMPY["metadata"]["buckets"]:
        print "List doesn't exist, create it first"
        return

    if k not in BOOMPY["data"][l]["keys"]:
        print "Key doesn't exist in list"
        return

    url = BOOMPY["data"][l]["values"][k]
    webbrowser.open(url)

def parse_and_do_job(args):

    if len(args) == 0:
        list_buckets_and_counts()
        return

    cmd = args[0].lower()

    if cmd == "all":
       list_everything()

    elif cmd == "delete":
        if len(args) == 2 or len(args) == 3:
            list_to_del = args[1].lower()
            if len(args) == 3:
                key_to_del = args[2].lower()
                delete_key(list_to_del, key_to_del)
            else:
                delete_list(list_to_del)

    elif cmd == "open":
        if len(args) == 2 or len(args) == 3:
            list_to_open = args[1].lower()
            if len(args) == 3:
                key_to_open = args[2].lower()
                open_key(list_to_open, key_to_open)
            else:
                open_list(list_to_open)

    else:
        list_to_use = cmd

        if len(args) == 1:
            create_list_or_print_contents(list_to_use)

        elif len(args) == 2:
            key_to_fetch = args[1].lower()
            fetch_value(list_to_use, key_to_fetch)

        elif len(args) == 3:
            key_to_create = args[1].lower()
            value_to_assoc = args[2].lower()
            add_kv_to_list(list_to_use, key_to_create, value_to_assoc)

def write_db():
    with open(FILE_LOCATION, "w") as w:
        w.write(json.dumps(BOOMPY))

def load_db():

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
    load_db()
    parse_and_do_job(args)
