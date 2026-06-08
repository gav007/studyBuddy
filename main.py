def read_data():
    import csv
    
    with open("data/study_log.csv", "r") as file:
        data = csv.reader(file)
        
        header = next(data)
        print(header)
        
        total_sessions = 0
        total_minutes = 0
        minutes_by_subject = {}
        weak_topics = []
        
        
        for row in data:
            date = row[0]
            subject = row[1]
            topic = row[2]
            mins = int(row[3])
            confidence = int(row[4])
            
            # find weak topics
            if confidence <= 2:
                weak_topics.append(subject + " - " + topic + " - confidence " + str(confidence))
            
            # how many minutes per subject
            if subject in minutes_by_subject:
                minutes_by_subject[subject] = minutes_by_subject[subject] + mins
            else:
                minutes_by_subject[subject] = mins
            
            # data testing
            print("DATE", date)
            print("SUBJECT", subject)
            print("TOPIC", topic)
            print("MINUTES", mins)
            print("CONFIDENCE", confidence)
            print("=" * 25)
            
            total_minutes += mins
            total_sessions += 1
            
        # print summary after loop  
        # total mins and sessions  
        print("TOTAL MINUTES", total_minutes)
        print("TOTAL SESSIONS", total_sessions)
        
        # mins by subject
        print("-" * 25)
        print("Minutes by subject:")
        
        for subject, time in minutes_by_subject.items():
            print(subject, time)
        
        # confidence of subject <= 2    
        print("-" * 25)
        for topic in weak_topics:
            print("TOPIC:", topic)
        


def main():
    read_data()

if __name__ == "__main__":
    main()