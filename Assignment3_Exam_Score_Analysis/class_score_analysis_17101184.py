def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                if not line.startswith('#'):
                    values = [int(text) for text in line.split(',')]
                    data.append(values)
            except ValueError as ex:
                print(f'Cannot find the file. (message: {ex})')
    return data
        

def add_weighted_average(data, weight):
    for row in data:
        average = weight[0] * row[0] + weight[1] * row[1]
        row.append(average)   # TODO

def getMedian(data):
    data.sort()
    n = len(data)
    if(n==0): return None
    center = int(n/2)
    
    if(n%2 == 0):
        return (data[center-1]+data[center])/2.0
    else:
        return data[center]
    

def analyze_data(data):
    mean = sum(data) / len(data)     # TODO
    var = (sum([dat**2 for dat in data]))/len(data) - mean**2      # TODO
    median = getMedian(data)          # TODO
    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2:
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')