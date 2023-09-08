from time import sleep
from utils import post_creator,rss,scrapper

Publication = "Pune Mirror"
RSS_feed = []
#incomplete_tasks = []
task_added = False

while(True):

    temp = rss.rss_feed(Publication)

    if(len(RSS_feed)!=0 ):
        if(temp[0]['title']!=RSS_feed[0]['title']):
            new_tasks = []
            i=0
            while(temp[0]['title']!=RSS_feed[0]['title']):
                new_tasks.append(temp[i])
                i+=1
            RSS_feed = new_tasks
            task_added = True
        else:
            print("Nothing to do I am sleeping agin...zzzZZZ")
    
    elif(len(RSS_feed)==0):
        RSS_feed = temp
        task_added = True

    if(task_added):
        #1 Iterate over RSS Feeds
        for feed in RSS_feed[::-1]:
            if(feed["comp_stat"]):
                continue
            else:
                #2. scrape for the post contents
                print("SCRAPING Contents................")
                Extracted = scrapper.scrape(feed['link'])

                #3. Rewrite the Scrapped Content
                print("HACKING.........................")
                Rewritten = post_creator.gpt_gen(Extracted['content'])
                #4. Mark the task as done 
                feed['comp_stat'] = True

                #5. Post to wordpress 
                #Post_to_press(Rewritten)
                print("++++++++++++++++++++++++++++++++++++++DONE BRO !!!!!!+++++++++++++++++++++++++++++++++++++++++++++")
                print("Original Title:", Extracted['title'])
                print(Rewritten)
                print("++++++++++++++++++++++++++++++++DOING NEXT++++++++++++++++++++++++++++++++++++++++++++++")

        print("ALL Done !!!!")

        


    
    sleep(3600)