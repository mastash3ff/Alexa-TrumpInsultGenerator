import json
import os
import random

_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(_dir, "trump.json")) as trump_file:
    quotes = json.load(trump_file)

templates = [
    ["subjectnametwice1", "user_name", "subjectnametwice2", "user_name", "predicate", "insult3", "kicker"],
    ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker"],
    ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker"],
    ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker"],
    ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker"],
    ["user_name", "subjectnamefirst", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
    ["subjectnamesecond", "user_name", "predicate", "insult3", "kicker"],
]

nice_quotes = [
    "What a beautiful person!",
    "That one should be our president!",
    "I know the best people. And that's one of them.",
    "Fantastic, yuge potential!",
]


def _rand_idx(n):
    return int(((random.random() * 1_000_000) + 1) % n)


def generateInsult(name):
    name_lower = name.lower()
    if "donald" in name_lower or "trump" in name_lower or "ivanka" in name_lower:
        return nice_quotes[_rand_idx(len(nice_quotes))]

    template = templates[_rand_idx(len(templates))]
    parts = []
    for word in template:
        if word == "user_name":
            parts.append(name)
        else:
            parts.append(quotes[word][_rand_idx(len(quotes[word]))])
    return "".join(parts)
