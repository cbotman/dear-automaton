# Elementary, Dear Automaton

Python is the de facto 🤖💡✨ _language of science_ ✨🧪🔬. As a self-directed learning exercise, I'm working on this Python implementation of an [elementary cellular automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton).

The current implementation stores and manipulates state as a string, which is assumedly inefficient. Once I've finished with other bits and bobs, I'll compare the performance of this to using integer arrays or binary.

### Usage

Run `./elementary.py` and follow the prompts, or run `./elementary.py -h` for help:
```
usage: elementary.py [-h] [-s STATE] [-p PAD_LEFT]

optional arguments:
  -h, --help            show this help message and exit
  -s STATE, --state STATE
                        set the initial state (e.g. --state 01101110)
  -p PAD_LEFT, --pad-left PAD_LEFT
                        pads the initial state (wtih zeroes) to this length (e.g. --pad-left=20)
```
Example using command line parameters to set the initial state (19 zeros and a one): `./elementary.py --state 1 --pad-left 20`, which will onput:
```
                   X
                  XX
                 XXX
                XX X
               XXXXX
              XX   X
             XXX  XX
            XX X XXX
           XXXXXXX X
```

### Status and todo

Currently only implements [Rule 110](https://en.wikipedia.org/wiki/Rule_110) and renders to console.

**Todo:**
- allow setting the initial iteration that should actually be output
   --range 0 1000 = show-from show-to
- can we prevent vomiting an error when quitting (^CTraceback (most recent call last):
- optionally write out the generation count beside the ouput... XX X XX X |2541
- allow setting the off and on characters (e.g. X) so can use emoji output
- allow outputting to image e.g. -output 110.png (only valid when capped number iterations via range)
- allow setting the rule to use e.g. -rule 110
- move from strings to integer arrays and possibly binary to be ⚡️?
