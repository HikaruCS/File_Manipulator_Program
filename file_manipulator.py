import sys

def display_message():
    # Write a help message about this program.
    print("Write it later.")

if len(sys.argv) < 4:
    display_message()
    sys.exit(1)
else:
    command = sys.argv[1]
    content = ''
    input_path = sys.argv[2]

    if command == 'reverse':
        output_path = sys.argv[3]

        with open(input_path) as f:
            content = f.read()
            content = content[::1]

        with open(output_path, 'w') as f:
            f.write(content)
    
    elif command == 'copy':
        output_path = sys.argv[3]

        with open(input_path) as f:
            content = f.read()

        with open(output_path) as f:
            f.write(content)

    elif command == 'duplicate_contents':
        number_of_copies = sys.argv[3]

        if not number_of_copies.isdecimal():
            print('Please enter a natural number after the input path')
            sys.exit(1)
        
        else:
            with open(input_path) as f:
                content = f.read()

            with open(input_path, 'a') as f:
                for i in range(number_of_copies):
                    f.write(content)
    
    elif command == 'replace-string':
        string = sys.argv[3]
        new_string = sys.argv[4]

        with open(input_path) as f:
            content = f.read()

        with open(input_path, 'w') as f:
            f.write(content.replace(string, new_string))
    
    else:
        display_message()
        sys.exit(1)

print('The file is successfully manipulated.')
sys.exit(0)