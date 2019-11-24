import random
import re

def main():
    command = input("> ")
    if (str(command) != "quit") and (str(command) != "exit"):
        try:
            #Split Up String into Useful Pieces
            find_dice = r"([0-9]*d[0-9]*)*(k[0-9]*)*(.*)"
            dice_groups = re.findall(find_dice, command)
            dice_groups = list(dice_groups)
            
            for group in dice_groups:
                if group != ('', '', ''):
                    # Do something With the Dice Bit
                    dice = group[0].split("d")
                    dice_results = [ random.randint(1, int(dice[1])) for _ in range(int(dice[0]))]
                    original_rolls = dice_results
                    
                    # Keepers
                    if group[1] !=  '':
                        keep_index = int(group[1].split("k")[1])
                        dice_results.sort(reverse=True)
                        dice_results = dice_results[0:keep_index]
                        original_rolls.sort(reverse=True)
                        original_rolls = original_rolls[0:keep_index]

                    new_results = []
                    # Calculations
                    if group[2] != '':
                        for roll in dice_results:
                            regex = r"[+]([0-9]*)"
                            number = list(re.findall(regex, group[2]))
                            if number != (''):
                                for num in number:
                                    roll += int(num)

                            regex = r"[-]([0-9]*)"
                            number = list(re.findall(regex, group[2]))
                            if number != (''):
                                for num in number:
                                    roll -= int(num)
                            
                            regex = r"[*]([0-9]*)"
                            number = list(re.findall(regex, group[2]))
                            if number != (''):
                                for num in number:
                                    roll *= int(num)

                            regex = r"[/]([0-9]*)"
                            number = list(re.findall(regex, group[2]))
                            if number != (''):
                                for num in number:
                                    roll //= int(num)

                            new_results.append(roll)

                    if len(new_results) != 0:
                        for x, y in zip(new_results, original_rolls):
                            print(f"{x}({y})")      
                    else:
                        for x,y in zip(dice_results, original_rolls):
                            print(f"{x}({y})")
        except:
            print("Unknown Command Presented. Please double check your command. e.g. 2d20k1+6 or 'exit' to exit the program")
        finally:
            main()
    else:
        quit()


print("Dice Roller!\nPlease input your command: ")
main()