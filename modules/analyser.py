def count_rows(rows):
    
    count = 0
    
    for row in rows:
        count += 1
    
    return count

def calculate_total_minutes(rows, header):
    
    minutes_index = header.index("Minutes")
    total_minutes = 0

    for row in rows:
        minutes = int(row[minutes_index])
        total_minutes += minutes

    return  total_minutes


def calculate_minutes_by_subject(rows, header):
    
    get_subject_index = header.index("Subject")
    get_minutes_index = header.index("Minutes")
    
    # creates a diction which will contain the suject as a key and minutes as a value
    minutes_by_subject = {}
    
    for row in rows:
        subject = row[get_subject_index]
        minutes = int(row[get_minutes_index])
        
        if subject in minutes_by_subject:
            minutes_by_subject[subject] = minutes_by_subject[subject] + minutes
        else:
            minutes_by_subject[subject] = minutes
            
    return minutes_by_subject