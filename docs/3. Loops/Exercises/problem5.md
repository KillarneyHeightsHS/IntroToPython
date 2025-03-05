# Nutrition Facts

Food Standards Australia and New Zealand offers an [online database](https://afcd.foodstandards.gov.au/default.aspx) for over 1600 foods with detailed nutritional information.

In a file called `nutrition.py`, implement a program that prompts ~~consumers~~ users to input a fruit (case-insensitively) and then outputs the number of kilojoules in 100g of that fruit or vegetable, per the table below. Capitalisation aside, assume that users will input fruits exactly as written in the table (e.g., `strawberries`, not `strawberry`). Ignore any input that isn’t a fruit.

??? Hints
    - Rather than use a conditional with 20 Boolean expressions, one for each fruit, better to use a `dict` to associate a fruit with its calories!
    - If `k` is a `str` and `d` is a `dict`, you can check whether `k` is a key in `d` with code like:

            if k in d:
                ...
    - Take care to output the fruit’s calories, not calories from fat!

## Data
| Fruit | Calories (Kilojoules per 100g) |
|-------|--------------------------|
| Apple          | 227       |
| Apricot        | 167       |
| Avocado        | 579      |
| Banana         | 394       |
| Blackberries   | 211      |
| Blueberries   | 194       |
| Cherries       | 250       |
| Feijoa     | 176       |
| Leek            | 136       |
| Mushroom        | 87        |
| Onion           | 139       |
| Peas            |  294      |
| Capsicum   | 115       |
| Potato          | 272       |
| Pumpkin         | 189       |
| Radish          | 62       |
| Strawberries  | 108 |

## Before You Begin
From the root of your repository execute `cd src/loops` So your current working directory is ...
```
src/loops $:
```
Next execute
```
code nutrition.py
```
to make a file called `nutrition.py` where you’ll write your program.

## How to Test
Here’s how to test your code manually:

1. Run your program with `python nutrition.py`. Type `Apple` and press Enter. Your program should output:
```
kilojoules: 227
```
2. Run your program with `python nutrition.py`. Type `Avocado` and press Enter. Your program should output:
```
kilojoules: 579
```
3. Run your program with `python nutrition.py`. Type `Cherries` and press Enter. Your program should output
```
kilojoules: 250
```
4. Run your program with `python nutrition.py`. Type `Tomato` and press Enter. Your program should output `No data available for this fruit.`

5. Be sure to try other fruits and vary the casing of your input. Your program should behave as expected, case-insensitively.

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\loops\nutrition.py
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
git commit -m "Upload completed nutrition.py"
```
Commit all changes in the REPO with the comment “Upload completed nutrition.py“ note: If the file is not complete, adjust the comment to describes what is being committed
```
git push 
```
Push all changes to the repo.