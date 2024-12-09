from typing import Literal

import pandas as pd

from regmonkey_edapy.errors.exceptions import InputError


def compute_transition_matrix(
    df: pd.DataFrame,
    sort_key: str,
    entity_key: list[str],
    state: str,
    summary_type: Literal["count", "percent"] = "count",
) -> pd.DataFrame:
    """
    Compute a transition matrix for the given DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    sort_key (str): The column name to sort the DataFrame by.
    entity_key (str): The column name representing the entity to group by.
    state (str): The column name representing the state to compute transitions for.
    summary_type (Literal["count", "percent"]): The type of summary to return, either
    "count" for raw counts or "percent" for normalized percentages.

    Returns:
    pd.DataFrame: A DataFrame representing the transition matrix, with either counts or
    percentages based on the summary_type.
    """

    if not isinstance(df, pd.DataFrame):
        raise InputError("df", "The input df must be a pandas DataFrame.")

    df = df.copy().sort_values([sort_key])
    df["previous_state"] = df.groupby(entity_key)[state].shift(1)
    df_transitions = df.dropna(subset=["previous_state"])

    # Create transition counts
    transition_df = (
        df_transitions.groupby(["previous_state", state]).size().unstack(fill_value=0)
    )

    if summary_type == "percent":
        return transition_df.div(transition_df.sum(axis=1), axis=0)
    elif summary_type == "count":
        return transition_df
    else:
        raise InputError("summary_type", "The input must be 'count' or 'size'")
