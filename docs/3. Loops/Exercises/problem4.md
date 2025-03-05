# My Plates

![Plates](../../images/myplates.jpg){ width="300" }


In NSW, home to Killarney Heights High School, it’s possible to [request custom license plate](https://www.myplates.com.au) for your vehicle, with your choice of letters and numbers instead of random ones. There are few requirements for custom license plates apart from offensive words and profanity.

Some countries have requirements like the following:

- "All plates must start with at least two letters."
- “plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

In `plates.py`, implement a program that prompts the user for a number plate and then output `Valid` if meets all of the requirements or `Invalid` if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein `is_valid` returns `True` if `s` meets all requirements and `False` if it does not. Assume that s will be a `str`. You’re welcome to implement additional functions for `is_valid` to call (e.g., one function per requirement).
```
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()
```

??? Hints
    - Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
    - Much like a `list`, a `str` is a “sequence” (of characters), which means it can be [“sliced”](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) into shorter strings with syntax like `s[i:j]`. For instance, if `s` is `"CS50"`, then `s[0:2]` would be "CS".

## Before You Begin
From the root of your repository execute `cd src/loops` So your current working directory is ...
```
src/loops $:
```
Next execute
```
code plates.py
```
to make a file called `plates.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python plates.py`. Type `CS50` and press Enter. Your program should output:
```
Valid
```
2. Run your program with `python plates.py`. Type `CS05` and press Enter. Your program should output:
```
Invalid
```
3. Run your program with `python plates.py`. Type `CS50P` and press Enter. Your program should output
```
Invalid
```
4. Run your program with `python plates.py`. Type `PI3.14` and press Enter. Your program should output
```
Invalid
```
5. Run your program with `python plates.py`. Type `H` and press Enter. Your program should output
```
Invalid
```
6. Run your program with `python plates.py`. Type `OUTATIME` and press Enter. Your program should output
```
Invalid
```

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\loops\plates.py
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

At the `/loops $` prompt in your terminal:
```
git add -A 
```
Add all changed files in the repository to be committed
```
git commit -m "Upload completed plates.py"
```
Commit all changes in the REPO with the comment “Upload completed plates.py“ note: If the file is not complete, adjust the comment to describes what is being committed
```
git push 
```
Push all changes to the repo.