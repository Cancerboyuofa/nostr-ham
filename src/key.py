from dotenv import load_dotenv
from pynostr.key import PrivateKey
from os.path import join, dirname
import os

# Check env for existing keys, if null, then create

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

pvt_key = os.environ.get('PRIVATE_KEY')
pub_key = os.environ.get('PUBLIC_KEY')

def create_keys():

    private_key = PrivateKey()
    private_key_hex = private_key.bech32()


    public_key = private_key.public_key
    public_key_hex = public_key.bech32()

    return [private_key_hex, public_key_hex]

new_keys = create_keys()

print(new_keys[0])
print(new_keys[1])
