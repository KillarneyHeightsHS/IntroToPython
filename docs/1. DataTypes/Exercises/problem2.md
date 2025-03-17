# Colour Code Creator

You're designing a website and need to work with color codes. Create a program that converts RGB color values (decimal) to hexadecimal color codes.

## Instructions
- Write a function `rgb_to_hex` that takes three integers representing the red, green, and blue components of a color.
- The function should return a string representing the hexadecimal color code in the format `#RRGGBB`.

??? Hints
    - Remember that RGB values range from 0-255
    - Use Python's built-in hex() function, but you'll need to format the output correctly
    - The final format should be "#RRGGBB" (like "#FF0000" for red)

The boilerplate code has been provided for you. Open the file `src/datatypes/color_code.py` in vscode. You will need to implement the function `rgb_to_hex`. 

## How to test
 1. Run your program with `python color_code.py`.
 2. Try changing the function calls in the `if __name__ == "__main__":` block and see if it works as expected.
 
``` python
if __name__ == "__main__":
    print(rgb_to_hex(255, 0, 0))  # Expected output: "#FF0000"
    print(rgb_to_hex(0, 255, 0))  # Expected output: "#00FF00"
    print(rgb_to_hex(0, 0, 255))  # Expected output: "#0000FF"
```    

## How to Submit
From github desktop or the command line, commit your changes and push them to your repository.

## Codespaces
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
git commit -m "Upload completed colour_code.py"
```
Commit all changes in the REPO with the comment “Upload completed colour_code.py“ note: If the file is not complete, adjust the comment to describes what is being committed
```
git push 
```
Push all changes to the repo.