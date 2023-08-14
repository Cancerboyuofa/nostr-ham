import fldigi as fl
import key
import relay



# -------------------- FLDigi Setup & TX ------------------------ #


# fl.radio_setup(7025000.0,"BPSK63", 1500)

# print('Setting up radio...')


# q = input("do you want to send or rx?\n")

# if q.upper() == 'RX':
#         print("Starting TO Receive...")
#         fl.get_rx()
# else:

#         transmit = input('Please enter the text to transmit:\n')

#         confirm_tx = input("Are you sure want to transmit:" + transmit + "? Y/N\n")

#         if confirm_tx.upper() == 'Y':

#                 fl.send_tx(transmit)

#         else:
#                 print("You chose not to transmit")




# --------------------- BEGIN NOSTR ----------------------------- #

# --- Check for keys in .env, if not then create --- #
def keys_gen():
        check_keys = key.get_keys()

        private_key = check_keys[0]
        public_key = check_keys[1]


        if public_key != '' or private_key != '':
                print("Existing Keys found!\n")
                #print("Public Key: " + public_key + "\n")
                #print("Private Key:" + private_key + "\n")

        else:
                print("Keys don't exist! Creating new ones\n")

                new_keys = key.create_keys()
                
                print('Created keypair.\n')
                
                #print("Public Key: " + new_keys[1] + "\n")
                #print("Private Key:" + new_keys[0] + "\n")

                private_key = check_keys[0]
                public_key = check_keys[1]      

        # --- Open Relay Socket and Get Last 10 Posts(test only) --- #
        

        relay.open_socket("e3aefda887252a72cee3578d33b2dcd90e9fe53b8bed6347ef5e26f74211adbb")

keys_gen()


        

       

