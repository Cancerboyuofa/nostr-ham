from dotenv import load_dotenv, set_key
from pynostr.key import PrivateKey
from os.path import join, dirname
import os


    # Check env for existing keys, if null, then create

def get_keys():

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)


    pvt_key = os.environ.get('PRIVATE_KEY')
    pub_key = os.environ.get('PUBLIC_KEY')

    return [pvt_key, pub_key]


    # Create Keys Function

def create_keys():

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    private_key = PrivateKey()
    private_key_hex = private_key.bech32()

    public_key = private_key.public_key
    public_key_hex = public_key.bech32()

    print(private_key)

    set_key('src/.env', 'PRIVATE_KEY', str(private_key))
    set_key('src/.env', 'PUBLIC_KEY', str(public_key))

    return [private_key_hex, public_key_hex]