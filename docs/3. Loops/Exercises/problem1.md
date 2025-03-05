# camelCase
![camelCase](../../images/CamelCase.png) 
Source: [en.wikipedia.org/wiki/Camel_case](https://en.wikipedia.org/wiki/Camel_case)

In some languages, it’s common to use [camel case](https://en.wikipedia.org/wiki/Camel_case) (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called `name`, a variable for a user’s first name might be called `firstName`, and a variable for a user’s preferred first name (e.g., nickname) might be called `preferredFirstName`.

Python, by contrast, [recommends](https://peps.python.org/pep-0008/#function-and-variable-names) [snake case](https://en.wikipedia.org/wiki/Snake_case), whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called `name`, `first_name`, and `preferred_first_name`, respectively, in Python.

In a file called `camel.py`, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

??? Hints
    - Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
    - Much like a `list`, a `str` is “iterable,” which means you can iterate over each of its characters in a loop. For instance, if `s` is a `str`, you could print each of its characters, one at a time, with code like:
    ```py
		for c in s:
    		print(c, end="")
    ```

## Before You Begin
From the root of your repository execute `cd src/2-Loops` So your current working directory is ...		
```bash
/src/2-Loops $:
```
Next execute
```bash
code camel.py
```
to make a file called `camel.py` where you’ll write your program.

!!! success
    Your program must have a function called `camel_to_snake` that takes a string as input and returns a new string with all of its camelCase words converted to snake_case. Your `main` function must call this function with a user input string and print the result.

## How to Test
Here’s how to test your code manually:

1. Run your program with `python camel.py`. Type `name` and press ++enter++. Your program should output:
```
name
```
2. Run your program with `python camel.py`. Type `firstName` and press ++enter++. Your program should output:
```
first_name
```
3. Run your program with `python camel.py`. Type `preferredFirstName` and press ++enter++. Your program should output
```
preferred_first_name
```

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\loops\test_camel.py
```

A green output from running the test means it was successful. A red output means there is a bug in your code that you need to fix.

## How to Submit

From github desktop or the command line, commit your changes and push them to your repository.

### Commandline 
You will need to have installed `git-scm` for this to work.

```bash
git add -A
git commit -m "Your message here"
git push origin main
```

### Codespaces
If you are using codespaces, you can commit your changes directly from the Codespace interface. Click on the Source Control icon in the left sidebar, then click on the "..." button and select "Commit to main". Enter a commit message and click "Commit".

### Codespace terminal 

At the `/loops/camel $` prompt in your terminal:
```
git add -A 
```
Add all changed files in the repository to be committed
```
git commit -m "Upload completed camel.py"
```
Commit all changes in the REPO with the comment “Upload completed camel.py“ note: If the file is not complete, adjust the comment to describes what is being committed
```
git push 
```
Push all changes to the repo.