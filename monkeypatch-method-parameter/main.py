import argparse
import datetime
import json
import os

from logger import logger

logger = logger(name=__name__)


class Birthday:
    def __init__(self, name, birthday, save):
        self.name = name
        self.birthday = birthday
        self.save = save

    def run(self):
        logger.info("%s's birthday: %s", self.name, self.birthday)

        if self.save:
            self.save_json_file()

    def save_json_file(self, path=None):
        if path is None:
            path = "birthday.jsonl"

        logger.debug("Saving %s's birthday to %s", self.name, path)

        # Check if the file already exist to add a new line if needed.
        # If the file exists, check that self.name is not already present.
        exists = False

        if os.path.exists(path=path):
            exists = True

            if not validator(path=path, name=self.name):
                logger.debug("%s's birthday is already present in %s", self.name, path)
                return

        with open(file=path, mode="a") as f:
            if exists:
                f.write("\n")
            json.dump(obj={self.name: str(self.birthday)}, fp=f, ensure_ascii=False)


def validator(path, name):
    with open(file=path, mode="rb") as f:
        lines = f.readlines()

    for line in lines:
        if name in json.loads(s=line):
            return False

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=("Create a calendar of birthday dates."),
    )
    parser.add_argument(
        "--name",
        type=str,
        help="the name of the person.",
        required=True,
    )
    parser.add_argument(
        "--birthday",
        type=str,
        help="the birthday's date (YYYY-MM-DD) of the person.",
        required=True,
    )
    parser.add_argument(
        "-s",
        "--save",
        action="store_true",
        help="save the birthday to a JSON Lines file.",
    )

    args = parser.parse_args()

    birthday_ = datetime.datetime.strptime(args.birthday, r"%Y-%m-%d").date()

    Birthday(name=args.name, birthday=birthday_, save=args.save).run()
