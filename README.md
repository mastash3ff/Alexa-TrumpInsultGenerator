# Trump Insult Generator

![Deploy](https://github.com/mastash3ff/Alexa-TrumpInsultGenerator/actions/workflows/deploy.yml/badge.svg)

An Alexa skill that generates personalized insults in the style of Donald Trump's quotes. Provide a first name and receive a randomly constructed insult built from real Trump phrases.

## Usage

**Invocation:** `insult generator`

| Say... | Response |
|--------|----------|
| "Alexa, open insult generator" | Welcome message, prompts for a name |
| "Insult [first name]" | Generates a Trump-style insult targeting that name |
| "Help" | Explains how to use the skill |
| "Stop" / "Exit" | Ends the skill |

## Development

**Stack:** Python 3.12 · ASK SDK v2 · AWS Lambda (us-east-1)

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
PYTHONPATH=. pytest tests/ -v

# Deploy — automatic on push to master via GitHub Actions
```

## Project structure

```
lambda_function.py      Intent handlers
generator.py            Insult construction logic (template-based)
trump.json              Source quote fragments
requirements.txt        ask-sdk-core dependency
tests/test_skill.py     Unit tests
.github/workflows/      CI/CD — tests gate deployment to Lambda
```
