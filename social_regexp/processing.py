from typing import Pattern

import re
import string

from social_regexp.constants import (
    HASH_TOKEN,
    MENTION_TOKEN,
    NON_RUSSIAN_CYRILLIC_LETTERS,
    PHONE_TOKEN,
    URL_TOKEN,
    _blank_spaces,
    _mentions,
    _phones,
    _single_letter_word,
    _spaces_before_punctuation,
    _url_regex,
)


def not_contains_non_russian_cyrillic_letters(text: str) -> bool:
    """Checks if a text contains any non-russian but cyrillic letter."""
    return all(letter not in NON_RUSSIAN_CYRILLIC_LETTERS for letter in text)


def url() -> Pattern[str]:
    """Returns a pattern to match URLs."""
    return _url_regex


def spaces_before_punctuation() -> Pattern[str]:
    """Returns a pattern to match spaces before punctuation."""
    return _spaces_before_punctuation


def single_letter_words() -> Pattern[str]:
    """Returns a pattern to match single letter words."""
    return _single_letter_word


def blank_spaces() -> Pattern[str]:
    """Returns a pattern to match blank spaces."""
    return _blank_spaces


def mentions() -> Pattern[str]:
    """Returns a pattern to match mentions from Twitter or Instagram."""
    return _mentions


def phones() -> Pattern[str]:
    """Returns a pattern to match phone numbers."""
    return _phones


def remove_urls(text: str, repl: str = "") -> str:
    """Return new string with replaced URLs to `repl`."""
    return re.sub(pattern=_url_regex, repl=repl, string=text)


def remove_spaces_before_punctuation(text: str) -> str:
    """Return new string without spaces before punctuations."""
    return re.sub(pattern=_spaces_before_punctuation, repl=r"\1", string=text)


def remove_punctuation(text: str) -> str:
    """Return new string without punctuations."""
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_mentions(text: str, repl: str = "") -> str:
    """Return new string with replaced Twitter/Instagram mentions to `repl`."""
    return re.sub(pattern=_mentions, repl=repl, string=text)


def remove_single_letter_words(text: str) -> str:
    """Return new string without single-letter words."""
    return re.sub(pattern=_single_letter_word, repl="", string=text)


def remove_blank_spaces(text: str) -> str:
    """Return new string without blank spaces."""
    return re.sub(pattern=_blank_spaces, repl=" ", string=text)


def remove_phones(text: str, repl: str = "") -> str:
    """Return new string with replaced phone numbers to `repl`."""
    return re.sub(pattern=_phones, repl=repl, string=text)


def preprocess_text(text: str) -> str:
    """Return new string with tokenized and processed text."""
    result = remove_mentions(text, repl=MENTION_TOKEN)
    result = remove_phones(result, repl=PHONE_TOKEN)
    result = remove_urls(result, repl=URL_TOKEN)
    result = remove_blank_spaces(result).strip()
    result = remove_spaces_before_punctuation(result)

    return result


__all__ = [
    "not_contains_non_russian_cyrillic_letters",
    "url",
    "spaces_before_punctuation",
    "single_letter_words",
    "blank_spaces",
    "mentions",
    "phones",
    "remove_urls",
    "remove_spaces_before_punctuation",
    "remove_punctuation",
    "remove_mentions",
    "remove_single_letter_words",
    "remove_blank_spaces",
    "remove_phones",
    "preprocess_text",
]
