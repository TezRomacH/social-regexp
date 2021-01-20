# social-regexp

<div align="center">

[![Build status](https://github.com/TezRomacH/social-regexp/workflows/build/badge.svg?branch=master&event=push)](https://github.com/TezRomacH/social-regexp/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/social-regexp.svg)](https://pypi.org/project/social-regexp/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/TezRomacH/social-regexp/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/TezRomacH/social-regexp/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/TezRomacH/social-regexp/releases)
[![License](https://img.shields.io/github/license/TezRomacH/social-regexp)](https://github.com/TezRomacH/social-regexp/blob/master/LICENSE)

Regexps for social data

</div>

## Installation

```bash
pip install social-regexp
```

## Methods

```python
>>> import social_regexp as sre
>>> text = "Hi, my Twitter is @tez_romach"

>>> sre.remove_mentions(text, sre.MENTION_TOKEN)
"Hi, I am <men>"
```

Full list of methods available here:

```python

def not_contains_non_russian_cyrillic_letters(text: str) -> bool:
    """Checks if a text contains any non-russian but cyrillic letter."""

def url() -> Pattern[str]:
    """Returns a pattern to match URLs."""


def spaces_before_punctuation() -> Pattern[str]:
    """Returns a pattern to match spaces before punctuation."""

def single_letter_words() -> Pattern[str]:
    """Returns a pattern to match single letter words."""

def blank_spaces() -> Pattern[str]:
    """Returns a pattern to match blank spaces."""

def mentions() -> Pattern[str]:
    """Returns a pattern to match mentions from Twitter or Instagram."""

def phones() -> Pattern[str]:
    """Returns a pattern to match phone numbers."""

def remove_urls(text: str, repl: str = "") -> str:
    """Return new string with replaced URLs to `repl`."""

def remove_spaces_before_punctuation(text: str) -> str:
    """Return new string without spaces before punctuations."""

def remove_punctuation(text: str) -> str:
    """Return new string without punctuations."""

def remove_mentions(text: str, repl: str = "") -> str:
    """Return new string with replaced Twitter/Instagram mentions to `repl`."""

def remove_single_letter_words(text: str) -> str:
    """Return new string without single-letter words."""

def remove_blank_spaces(text: str) -> str:
    """Return new string without blank spaces."""

def remove_phones(text: str, repl: str = "") -> str:
    """Return new string with replaced phone numbers to `repl`."""

def preprocess_text(text: str) -> str:
    """Return new string with tokenized and processed text."""
    result = remove_mentions(text, repl=MENTION_TOKEN)
    result = remove_phones(result, repl=PHONE_TOKEN)
    result = remove_urls(result, repl=URL_TOKEN)
    result = remove_blank_spaces(result).strip()
    result = remove_spaces_before_punctuation(result)

    return result
```

## Constants

```python
MENTION_TOKEN = "<men>"
URL_TOKEN = "<url>"
PHONE_TOKEN = "<phn>"
HASH_TOKEN = "<hsh>"

ALL_TOKENS = [MENTION_TOKEN, URL_TOKEN, PHONE_TOKEN, HASH_TOKEN]

NON_RUSSIAN_CYRILLIC_LETTERS = {
    "ә", "җ", "ң", "ө", "ү",
    "қ", "ӯ", "ҳ", "ҷ", "ғ",
    "ұ", "ә", "һ", "ґ", "є",
    "ї", "ӑ", "ӗ", "ҫ", "ӳ",
    "ҝ", "ғ", "ҹ",
}
```

## 🛡 License

[![License](https://img.shields.io/github/license/TezRomacH/social-regexp)](https://github.com/TezRomacH/social-regexp/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/TezRomacH/social-regexp/blob/master/LICENSE) for more details.

## 📃 Citation

```
@misc{social-regexp,
  author = {TezRomacH},
  title = {Regexps for social data},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/TezRomacH/social-regexp}}
}
```

## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
