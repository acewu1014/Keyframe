import cv2
from scenedetect import detect, ContentDetector
from video_reader import VideoReader

video = '2JXJ8omdLPI71OQ1JaKILTFwswP.mp4'
reader = VideoReader(video)

scene_list = detect(video , ContentDetector())
for i, scene in enumerate(scene_list):
    # print('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
    #     i+1,
    #     scene[0].get_timecode(), scene[0].get_frames(),
    #     scene[1].get_timecode(), scene[1].get_frames(),))
    target = (scene[1].get_frames()+scene[0].get_frames())/2
    target = int(target)
    print(target)
    reader.seek(target)
    frame = reader.read()
    
    cv2.imwrite(f"keyframe/{i}.jpg", frame)


