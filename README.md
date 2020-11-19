# Elementary, Dear Automaton

Python is the de facto 🤖💡✨ _language of science_ ✨🧪🔬. As a self-directed learning exercise, I'm working on this Python implementation of an [elementary cellular automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton).

The current implementation stores and manipulates state as a string, which is assumedly inefficient. Once I've finished with other bits and bobs, I'll compare the performance of this to using integer arrays or bytes.

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
Example: Set the initial state (19 zeros and a one): `./elementary.py --state 1 --pad-left 20`
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
Example: Emojis `./elementary.py -s 1 -p 20 --on=🌳 --off=🌲`
```
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌲🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌳🌳🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌲🌲🌲🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌳🌲🌲🌳🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌲🌳🌲🌳🌳🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌳🌳🌳🌳🌳🌲🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌲🌲🌲🌲🌲🌳🌳🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌳🌲🌲🌲🌲🌳🌳🌲🌳
🌲🌲🌲🌲🌲🌲🌲🌲🌳🌳🌲🌳🌲🌲🌲🌳🌳🌳🌳🌳
🌲🌲🌲🌲🌲🌲🌲🌳🌳🌳🌳🌳🌲🌲🌳🌳🌲🌲🌲🌳
🌲🌲🌲🌲🌲🌲🌳🌳🌲🌲🌲🌳🌲🌳🌳🌳🌲🌲🌳🌳
🌲🌲🌲🌲🌲🌳🌳🌳🌲🌲🌳🌳🌳🌳🌲🌳🌲🌳🌳🌳
🌲🌲🌲🌲🌳🌳🌲🌳🌲🌳🌳🌲🌲🌳🌳🌳🌳🌳🌲🌳
🌲🌲🌲🌳🌳🌳🌳🌳🌳🌳🌳🌲🌳🌳🌲🌲🌲🌳🌳🌳
🌲🌲🌳🌳🌲🌲🌲🌲🌲🌲🌳🌳🌳🌳🌲🌲🌳🌳🌲🌳
🌲🌳🌳🌳🌲🌲🌲🌲🌲🌳🌳🌲🌲🌳🌲🌳🌳🌳🌳🌳
🌳🌳🌲🌳🌲🌲🌲🌲🌳🌳🌳🌲🌳🌳🌳🌳🌲🌲🌲🌳
```
Example: Emojis 2 `./elementary.py -s 1 -p 20 --on=🐙 --off=💦`
```
💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦🐙
💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦🐙🐙
💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦🐙🐙🐙
💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦🐙🐙💦🐙
💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦🐙🐙🐙🐙🐙
💦💦💦💦💦💦💦💦💦💦💦💦💦💦🐙🐙💦💦💦🐙
💦💦💦💦💦💦💦💦💦💦💦💦💦🐙🐙🐙💦💦🐙🐙
💦💦💦💦💦💦💦💦💦💦💦💦🐙🐙💦🐙💦🐙🐙🐙
💦💦💦💦💦💦💦💦💦💦💦🐙🐙🐙🐙🐙🐙🐙💦🐙
💦💦💦💦💦💦💦💦💦💦🐙🐙💦💦💦💦💦🐙🐙🐙
💦💦💦💦💦💦💦💦💦🐙🐙🐙💦💦💦💦🐙🐙💦🐙
💦💦💦💦💦💦💦💦🐙🐙💦🐙💦💦💦🐙🐙🐙🐙🐙
💦💦💦💦💦💦💦🐙🐙🐙🐙🐙💦💦🐙🐙💦💦💦🐙
💦💦💦💦💦💦🐙🐙💦💦💦🐙💦🐙🐙🐙💦💦🐙🐙
💦💦💦💦💦🐙🐙🐙💦💦🐙🐙🐙🐙💦🐙💦🐙🐙🐙
💦💦💦💦🐙🐙💦🐙💦🐙🐙💦💦🐙🐙🐙🐙🐙💦🐙
💦💦💦🐙🐙🐙🐙🐙🐙🐙🐙💦🐙🐙💦💦💦🐙🐙🐙
💦💦🐙🐙💦💦💦💦💦💦🐙🐙🐙🐙💦💦🐙🐙💦🐙
💦🐙🐙🐙💦💦💦💦💦🐙🐙💦💦🐙💦🐙🐙🐙🐙🐙
🐙🐙💦🐙💦💦💦💦🐙🐙🐙💦🐙🐙🐙🐙💦💦💦🐙
```


### Status and todo

Currently only implements [Rule 110](https://en.wikipedia.org/wiki/Rule_110) and renders to console.

**Todo:**
- when asking for initial state, inline linebreak
- optionally write out the generation count beside the ouput... XX X XX X |2541
- allow setting the initial iteration that should actually be output
   --range 0 1000 = show-from show-to
- allow outputting to image e.g. -output 110.png (only valid when capped number iterations via range)
- allow setting the rule to use e.g. -rule 110 (include a prompt when run w/o params)
- move from strings to integer arrays and possibly binary to be ⚡️?
- add a --delay option to set the delay between iterations when doing console output
- add a --stats flag that outputs the number of iterations and how long it took to run (only makes sense w/ 0 delay...)
