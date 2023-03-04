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

import random
import pyfiglet
import shutil
import time

# Get the width of the console
columns, _ = shutil.get_terminal_size()

# Add random characters to the output
def corrupt_output(text):
    result = ""
    for char in text:
        if random.random() < 0.2:
            result += random.choice(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "/", "\\", "|", " "])
        else:
            result += char
    return result

space_addicts_banner = pyfiglet.figlet_format("SPACE ADDICTS", font="isometric1", width=columns)
print(space_addicts_banner)

# Print the corrupted Viper Console message
viper_console_banner = corrupt_output(pyfiglet.figlet_format("VIPER CONSOLE", font="isometric1", width=columns))
print(viper_console_banner)

# Generate the BROCC OWNS YOU banner
brocc_banner = pyfiglet.figlet_format("BROCC OWNS YOU", font="larry3d", width=columns)
print(brocc_banner)

# Print the menacing yet charming message from Brocc
print("Your tools are no match for me, puny human. I am Brocc, the all-powerful ruler of the universe! Bow down before me or face my wrath! Ha ha ha!") 
# Pause for 2 seconds
time.sleep(2)

print("--=-=-=-= Reverse Shell exploit initiated -=-=-=-=-=")
# Pause for 2 seconds
time.sleep(2)

print("Capturing handshake....ok!")
# Pause for 2 seconds
time.sleep(2)

print("Transfer payload....ok!")
# Pause for 2 seconds
time.sleep(2)

print("Terminal console daemon initiated reverse shell exploit active")
# Pause for 2 seconds
time.sleep(2)

print("gO0D bYE")
# Pause for 2 seconds
time.sleep(2)

print("""

########B###BGBBBGBBBBBBBBGGGGBBBBBBGGPPPGBBBBGP5PPGPGGGGBBBGGBBBGPPBGPPPPPPPGGBG5YYPGGGGGG555PPPPPG
BBBBGGGPGBGGGGBGGPGGP5PP555Y55555555YJ?Y5PGGGGGPY??JJ5PPPPPPPP555555P5YY5YYJYGGGPJ!!7J5PGGG5Y?7???J5
BBBBGGGPYY5PGGGGPGGPYJJJYJJYYJJJ?77!77YP55YJJ?YGGP5YYJYPPPP55555PP5YG5Y55YYJJPGGGG5?77YPGGGBGP?!J775
BBBBGGGGGPYPGGGP5J?Y5Y7?5YJJ?7!7!!!7YPGGPJ?777J555GGPPYYY5YY55PPPYJ5PP5YYY5JY5PGGGGGP55PP5GGGPP5GGPP
BBBBGGGGBP555YYJYY?YPPY?PYJJ?7!!!!?5PPPGPJ??7JGGPPPPY5JY77YJ7J5P555JPP55P5YP5JY5PGGGP5YJJY5P5PPP5YJ5
PGGGBBGGPY5YPP5PGYYBGGGJYP5J??7!!!Y55555555?7?5GGPGP?7?7!!!!!!55Y5PJYGGGPPPGP5YYYY55YYYYY5YYYYYYYYPP
Y5P55PP555PPPYY5GPGGGGBY7Y5YJ?7!!!?5P5PPPPG5?7!JPGGPJ!?J?!!!!?P5J5PPYY55YY5GGPY5555PGPYY5P55YY55YYPG
5JJY5PGBBBBG5Y5PGGBGGBGG!JYYJJ?!!!!JPPPP5PGP5?!~!J5PJ7YJ?!!!!YP5555GBGGP55PPPGPGGGGGP55YPGPPP555P5PB
JJYYY5PGGGG55PGGGBBBBBGGJ755YJ??!!!75GPGPPGGB57!!!7JYYJ?7!!!!Y5Y5PPGGGGGGGGP55PGGGGPPPPPPPPGGGGGGBBB
!!!!77??JJ?75GGGBBGBBBBGP?Y55J?7!!!!?YGGGGPPGG?7!!7!J55?Y?7!!J5JYYPGGGGP5JPG5YPGGGGGGGGGGGG5PGGGGBGB
77?7!!!!!77?PGGGGGGGGBBGGYJ555JJ7!!!!75PPGGGGG57?7!!?77!?J?!!?5PGGGGGGG5Y!PJ7?PGGGGGGGGGGG5YPPPGGGGB
Y75JJJ7?7!!!!?Y5GGGGGGG5GYY555J77!!!!77YYPGGGGG??7!!777!!7!!!7GGGGGGGGGPJJP??7?Y55PPGGGGGPPGP5GGGGGB
5JYYGYY5?J7!7!!!7YPPPPPGPJJJJ???7!!!!7J??5PGGGPJJ77!!!!!Y?!!!!5GGGGGGGGYPGPYJJ?!!?YYPPPPPP55??PGGGGB
GPYJJYP555JJ?7!!~!?5PP5YJ?J777777!!!!?Y5PG5Y555J77!!!!7Y?!!!!?YPGGGGGPJYGP5Y?77!!JYJGP5J?!!!!!?YGGGB
PY5YY5YJYYPPYJ?7!!!!777!7!!!!!!!!!!!!!7!7??JYYJ77!!!!JY?!!!!!?J5P55PY?YGPP5?777775JJG5?!!7!!!?55GGB#
5YP55GP5YJ55P5?777!!!!~~!!777!!!~~~!!!!7!!?J77!!!!!!J5!~!!!!!7??Y5YJJJY55J?7!77!!7J??777777JY55Y5GBB
JY5YPGGY?PJ?5P5??7!!Y5J7~~!7J7!777!~!!!?!!7!7!~!!~!J57~!!!!!!!!777?Y7?JJ77!!!!!777?J777!7J5P5JYYYGB#
5J5PGGPY7JP??JYJ?77?7JPP5?~!!J7!!J557!!J7!!!~!~~~7J5J~~~~!!!!!!!!!!!J7!!!!!!!!!!?J!777?YYYYY555Y5PB#
55P55YYYY5PY??YY?!7?????5Y?!!!?7!!?55!~7J7!~~7!~7YJ7~~~~~~~7!~~!!!!?J!!??!!!7!!!!!?Y5PPYJY5PP55Y55GB
JY5J5PPPPPP5J7?J7~7J????5YYY?7!?Y?7!?J^!7?!~~~!J5Y!~~~!!!7!7~~!!~~!!!~!!!!!!57!!!7GBGGGG5Y5G5Y5YYYBB
P55PPYY5Y??5J?J??7!?5GJ5G57JYYJ??JJ77J7!!7J7~~!YJ7!!!7J?7!~!!!~?J7!~~!~!!!7!5Y7!!JGGGGBGGPPPGPPPP5GB
GGGGGGYYJ?J55??YGY7?YGGGPP5YJYY5?!!!7?Y7!7JJJ~~~!JJ???7~~!JJ7!7!77!?Y?7?JYY5J?7!!?BBGGBBGBGGGGGGGGB#
GGGGGGPP55555?JPP??JJPG5JPPPPPP5P5YJ77?YJ??YY~~~JGP?!~!7?5Y77Y5Y5PPYJ???YJ7?!!!!7!YPGBBBBBGYYPGBGGGB
GGGGGGGGGPPP5JYPPY??JPGJ~PP5Y?JJYY5555YY5YYY?!~~?PGP?~!Y5J?JPGPGGPP777!!7!!~~!!!!!75GGGGGBBGGGGGGGGB
GGGPPGGGGPPGG55PY!???JYJ!PPP5!::^^^~~~7PGPY555Y77JPGGP5Y5PGPY7!7J5G5!J?7777?77777!JBGGGBGGGBBGBGGGGB
GGGPPGGGGGGGGGP?!!JYJ77J75PPPY7~~^^~~?PGGYJYY?Y7YJ?5PG5YJ?!~^^^^~!JB?!?7!77!!!!!775GBBBBGGGGGGGGGGBB
GGGGGGGGGGGGBGP?~7J5???J57Y55PPP5YYYPGPPY7??J!?~??!??5PPY!^^^^^^^~JB?!!!!!7??7!7Y5PGGBBBGGGGGBGGGBGB
GGGPGPGGGGGGBGPJ!?Y77J5J?JJJJY5GGGGGGG5Y!!!!!!7!77!777J5PPPY?JJY5GGY??7!!!!!!7!JGBPBBBBBBGGBBGGGGGBB
GGGGGGGGGGGGGGPY7Y?^!?J???JYY??YY55YPP5?77!!!!!!!!!77??77?J5P555YJ77YJ7!!7?7!!!5GGPBGBBBBGGGGGGGGGPG
GGGGGGGGGGGGBGG5?Y7~!!7?7?J??J???YYJ55J!!7!!!!!!!77!??777!77?77777!77!!!!!!!!!75BGPBGBGBBBBBBGBGGGGG
GGGGGGGGGGGGGGGGY???!!!!!77?JYY555JJ55?!!!!!!!!!!77!??7!77!!!7?JYJY?!!!!!!!!!!?GGPYBBBGGGGBBBGGBBGGB
GGGGGGGGGGGPGGGGG5????7??7JYPGPP5?YJ??!!!!!!!!!!!77?!!!!!!!!~7YY5PJ77!!!!!!75Y55YJYBBBBBBBBBGPGGBGGB
GGPGGGGGGGPGGGGGGG5Y?J5555GGPPYJ?JJ?7!!!!!!!!!!!!!7J7!!!!!!?7!!!77?J!!!7!!!!?PY7!?GBGGBBGGGBBGBGGBGG
GGGGGGGGGPGGGGGGGBGPJYPPGBG5J?7?7?J?!!!!!!!!77!!!!!??!!!!!!?YYJ?7!!!!!!!!!!!Y57!!PBGGGGGGGGGBBBBGBGG
GGGGGGGGGGGGGGGGGBBG55GGBP???5???J7!!~!!!!!J5Y7!!!!7?!!!!!!!~!?YYYJ?7!!!!!~Y57!!5BBGGBBBBBGBBBBBBBBB
GGGGGGGGGPYJYPPGGGGGGGGGG??7?Y7JPPJ7JJYYYYJYYYJYYY55P5Y5YY5J!7?!!?JYJ??77!?P?!!7GBBBBBBBBBBBBBBBBBB#
GGPGGGPP5GP5Y55YGGGGGGGGY!7?J5Y7P5PJ?JY5PPPPP5P5YYJ?777?JJ?!!?7!~~~7JYYY5Y5?77!?GBBBBBBBBBBGBGBBBBB#
GGGGGGGGGGGPGGPJ5GGGGGGGJ7??JJJYP55PP5YJJJJJ????????7?7J7JJ!!!!!!!!!!7?5YJ77?7!?GBBBBBBBBBBBBBBBBBB#
GGGGGGGGGGGGGGPJ5GGGGGGGY7???JYYYY5555PPPPPPPPPPPPPP557?7!!!!!!!!77!77J5?7?7!~~7GGBBBBGBBBBBBBBBBBBB
GGGGGGGGGGGGGGP?5BGGGPPP577?YPP5YJ555YYYYYJJJJJJJJJJJYY?7!!!!!!!!!!777???JY7!!~?GGGGGGGGBBBBBBBBBBB#
GGGBGGPGGGGGGG5YYGGPPPPPP5JJYPP5555P5??J?77777777777??7!!!!!!!!!77777777?5Y!!~~?PGGBBBBGGGBGGBBBBBB#
PGGBBBBBBBBGGGY?YGPPPPPPPGP5555PPPP5YJJ?7~!7J?7777?J?~~!!77!!!!7777?7!!7?557!~!YGGGGGGBBBBBBBBBBBGB#
GGBBBBBBBBGGGPJJ5GGGPPPPPPPP55PPPPP555J?7~!JY7~!7JJ?!!!!!75Y77777?YJ!7?5YJ7!!!JGGGGGPPGBBBBB#BB#BBB#
BB##BBGGGPGGGG5Y5GGPPPPP5PPPPPP5PPGPPPYJ?!7JY7~~??!!777777J5Y7??777!!?Y5J7777?PGBBBBGGGGGBBBBB###BBB
BBBBGGBGGGGGGGGPPGGPGGPPPPPPPPPPPPPPPPPJ7!777!7J?!!7!!!7777Y55J7!??!!?YJ77777?YPGBBBBBBBGBBBBBB#BGBB
BBGPGGGGGGGGGGPGGPPPGGGPGGPPPGPPPPGPPPGGYJ???J5JJJJJJYYYYYY55Y??JY??7Y5J7!77???YGGBBBBBGGGBBBBBBB#B#
PGGGGGPPGGG5Y5PPYYYYY555PGGBBP55PPGBBGGGPGBBBBBBBBBBBGBBB##BGGBBBBGGGGGGPPPPPGGGB##BBBGGPGGGB##BBB##

""")


exit()

