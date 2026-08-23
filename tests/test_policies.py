from iam_automation.policies import build_allow_policy


def test_build_allow_policy_deduplicates_values():
    policy = build_allow_policy(["s3:GetObject", "s3:GetObject"], ["arn:aws:s3:::bucket/*"])
    assert policy["Version"] == "2012-10-17"
    assert policy["Statement"][0]["Action"] == ["s3:GetObject"]
    assert policy["Statement"][0]["Resource"] == ["arn:aws:s3:::bucket/*"]
