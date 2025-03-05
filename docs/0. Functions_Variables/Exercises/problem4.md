# Einstein

Even if you haven’t studied physics (recently or ever!), you might have heard that $E=mc^2$, wherein $E$ represents energy (measured in Joules), $m$ represents mass (measured in kilograms), and $c$ represents the speed of light (measured approximately as 300000000 meters per second), per [Albert Einstein et al](https://en.wikipedia.org/wiki/Albert_Einstein). Essentially, the formula means that mass and energy are equivalent.

In a file called `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer. There should be a function called `realativity`, which takes an integer as input and returns an integer representing the equivalent number of Joules.


??? Tip
    - Recall that `input` returns a `str`, per [input](https://docs.python.org/3/library/functions.html#input).
    - Recall that a `str` comes with quite a few methods, per [string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
    - Recall that Python comes with several built-in functions, per [functions](https://docs.python.org/3/library/functions.html).

## Before You Begin

1. Ensure you are in the root directory of the repository that you cloned to your machine.
2. Change directory to `src/function_variables/` in your terminal window.
```
cd src/function_variables/
```
3. create or open the file `einstein.py`
```
code einstein.py
```
This is where you’ll write your program.

## How to Test

### Here’s how to test your code manually:

- Run your program with `python einstein.py`. Type `1` and press ++enter++. Your program should output:
```
    90000000000000000
```
- Run your program with `python einstein.py`. Type `14` and press ++enter++. Your program should output:
```
    1260000000000000000
```
- Run your program with `python einstein.py`. Type `50` and press ++enter++. Your program should output
```
    4500000000000000000
```

You can execute the below to check your code using `pytest` from the root directory.

```
.\tests\function_variables\test_faces.py
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