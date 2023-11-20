import requests
import hashlib
import sys

#Request the Api passing a string, return a HTTP status code.
def resquest_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res

#Receive the first 5 character in a hash and the rest of the hash as tail.
#If the first 5 chars are found, return how many times has been found. 
def get_password_leaks_counts(hashes_res, hash_to_check):
    hashes = (line.split(':') for line in hashes_res.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

#check password if it exist in API response.
def pwned_api_cheack(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char, tail = sha1password[:5], sha1password[5:]
    response = resquest_api_data(first_5char)
    return get_password_leaks_counts(response, tail)

def main(args):
    for password_to_check in args:
        count = pwned_api_cheack(password_to_check)
        if count:
            print(f'{ password_to_check } was found { count } times... you should probably change your password!')
        else:
            print(f'{password_to_check} was NOT found. You are good... for now.')   
    return 'Done!' 

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))