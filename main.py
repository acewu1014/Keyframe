import cv2
import json
import os
import pandas as pd
from scenedetect import detect, ContentDetector
from video_reader import VideoReader
from time_change import milisec

download_img = True
#read meatdate
entries = {}
translate = {}
for entry in open('metadata.json',"r",encoding="utf-8"):
    #since the metadata contains multiple json objects
    #and json can only load one object at a time 
    entry = json.loads(entry)
    entries[entry['id']] = entry

#Read translation file
tran = pd.read_csv("Corrected_keywords.csv") 
for i in range(len(tran['Keywords'])):
    translate[tran['Keywords'][i]] = tran['Chinese'][i]
#get all videos in video directory
if 'videos' in os.listdir():
    os.chdir('videos')
    video_list = os.listdir()
else:
    print("Error on the path")

for video in  video_list:
    #save all shots
    name = video[:-4]
    shots = []
    reader = VideoReader(video)
    scene_list = detect(video , ContentDetector())
    #json file in the below format
    #{"index": , "boundary_timecode": ( , ), "boundary_frame": ( , ), "tag": [], "artists": []}

    #access the metadata to get the tag and artists information
    keyword = entries[name]['keywords']
    artists = entries[name]['artists']

    #Translate keywords
    for i in range(len(keyword)):
        keyword[i] = translate[keyword[i]]
    
    print(keyword)

    for i, scene in enumerate(scene_list):
        # print('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
        #     i+1,
        #     scene[0].get_timecode(), scene[0].get_frames(),
        #     scene[1].get_timecode(), scene[1].get_frames(),))
        shot = {}
        shot['index'] = i
        shot['boundary_timecode'] = (milisec(scene[0].get_timecode()), milisec(scene[1].get_timecode()))
        shot['boundary_frame'] = (scene[0].get_frames(), scene[1].get_frames())
        shot['keywords'] = keyword
        shot['artists'] = artists
        shots.append(shot)

        if download_img:
            target = (scene[1].get_frames()+scene[0].get_frames())/2
            target = int(target)
            print(target)
            reader.seek(target)
            frame = reader.read()
            
            cv2.imwrite(f"keyframe/{i}.jpg", frame)
    
    name = name+".json"
    with open(name , 'w',encoding="utf-8") as outputfile:
        for shot in shots:
            json.dump(shot, outputfile, ensure_ascii=False)
            outputfile.write('\n')

