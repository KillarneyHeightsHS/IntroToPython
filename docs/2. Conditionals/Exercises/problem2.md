# Home Federal Savings Bank

Watch: [Season 7, Episode 24 Seinfeld](https://youtu.be/IN6cJ_wGmsk)

In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give `$100` to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for `$100`. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does `$20` sound?” Kramer accepts.

In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output `$0`. If the greeting starts with an “h” (but not “hello”), output `$20`. Otherwise, output `$100`. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

??? Hints
    - Recall that a str comes with quite a few methods, per https://docs.python.org/3/library/stdtypes.html#string-methods.
    - Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

## Before You Begin

From the root of your repository execute cd `conditionals` So your current working directory is ...
```
/conditionals $:
```
Next execute
```
code bank.py
```
to make a file called bank.py where you’ll write your program.

!!! success
    Your program must have a function call `greeting` that takes a string as an argument and returns an integer. Your `main` function must call this function and print the result.

## How to Test

Here’s how to test your code manually. At the bank/ $ prompt in your terminal:

Run your program with python bank.py. Type `Hello` and press ++enter++. Your program should output:
```
$0
```
Run your program with python bank.py. Type `Hello, Newman` and press ++enter++. Your program should output:
```
$0
```
Run your program with python bank.py. Type `How you doing?` and press ++enter++. Your program should output:
```
$20
```
Run your program with python bank.py. Type` What's happening?` and press ++enter++. Your program should output:
```
$100
```

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\conditionals\test_bank.py
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