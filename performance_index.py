# performance_index.py

def calculate_ppi(data):
    # Custom formula to calculate a performance index
    data['ppi'] = (data['overall_rating'] * 2 + data['potential'] + data['reactions'] +
                   data['composure'] + data['vision']) / data['age']
    return data
