# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
from typing import Dict, List, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS, EMOJI_SCORES


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
        emoji_scores: Optional[Dict[str, int]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS
        emoji_scores = emoji_scores if emoji_scores is not None else EMOJI_SCORES

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)
        # Centralized emoji vocabulary and weights.
        self.emoji_scores = dict(emoji_scores)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        Steps:
          - Strip leading/trailing whitespace and lowercase the text
          - Normalize common slang phrases
          - Expand a few contractions for easier negation handling
          - Tokenize emoji/emoticons even when attached to words
          - Normalize repeated characters ("soooo" -> "soo")
          - Remove most punctuation and split into tokens
        """
        cleaned = text.strip().lower()
        if not cleaned:
            return []

        # Keep common phrase level slang as one token.
        cleaned = re.sub(r"\bno\s+cap\b", "no_cap", cleaned)

        # Expand a few common contractions so negation logic is easier.
        contractions = {
            "can't": "can not",
            "cant": "can not",
            "won't": "will not",
            "wont": "will not",
            "don't": "do not",
            "dont": "do not",
            "didn't": "did not",
            "didnt": "did not",
            "isn't": "is not",
            "isnt": "is not",
            "aren't": "are not",
            "arent": "are not",
            "i'm": "i am",
            "im": "i am",
        }
        for source, target in contractions.items():
            # Word-boundary replacement avoids changing substrings inside other words.
            cleaned = re.sub(rf"\b{re.escape(source)}\b", target, cleaned)

        # Normalize elongated words: "soooo" -> "soo".
        cleaned = re.sub(r"([a-z])\1{2,}", r"\1\1", cleaned)

        # Tokenize by matching known emoji markers or alphanumeric words.
        marker_pattern = "|".join(
            re.escape(marker)
            for marker in sorted(self.emoji_scores.keys(), key=len, reverse=True)
        )
        token_pattern = rf"{marker_pattern}|[a-z0-9_']+"

        return re.findall(token_pattern, cleaned)

    def _is_negated(self, tokens: List[str], idx: int) -> bool:
        """
        Return True if token at idx appears in a simple negation scope.
        """
        negators = {"not", "never", "no"}
        intensifiers = {"very", "really", "so", "too", "kind", "kinda", "kindof"}

        if idx > 0 and tokens[idx - 1] in negators:
            # Direct negation window: "not happy", "never fun".
            return True

        # Handles patterns like "not very happy".
        if idx > 1 and tokens[idx - 2] in negators and tokens[idx - 1] in intensifiers:
            return True

        return False

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric mood score for the given text.

        Positive words increase the score.
        Negative words decrease the score.
        Negation flips nearby polarity in simple patterns.
        """
        tokens = self.preprocess(text)
        score = 0

        for idx, token in enumerate(tokens):
            if token in self.emoji_scores:
                # Emojis/emoticons act as direct sentiment signals.
                score += self.emoji_scores[token]
                continue

            if token in self.positive_words:
                # Negation flips polarity: "not good" should count negative.
                score += -1 if self._is_negated(tokens, idx) else 1
            elif token in self.negative_words:
                # Negation flips polarity: "not bad" should count positive.
                score += 1 if self._is_negated(tokens, idx) else -1

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        Mapping:
          - score >= 2 -> "positive"
          - score <= -2 -> "negative"
          - score == 0 -> "neutral"
          - otherwise -> "mixed"
        """
        score = self.score_text(text)

        if score >= 2:
            return "positive"
        if score <= -2:
            return "negative"
        if score == 0:
            return "neutral"
        # Near-zero but non-zero scores are treated as mixed sentiment.
        return "mixed"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining why the model chose its label.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for idx, token in enumerate(tokens):
            if token in self.emoji_scores:
                if self.emoji_scores[token] > 0:
                    positive_hits.append(token)
                else:
                    negative_hits.append(token)
                # Keep explain() scoring aligned with score_text().
                score += self.emoji_scores[token]
                continue

            if token in self.positive_words:
                positive_hits.append(token)
                score += -1 if self._is_negated(tokens, idx) else 1
            elif token in self.negative_words:
                negative_hits.append(token)
                score += 1 if self._is_negated(tokens, idx) else -1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
