# %%
import pandas as pd
import pytest

from regmonkey_edapy.errors.exceptions import InputError
from regmonkey_edapy.pandas.descriptive_statistics import compute_transition_matrix

# ----------------------------
# Test 1: state transitioon matrix
# ----------------------------

def test_compute_transition_matrix_count():
    data = {
        "entity": ["A", "A", "A", "B", "B", "B"],
        "state": ["X", "Y", "X", "Y", "X", "Y"],
        "time": [1, 2, 3, 1, 2, 3],
    }
    df = pd.DataFrame(data)
    result = compute_transition_matrix(df, "time", ["entity"], "state", "count")
    expected_data = {"X": {"X": 0, "Y": 2}, "Y": {"X": 2, "Y": 0}}
    expected_df = pd.DataFrame(expected_data)
    expected_df = expected_df.rename_axis("previous_state", axis=0).rename_axis(
        "state", axis=1
    )
    pd.testing.assert_frame_equal(result, expected_df)


def test_compute_transition_matrix_percent():
    data = {
        "entity": ["A", "A", "A", "B", "B", "B"],
        "state": ["X", "Y", "X", "Y", "X", "Y"],
        "time": [1, 2, 3, 1, 2, 3],
    }
    df = pd.DataFrame(data)
    result = compute_transition_matrix(df, "time", ["entity"], "state", "percent")
    expected_data = {"X": {"X": 0.0, "Y": 1.0}, "Y": {"X": 1.0, "Y": 0.0}}
    expected_df = pd.DataFrame(expected_data)
    expected_df = expected_df.rename_axis("previous_state", axis=0).rename_axis(
        "state", axis=1
    )
    pd.testing.assert_frame_equal(result, expected_df)


def test_compute_transition_matrix_invalid_df():
    with pytest.raises(InputError):
        compute_transition_matrix(
            "not a dataframe",  # pyright: ignore
            "time",
            ["entity"],
            "state",
            "count",
        )
