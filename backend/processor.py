

import cv2
import mediapipe as mp
from moviepy.editor import VideoFileClip
from faster_whisper import WhisperModel
import os

class VideoProcessor:
    def __init__(self):
        self.face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
        self.whisper = WhisperModel("base", device="cpu", compute_type="int8")

    def process(self, video_path):
    
        audio_path = f"{video_path}.mp3"
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path, logger=None)
        
        segments, _ = self.whisper.transcribe(audio_path)
        transcript = [{"start": s.start, "end": s.end, "text": s.text} for s in segments]

        
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frames_to_check = int(fps) 
        
        visual_data = []
        count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            
            if count % frames_to_check == 0:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.face_detection.process(rgb_frame)
                has_face = True if results.detections else False
                visual_data.append({"timestamp": count/fps, "active_speaker": has_face})
            count += 1
        
        cap.release()
        os.remove(audio_path)
        return {"transcript": transcript, "visuals": visual_data}