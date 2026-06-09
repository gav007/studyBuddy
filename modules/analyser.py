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
