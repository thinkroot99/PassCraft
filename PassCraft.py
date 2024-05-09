"""
Script for generating random passwords.

Script: PassCraft
Author: ThinkRoot
Version: 7

Description:
This script allows the user to generate random passwords according to desired specifications, including password length, inclusion or exclusion of special characters, and specifying the number of generated passwords.

Usage:
    - Make sure you have Python installed on your computer. You can download and install Python from https://www.python.org/downloads/.
    - Download the script for generating random passwords or create a new text file and copy the code from the script into the text file.
    - Open the terminal or command line and navigate to the directory where the script is located.
    - Run the script using Python. To do this, type `python PassCraft.py` and press Enter.
    - Follow the instructions displayed by the script to specify the desired password length, whether you want to include special characters, the number of desired passwords, and whether you want to generate more passwords.
    - The script will generate and display random passwords according to the provided specifications.
    - You can repeat steps 5-6 to generate more sets of passwords if desired.
"""

import random
import string
import secrets

def generate_password(length=16, include_special_chars=True, custom_charset=None):
    """
    The function generates a random password according to the given specifications.

    Parameters:
    length (int): The desired length of the password (default is 16).
    include_special_chars (bool): Indicator for including special characters (default is True).
    custom_charset (str): The custom set of characters for password generation.

    Returns:
    str: The generated password.
    """
    if custom_charset:
        # Check custom character set
        if len(set(custom_charset)) != len(custom_charset):
            raise ValueError("The custom character set contains duplicate characters.")
        if any(char not in string.printable for char in custom_charset):
            raise ValueError("The custom character set contains invalid characters.")
        characters = custom_charset
    else:
        characters = string.ascii_letters + string.digits
        if include_special_chars:
            characters += string.punctuation

    if not isinstance(length, int) or length <= 0:
        raise ValueError("The password length must be a positive integer.")

    if length < 8:
        raise ValueError("The minimum password length must be at least 8 characters.")

    password = [secrets.choice(string.ascii_lowercase),
                secrets.choice(string.ascii_uppercase),
                secrets.choice(string.digits)]
    if include_special_chars:
        password.append(secrets.choice(string.punctuation))

    password.extend(secrets.choice(characters) for _ in range(length - len(password)))
    random.shuffle(password)

    return ''.join(password)

def get_password_requirements():
    """
    The function prompts the user for the length, option to include special characters, and option to repeat.

    Returns:
    int: The length of password specified by the user.
    bool: Indicator for including special characters.
    bool: Indicator for repeating password generation.
    """
    print("Enter the desired password length (minimum 8): ")
    while True:
        try:
            password_length = int(input())
            if password_length < 8:
                raise ValueError("The minimum password length must be at least 8 characters.")
            break
        except ValueError:
            print("Please enter an integer for the password length: ")

    print("Do you want to include special characters? (Yes/No): ")
    while True:
        choice = input().strip().lower()
        if choice in ["yes", "no"]:
            include_special_chars = choice == "yes"
            break
        else:
            print("Please respond with Yes or No: ")

    print("How many passwords do you want to generate?")
    while True:
        try:
            num_passwords = int(input())
            if num_passwords <= 0:
                raise ValueError("The number of generated passwords must be a positive number.")
            break
        except ValueError:
            print("Please enter a positive number for the number of generated passwords: ")

    print("Do you want to generate more passwords? (Yes/No): ")
    while True:
        choice = input().strip().lower()
        if choice in ["yes", "no"]:
            repeat = choice == "yes"
            break
        else:
            print("Please respond with Yes or No: ")

    return password_length, include_special_chars, num_passwords, repeat

if __name__ == "__main__":
    try:
        print("This script generates random passwords.")
        print("Instructions: Enter the desired length for the password (minimum 8), choose whether to include special characters, specify the number of passwords, and whether you want to generate more passwords.")

        while True:
            password_length, include_special_chars, num_passwords, repeat = get_password_requirements()

            for _ in range(num_passwords):
                password = generate_password(password_length, include_special_chars)
                print("Generated password:", password)

            if not repeat:
                break
    except Exception as e:
        print("Error:", e)