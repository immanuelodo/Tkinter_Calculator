This project is a simple calculator application developed using Python's Tkinter library, which is used to create graphical user interfaces.

First, I imported the Tkinter module and created the main application window. I set the window title as 'Calculator', changed the background color to black, and disabled resizing so that the window size remains fixed.

Next, I created an Entry widget that acts as the calculator's display. It uses a Segoe UI font with a size of 20, has a black background, white text, no border, and aligns the text to the right, just like a real calculator.

Then, I defined three functions. The press() function inserts the number or operator that the user clicks into the display. The clear() function removes all the text from the display. The calc() function evaluates the mathematical expression using Python's eval() function. If the expression is valid, it displays the result. If an invalid expression is entered, it catches the error and displays 'Error' instead of crashing the program.

After that, I created a list containing all the calculator buttons, including numbers, operators, the decimal point, and the equals sign. Using a for loop, I generated each button dynamically and arranged them in a grid layout. The equals button is linked to the calculation function, while the other buttons call the press() function. The operator buttons are displayed in blue, while the number buttons have a black background.

Finally, I added a red 'C' button that clears the display when clicked. The mainloop() function keeps the application running and waits for user interactions.

Overall, this project demonstrates my understanding of Python programming, GUI development using Tkinter, event handling, functions, loops, and exception handling while creating a functional and user-friendly calculator application."
