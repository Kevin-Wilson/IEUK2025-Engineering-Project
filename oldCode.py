'''
import pprint # used for nice printing 
pp = pprint.PrettyPrinter(indent=2)
for entry in convertedData[:4]:
    pp.pprint(entry)
'''

'''
timestamps = [
    datetime.strptime(entry['datetime'], "%d/%m/%Y:%H:%M:%S")
    for entry in convertedData
]

if timestamps:
    earliest = min(timestamps)
    latest = max(timestamps)
    print(f"Earliest timestamp: {earliest}")
    print(f"Latest timestamp: {latest}")
    print(f"Period covered: {latest - earliest}")
else:
    print("No valid timestamps")
'''

'''
    counts = np.array(list(ipCount.values()))
    if counts.size > 0:
        q1 = np.percentile(counts, 25)
        q3 = np.percentile(counts, 75)
        IQR = q3 - q1
        UB = q3 + IP_OUTLIER_THRESHOLD * IQR  
        print(f"Q1: {q1}, Q3: {q3}, IQR: {IQR}, Upper Bound: {UB} with threshold: {IP_OUTLIER_THRESHOLD}\n")
        for ip, count in ipCount.items():
            if count >= UB:
                print(f"{ip}: {count} times")
'''

'''
def countRepeatIP(convertedData):
    entryCount = {}
    for entry in convertedData:
        ip = entry['ipAddress']
        if ip in entryCount:
            entryCount[ip] += 1
        else:
            entryCount[ip] = 1
    return entryCount 
'''