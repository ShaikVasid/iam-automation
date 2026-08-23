"""IAM policy generation helpers."""

from __future__ import annotations

from typing import Iterable


def build_allow_policy(actions: Iterable[str], resources: Iterable[str]) -> dict:
    """Build a small IAM policy document from explicit actions/resources."""
    return {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": sorted(set(actions)),
                "Resource": sorted(set(resources)),
            }
        ],
    }
