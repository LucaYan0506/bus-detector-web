import os
import cv2
import argparse

from ultralytics import YOLO
from moviepy.editor import VideoFileClip

def process_video(video_path,model_path):
    #get the video
    

    #path of the result video
    video_path_out = 'media/temp.mp4'

    #get frames of the videos
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    H, W, _ = frame.shape
    out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

    # Load a model
    model = YOLO(model_path)  # load a custom model

    threshold = 0.7

    while ret:
        results = model(frame)[0]

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            
            #filter the result
            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

        out.write(frame)
        ret, frame = cap.read()

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    # Ensure that video_path_out is no longer in use before deleting it
    # Load the video file
    clip = VideoFileClip(video_path_out)
    # Write the video file with a different codec
    result_path = 'media/result.mp4'
    clip.write_videofile(result_path, codec='libx264', audio_codec='aac')
    clip.close()  # Close the VideoFileClip object to release the file

    # Remove the original video file
    if os.path.exists(video_path_out):
        os.remove(video_path_out)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process a video file.")
    parser.add_argument('--path', type=str, required=True, help='relative path to the video file')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function with the provided path
    process_video(args.path)
