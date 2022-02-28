import argparse


def print_error(message):
    if len(message) == 1:
        message = message[0]
    print(f'ERROR: {message}!!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('message', nargs='*')
    mess = parser.parse_args().message
    print('Welcome to my program')
    print_error(mess)
