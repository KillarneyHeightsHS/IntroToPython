# Math Interpreter

Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called `interpreter.py`, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as `x` `y` `z`, with one space between `x` and `y` and one space between `y` and `z`, wherein:

- `x` is an integer
- `y` is `+`, `-`, `*`, or `/`
- `z` is an integer

For instance, if the user inputs `1 + 1`, your program should output `2.0`. Assume that, if `y` is `/`, then `z` will not be `0`.

Note that, just as `python` itself is an interpreter for Python, so will your `interpreter.py` be an interpreter for math!

??? Hints
    - Recall that a `str` comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>, including `split`, which separates a `str` into a sequence of values, all of which can be assigned to variables at once. 
    
    For instance, if `expression` is a `str` like `1 + 1`, then
    ```
	x, y, z = expression.split(" ")
    ```
    will assign `1` to `x`, `+` to `y`, and `1` to `z`.

## Before You Begin
From the root of your repository execute `cd conditionals` So your current working directory is ...		
```
/conditionals $:
```
Next execute
```
code interpreter.py
```
to make a file called `interpreter.py` where you’ll write your program.

!!! success
    Your program must have a function called `calculate` that takes 3 parameters: `x`, `y`, and `z`. These parameters will be strings representing numbers or mathematical operators. For example, if the user types `1 + 1`, then `x` would be `"1"`, `y` would be `"+"`, and `z` would be `"1"`. It should return the result of the calculation as a float.

# How to Test
Here’s how to test your code manually. At the `conditionals/ $` prompt in your terminal: :

1. Run your program with `python interpreter.py`. Type `1 + 1` and press Enter. Your program should output:
```
2.0
```
2. Run your program with `python interpreter.py`. Type `2 - 3` and press Enter. Your program should output:
```
-1.0
```
3. Run your program with `python interpreter.py`. Type `2 * 2` and press Enter. Your program should output:
```
4.0
```
4. Run your program with `python interpreter.py`. Type `50 / 5` and press Enter. Your program should output:
```
10.0
```

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\conditionals\test_interpreter.py
```

A green output from running the test means it was successful. A red output means there is a bug in your code that you need to fix.

## How to Submit

From github desktop or the command line, commit your changes and push them to your repository.

### Codespaces
If you are using codespaces, you can commit your changes directly from the Codespace interface. Click on the Source Control icon in the left sidebar, then click on the "..." button and select "Commit to main". Enter a commit message and click "Commit".

#### Codespace terminal or your local terminal. 

!!! Note
    You will need to have installed `git-scm` for this to work locally

At the `/datatypes $` prompt in your terminal:
```
git add -A 
```
Add all changed files in the repository to be committed
```
git commit -m "your message here"
```
Commit all changes in the REPO with the comment “your message here“ note: If the file is not complete, adjust the comment to describes what is being committed
!!! Note
    Remember to replace "your message here" with a meaningful commit message that describes your changes.

```
git push 
```
Push all changes to the repo.