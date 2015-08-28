import soundcloud
import time
searchTerms = {
    0: 'indie rock',
    1: 'indie',
    2: 'electronic indie',
    3: 'electronic',
    4: 'rock',
    5: 'chill'
}

# create a client object with your app credentials
client = soundcloud.Client(client_id='YOUR_ID',
                           client_secret='YOUR_SECRET',
                           username='YOUR_USERNAME',
                           password='YOUR_PASSWORD')
def likeTracks(tag):
    print "searching for " + tag + " tracks"
    # find all sounds of buskers licensed under 'creative commons share alike'
    tracks = client.get('/tracks', tag_list={tag}, q='')

    #store the liked tracks in a file for easy unliking
    f = open("likes.txt","a")


    for track in tracks:
        print track.id
        try:
            client.put('/me/favorites/%d' % track.id)
            #client.delete('/me/favorites/%d' % track.id)
            f.write('%d \n' % track.id)
        except Exception as ex:
            print "     whoopsies, something went wrong "
    f.close()

def unlikeTracks():
    print "unliking..."
    with open("likes.txt","r") as f:
        for line in f:
            try:
                client.delete('/me/favorites/' + line)
            except Exception as ex:
                print "     whoopsies, something went wrong "
    f.close()
    f = open("likes.txt", "w")
    f.close()

def executeSomething():
    likeTracks(searchTerms[count % 5])
    print "waiting..."
    print ""
    time.sleep(900)

count = 0
while(count<20):
    executeSomething()
    count += 1
unlikeTracks()
