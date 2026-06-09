import csv

# gets the header
def get_header(file_path):
    
    
    try:
        with open(file_path, "r") as file:
            data = csv.reader(file)
            
            
            header = next(data)
            
            return header
    
    except FileNotFoundError:
        print("File not found in location")
        # Python can throw a tantrum
        return []
        
    

# gets the rows 
def read_data(file_path):
    rows = []
   
    try:
        with open(file_path, "r") as file:
            data = csv.reader(file)
            
            header = next(data)
            for line in data:
                rows.append(line)
        return rows
    except FileNotFoundError:
        print("File not found")
        return []
        

def display_table(header, rows):
    print(header)

    for row in rows:
        print(row)