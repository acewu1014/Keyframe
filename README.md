# KeyFrame(Shot detection)
## Data preparation
Assume we have 3 videos have to extract shot.
```
-1.mp4
-2.mp4
-3.mp4
```
First of all, we need a metadata in json format. And matadata should at least contain id, keywords, and artists. Look like something below

Notice: the id in metadata should share the same name with the video.
```
{"id":"XXXXX", "artists":["Amy", "Bryant"],"keywords":["Scary","Police","Drugs"]"}
```

Before start the extraction, your folder should look something like below
```
-ANY_FOLDER
    -videos
        -1.mp4
        -2.mp4
        -3.mp4
    -metadata.json
    -main.py
    -time_change.py
    -video_reader.py
```
##Quick Start
```
python main.py
```
After successfully run this program, corresponding label files should be the same place as your Videos.

