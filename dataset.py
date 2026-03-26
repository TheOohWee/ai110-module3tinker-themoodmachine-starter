"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
    - EMOJI_SCORES: emoji and emoticon sentiment vocabulary
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "nice",
    "wonderful",
    "fantastic",
    "excellent",
    "brilliant",
    "perfect",
    "glad",
    "grateful",
    "hopeful",
    "proud",
    "winning",
    "win",
    "yay",
    "best",
    "funny",
    "hilarious",
    "calm",
    "peaceful",
    "thriving",
    "improving",
    "blessed",
    "lit",
    "dope",
    "fire",
    "wicked",
    "sick",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "horrible",
    "miserable",
    "depressed",
    "anxious",
    "worried",
    "nervous",
    "exhausted",
    "drained",
    "hurt",
    "pain",
    "crashed",
    "broken",
    "failing",
    "failure",
    "lost",
    "rejected",
    "stuck",
    "annoyed",
    "frustrated",
    "mad",
    "furious",
    "worst",
    "rough",
    "overwhelmed",
    "burned",
    "burnt",
]

# Shared emoji/emoticon vocabulary used by the analyzer.
EMOJI_SCORES = {
    ":)": 1,
    ":-)": 1,
    "😂": 1,
    "😄": 1,
    "🙂": 1,
    "❤️": 1,
    "🔥": 1,
    ":(": -1,
    ":-(": -1,
    "🥲": -1,
    "💀": -1,
    "😢": -1,
    "😭": -1,
    "😡": -1,
    "😞": -1,
    "😅": -1,
}

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    # Added samples to broaden style coverage: slang, sarcasm, emojis, and ambiguity.
    "Lowkey proud I finished that project tonight",
    "No cap, this weather is ruining my mood",
    "I absolutely love waiting 40 minutes in traffic",
    "Coffee kicked in and now I feel amazing :)",
    "I laughed so hard at that meme 😂",
    "Everything is on fire but hey, we move",
    "Got rejected, but maybe it is a blessing in disguise",
    "Highkey exhausted and done with everyone",
    "The concert was loud, chaotic, and kind of fun",
    "I cannot tell if I am thriving or just surviving 🥲",
    # Breaker set: realistic edge cases designed to confuse simple models.
    "I love getting stuck in traffic for an hour.",
    "Amazing, my laptop crashed right before the deadline.",
    "Best day ever, spilled coffee on my notes.",
    "That beat is sick.",
    "This party was wicked.",
    "Your new setup is fire.",
    "This exam was sick in the worst way.",
    "I'm fine 🙂",
    "Great, just great 😅",
    "Love that for me 💀",
    "I'm exhausted but proud of myself.",
    "I am stressed and excited at the same time.",
    "I hate how hard this is, but I know I'm improving.",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    # Labels are kept in the exact same order as SAMPLE_POSTS above.
    "positive",  # "Lowkey proud I finished that project tonight"
    "negative",  # "No cap, this weather is ruining my mood"
    "negative",  # "I absolutely love waiting 40 minutes in traffic"
    "positive",  # "Coffee kicked in and now I feel amazing :)"
    "positive",  # "I laughed so hard at that meme 😂"
    "mixed",     # "Everything is on fire but hey, we move"
    "mixed",     # "Got rejected, but maybe it is a blessing in disguise"
    "negative",  # "Highkey exhausted and done with everyone"
    "mixed",     # "The concert was loud, chaotic, and kind of fun"
    "mixed",     # "I cannot tell if I am thriving or just surviving 🥲"
    "negative",  # "I love getting stuck in traffic for an hour."
    "negative",  # "Amazing, my laptop crashed right before the deadline."
    "negative",  # "Best day ever, spilled coffee on my notes."
    "positive",  # "That beat is sick."
    "positive",  # "This party was wicked."
    "positive",  # "Your new setup is fire."
    "negative",  # "This exam was sick in the worst way."
    "neutral",   # "I'm fine 🙂"
    "mixed",     # "Great, just great 😅"
    "mixed",     # "Love that for me 💀"
    "mixed",     # "I'm exhausted but proud of myself."
    "mixed",     # "I am stressed and excited at the same time."
    "mixed",     # "I hate how hard this is, but I know I'm improving."
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
