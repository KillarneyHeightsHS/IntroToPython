# Playback Speed

Some people have a habit of ~~lecturing~~ speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with `...` (i.e., three periods).

## Hints
??? Tip
    - Recall that input returns a str, per [input](http://docs.python.org/3/library/functions.html#input).
    - Recall that a `str` comes with quite a few methods, per [string-methods](http://docs.python.org/3/library/stdtypes.html#string-methods).

## Before You Begin

1. Ensure you are in the root directory of the repository that you cloned to your machine.
2. Change directory to `src/function_variables/` in your terminal window.
```
cd src/function_variables/
```
3. create or open the file `playback.py`
```
code indoor.py
```
This is where you’ll write your program.

## How to Test

Here’s how to test your code manually:

- Run your program with `python playback.py`. Type `This is Killarney Heights!` and press ++enter++. Your program should output:
```
    This...is...Killarney...Heights! 
```

- Run your program with `python playback.py`. Type `This is our week on functions` and press ++enter++. Your program should output:
```
    This...is...our...week...on...functions
```
- Run your program with `python playback.py`. Type `Let's implement a function called hello` and press ++enter++. Your program should output
```
    Let's...implement...a...function...called...hello
```

You can execute the below to check your code using `pytest` from the root directory.

```
.\tests\function_variables\test_playback.py
```

A green output from running the test means it was successful. A red output means there is a bug in your code that you need to fix.

## How to Submit

From github desktop or the command line, commit your changes and push them to your repository.

### Commandline 
You will need to have installed `git-scm` for this to work.

```bash
git add .
git commit -m "Your message here"
git push origin main
```