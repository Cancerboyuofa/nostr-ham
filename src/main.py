import fldigi as fl


# ------- FLDigi Setup Calls and TX HERE ----------#

fl.radio_setup("BPSK63", 1000)

print('Setting up radio...')

text = input('Please enter the text to transmit:\n')

confirm_tx = input("Do you want to transmit? Y/N\n")

if confirm_tx.upper() == 'Y':

    fl.send_tx("<MYCALL> " + text)

else:
    print("You chose not to transmit")



# ------- BEGIN NOSTR ------------ #

