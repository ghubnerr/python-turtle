# Python Turtle Daniel Hirst Art
By running, `main.py`, the code uses the `colorgram` external library to pick the most abundant colors in an image. My personal favourite -- Van Gogh's "A Stary Night" -- was used in this code as sample for the module. The turtle will create a Daniel Hirst-inspired "dot-art" style using the colors seleted from the `colorgram` package. Feel free to adjust the dot-sizes, gaps, number of rows as well as number of dots per row as you call for the `draw()` function inside `main.py`.

You can also download your own image files, pass its address in your shell as the argument of the `colorgram` color-picking function to run this code on your own images as well.

![image](https://github.com/ghubnerr/python-turtle/assets/91924667/531665f4-3ec1-4894-8160-f08db61a4aa3)

P.S.: Kevin, the turtle, is hidden in this snippet of the code as it makes the code run more smoothly

This repository also contains Python code for creating spirographs and printing the Google logo using the Turtle graphics library, as well as some basic instructions and documentation links on how to use this library :)

## Spirographs -- Additional Segment

The spirograph module allows you to create intricate geometric patterns known as spirographs. Spirographs are created by rolling a small circle inside or outside a larger fixed circle, while a pen traces the resulting curves.

Here, Kevin the Turtle is given the number of circles to be made in the spirograph, and loops through that amount 'n' while making a 360/n degree turn for every circle that it draws, while at the same time choosing a random color from an RGB generator to make the spirograph look prettier. 

To run the spirograph program, execute the `spirograph.py` script. You can customize the spirograph patterns by modifying the parameters such as radii, and speeds within the code.

## Google Logo -- Additional Segment

The `google-logo.py` script demonstrates how to draw the Google logo using Python Turtle. It recreates the iconic multi-colored logo of the search engine giant by using the appropriate colors and positioning.

To print the Google logo, run the `google-logo.py` script. Make sure the `turtle` module is installed on your Python environment.

## Tutorial and Documentation

Although these instructions are already contained within the `tutorial.py` file, if you are new to Python Turtle or need a refresher, here are some resources to get started:

- [Python Turtle Documentation](https://docs.python.org/3/library/turtle.html) - Official Python documentation for the Turtle graphics library.
- [Turtle Graphics Tutorial](https://realpython.com/beginners-guide-python-turtle/) - A beginner-friendly tutorial on Turtle graphics from Real Python.
- [Spirograph Tutorial](https://en.wikipedia.org/wiki/Spirograph) - Wikipedia article explaining the principles and history of spirographs.

Feel free to explore this code and modify it.

## Credit

The idea for this Project was inspired by Dr. Angela Yu, from the App Brewery on here Python 100 Days of Code Bootcamp for Udemy.

## License

This project is licensed under the [MIT License](LICENSE).
