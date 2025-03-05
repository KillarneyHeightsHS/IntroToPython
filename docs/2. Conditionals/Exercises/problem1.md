# Deep Thought

    “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
    “You’re really not going to like it,” observed Deep Thought.
    “Tell us!”
    “All right,” said Deep Thought. “The Answer to the Great Question…”
    “Yes…!”
    “Of Life, the Universe and Everything…” said Deep Thought.
    “Yes…!”
    “Is…” said Deep Thought, and paused.
    “Yes…!”
    “Is…”
    “Yes…!!!…?”
    “Forty-two,” said Deep Thought, with infinite majesty and calm.”

    — The Hitchhiker’s Guide to the Galaxy, Douglas Adams

In `deep.py`, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise output `No`.

??? Hints
    - No need to convert the user’s input to an `int` if you check for equality with `"42"`, a `str`, rather than `42`, an `int`!
    - It’s okay if your output or the user’s wraps onto multiple lines.

## Before You Begin
From the root of your repository execute `cd conditionals` So your current working directory is ...		
```
/conditionals $:
```
Next execute
```
code deep.py
```
to make a file called `deep.py` where you’ll write your program.

!!! success
    Your program must have a function call `deep_thought` that takes 1 argument, a string. The function must return a boolean value of `True` if the argument is equal to `"42"`, case insensitive `"Forty Two"`, or `"forty-two"`, otherwise it returns `False`. Your `main()` function should call the function with user input, print the result of that function call to the console.

## How to Test
Here’s how to test your code manually. At the `deep/ $` prompt in your terminal: :

1. Run your program with `python deep.py`. Type `42` and press Enter. Your program should output:
```
Yes
```
2. Run your program with `python deep.py`. Type `Forty Two` and press Enter. Your program should output:
```
Yes
```
3. Run your program with `python deep.py`. Type `forty-two` and press Enter. Your program should output:
```
Yes
```
4. Run your program with `python deep.py`. Type `50` and press Enter. Your program should output:
```
No
```

You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\conditionals\test_deep.py
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