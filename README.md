# Elementary, Dear Automaton

Python is the de facto ✨💡🤖 _language of science_ 🔬🧪✨. As a self-directed learning exercise, I'm working on this Python implementation of the 256 [elementary cellular automatons](https://en.wikipedia.org/wiki/Elementary_cellular_automaton).

The current implementation stores and manipulates state as a string, which is assumedly inefficient. Once I've finished with other bits and bobs, I'll compare the performance of this to using integer arrays or bytes.

### Usage

Run `./elementary.py` and follow the prompts, or run `./elementary.py -h` for help:
```
usage: elementary.py [-h] [-r RULE] [-p PAD] [-d {left,right,both}] [--delay DELAY] [--counter] [--off OFF] [--on ON] [--random RANDOM] [--random-rule] [--seed SEED] [--no-wrap] [STATE]

positional arguments:
  STATE                 set the initial state (e.g. 01101110)

optional arguments:
  -h, --help            show this help message and exit
  -r RULE, --rule RULE  set the rule to use (between 0 to 255, inclusive). defaults to rule 110
  -p PAD, --pad PAD     pads the initial state (with zeroes) to this length (e.g. --pad=20)
  -d {left,right,both}, --pad-side {left,right,both}
                        set which side to pad the initial state: left (default), right, or both
  --delay DELAY         delay between displaying each generation in milliseconds (defaults to 250 ms)
  --counter             show the iteration count
  --off OFF             character to show when a cell is off (defaults to a blank space)
  --on ON               character to show when a cell is on (defaults to X)
  --random RANDOM       generate random starting state of N length
  --random-rule         pick a rule at random
  --seed SEED           set the base seed for the random number generator
  --no-wrap             prevent edges wrapping
```
**Example:** Set the initial state (19 zeros and a one):
```
./elementary.py 1 --pad 20
                   X
                  XX
                 XXX
                XX X
               XXXXX
              XX   X
             XXX  XX
            XX X XXX
           XXXXXXX X
          XX     XXX
```
**Example:** Emojis
```
./elementary.py 1 -p 20 --on=🌲 --off=🌳
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌳🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌲🌲🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌳🌳🌳🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌲🌳🌳🌲🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌳🌲🌳🌲🌲🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌲🌲🌲🌲🌲🌳🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌳🌳🌳🌳🌳🌲🌲🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌲🌳🌳🌳🌳🌲🌲🌳🌲
🌳🌳🌳🌳🌳🌳🌳🌳🌲🌲🌳🌲🌳🌳🌳🌲🌲🌲🌲🌲
🌳🌳🌳🌳🌳🌳🌳🌲🌲🌲🌲🌲🌳🌳🌲🌲🌳🌳🌳🌲
🌳🌳🌳🌳🌳🌳🌲🌲🌳🌳🌳🌲🌳🌲🌲🌲🌳🌳🌲🌲
🌳🌳🌳🌳🌳🌲🌲🌲🌳🌳🌲🌲🌲🌲🌳🌲🌳🌲🌲🌲
🌳🌳🌳🌳🌲🌲🌳🌲🌳🌲🌲🌳🌳🌲🌲🌲🌲🌲🌳🌲
🌳🌳🌳🌲🌲🌲🌲🌲🌲🌲🌲🌳🌲🌲🌳🌳🌳🌲🌲🌲
🌳🌳🌲🌲🌳🌳🌳🌳🌳🌳🌲🌲🌲🌲🌳🌳🌲🌲🌳🌲
🌳🌲🌲🌲🌳🌳🌳🌳🌳🌲🌲🌳🌳🌲🌳🌲🌲🌲🌲🌲
🌲🌲🌳🌲🌳🌳🌳🌳🌲🌲🌲🌳🌲🌲🌲🌲🌳🌳🌳🌲
```
**Example:** More emojis
```
./elementary.py 1 -p 20 --on=🐙 --off=💦
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
**Example:** Use `--rule` to set the rule (any value from 0 to 255), and use `--pad` and `--pad-side` to quickly set the starting state.
```
./elementary.py 1 --rule 30 --no-wrap --pad 20 --pad-side left
                   X
                  XX
                 XX 
                XX X
               XX  X

./elementary.py 1 --rule 30 --no-wrap --pad 20 --pad-side right
X                   
XX                  
X X                 
X XX                
X X X               

./elementary.py 1 --rule 30 --no-wrap --pad 20 --pad-side both 
          X         
         XXX        
        XX  X       
       XX XXXX      
      XX  X   X     
```

**Example:** Use `--counter` to output the number of iterations/generations.
```
./elementary.py --counter 
🤖 Enter an initial string of ones and zeroes:
0000100001
    X    X|0
   XX   XX|1
  XXX  XXX|2
 XX X XX X|3
XXXXXXXXXX|4
          |5
```
**Example:** Use `--random` to create a random initial state of given length. Use `--seed` to set the random number generator's base seed and reproduce the same random number series.
```
./elementary.py --random 10 --seed 123 --pad 20 --counter
          XXX  XX X |0
         XX X XXXXX |1
        XXXXXXX   X |2
       XX     X  XX |3
      XXX    XX XXX |4
     XX X   XXXXX X |5

./elementary.py --random 15 --seed 123 --pad 20 --counter
     XX   XXX  XX X |0
    XXX  XX X XXXXX |1
   XX X XXXXXXX   X |2
  XXXXXXX     X  XX |3
 XX     X    XX XXX |4
XXX    XX   XXXXX X |5
```
**Example:** Use `--random-rule` to pick a rule at random.
```
./elementary.py 1 --random-rule --pad 40 --pad-side both
🤖🎲 Picked rule 133
                    X                   
XXXXXXXXXXXXXXXXXXX X XXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXX  X  XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX   X   XXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXX  X X X  XXXXXXXXXXXXXXX
XXXXXXXXXXXXXXX   X X X   XXXXXXXXXXXXXX
XXXXXXXXXXXXXX  X X X X X  XXXXXXXXXXXXX
```
**Example:** Use `--no-wrap` to prevent edges from wrapping. Compare the output of the 20th generation.
```
./elementary.py 1 -p 20 --counter
XX X    XXX XXXX   X|19
 XXX   XX XXX  X  XX|20
XX X  XXXXX X XX XXX|21

 ./elementary.py 1 -p 20 --counter --no-wrap
XX X    XXX XXXX   X|19
XXXX   XX XXX  X  XX|20
X  X  XXXXX X XX XXX|21
```

### Todo
- allow setting the initial iteration that should actually be output
   --range 0 1000 = show-from show-to
- add a --stats flag that outputs the number of iterations and how long it took to run (only makes sense w/ 0 delay...)
- allow saving state to file and resuming from save (periodically or when exit). 
    this would be more like a json blob that includes recent history, and not just the last generation
- allow outputting to image e.g. -output 110.png (only valid when capped number iterations via range)
- move from strings to integer arrays and then bytes to be ⚡️?
- add a flag to exit if pattern stabilises (repeats itself indefinitely) (e.g. --limit-repeats 3). need an associated parameter to set how much history to keep in memory.
