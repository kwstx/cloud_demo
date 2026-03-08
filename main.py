import os
import sys

# Import the Guard SDK
# This tests that the editable install was successful
try:
    from guard import sdk
    print("Guard SDK imported successfully!")
except ImportError as e:
    print(f"Failed to import Guard SDK: {e}")

def main():
    print("Autonomous SRE Application Initialized.")
    print("This application interacts with the Guard Backbone using the SDK.")

if __name__ == "__main__":
    main()
