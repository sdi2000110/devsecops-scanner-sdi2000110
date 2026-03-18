#!/usr/bin/env python3
"""Temperature converter - sdi2000110 @ EKPA"""

import sys

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("=== Temperature Converter - sdi2000110 ===")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    choice = input("Pick (1 or 2): ")
    temp = float(input("Enter temperature: "))
    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
