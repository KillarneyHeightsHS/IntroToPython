# Binary Data Visualiser

You're developing an educational tool that helps students visualise binary-to-decimal and decimal-to-binary conversions. Create a program that not only performs the conversions but also shows each step of the process visually.

??? Hints
    - You may want to look at lists, loops and string formatting for creating a clear output.
    - For binary to decimal conversion:
        - Create a visual representation showing each bit position (from right to left)
        - Display the power of 2 for each position
        - Show the contribution of each bit to the final sum when it's 1
        - Use string formatting to create an aligned, easy-to-read output
    - For decimal to binary conversion:
        - Show each step of the "divide by 2" algorithm
        - Display both the quotient and remainder at each step
        - Demonstrate how the remainders, read from bottom to top, form the binary result
        - Consider adding a visual representation like a division ladder

- Test with different numbers to ensure your visualisation works for various lengths of binary and decimal values
- **Challenge extension:** Add a graphical representation using ASCII art or simple console graphics to make the powers of 2 more visually apparent

## Before You Begin
The boilerplate code has been provided for you. Open the file `src/datatypes/numbers.py` in vscode.


## How to test
1. Run your program with `python numbers.py`.
2. Try changing the function calls in the `if __name__ == "__main__":` block and see if it works as expected.

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
git commit -m "Upload completed numbers.py"
```
Commit all changes in the REPO with the comment “Upload completed numbers.py“ note: If the file is not complete, adjust the comment to describes what is being committed
```
git push 
```
Push all changes to the repo.