import unittest
from unittest.mock import patch

from game import HangmanGame


class HangmanGameTests(unittest.TestCase):
    def setUp(self):
        self.game = HangmanGame()
        self.game.category = "technology"
        self.game.secret = "python"

    def test_repeated_correct_guess_does_not_change_state(self):
        self.assertEqual(self.game.guess("P"), "Correct.")
        self.assertEqual(self.game.guess("p"), "Already guessed.")
        self.assertEqual(self.game.lives, 6)
        self.assertEqual(self.game.guessed, {"p"})

    def test_repeated_wrong_guess_does_not_consume_another_life(self):
        self.assertEqual(self.game.guess("z"), "Wrong.")
        self.assertEqual(self.game.guess("Z"), "Already guessed.")
        self.assertEqual(self.game.lives, 5)
        self.assertEqual(self.game.wrong, {"z"})

    def test_invalid_input_does_not_change_state(self):
        for value in ("", "ab", "1", "/hint"):
            self.assertEqual(self.game.guess(value), "Enter one letter.")
        self.assertEqual(self.game.lives, 6)
        self.assertEqual(self.game.guessed, set())
        self.assertEqual(self.game.wrong, set())

    def test_hint_is_applied_once_and_penalizes_score_once(self):
        self.game.score = 3
        self.assertIsNotNone(self.game.use_hint())
        self.assertEqual(self.game.score, 2)
        self.assertIsNone(self.game.use_hint())
        self.assertEqual(self.game.score, 2)

    def test_difficulty_sets_lives_and_score(self):
        self.game.difficulty = "hard"
        with patch("game.random.choice", return_value="python"), patch(
            "builtins.input", side_effect=list("python")
        ):
            self.assertTrue(self.game.play_round())
        self.assertEqual(self.game.lives, 4)
        self.assertEqual(self.game.streak, 1)
        self.assertEqual(self.game.score, 9)

    def test_starting_round_resets_round_state_but_keeps_session_stats(self):
        self.game.stats.record(True, 1)
        self.game.guessed.add("p")
        self.game.wrong.add("z")
        self.game.difficulty = "easy"
        with patch("game.random.choice", return_value="python"):
            self.game.start_round()
        self.assertEqual(self.game.lives, 8)
        self.assertEqual(self.game.guessed, set())
        self.assertEqual(self.game.wrong, set())
        self.assertEqual(self.game.stats.rounds, 1)
        self.assertEqual(self.game.stats.wins, 1)

    def test_play_round_records_win_and_loss(self):
        with patch("game.random.choice", return_value="a"), patch(
            "builtins.input", side_effect=["a"]
        ):
            self.assertTrue(self.game.play_round())
        with patch("game.random.choice", return_value="a"), patch(
            "builtins.input", side_effect=list("zxcvbq")
        ):
            self.assertTrue(self.game.play_round())
        self.assertEqual(self.game.stats.rounds, 2)
        self.assertEqual(self.game.stats.wins, 1)
        self.assertEqual(self.game.stats.best_streak, 1)

    def test_quit_does_not_record_a_round(self):
        with patch("builtins.input", return_value="/quit"):
            self.assertFalse(self.game.play_round())
        self.assertEqual(self.game.stats.rounds, 0)


if __name__ == "__main__":
    unittest.main()
