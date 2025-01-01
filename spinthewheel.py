import random
import time
import os
from colorama import Fore, init

init(autoreset=True)

resolutions = [
    "Learn Flask",
    "Master Pandas",
    "Build a Portfolio",
    "Explore AI/ML",
    "Crack Coding Interviews",
    "Contribute to Open Source",
    "Automate Tasks",
    "Master Python OOP",
    "Learn Web Scraping",
    "Develop Problem-Solving",
    "Understand Data Structures",
    "Learn Django",
    "Create a Machine Learning Model",
    "Write Unit Tests",
    "Build a Full-Stack App",
    "Master Git and GitHub",
    "Learn SQL Databases",
    "Understand Cloud Computing",
    "Work with APIs",
    "Build REST APIs",
    "Learn Data Visualization",
    "Master Regular Expressions",
    "Understand Data Cleaning",
    "Get Comfortable with Docker",
    "Learn about DevOps",
    "Create Interactive Dashboards",
]

print("Spinning the Wheel of Resolutions.....")
print(" ")

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]

for _ in range(30):  
    selected = random.choice(resolutions)
    color = random.choice(colors) 
    print(f"\r{color}{selected}", end="", flush=False)
    time.sleep(0.1)  

time.sleep(0.7)  
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{Fore.YELLOW}Your 2025 Coding Resolution is: ")
print(" ")
time.sleep(0.7)
print(f"{Fore.GREEN}{selected}")
print(f"\n{Fore.CYAN}What's your 2025 coding resolution? Comment below! 👇")

