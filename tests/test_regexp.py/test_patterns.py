import pytest
import social_regexp as sre


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("Hi, my Twitter is @tez_romach :)", "Hi, my Twitter is <men> :)"),
        ("@a_very_long_long_long_mention!", "<men>!"),
    ],
)
def test_mentions(input, expected):
    """Example test with parametrization."""
    assert sre.remove_mentions(input, sre.MENTION_TOKEN) == expected
