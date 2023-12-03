# vote_handler.py

"""
Module for handling votes and candidates.
"""
class VotingHandler:
    """
    Class to manage votes and candidates.
    """
    def __init__(self):
        """
        Initialize the VotingHandler.

        Parameters:
        - candidates (list): List of candidate names.
        - vote_count (list): List to store the vote count for each candidate.
        """
        self.candidates = ["Cameron", "Allison", "Diego"]
        self.vote_count = [0, 0, 0]

    def record_vote(self, candidate_choice):
        """
        Record a vote for the specified candidate.

        Parameters:
        - candidate_index (int): Index of the voted candidate.
        """
        self.vote_count[candidate_choice - 1] += 1

    def get_results(self):
        """
        Get the current voting results.

        Returns:
        - list: List of candidate names.
        - list: List of corresponding vote counts.
        """
        return self.candidates, self.vote_count
