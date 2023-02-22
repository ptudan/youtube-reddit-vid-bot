from gtts import gTTS
import praw
from requests import Session
import re
from moviepy.editor import *


reddit = praw.Reddit(
    client_id="insert-here",
    client_secret="insert-here",
    password="hunter2",
    user_agent="testscript",
    username="my-user",
)
subreddit_name = "AMPToken"
amp_sub = reddit.subreddit(subreddit_name)

overall_text = "People in the " + subreddit_name + " once said... "
body_text  = ""
for submission in amp_sub.hot(limit=1):
    overall_text += submission.title
    body_text += submission.selftext

    # subm = reddit.submission(submission.id)
    # cmts = subm.comments
    # for cmt in cmts:
    #     overall_text += " . . . "
    #     overall_text += cmt.author.name
    #     overall_text += ": "
    #     overall_text += cmt.body

clip = VideoFileClip("Skate - 110734 (1).mp4") 

print(overall_text)


# tts = gTTS(overall_text)
# tts.save('hello.mp3')
audio = AudioFileClip('hello.mp3') 
txt_clip = TextClip(overall_text, fontsize = 25, color = 'white', stroke_color='black', stroke_width=3) 
txt_clip = txt_clip.set_position((0.0,0.7), relative=True).set_duration(13) 
txt_clip = TextClip(body_text, fontsize = 25, color = 'white', stroke_color='black', stroke_width=3) 
txt_clip = txt_clip.set_position((0.0,0.5), relative=True).set_duration(13) 
video = CompositeVideoClip([clip, txt_clip]) 

video = video.set_audio(audio)
output = video.write_videofile("test.mp4")
