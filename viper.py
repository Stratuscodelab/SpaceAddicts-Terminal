

                                                                                                                     
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


import random
import pyfiglet
import shutil

# Get the width of the console
columns, _ = shutil.get_terminal_size()

space_addicts_banner = pyfiglet.figlet_format("SPACE ADDICTS", font="isometric1", width=columns)
print(space_addicts_banner)

ascii_banner = pyfiglet.figlet_format("VIPER CONSOLE")
padding = (columns - len(ascii_banner.split('\n')[0])) // 2
ascii_banner = '\n'.join([' ' * padding + line for line in ascii_banner.split('\n')])
print(ascii_banner)

# Define the rival pizza companies and their weakness
rivals = {'Sokan Pizza': 'weak security system',
          'King Pizza': 'vulnerable delivery drones',
          'Uncle Sals': 'unprotected customer data',
          'Bad Bones': 'antiquated phone system '}

# Define the player's pizza company and their strengths
player_company = {'name': 'Viper, Cipher',
                  'strength': 'advanced hacking tools'}

# Define the available hacking tools and their power
hacking_tools = {'Data Breach': 3,
                 'DDoS Attack': 4,
                 'Phishing Scam': 5,
                 'Phone Phreaker': 6}

# Define the rival company's defenses and their strength
company_defenses = {'Firewall': 3,
                    'Anti-Virus Software': 4,
                    'Intrusion Detection System': 5,
                    ' Phone Tampering System': 6}

# Define the number of turns
turns = 3

# Start the game
print(f"Welcome to {player_company['name']}'s Pizza! Your mission is to hack into rival pizza companies and steal their secret recipes.")
print(f"You have {turns} turns to complete your mission.")

# Loop through each turn
for turn in range(1, turns+1):
    
    # Display the available hacking tools and their power
    print("\nAvailable hacking tools:")
    for tool, power in hacking_tools.items():
        print(f"{tool} ({power} power)")
    
    # Ask the player to choose a hacking tool
    tool_choice = input("\nChoose a hacking tool: ")
    
    # Check if the tool choice is valid
    if tool_choice not in hacking_tools:
        print("Invalid tool choice. Please try again.")
        continue
    
    # Display the rival pizza companies and their weakness
    print("\nRival pizza companies and their weakness:")
    for rival, weakness in rivals.items():
        print(f"{rival} ({weakness})")
    
    # Ask the player to choose a rival company
    rival_choice = input("\nChoose a rival pizza company: ")
    
    # Check if the rival choice is valid
    if rival_choice not in rivals:
        print("Invalid rival choice. Please try again.")
        continue
    
    # Display the rival company's defenses and their strength
    print(f"\n{rival_choice}'s defenses and their strength:")
    for defense, strength in company_defenses.items():
        print(f"{defense} ({strength} strength)")
    
    # Calculate the hacking power and defense strength
    hacking_power = hacking_tools[tool_choice]
    defense_strength = company_defenses[random.choice(list(company_defenses))]
    
    # Determine the outcome of the hack
    if hacking_power > defense_strength:
        print("Hacking successful!")
        print(f"You have accessed {rival_choice}'s secret recipe transfer initiated.")
        break
    else:
        print("Hacking failed!")
        print(f"{rival_choice} has detected your attempt and strengthened their defenses.")
        company_defenses[random.choice(list(company_defenses))] += 1

# Game over
print("\nTransfer Complete... Closing connection *gOOD bYE*.")



