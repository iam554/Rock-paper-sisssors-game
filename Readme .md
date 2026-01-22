Rock Paper Scissors Game

Project Description

This project is a Rock Paper Scissors Game developed as part of a Software Engineering (SEN) assignment. The aim of the project is to demonstrate the complete Software Development Life Cycle (SDLC) while implementing a simple, functional software system.

The game allows a user to play against the computer, which randomly selects Rock, Paper, or Scissors, and the winner is determined based on standard game rules.

⸻

Objectives
 • Implement a Rock Paper Scissors game
 • Apply SDLC concepts in a real project
 • Ensure consistency between system design and implementation
 • Use Git and GitHub for version control

⸻

Technologies Used
 • Programming Language: Python 3
 • Version Control: Git
 • Repository Hosting: GitHub

⸻

How the Game Works
 1. The user enters rock, paper, or scissors.
 2. The computer randomly selects a choice.
 3. The system compares both choices using the rules:
 • Rock beats Scissors
 • Scissors beats Paper
 • Paper beats Rock
 4. The result (Win, Lose, or Draw) is displayed to the user.

⸻

Project Structure

rock-paper-scissors/
│
├── rock_paper_scissors.py
└── README.md


⸻

How to Run the Program
 1. Make sure Python 3 is installed on your system.
 2. Open a terminal or command prompt in the project directory.
 3. Run the program using the command:

python rock_paper_scissors.py


⸻

Testing

The application was tested using:
 • Valid inputs (rock, paper, scissors)
 • Invalid inputs to ensure proper error handling

All test cases produced the expected results.

⸻

SDLC Process

1. Planning

The objective of the project is to develop a simple Rock Paper Scissors game that allows a user to play against the computer. The scope includes a command-line interface, random computer choices, and result display.

2. Requirements Analysis

Functional Requirements:
 • The system shall allow the user to enter rock, paper, or scissors.
 • The system shall generate a random choice for the computer.
 • The system shall determine and display the game result.

Non-Functional Requirements:
 • The program should be easy to use.
 • The program should run efficiently with minimal delay.

3. System Design

The system is designed as a console-based application. The logic follows standard Rock Paper Scissors rules, and variables such as user_choice, computer_choice, and choices are used consistently in both design and implementation.

4. Implementation

The game is implemented in Python using a single file (rock_paper_scissors.py). The random module is used to generate the computer’s choice, and conditional statements are used to determine the winner.

5. Testing

The system was tested using different valid and invalid inputs to ensure correct winner determination and proper handling of errors.

6. Deployment

The application was deployed by pushing the source code to a GitHub repository using Git version control commands.

7. Maintenance

Future maintenance may include adding new features such as score tracking, replay functionality, or a graphical user interface.

⸻

Future Enhancements
 • Add score tracking
 • Add replay functionality
 • Implement a graphical user interface (GUI)
 • Support multiplayer mode

⸻

Author

Name: Eromonsele Inegbedion Iwenose
Matric Number: 24/14099