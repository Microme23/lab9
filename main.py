import random
#Функція для виводу тексту файла
def read_and_print_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())
    except:
        print(f"File", file_name, "wasn't opened!")
    else:
        print(f"File", file_name, "was opened!")

#Функція для випадкового заповнення першого файлу
def create_text_file(file_name):
    try:
        with open(file_name, 'w') as file:
            for _ in range(10):
                line = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(5, 15)))
                file.write(line + '\n')
    except:
        print(f"File", file_name, "wasn't created!")
    else:
        print("File", file_name, "was created!")
#Функція для розділення чисел та літер
def Function_digit(file_input, file_output, file_help):
    try:
        with open(file_input, 'r') as input_file, open(file_help, 'w') as help_file, open(file_output, 'w') as out_file:
            digits = ''
            other_chars = ''
            for line in input_file:
                for char in line:
                    if char.isdigit():
                        digits += char
                    else:
                        other_chars += char
            help_file.write(other_chars)
            out_file.write(digits)
    except:
        print(f"One or more files weren`t opened")
    else:
        print(f"All the files were opened")
#Функція для запису чисел та розділення по 10 літер в другий файл
def Function_other (file_input, file_output):
      try:
          with open(file_input, 'r') as file1:
              numbers = file1.readline().strip()

          with open(file_output, 'r') as file2:
              characters = ''.join(file2.read().split())

          characters_lines = [characters[i:i + 10] for i in range(0, len(characters), 10)]
          merged_content = numbers + '\n' + '\n'.join(characters_lines)

          with open(file_output, 'w') as output_file:
              output_file.write(merged_content)
      except:
          print(f"One or more files weren`t opened")
      else:
          print(f"All the files were opened")


file1 = "TF17_1.txt"
file3 = "TF17_3.txt"
file2 = "TF17_2.txt"

create_text_file(file1)
Function_digit(file1, file3, file2)
Function_other(file3, file2)
read_and_print_file(file2)