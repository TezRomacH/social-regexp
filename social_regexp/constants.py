import re

MENTION_TOKEN = "<men>"
URL_TOKEN = "<url>"
PHONE_TOKEN = "<phn>"
HASH_TOKEN = "<hsh>"

ALL_TOKENS = [MENTION_TOKEN, URL_TOKEN, PHONE_TOKEN, HASH_TOKEN]

NON_RUSSIAN_CYRILLIC_LETTERS = {
    "ә",
    "җ",
    "ң",
    "ө",
    "ү",
    "қ",
    "ӯ",
    "ҳ",
    "ҷ",
    "ғ",
    "ұ",
    "ә",
    "һ",
    "ґ",
    "є",
    "ї",
    "ӑ",
    "ӗ",
    "ҫ",
    "ӳ",
    "ҝ",
    "ғ",
    "ҹ",
}

__all__ = [
    "MENTION_TOKEN",
    "URL_TOKEN",
    "PHONE_TOKEN",
    "HASH_TOKEN",
    "ALL_TOKENS",
    "NON_RUSSIAN_CYRILLIC_LETTERS",
]


_url_regex = re.compile(
    r"""(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+""",
    flags=re.ASCII,
)

_spaces_before_punctuation = re.compile(r'\s([?.!,:"\)]+(?:\s|$))')

_single_letter_word = re.compile(r"(?<![\w\-])\w(?![\w\-])")

_blank_spaces = re.compile(r"\s{2,}|\t|\\n|\\\\n|\\u200a|\\u200d|\\u200c")

_mentions = re.compile(r"@[\w\._]*")

_phones = re.compile(
    r"(\+?\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?(\d{4}|\d{2}[\s.-]\d{2})"
)
