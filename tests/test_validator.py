from iam_automation.validator import validate_policy


def test_validator_accepts_scoped_policy():
    policy = {
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": ["arn:aws:s3:::bucket/*"],
        }]
    }
    assert validate_policy(policy) == []


def test_validator_flags_wildcard_resource():
    policy = {
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:GetObject"],
            "Resource": ["*"],
        }]
    }
    assert "statement[0]: wildcard resource" in validate_policy(policy)


def test_validator_flags_wildcard_action():
    policy = {
        "Statement": [{
            "Effect": "Allow",
            "Action": ["*"],
            "Resource": ["arn:aws:s3:::bucket/*"],
        }]
    }
    assert "statement[0]: broad IAM action permission" in validate_policy(policy)
