# main.py

"""
Main module to run the voting application.
"""
from gui import VotingGUI
from vote_handler import VotingHandler


def main():
    """
    Main function to initialize the VotingHandler and VotingGUI, and start the application.
    """
    # Initialize the VotingHandler
    voting_handler = VotingHandler()
    # Initialize the VotingGUI
    voting_gui = VotingGUI(voting_handler)
    # Run the application
    voting_gui.run()


if __name__ == "__main__":
    main()
