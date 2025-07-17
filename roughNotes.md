// Knowledge and Comprehension
There is a log file that shows website data. There's a problem cause it keeps crashing...so what's the exact problem and how do you fix it?

// Creativity ... what you tried to do to complete it 

- Convert it into structured data, and then use Pandas 


// Structure and Presentation
First I identified what each part of the log means, since each line is in a simialr way. 


//Problem-solving, analysis and evaluation 

- 100.34.17.233 is an IP address
- {NO, SE, US, FR, DK, etc.} are country codes, e.g. Norway, Sweden, United States, France and Denmark
- 

Strategy:
1. Understand the log data's format
2. Handle the log data so it's usable 
3. Decide what parts of the log data we want to analyse. Treat it like Hypothesis Testing, where you decide the hypothesis, margin for whatever and stuff. 

- Repeated IP addresses  
- Identical user-agent strings
- Repeated timestamps
- Frequent requests to the same path

--- I'm going to use a dictionary to count the occurences of something in the total dataset and then flag any of the entries where the number is way too high. Since it's a 4 day period, I should do some research to find how often these things should pop up within a 4 day period. 


4. Analyse the data to get the results from whatever you've done
5. Analyse the results to see if there are problems and what those problems are...if any
6. Look into possible solutions and write the report. 

B. run from docker
https://docs.docker.com/get-started/



// Numeracy and commercial awareness 

(any numbers you use are accurate and you use some technical terms)


//Research 

https://www.arkoselabs.com/blog/blog-how-to-distinguish-bot-vs-human-traffic/

- We're assuming the log file does not use a standardised format as we failed to find one that matches

- CAPTCHAs are a way to help stop bot traffic

How does Docker container works?


https://www.cloudflare.com/en-gb/learning/bots/what-is-bot-traffic/

