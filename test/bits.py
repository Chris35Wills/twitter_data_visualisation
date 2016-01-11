###############################
'''

results = api.search(q="geocode:37.781157,-122.398720,10000mi AND #2016 AND since:2015-12-31 AND until:2016-01-01", 
    rpp=1, page=1)

f = open("tweets_ny2016.csv", "a")

for result in results:
    #tweet_data=result.text.encode('utf-8')
    tweet_data=result.text.encode(encoding='utf-8', errors='ignore')
    print(tweet_data)
    f.write(str(tweet_data))
   
f.close()

rpp = 100.
page – The page number (starting at 1) to return, up to a max of roughly 1500 results (based on rpp * page.


    try:
        print(result.text)
        #f.write(result.text)
        #f.write("\n")
    except UnicodeEncodeError:
        for char in result.text:
            string=''
            try:
                print(char)
                string = string + char
            except UnicodeEncodeError:
                print("X")
                string = string + 'X'
            print(string)
        
f.close()

## loop data
## get tweets with geo
## get UTC time

class MyListener(StreamListener):

    # only write within a certain date
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#software_carpentry']) #Change the hastag
'''

