import turtle
import random

# Set up the screen
screen = turtle.Screen()
turtle.setup(width=1000, height = 850)

# Set the background image (make sure the image path is correct)
screen.bgpic("race_track2.png")

# Create a turtle object to draw
screen.addshape("grits.gif")
screen.addshape("mabel.gif")
screen.addshape("dolly.gif")
screen.addshape("evan.gif")


def RadRatRace():
    # Create turtle objects for each character
    grits = turtle.Turtle()
    grits.shape("grits.gif")
    grits.speed(100)
    grits.penup()
    grits.goto(-400, 70)

    mabel = turtle.Turtle()
    mabel.shape("mabel.gif")
    mabel.speed(100)
    mabel.penup()
    mabel.goto(-400, -45)
    
    dolly = turtle.Turtle()
    dolly.shape("dolly.gif")
    dolly.speed(100)
    dolly.penup()
    dolly.goto(-400, -170)

    evan = turtle.Turtle()
    evan.shape("evan.gif")
    evan.speed(100)
    evan.penup()
    evan.goto(-400, -285)

    # Ask user to choose a rat racer
    player_character = input("Please choose your rat racer (grits, mabel, dolly, evan): ").lower()
    print(f"Your racer is: {player_character}")
    
    # Open CSV files and count lines (representing movements)
    with open("rat_movement1.csv") as csv1:
        movement1 = len(csv1.readlines())
    with open("rat_movement2.csv") as csv2:
        movement2 = len(csv2.readlines())
    with open("rat_movement3.csv") as csv3:
        movement3 = len(csv3.readlines())
    with open("rat_movement4.csv") as csv4:
        movement4 = len(csv4.readlines())

    # Randomly assign each turtle a movement file
    movements = [movement1, movement2, movement3, movement4]
    random.shuffle(movements)  # Shuffle the list of movements randomly

    # Assign shuffled movements to turtles
    turtles = [grits, mabel, dolly, evan]
    distances = {}  # Dictionary to store the final distance each turtle moves

    for i, t in enumerate(turtles):
        movement = movements[i]
        print(f"{t.shape()} will move {movement} steps.")
        t.forward(movement)  # Move the turtle
        distances[t.shape()] = movement  # Store the final movement distance for each turtle

    # Check if the player's character has won
    if player_character == "grits" and distances["grits.gif"] >= 800:
        print("You Win!")
    elif player_character == "mabel" and distances["mabel.gif"] >= 800:
        print("You Win!")
    elif player_character == "dolly" and distances["dolly.gif"] >= 800:
        print("You Win!")
    elif player_character == "evan" and distances["evan.gif"] >= 800:
        print("You Win!")
    else:
        print("You Lose. Better Luck next time!")
        
#RAT RACE!
RadRatRace()
