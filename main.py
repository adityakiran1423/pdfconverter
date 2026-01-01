import sys


def main():
    pdf_file_path = sys.argv[1]
    conversion_type = sys.argv[2]

    if pdf_file_path[-4:] != ".pdf":
        print("the file you have entered is not a pdf")
        sys.exit()
    else:
        # check if file actually exists
        # if pdf should be converted to excel then use tabula-py
        # if pdf should be converted to word then use dfminer.six
        print(f"pdf file path is : {pdf_file_path}")
        print(f"conversion type is : {conversion_type}")


if __name__ == "__main__":
    main()
