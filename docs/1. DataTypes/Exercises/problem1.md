# Secret Code Translator

You're developing a secret messaging app for your friends. Create a program that converts text messages into their ASCII decimal values and back again.

??? Hints
    - Use Python's `ord()` function to convert a character to its ASCII value
    - Use `chr()` to convert an ASCII value back to a character
    - Try storing the decimal values in a list. A list in python is a collection of items which can be of different types. You can store any type of data in a list, such as integers, strings, floats, etc. 
    ``` python
    # List example
    my_list = [1, 2, 3, "hello", 4.5]
    for item in my_list:
        print(item)
    ```

## Before You Begin
The boilerplate code has been provided for you. Open the file `src/datatypes/translator.py` in vscode. You will need to implement two functions: `text_to_decimal()` and `decimal_to_text()`. 

The first function should take a string as input and return a list of integers representing the ASCII values of each character in the string. 

The second function should take a list of integers as input and return a string that is the concatenation of the characters represented by those ASCII values.

## How to test
1. Run your program with `python translator.py`.
2. Try changing the function calls in the `if __name__ == "__main__":` block and see if it works as expected.
```python
if __name__ == "__main__":
    # Test with a secret message
    secret = text_to_decimal("Hi, my name is Slim Shady!")
    print(secret)
    decoded = decimal_to_text(secret)
    print(decoded)
```

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