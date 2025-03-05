# Making Faces

Before there were emoji, there were [emoticons](https://en.wikipedia.org/wiki/List_of_emoticons){target="_blank"}, whereby text like `:)` was a happy face and text like `:(` was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called `faces.py`, implement a function called `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂 (otherwise known as a [slightly smiling face](https://emojipedia.org/slightly-smiling-face/)) and any :( converted to 🙁 (otherwise known as a [slightly frowning face](https://emojipedia.org/slightly-frowning-face/)). All other text should be returned unchanged.

Then, in that same file, implement a function called `main` that prompts the user for input, calls `convert` on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to input. Be sure to call `main` at the bottom of your file.

??? Tip
    - Recall that `input` returns a `str`, per [input](https://docs.python.org/3/library/functions.html#input).
    - Recall that a `str` comes with quite a few methods, per [string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
    - An emoji is actually just a character, so you can quote it like any `str`, a la `"😐"`. And you can copy and paste the emoji from this page into your own code as needed.

## Before You Begin

1. Ensure you are in the root directory of the repository that you cloned to your machine.
2. Change directory to `src/function_variables/` in your terminal window.
```
cd src/function_variables/
```
3. create or open the file `faces.py`
```
code faces.py
```
This is where you’ll write your program.

## How to Test

### Here’s how to test your code manually:

- Run your program with python faces.py. Type `Hello :)` and press Enter. Your program should output:
```
Hello 🙂
```
- Run your program with python faces.py. Type `Goodbye :(` and press Enter. Your program should output:
```
Goodbye 🙁
```
- Run your program with python faces.py. Type `Hello :) Goodbye :(` and press Enter. Your program should output
```
Hello 🙂 Goodbye 🙁
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