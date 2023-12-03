# This is the gui for the project
import tkinter as tk
from tkinter import ttk
from vote_handler import VotingHandler

"""
Module for the graphical user interface (GUI).
"""


class VotingGUI:
    """
    Class to create and manage the GUI for the voting application.
    """

    def __init__(self, voting_handler):
        """
        Initialize the VotingGUI.

        Parameters:
        - voting_handler (VotingHandler): Instance of VotingHandler to manage votes and candidates.
        """

        self.voting_handler = voting_handler
        self.root = tk.Tk()
        self.root.title("Voting Application")

        # Set the initial Size of the Window
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        """
        Create and configure widgets for the GUI.
        """
        # Vote Menu Frame
        vote_frame = ttk.Frame(self.root, padding="10")
        vote_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(vote_frame, text="VOTE MENU", font=('Helvetica', 14)).grid(row=0, column=0, columnspan=2, pady=10)

        vote_button = ttk.Button(vote_frame, text="Vote", command=self.vote_button_clicked)
        vote_button.grid(row=1, column=0, padx=5, pady=5)

        exit_button = ttk.Button(vote_frame, text="Exit", command=self.exit_button_clicked)
        exit_button.grid(row=1, column=1, padx=5, pady=5)

        # Tally Button
        tally_button = ttk.Button(self.root, text="Tally Results", command=self.tally_button_clicked)
        tally_button.grid(row=1, column=0, pady=10)

        # Center the widgets in the middle of the window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def vote_button_clicked(self):
        """
        Callback function for the Vote button.
        """
        candidate_choice = self.get_candidate_choice()
        self.voting_handler.record_vote(candidate_choice)
        print("Voted", self.voting_handler.candidates[candidate_choice - 1])

    def exit_button_clicked(self):
        """
        Callback function for the Exit button.
        """
        self.display_results()
        print("Exiting.")
        self.root.destroy()

    def tally_button_clicked(self):
        """
        Callback function for the Tally Results button.
        """
        self.display_results()

    def get_candidate_choice(self):
        """
        Display the candidate menu and return the selected candidate index.
        """
        candidate_window = tk.Toplevel(self.root)
        candidate_window.title("Candidate Menu")

        # Set the size of the candidate window
        candidate_window.geometry("400x300")

        ttk.Label(candidate_window, text="CANDIDATE MENU", font=('Helvetica', 14)).pack(pady=10)

        for i, candidate in enumerate(self.voting_handler.candidates, start=1):
            ttk.Button(candidate_window, text=f"{i}: {candidate}",
                       command=(lambda i=i: self.candidate_button_clicked(i))).pack()

    def candidate_button_clicked(self, candidate_choice):
        self.voting_handler.record_vote(candidate_choice)
        print("Voted", self.voting_handler.candidates[candidate_choice - 1])

    def display_results(self):
        """
        Display the voting results in a separate window.
        """
        candidates, vote_count = self.voting_handler.get_results()
        result_window = tk.Toplevel(self.root)
        result_window.title("Voting Results")

        ttk.Label(result_window, text="VOTING RESULTS", font=('Helvetica', 14)).pack(pady=10)

        for i, candidate in enumerate(candidates):
            ttk.Label(result_window, text=f"{candidate}: {vote_count[i]} votes").pack()

        ttk.Label(result_window, text=f"Total Votes: {sum(vote_count)}").pack()

    def run(self):
        """
        Run the main loop for the GUI.
        """
        self.root.mainloop()
