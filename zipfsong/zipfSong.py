#!/usr/bin/python

# Author Forrest

import sys

# quality = number of times played / number of times law thinks it would
# be played (value of first song divided by songs position on list).

class topSongs(object):

    def zipfItGood(self, songList):
        splitData = [i.split() for i in songList]
        numSongs = int(splitData[0][0])
        songsSelected = int(splitData[0][1])
        t = 1
        finalList = []
# We are using Zipfs law here, the interpreted law can be found above.
        for i in splitData[1::]:
            zipfVal = (float(splitData[1][0]) / t )
            actVal = (float(i[0]))
            quality = (actVal / zipfVal)
            theTuple = (splitData[t][1], numSongs, quality)
            finalList.append(theTuple)
            t += 1
            numSongs -= 1
        return(finalList, songsSelected)

    def sortSongs(self, zipfSongs, songsSelected):
        z = 1
# We take the passed in songs that have their zipf value figured, and
        # then sort them based on the value of the of they key
        zipfSongs.sort(key=lambda t: (t[2], t[1]), reverse = True)
        print(zipfSongs)
        for i in zipfSongs:
            print(i[0])
            z += 1
            if z > songsSelected:
                break
if not sys.stdin.isatty():
    songData = (line for line in sys.stdin.readlines() if line.strip() != '')
    topSongsInstance = topSongs()
    (zipfSolution, totalSongs) = topSongsInstance.zipfItGood(songData)
    topSongsInstance.sortSongs(zipfSolution, totalSongs )

if __name__ == '__main__' and sys.stdin.isatty():
    print("No file provided, exiting.")
