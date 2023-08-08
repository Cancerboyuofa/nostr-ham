from dotenv import load_dotenv, set_key
from pynostr.key import PrivateKey
from os.path import join, dirname
import os

if __name__ == "__main__":

    # Check env for existing keys, if null, then create

    def get_key():

        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)


        pvt_key = os.environ.get('PRIVATE_KEY')
        pub_key = os.environ.get('PUBLIC_KEY')

        return pvt_key, pub_key


    #Create Keys Function

    def create_keys():

        private_key = PrivateKey()
        private_key_hex = private_key.bech32()


        public_key = private_key.public_key
        public_key_hex = public_key.bech32()

        return [private_key_hex, public_key_hex]


    if pvt_key == '' or pub_key == '':

        print("No Existing Keys Found. Creating...\n")

        new_keys = create_keys()

        set_key('src/.env', 'PRIVATE_KEY', new_keys[0])
        set_key('src/.env', 'PUBLIC_KEY', new_keys[1])

        print("Here are your new keys, write them down!\n")

        print("Public Key: " + new_keys[0] + "\n")
        print("Private Key:" + new_keys[1] + "\n")
        
    else:
        print("Existing Keys Found, they are:\n")

        print("Public Key: " + pub_key + "\n")
        print("Private Key:" + pvt_key + "\n")
