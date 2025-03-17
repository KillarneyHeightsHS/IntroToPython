# Binary Bit Manipulation Challenge

You're writing security software that needs to encrypt data using bitwise operations. Create a program that demonstrates how to manipulate individual bits in a byte of data.

??? Hints
    - Research Python's bitwise operators: & (AND), | (OR), ^ (XOR), ~ (NOT), <<    (left - shift), >> (right shift)
    - To flip a specific bit, use the XOR operator with a value that has only that  bit - set
    - Visualise the binary representations at each step to understand what's happening
    - Challenge: Add a function that rotates bits left or right in a circular pattern

Boilerplate code has been provided for you. Complete the functions and add tests to ensure your program works as expected.

# How to Test
Here is how to test you code manually. At the `datatypes/ $` prompt in your terminal: :

1. Run your program with `python security.py`. Check that the default values in the program are correctly encrypted and decrypted.

2. Add additional values to check if the code works. Sometimes it is easier to start with a small number as you can desk check your work.

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\datatypes\test_security.py
```

A green output from running the test means it was successful. A red output means there is a bug in your code that you need to fix.

## How to Submit

From github desktop or the command line, commit your changes and push them to your repository.

### Codespaces
If you are using codespaces, you can commit your changes directly from the Codespace interface. Click on the Source Control icon in the left sidebar, then click on the "..." button and select "Commit to main". Enter a commit message and click "Commit".

#### Codespace terminal or your local terminal. 

!!! Note
    You will need to have installed `git-scm` for this to work locally

At the `/datatypes/security $` prompt in your terminal:
```
git add -A 
```
Add all changed files in the repository to be committed
```
git commit -m "Upload completed security.py"
```
Commit all changes in the REPO with the comment “Upload completed security.py“ note: If the file is not complete, adjust the comment to describes what is being committed
```
git push 
```
Push all changes to the repo.