# BOOMpy

This is a clone of @holman's [BOOM](https://github.com/holman/BOOM) in Python.

Commands:

Shows available lists with the number of keys in them

    $ boom

Creates the list `<list>` if it doesn't exist or lists out the contents of it if
it does.

    $ boom <list>

Creates the `<key>` under the list `<list>` with value `<value>`

    $ boom <list> <key> <value>

Prints out the value for the `<key>` under the `<list>` and copies it to the clipboard.

    $ boom <list> <key>

Delete list `<list>` and all its keys

    $ boom delete <list>

Delete key `<key>` in `<list>`

    $ boom delete <list> <key>

List everything

    $ boom all

---

Written on a lazy, rainy, Sunday afternoon in Chennai.
