# Collatz Sequences (3n+1) - Collatz Conjecture Exploration

This script computes and stores Collatz sequences for integers from 1 to 10000, then prints the resulting dictionary of sequences.

The folder also contains a Manim animation that shows you a graphical depiction of the conjecture for the numbers 1-18 and their relations to each other.

## How to Execute

### Prerequisites
Make sure you have Python installed on your machine. If not, download and install Python from [python.org](https://python.org).

### Running the Calculation Script
1. Navigate to the main folder (YOUR_FOLDER_PATH/collatz_conjecture(3n+1)).
2. Execute the `main.py` script using Python:
    ```bash
    python main.py
    ```
   This will run the calculations and print the resulting dictionary of sequences to the console.

### Running the Manim Animation
1. Navigate to the main folder (YOUR_FOLDER_PATH/collatz_conjecture(3n+1)).
2. Make sure you have Manim installed. If not, install it according to the instructions provided on the Manim GitHub repository.
3. Execute the animation script `animation.py` using the following command:
    ```bash
    manim animation.py DynamicCameraScene -p -qh
    ```
   This will run the Manim animation and create a .mp4 video file in the `/collatz_conjecture(3n+1)/media/videos/animation/1080p60` directory.
