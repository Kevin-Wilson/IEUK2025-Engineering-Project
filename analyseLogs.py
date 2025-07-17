import re # This uses regular expressions to convert the log file into a list of strings
import numpy as np # This uses numpy functions to calcualte outliers using an interquartile range
import pytz # This is used for timezoners when the current timestamp is printed
from datetime import datetime # This is used to handle datetime strings

IP_OUTLIER_THRESHOLD = 8            # Default value = 8
AGENT_OUTLIER_THRESHOLD = 1.5       # Default value = 1.5
PATH_OUTLIER_THRESHHOLD = 4000      # Default value = 4000
DATETIME_OUTLIER_THRESHOLD = 2.5    # Default value = 2.5

# This is a regex pattern to match the log entries
log_pattern = re.compile(
    r'(?P<ipAddress>\S+)\s+-\s+(?P<countryCode>\S+)\s+-\s+\[(?P<datetime>[^\]]+)\]\s+'
    r'"(?P<httpMethod>\S+)\s+(?P<httpPath>\S+)\s+(?P<httpProtocol>[^"]+)"\s+'
    r'(?P<statusCode>\d+)\s+(?P<responseSize>\d+)\s+"(?P<referrer>[^"]+)"\s+'
    r'"(?P<userAgent>[^"]+)"\s+(?P<responseTime>\d+)'  
)

def convertData(filePath):
    """Convert the text from a log file into a list of lines.

    Keyword arguments:
    filePath -- a path to the relevant file, e.g. 'sample-log.log'
    """
    convertedData = []
    with open(filePath, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                convertedData.append(data)
    return convertedData

def countRepeats(key, convertedData):
    """Return a dictionary with each unique value and their respective counts.

    Keyword arguments:
    key -- the key of the line to count, e.g. 'ipAddress'
    convertedData -- the list of Match strings from the log file
    """
    entryCount = {}
    for entry in convertedData:
        value = entry[key]
        if value in entryCount:
            entryCount[value] += 1
        else:
            entryCount[value] = 1
    return entryCount

def flagOutliers(entryCount, threshold, keyName):
    """Return a dictionary with every key with an anamolously high count

    Keyword arguments:
    entryCount -- a dictionary that counts the values for a key
    threshold -- the custom threshold that this key corresponds to
    keyName -- the name of the key used for print statements
    """
    counts = np.array(list(entryCount.values()))
    if counts.size > 0:
        q1 = np.percentile(counts, 25)
        q3 = np.percentile(counts, 75)
        IQR = q3 - q1
        UB = q3 + threshold * max(IQR,1)  # to prevent getting stuck at q3
        print(f"{keyName} \n Q1: {q1}, Q3: {q3}, IQR: {IQR}, Upper Bound: {UB} with threshold: {threshold}\n")
        return {k: v for k, v in entryCount.items() if v > UB} #using > and not >= to avoid edge cases with many identical numbers
    return {}

def printOutliers(outliers):
    """Print the outliers in a readable format
    
    Keyword arguments:
    outliers -- a dictionary of outliers to print
    """
    if outliers:
        for key, value in outliers.items():
            print(f"{key}: {value} times")
        print()
    else:
        print("No outliers found\n")

def countAllRepeats(convertedData):
    """Returns a tuple of dictionaries for each key counted
    
    Keyword arguments:
    convertedData -- the list of Match strings from the log file
    """
    ipCount = countRepeats('ipAddress', convertedData)
    userAgentCount = countRepeats('userAgent', convertedData)
    httpPathCount = countRepeats('httpPath', convertedData)
    datetimeCount = countRepeats('datetime', convertedData)
    return ipCount, userAgentCount, httpPathCount, datetimeCount

def flagAllOutliers(ipCount, userAgentCount, httpPathCount, datetimeCount):
    """Returns a tuple of dictionaries for each outlier flagged
    
    Keyword arguments:
    ipCount -- the dictionary of IP counts
    userAgentCount -- the dictionary of User Agent counts
    httpPathCount -- the dictionary of HTTP Path counts
    datetimeCount -- the dictionary of Datetime counts
    """
    flaggedIP = flagOutliers(ipCount, IP_OUTLIER_THRESHOLD, 'ipAddress')
    flaggedUserAgent = flagOutliers(userAgentCount, AGENT_OUTLIER_THRESHOLD, 'userAgent')
    flaggedHttpPath = flagOutliers(httpPathCount, PATH_OUTLIER_THRESHHOLD, 'httpPath')
    flaggedDatetime = flagOutliers(datetimeCount, DATETIME_OUTLIER_THRESHOLD, 'datetime')
    return flaggedIP, flaggedUserAgent, flaggedHttpPath, flaggedDatetime

def printAllOutliers(flaggedIP, flaggedUserAgent, flaggedHttpPath, flaggedDatetime):
    """Prints all the outliers in a readable format
    
    Keyword arguments:
    flaggedIP -- the dictionary of flagged IPs 
    flaggedUserAgent -- the dictionary of flagged User Agents
    flaggedHttpPath -- the dictionary of flagged HTTP Paths
    flaggedDatetime -- the dictionary of flagged Datetimes
    """
    print("Flagged IPs:")
    printOutliers(flaggedIP)
    print("Flagged User Agents:")
    printOutliers(flaggedUserAgent)
    print("Flagged HTTP Paths::")
    printOutliers(flaggedHttpPath)
    print("Flagged datetimes:")
    printOutliers(flaggedDatetime)

def main():
    """Main function to analyse the log file"""
    print(f"====================================== {datetime.now(pytz.timezone('Europe/London'))} ======================================")
    convertedData = convertData('sample-log.log')
    allCounts = countAllRepeats(convertedData)
    allFlagged = flagAllOutliers(*allCounts)
    try:
        printAllOutliers(*allFlagged)
    except ValueError as e:
        print(f"Error: {e}")
    print("=================================================================================================")

if __name__ == "__main__":
    main()
