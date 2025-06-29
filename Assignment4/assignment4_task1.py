try:
    with open ('sample.txt','r') as file:
        print("Reading file content: ")
        lines = file.readlines()
        line_num = 1
        for line in lines:
            print(f"Line {line_num}: {line.strip()}")
            line_num += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' not found")

    
