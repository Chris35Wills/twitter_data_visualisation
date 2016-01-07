#Notes for twitter project

##Purpose of development exercise

1. Access some data 
2. Analyse that data somehow
3. Explain + visualise results
4. Enable interactivity

##Loose plan

Lots of people have played with twitter data, visualising locations of "good moring" hashtags etc. as exemplified [here](http://mashable.com/2009/06/30/gorgeous-twitter-visualizations/#vSboAlmalgqC). So perhaps we could use something topical. 

In terms of a rough plan:

-Download some twitter data

-Search the data and pull out specific hash tags, time stamps and geolocations

-Plot geodata (using basemap) in space

-Plot geodata (using basemap) in space and time

-Incorporate the visualisation over a rotating globe with a timer on screen?

So this could result in a few modules:

	twitter_analysis.py
		- accessing data
		- subsetting/querying
		- creating xyz(time) files

	visualisation.py
		- develop a globe map
		- get it rotating (embed this in a browser?)
		- take in data from twitter_analysis.py

	main.py
		- call all modules
		- only this has to be run 

##Project ideas

Just like the [original cholera map](https://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak), it would be inetresting to see how people respond to events through hashtags.

### Natural disaster reponse

Possible to map the recent flood events in the UK by considering the spread of hashtags like #flood or #stormfrank?

### Meme ideas

Memes are abundant with twitter, facebook etc. and are more and more seen as empathy buttons (see [here for example](http://www.theatlantic.com/entertainment/archive/2015/11/pray-for-paris-empathy-facebook/416196/)). However, others are more skeptical about their use.

Could use hashtag data to consider how these memes spread through time and space relative to specific events?

## Useful packages:

[pandas](http://pandas.pydata.org/)

[numpy](http://www.numpy.org/)

[basemap](http://matplotlib.org/basemap/)

[tweepy]() (pip install tweepy==3.5.0 -- see [here](http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/))

##Helpful links:

[Twitter data visualisations]( http://mashable.com/2009/06/30/gorgeous-twitter-visualizations/#vSboAlmalgqC )

[Accessing hashtag data (discussion)](https://www.quora.com/What-is-the-best-tool-to-download-and-archive-Twitter-data-of-certain-hashtags-and-mentions-for-academic-research)

[Twitter mining with Python part 1](http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)

[Twitter mining with python part 2](http://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/)

[More resources for accessing twitter with python](https://dev.twitter.com/overview/api/twitter-libraries)

[Rotating globe using basemap (not tested yet!)](https://gist.github.com/jdherman/7282653)