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
            print(dice_groups[:len(dice_groups)-1])
            for group in dice_groups[:len(dice_groups)-1]:
                # Do something With the Dice Bit
                dice = group[0].split("d")
                dice_results = [ random.randint(1, int(dice[1])) for _ in range(int(dice[0]))]
                
                # Keepers
                if group[1] !=  '':
                    keep_index = int(group[1].split("k")[1])
                    dice_results.sort(reverse=True)
                    dice_results = dice_results[0:keep_index]

                result = int()
                for roll in dice_results:
                    result += roll
                    print(result)

                # Calculations
                if group[2] != '':
                    regex = r"[+]([0-9]*)"
                    number = list(re.findall(regex, group[2]))
                    if number != (''):
                        for num in number:
                            result += int(num)
                            print(f"Addition {num}")

                    regex = r"[-]([0-9]*)"
                    number = list(re.findall(regex, group[2]))
                    if number != (''):
                        for num in number:
                            result -= int(num)
                            print(f"Subtraction {num}")
                    
                    regex = r"[*]([0-9]*)"
                    number = list(re.findall(regex, group[2]))
                    if number != (''):
                        for num in number:
                            result *= int(num)
                            print(f"Multiplication {num}")

                    regex = r"[/]([0-9]*)"
                    number = list(re.findall(regex, group[2]))
                    if number != (''):
                        for num in number:
                            result //= int(num)
                            print(f"Division {num}")

                print(f"{result} {dice_results}")      
        except:
            print("Unknown Command Presented. Please double check your command. e.g. 2d20k1+6 or 'exit' to exit the program")
        finally:
            main()
    else:
        quit()


print("Dice Roller!\nPlease input your command: ")
main()