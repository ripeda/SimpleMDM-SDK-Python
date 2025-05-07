"""
validation.py: Validate SimpleMDM SDK with strict Pydantic checks.
"""

import os

os.environ["SimpleMDMSDKModelExtra"] = "forbid"

import argparse
import validation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate SimpleMDM SDK.")
    parser.add_argument(
        "--api-key",
        type=str,
        required=True,
        help="API key for SimpleMDM.",
    )
    parser.add_argument(
        "--read-only",
        action="store_true",
        help="Run in read-only mode.",
    )
    args = parser.parse_args()
    api_key = args.api_key
    read_only = args.read_only

    validation.Validation(api_key, read_only).validate()

    print("Validation completed successfully.")