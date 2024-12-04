import argparse
import os
import requests
from datetime import datetime


def generate_boilerplate(day):
    TEMPLATE_FILE = 'template.py'
    filename = f'day{day}/day{day}.py'

    if not os.path.exists(TEMPLATE_FILE):
        print(f"Error: Template file '{TEMPLATE_FILE}' does not exist.")
        return

    with open(TEMPLATE_FILE, 'r') as template:
        content = template.read()

    content = content.replace('{day}', str(day))

    with open(filename, 'w') as f:
        f.write(content)

    print(f"Python file '{filename}' has been created from the template '{TEMPLATE_FILE}'.")

    examplefilename = f'day{day}/example{day}.txt'
    open(examplefilename, 'a').close()
    print(f"Text file '{examplefilename}' has been created.")


def download_input(day):
    BASE_URL = 'https://adventofcode.com/2024/day/{day}/input'
    url = BASE_URL.format(day=day)

    cookie = open("cookie.txt").read()

    response = requests.get(url, cookies={"session": cookie})

    if response.status_code == 200:
        filename = f'day{day}/input{day}.txt'
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Input downloaded and saved as '{filename}'.")
    else:
        print(f"Error: Unable to download file from '{url}'. Status code: {response.status_code}")


def main():
    parser = argparse.ArgumentParser(
        description="Generates a folder with a .py file to hold your solution and downloads puzzle input.")
    parser.add_argument('-d', '--day', type=int, help='The day of the puzzle you want to solve.')

    args = parser.parse_args()

    # Use today's day as the default if not provided
    if args.day is None:
        args.day = datetime.now().day

    os.mkdir('day{}'.format(args.day))
    download_input(args.day)
    generate_boilerplate(args.day)


if __name__ == '__main__':
    main()
