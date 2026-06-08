def read_data():
    import csv
    
    with open("data/study_log.csv", "r") as file:
        data = csv.reader(file)
        
        header = next(data)
        print(header)
        for row in data:
            date = row[0]
            subject = row[1]
            topic = row[2]
            mins = int(row[3])
            confidence = int(row[3])
            
            print("DATE", date)
            print("SUBJECT", subject)
            print("TOPIC", topic)
            print("MINUTES", mins)
            print("CONFIDENCE", confidence)
            print("=" * 25)
            
def main():
    read_data()

if __name__ == "__main__":
    main()