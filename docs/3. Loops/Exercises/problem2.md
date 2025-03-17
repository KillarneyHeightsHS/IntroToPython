# Ginger Beer Machine

![ginger beer](../../images/ginger_beer.jpg)

Suppose that a machine sells bottles of Ginger Beer for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called `ginger_beer_machine.py`, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

!!! Note
    The commandline supports tab completion. You can use tab to complete commands or filenames after typing the first few characters of a command or filename.

## Before You Begin
From the root of your repository execute `cd src/loops` So your current working directory is ...		
```
src/loops $:
```
Next execute
```
code ginger_beer_machine.py
```
to make a file called `ginger_beer_machine.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:

1. Run your program with `python ginger_beer_machine.py`. At your `Insert Coin`: prompt, type `25` and press Enter. Your program should output:
```
Amount Due: 25
```
and continue prompting the user for coins.

2. Run your program with `python ginger_beer_machine.py`. At your `Insert Coin`: prompt, type `10` and press Enter. Your program should output:
```
Amount Due: 40
```
and continue prompting the user for coins.

3. Run your program with `python ginger_beer_machine.py`. At your `Insert Coin`: prompt, type `5` and press Enter. Your program should output:
```
Amount Due: 45
```
and continue prompting the user for coins.

4. Run your program with `python ginger_beer_machine.py`. At your `Insert Coin`: prompt, type `30` and press Enter. Your program should output:
```
Amount Due: 50
```
because the machine doesn’t accept 30-cent coins! Your program should then continue prompting the user for coins.

5. Run your program with `python ginger_beer_machine.py`. At your `Insert Coin`: prompt, type `25` and press Enter, then type `25` again and press Enter. Your program should halt and display:
```
Change Owed: 0
```
6. Run your program with `python ginger_beer_machine.py`. At your Insert Coin: prompt, type `25` and press Enter, then type 10 and press Enter. Type `25` again and press Enter, after which your program should halt and display:
```
Change Owed: 10
```

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\loops\test_ginger_beer_machine.py
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