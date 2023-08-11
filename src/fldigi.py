import pyfldigi
import time

fldigi = pyfldigi.Client()
rx_len = 0
msg_recived = False

# ----------FLDIGI START AND INIT CLASS  ---------- #

 
#if __name__ == "__main__":


# ---- GETTERS AND SETTERS HERE ---- #


def get_modem_name():

    return fldigi.modem.name

def get_modem_carrier():

    return fldigi.modem.name

def get_rig_frequency():

    return fldigi.rig.frequency

def get_rig_mode():

    return fldigi.rig.frequency

def get_text():

    print(fldigi.text.get_tx_data())

def set_modem(name, carrier):

    fldigi.modem.name = name

    fldigi.modem.name = name

    fldigi.modem.carrier = carrier

def set_frequency(frequency, mode):
    fldigi.rig.frequency = frequency
    fldigi.rig.mode = mode


def send_tx(json):

    
    fldigi.text.clear_tx()
    fldigi.text.add_tx(json)
    fldigi.main.send(json, block=True, timeout=500)

    print("Text Sent..")

"""
Docstring Test

"""
def get_rx():
   
    fldigi.text.clear_rx()

    while True:
        
        rx_len = fldigi.text.get_rx_length()
        print("Length:", rx_len)
        rx_text = fldigi.text.get_rx(0,rx_len)
        #rx_text = fldigi.text.get_rx_data()

        rx_text = str(rx_text, 'ISO-8859–1')

        if rx_text == '':
            print("Nothing RX'd")
            time.sleep(100)
        else:        
            print(rx_text)
            fldigi.text.clear_rx()
            time.sleep(100)

    # while True:

    #     if get_rx():

    #         decoded = (get_rx())
    #         #decoded_string = decoded.decode()
    #         print (decoded)

    #         msg_recived = True
            


    #     if msg_recived == True:


    #         print("Received found data. Yay!")

    #         print(get_rx())

    #         time.sleep(1)


    #     else:
        
    #         print("Nope, continuing to listen")
    #         time.sleep(1)

    
        


#LOGIC GOES UNDER HERE

def radio_setup(frequency, mode, c_freq):

    if get_modem_name != mode or get_modem_carrier != c_freq:

        set_modem(mode, c_freq)

    if get_rig_frequency != frequency or get_rig_mode != 'USB':

        set_frequency(frequency, 'USB')


