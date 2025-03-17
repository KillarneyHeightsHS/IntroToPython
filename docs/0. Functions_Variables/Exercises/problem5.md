# GST Calculator

Some countries charge GST ([goods and services tax](https://treasury.gov.au/review/tax-white-paper/chart-data/8-the-goods-and-services-tax-and-state-taxes){:target="_blank"}), which is paid on most services and purchased items. This tax is:

- 10% in Australia
- 15% in New Zealand
- 17% in China. 

Write a program that prompts the user for the amount of their purchase and the percentage the country charges for GST. The program should print GST amount being charged on their purchase. For example, if the user inputs `$100` and `10%`, the program should output $10.00.

!!! Warning
    Symbols like ¥ and £ are non ASCII characters and should not be used in this program. Only use ASCII characters for now. We will cover internationalisation (I18n) in a later lesson.


```py
def main():
    purchase = input("How much was the purchase? ")
    percentage = input("What percentage is the GST rate? ")
    gst = calculate_gst(purchase, percentage)
    print(f"GST will be ${gst:.2f}")

def calculate_gst(purchase, percentage):
    price = currency_to_float(purchase)
    percent = percent_to_float(percentage)
    gst = price * percent

    return gst


def currency_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
```

Well, we’ve written most of a GST calculator for you. Unfortunately, we didn’t have time to implement two functions:

- `currency_to_float`, which should accept a `str` as input (formatted as `$##.##,` wherein each `#` is a decimal digit), remove the leading `$`, and return the amount as a `float`. For instance, given `$50.00` as input, it should return `50.0`.
- `percent_to_float`, which should accept a `str` as input (formatted as `##%,` wherein each `#` is a decimal digit), remove the trailing `%`, and return the percentage as a `float`. For instance, given `15%` as input, it should return `0.15`.

Assume that the user will input values in the expected formats.

??? Tip
    - Recall that `input` returns a `str`, per [input](https://docs.python.org/3/library/functions.html#input).
    - Recall that a `str` comes with quite a few methods, per [string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
    - Recall that `float` can convert a `str` to a `float`, per [float](https://docs.python.org/3/library/functions.html#float).

## Before You Begin

1. Ensure you are in the root directory of the repository that you cloned to your machine.
2. Change directory to `src/function_variables/` in your terminal window.
```
cd src/function_variables/
```
3. create or open the file `gst.py`
```
code gst.py
```
This is where you’ll write your program.

## How to Test

### Here’s how to test your code manually:

Run your program with python gst.py. Type $50.00 and press Enter. Then, type 15% and press Enter. Your program should output:
```
GST will be $7.50    
```
Run your program with python gst.py. Type $100.00 and press Enter. Then, type 18% and press Enter. Your program should output:
```
GST will be $18.00
```
Run your program with python gst.py. Type ¥15.00 and press Enter. Then, type 17% and press Enter. Your program should output:
```
GST will be ¥3.75
```

You can execute the below to check your code using `pytest` from the root directory.

```
.\tests\function_variables\test_gst.py
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