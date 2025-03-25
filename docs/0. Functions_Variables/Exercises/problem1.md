# Indoor Voice

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, by passing a `str` of your own as an argument to `input`.

??? Tip
    - Recall that input returns a str, per [functions](https://docs.python.org/3/library/functions.html#input).
    - Recall that a str comes with quite a few methods, per [string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Before You Begin

1. Ensure you are in the root directory of the repository that you cloned to your machine.
2. Change directory to `src/function_variables/` in your terminal window.
```
cd src/function_variables/
```
3. create or open the file `indoor.py`
```
code indoor.py
```
This is where you’ll write your program.

## How to Test
Here’s how to test your code manually. At the indoor/ $ prompt in your terminal:

- Run your program with `python indoor.py`. Type `HELLO` and press ++enter++. Your program should output `hello`.
- Run your program with `python indoor.py`. Type `THIS IS CS50` and press ++enter++. Your program should output `this is cs50`.
- Run your program with `python indoor.py`. Type `50` and press ++enter++. Your program should output `50`.

If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `function_variables` folder and have saved your `indoor.py` file there. Remember how?

You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\function_variables\test_indoor.py
```

A green output from running the test means it was successful. A red output means there is a bug in your code that you need to fix.

```
============================= test session starts ===============================
platform win32 -- Python 3.13.1, pytest-7.2.2, pluggy-1.5.0
rootdir: C:\Users\jabba\khhs\github\IntroToPython, configfile: pyproject.toml
plugins: cov-4.0.0
collected 1 item                                                                                                                                                                                                                                                       

tests\function_variables\test_indoor.py .                                                                                                                                                                                                                                  [100%] 

========================= 1 passed in 0.03s ========================================

```

## How to Submit

From github desktop or the command line, commit your changes and push them to your repository.

### Codespaces
If you are using codespaces, you can commit your changes directly from the Codespace interface. Click on the Source Control icon in the left sidebar, then click on the "..." button and select "Commit to main". Enter a commit message and click "Commit".

#### Codespace terminal or your local terminal. 

!!! Note
    You will need to have installed `git-scm` for this to work locally

At the `/functions_variables $` prompt in your terminal:
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