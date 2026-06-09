from modules.file_handler import get_header, read_data, display_table
from modules.analyser import calculate_total_minutes, count_rows


def main():
    
    # user input for the file (dummy data set)
    get_file = input("Enter file name: ")
    
    # get the header
    header = get_header(get_file)
    
    # get the rows
    rows = read_data(get_file)
    
    # print the table
    display_table(header, rows)
    
    print("-" * 80)
    
    # count rows
    get_row_count = count_rows(rows)
    print("NUMBER OF ROWS", get_row_count)
    
    # count minutes 
    get_minutes = calculate_total_minutes(rows, header)
    print("Total Minutes", get_minutes)
    
    
    

if __name__ == "__main__":
    main()