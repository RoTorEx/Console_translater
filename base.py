import random as r
import sys
import time

import pandas as pd
import xlwings as xw


class WordsDictionary:
    @staticmethod
    def config(*args, **kwargs):
        excel_data_df = pd.read_excel('words.xlsx')
        print(f"Excel size: {excel_data_df.shape}", excel_data_df, sep="\n\n")

    @staticmethod
    def add(*args, **kwargs):
        excel_data_df = pd.read_excel('words.xlsx')
        eng_list = excel_data_df['English'].tolist()
        rus_list = excel_data_df['Russian'].tolist()

        while True:
            eng_word = input("Enter\u001b[35m English\u001b[0m word: ").capitalize().strip()
            rus_word = input("Enter\u001b[35m Russian\u001b[0m word: ").capitalize().strip()

            zipped_words = zip(eng_list, rus_list)

            if (eng_word, rus_word) in zipped_words:
                print(f"Pare\u001b[31m {eng_word}\u001b[0m :\u001b[31m {rus_word}\u001b[0m already exist!")
                continue

            if eng_word == '' or rus_word == '':
                print("Empty fields are not added.")
                continue

            elif eng_word.lower() == 'stop' or rus_word.lower() == 'stop':
                exit()

            eng_list.append(eng_word)
            rus_list.append(rus_word)

            data = pd.DataFrame({"English": eng_list, "Russian": rus_list})
            data.to_excel('./words.xlsx', index=False)

            print(f"Added:\u001b[34m {eng_word}\u001b[0m <~>\u001b[34m {rus_word}\u001b[0m")

    @staticmethod
    def show(*args, **kwargs):
        # xls = pd.ExcelFile(f"{os.getcwd()}/words.xlsx")
        excel_data_df = pd.read_excel("./words.xlsx")
        eng = excel_data_df['English'].tolist()
        rus = excel_data_df['Russian'].tolist()
        eng_dict = {e: r for e, r in zip(eng, rus)}
        rus_dict = {r: e for e, r in zip(eng, rus)}

        while True:
            random_dict = r.choice([eng_dict, rus_dict])
            random_word = r.choice(list(random_dict.keys()))

            sys.stdout.write(f"\u001b[31m{random_word}\u001b[0m :\u001b[31m {random_dict[random_word]}\u001b[0m")
            sys.stdout.flush()
            time.sleep(2)

            sys.stdout.write(u"\x1b[2K\u001b[1000D")  # sys.stdout.write(u"\u001b[1000D")
            sys.stdout.flush()
            time.sleep(.1)

    @staticmethod
    def guess(*args, **kwargs):
        excel_data_df = pd.read_excel('words.xlsx')

        eng = excel_data_df["English"].tolist()
        rus = excel_data_df["Russian"].tolist()

        while True:
            language = r.choice(["English", "Russian"])
            words_couple = r.choice(list(zip(eng, rus)))

            match language:
                case "English":
                    guess = words_couple[0]
                    answer = words_couple[1]

                case "Russian":
                    guess = words_couple[1]
                    answer = words_couple[0]

            user_input = input(f"Translate\u001b[32m {guess}\u001b[0m from\u001b[35m {language}\u001b[0m: ")

            if user_input.lower().strip() == answer.lower():
                continue

            else:
                print(f"Correct translate is \u001b[31;1m{answer.capitalize()}\u001b[0m.")
