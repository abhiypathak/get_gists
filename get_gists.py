import argparse
import requests
import json
import datetime
import os.path
from pathlib import Path


def create_timestamp(user):
    home_dir = str(Path.home())
    file_path = home_dir + "/." + user + "_get_gists"
    with open(file_path, 'w') as f:
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        f.write(date + " --- " + user + "\n")


def get_users(user):
    home_dir = str(Path.home())
    file_path = home_dir + "/." + user + "_get_gists"
    existing_users = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            line = f.readline()
            time = line.split(' --- ')
            while line:
                existing_users.append(time[1])
                line = f.readline()
            f.close()
            return existing_users
    else:
        return False


def get_gist(user):
    request = "https://api.github.com/users/"+user+"/gists"
    response = requests.get(request)

    if response.status_code == 200:
        print(f'Connection to {request} successful!\nWill now proceed to get public gists for {user} user...')
        data = json.loads(response.text)
        if data:
            print("Following public gists are available")
            for k in data:
                print(f"{k['url']}")
            create_timestamp(user)
        else:
            print(f"No gists available for this user: {user}")
    else:
        print(f'Cannot connect to {request} failed with response code http {response.status_code}')


def main(user):
    existing_user = get_users(user)
    if existing_user:
        home_dir = str(Path.home())
        file_path = home_dir + "/." + user + "_get_gists"
        with open(file_path, 'r') as f:
            line = f.readline()
            time = line.split(' --- ')
        request = "https://api.github.com/users/"+user+"/gists?since="+time[0]
        response = requests.get(request)

        if response.status_code == 200:
            print(f'Connection to {request} successful!\nWill now proceed to get public gists for {user} user...')
            data = json.loads(response.text)
            if data:
                print(f"Following public gists are available since you last looked up at {time[0]}")
                for k in data:
                    print(f"{k['url']}")
                create_timestamp(user)
            else:
                print(f"No new gists available since your last look up at {time[0]}")
        else:
            print(f'Cannot connect to {request} failed with response code http {response.status_code}')
    else:
        get_gist(user)


parser = argparse.ArgumentParser(description="Python Utility to get publicly available github gists for a given user")
parser.add_argument('-u', '--user', help='Provide the github username whose gists you want to lookup', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    main(args.user)
