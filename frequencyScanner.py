

                                                                                                                     
#@@@@@@   @@@@@@@    @@@@@@    @@@@@@@  @@@@@@@@      @@@@@@   @@@@@@@   @@@@@@@   @@@   @@@@@@@  @@@@@@@   @@@@@@   
#@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@   
#!@@       @@!  @@@  @@!  @@@  !@@       @@!          @@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@         @@!    !@@       
#!@!       !@!  @!@  !@!  @!@  !@!       !@!          !@!  @!@  !@!  @!@  !@!  @!@  !@!  !@!         !@!    !@!       
#!!@@!!    @!@@!@!   @!@!@!@!  !@!       @!!!:!       @!@!@!@!  @!@  !@!  @!@  !@!  !!@  !@!         @!!    !!@@!!    
# !!@!!!   !!@!!!    !!!@!!!!  !!!       !!!!!:       !!!@!!!!  !@!  !!!  !@!  !!!  !!!  !!!         !!!     !!@!!!   
#     !:!  !!:       !!:  !!!  :!!       !!:          !!:  !!!  !!:  !!!  !!:  !!!  !!:  :!!         !!:         !:!  
#    !:!   :!:       :!:  !:!  :!:       :!:          :!:  !:!  :!:  !:!  :!:  !:!  :!:  :!:         :!:        !:!   
#:::: ::    ::       ::   :::   ::: :::   :: ::::     ::   :::   :::: ::   :::: ::   ::   ::: :::     ::    :::: ::   
#:: : :     :         :   : :   :: :: :  : :: ::       :   : :  :: :  :   :: :  :   :     :: :: :     :     :: : :    
# =-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- @Arm_710 -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# =-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-   2023   -=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  


import time
import shutil
import pyfiglet

# Get the width of the console
columns, _ = shutil.get_terminal_size()

space_addicts_banner = pyfiglet.figlet_format("SPACE ADDICTS", font="isometric1", width=columns)
print(space_addicts_banner)

# Print console welcome
ascii_banner = pyfiglet.figlet_format("-Frequency- \n ^^Scanner^^", font = "banner3-D", width=columns )
padding = (columns - len(ascii_banner.split('\n')[0])) // 2
ascii_banner = '\n'.join([' ' * padding + line for line in ascii_banner.split('\n')])
print(ascii_banner)


print("\nWelcome to the Asteroid City Scanner.")
print("I am SAACS, an artificial intelligence designed to scan frequencies for wanted suspects.")
print("Please note that this scanner is restricted to authorized personnel only.")
text = "\nWelcome to the Asteroid City Scanner. \n "
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)  # adjust this number to change the delay

    print("\nPlease enter the name of the suspect you're looking for (type 'exit' to quit): ")
    suspect_name = input("> ")
    if suspect_name.lower() == "exit":
        print("Exiting Asteroid City Frequency Scanner...")
        break
    else:
        print(f"\nScanning the Asteroid City for signal of {suspect_name}...")
        time.sleep(2) # wait for 2 seconds to simulate scanning
        found = False # assume suspect not found
        for i in range(10):
            print(f"Tracing signal in quadrant {i+1}...")
            time.sleep(1) # wait for 1 second to simulate tracing signal
            if i == 5: # simulate finding the suspect in galaxy 6
                found = True
                break
        if found:
            print(f"\n -=-=-=-=-= Suspect {suspect_name} has been located in quadrant 6.-=-=-=-=-=")
            print("\n Sending drones to capture target...")
            time.sleep(2) # wait for 2 seconds to simulate sending drones
            print("Drones en route to quadrant 6...")
            time.sleep(2) # wait for 2 seconds to simulate drones en route
            print("Preparing to capture visual identification of suspect...")
            time.sleep(2) # wait for 2 seconds to simulate preparing to capture suspect
            print("\n -=-=-=-=-= Target captured successfully. Awaiting data link for Opensea Minting -=-=-=-=-=")
            time.sleep(2) # wait for 2 seconds to simulate awaiting data
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\n https://opensea.io/assets/ethereum/0xb5ec720f23804df2ef377764c714e4470a7dd539/33/")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            time.sleep(2) # wait for 2 seconds to simulate link for minting.
            print("\n Would you like to initiate transfer of ETH ")
            text = "\n > Yes, send 0.01ETH please . \n "
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.1)  # adjust this number to change the delay
            time.sleep(4) # wait for 2 seconds to simulate link for minting.
            print("\n **Waiting**")
            time.sleep(4) # wait for 2 seconds to simulate link for minting.
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\n ******* WARNING ! ******* Signal jammer has been detected ******* WARNING ! *******")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            text = "\n > Use Proximity avoidance, switch to Asteroid City Low Orbit Satelite \n "
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.1)  # adjust this number to change the delay
            print("\n Asteroid City Low Orbit Satelite handshake complete")

            def waiting_animation():
                    for i in range(4):
                        print("[=   ]", end="\r")
                        time.sleep(0.1)
                        print("[ =  ]", end="\r")
                        time.sleep(0.1)
                        print("[  = ]", end="\r")
                        time.sleep(0.1)
                        print("[   =]", end="\r")
                        time.sleep(0.1)
                    for i in range(4):
                        print("[==  ]", end="\r")
                        time.sleep(0.1)
                        print("[ == ]", end="\r")
                        time.sleep(0.1)
                        print("[  ==]", end="\r")
                        time.sleep(0.1)
                        print("[ == ]", end="\r")
                        time.sleep(0.1)
                    for i in range(4):
                        print("[=== ]", end="\r")
                        time.sleep(0.1)
                        print("[ ===]", end="\r")
                        time.sleep(0.1)
                        print("[==  ]", end="\r")
                        time.sleep(0.1)
                        print("[ == ]", end="\r")
                        time.sleep(0.1)
                    for i in range(4):
                        print("[ == ]", end="\r")
                        time.sleep(0.1)
                        print("[  ==]", end="\r")
                        time.sleep(0.1)
                        print("[ == ]", end="\r")
                        time.sleep(0.1)
                        print("[=== ]", end="\r")
                        time.sleep(0.1)

            waiting_animation()

            print("\n Transaction successful!")
            time.sleep(2)
            print("\n \n ** Closing Dataport **")
            time.sleep(2)
            print("** gO0D bYE **")
            exit()

        else:
            print(f"\nUnable to locate suspect {suspect_name} in any scanned quadrants.")
            print("Initiating secondary scans...")
            time.sleep(2) # wait for 2 seconds to simulate initiating secondary scans
            print("Scanning intergalactic frequencies...")
            time.sleep(2) # wait for 2 seconds to simulate scanning intergalactic frequencies
            print("No trace of suspect found.")
            print("Exiting Asteroid City Frequency Scanner...")
            break
