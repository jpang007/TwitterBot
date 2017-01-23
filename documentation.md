So this project was something that my friend mentioned to me which would be a cool idea to implement. So I began to work on it and finally after so long I can finally say it works. I would like to implement more features in the future but for now this is okay. 
<br>
<h2>What is this?</h2>
<br>
TwitterBot is a bot that "streams" new Tweets related to the phrase you provide it then in turn retweets and follows all accounts. The point of this project is to develop my first bot to actually perform a real world task. Using Tweepy, this is possible as we have easy access to the Twitter API.
<br>
<h2>How is this useful?</h2>
<br>
We know that bots really are invovled in almost everything online, espeically when it comes to shopping for exclusive clothings, giveaways, etc. I wanted to develop my own that can potential win free stuff from Twitter (If you really believe that retweeting something will win you a free Iphone).
<br>
My main thought process through this project flip-flopped a lot, I was first attemping to store all the text IDs and user IDs into arrays and then retweet but that just causes issues mainly when you attempt to retweet a tweet that you have already tweeted. I experimented with streaming at first, switched to my own method, then switched back when I realized I was making no progress. However I really wanted to work and add more features than just a simple bot that could RT and follow people. I thought about it and realized most of the seemingly legit giveaways include pictures so I just filtered out only tweets with pictures to increase the number of legit tweets my bot works with. Then I have to work around the problem of Twitter imposing a following limit, and will implement a strategy around that too. 
<br>
My bot also takes into consideration and makes sure you haven't already tweeted a tweet before (as many spam accounts try to repost their tweets), if this wasn't handled the program would stop working. 
<h2> Problems </h2>
<br>
So naturally, there are several unexpected problems that come up when dealing with the internet. Tweets that attempted to defeat my glorious bot included: Fake Giveaways, IHEARTAWARDS, and even twitter accounts dedicated to finding bots! To deal with fake giveaways, I just implemented the photos only strategy above. Iheartawards is a music awards of sorts, and my twitter stream would just get cluttered with Justin Beiber and Selena Gomez fans, I just scanned the tweet text and if it contained Iheartawards I ignored it. Another problem is there exists accounts that just spam fake giveaways! Most of these accounts have a screen name such as BotFinder (https://twitter.com/botfinder_g). Therefore, I had to locate the screen names of all tweets I was reading and kill the bots. 
