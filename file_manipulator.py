import sys

def display_message():
    print('Please enter one of the following commands to manipulate your file: reverse, copy, duplicate-contents, and replace-string')
    print('If you enter "python3 file_manipulator.py reverse <inputpath> <outputpath>", you can reverse the contents of inputpath and then write them to outputpath.')
    print('If you enter "python3 file_manipulator.py copy <inputpath> <outputpath>", you can copy the contents of inputpath to outputpath.')
    print('If you enter "python3 file_manipulator.py duplicate-contents <inputpath> n", you can duplicate the contents of inputpath n times.')
    print('If you enter "python3 file.manipulator.py replace-string <inputpath> needle newstring", you can replace needle with newstirng in inputpath.')

if len(sys.argv) < 4:  # Check whether the command is long enough to exexute the program.
    display_message()
    sys.exit(1)
else:
    command = sys.argv[1]
    content = ''
    input_path = sys.argv[2]

    if command == 'reverse':
        output_path = sys.argv[3]

        with open(input_path, 'r') as f:
            content = f.read()

        with open(output_path, 'w') as f:
            f.write(content[::-1])
    
    elif command == 'copy':
        output_path = sys.argv[3]

        with open(input_path, 'r') as f:
            content = f.read()

        with open(output_path, 'w') as f:
            f.write(content)

    elif command == 'duplicate-contents':
        number_of_copies = sys.argv[3]

        if not number_of_copies.isdecimal():  # Check whether the user inputs the number to duplicate the contents
            print('Please enter a natural number after the input path')
            sys.exit(1)
        
        else:
            number_of_copies = int(number_of_copies)

            with open(input_path, 'r') as f:
                content = f.read()

            with open(input_path, 'a') as f:
                for i in range(number_of_copies):
                    f.write(content)
    
    elif command == 'replace-string':
        if len(sys.argv) < 5:
            print("Illegal Command: Do you forget to enter something?")
            sys.exit(1)
        else:
            string = sys.argv[3]
            new_string = sys.argv[4]

            with open(input_path, 'r') as f:
                content = f.read()

            with open(input_path, 'w') as f:
                f.write(content.replace(string, new_string))
    
    else:
        display_message()
        sys.exit(1)

print('The file is successfully manipulated.')
sys.exit(0)