#!/bin/bash
ffmpeg -i final_video.mp4 -i voiceover.mp3 -c:v copy -c:a aac -strict experimental output_with_audio.mp4
