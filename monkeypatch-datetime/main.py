import argparse
import datetime as dt


def now() -> dt.datetime:
    """Defines a utility function that allow us to easily test the main function."""
    return dt.datetime.now()


def create_versioning_name(date: dt.date | dt.datetime | str | None) -> str:
    if date is None:
        date = now()

    if isinstance(date, str):
        date = dt.datetime.strptime(date, r"%Y-%m-%d")

    return date.strftime(r"%Y%m%d_%H%M%S")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=("Create a versioning name from date."),
    )
    parser.add_argument(
        "--date",
        type=str,
        help="the date to use to create the versioning name.",
    )

    args = parser.parse_args()

    print(create_versioning_name(date=args.date))
