import fldigi as fl
import key
import relay




# -------------------- FLDigi Setup & TX ------------------------ #


# fl.radio_setup("BPSK63", 1000)

# print('Setting up radio...')

# text = input('Please enter the text to transmit:\n')

# confirm_tx = input("Do you want to transmit? Y/N\n")

# if confirm_tx.upper() == 'Y':

#     fl.send_tx("<MYCALL> " + text)

# else:
#     print("You chose not to transmit")




# --------------------- BEGIN NOSTR ----------------------------- #

# --- Check for keys in .env, if not then create --- #

check_keys = key.get_keys()

private_key = check_keys[0]
public_key = check_keys[1]


if public_key != '' or private_key != '':
        print("Keys found! They are:")
        print("Public Key: " + public_key + "\n")
        print("Private Key:" + private_key + "\n")

else:
        print("Keys don't exist! Creating new ones\n")

        new_keys = key.create_keys()
        
        print('Created keypair:')
        
        print("Public Key: " + new_keys[1] + "\n")
        print("Private Key:" + new_keys[0] + "\n")

        private_key = check_keys[0]
        public_key = check_keys[1]      

# --- Open Relay Socket and Get Last 10 Posts(test only) --- #

relay.open_socket("32e1827635450ebb3c5a7d12c1f8e7b2b514439ac10a67eef3d9fd9c5c68e245")