"""
Write a Hypothesis test for reverse_string that:
* accepts any printable text up to length 100
* asserts reverse_string(reverse_string(s)) == s
"""
from hypothesis import given, strategies as st
from reverse_string import reverse_string

@given(st.text(printable=True, max_size=100))