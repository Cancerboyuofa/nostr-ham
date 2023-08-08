import pyfldigi
import time

if __name__ == "__main__":

    msg_recived = False


    #FLDIGI START AND INITIALIZE HERE

    fldigi = pyfldigi.Client()


    #GETTERS AND SETTERS HERE


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

        fldigi.text.clear_rx()
        fldigi.text.clear_tx()
        fldigi.text.add_tx(json)
        fldigi.main.send(json, block=True, timeout=500)

        print("Text Sent..")


    def get_rx():

        
        rx_text = fldigi.text.get_rx_data()

        return rx_text


    #LOGIC GOES UNDER HERE

    def radio_setup(mode, c_freq):

        if get_modem_name != mode or get_modem_carrier != c_freq:

            set_modem(mode, c_freq)

        if get_rig_frequency != 7071000.0 or get_rig_mode != 'USB':

            set_frequency(7071000.0, 'USB')

    while True:

        if get_rx():

            decoded = (get_rx())
            decoded_string = decoded.decode()
            print (decoded_string)

            msg_recived = True
            


        if msg_recived == True:


            print("Received found data. Yay!")

            print(get_rx())

            time.sleep(1)


        else:
        
            print("Nope, continuing to listen")
            time.sleep(1)

