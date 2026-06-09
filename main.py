from modules.file_handler import get_header, read_data, display_table



def main():
    
    get_file = input("Enter file name: ")
    
    
    header = get_header(get_file)
    
    rows = read_data(get_file)
    
    display_table(header, rows)
    
    
    
    

if __name__ == "__main__":
    main()