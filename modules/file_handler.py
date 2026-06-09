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
    
    print("STUDY BUDDY")
    print("-" * 80)

    date = header[0].ljust(15)
    subject = header[1].ljust(15)
    topic = header[2].ljust(25)
    minutes = header[3].ljust(12)
    confidence = header[4].ljust(12)

    header_display = date + subject + topic + minutes + confidence
    print(header_display)
    print("-" * 80)
    
    for row in rows:
        row_date = row[0].ljust(15)
        row_subject = row[1].ljust(15)
        row_topic = row[2].ljust(25)
        row_minutes = row[3].ljust(12)
        row_confidence = row[4].ljust(12)
        
        row_display = row_date + row_subject + row_topic + row_minutes + row_confidence
        print(row_display)