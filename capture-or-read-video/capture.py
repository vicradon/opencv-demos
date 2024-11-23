import numpy as np
import cv2 as cv
import argparse 

def main(device, capture=False, output_file="output.avi"):
    cap = cv.VideoCapture(device)

    if not cap.isOpened():
        print("Error: Cannot open device")
        return
    
    if capture:
        frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv.CAP_PROP_FPS) or 30

        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height), isColor=False)
    
    while True:
        ret, frame = cap.read()
     
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if capture:
            out.write(gray)

        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
     
    cap.release()
    if capture:
        out.release()
    cv.destroyAllWindows()


'''
Usage:
    # capture camera 0 (default camera)
    python capture.py 0 --capture --output_file newvid.avi

    # see the content of a video
    python capture.py stretch.avi
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video capture arguments")
    parser.add_argument("device", help="Camera or video file number")
    parser.add_argument("--capture", action="store_true", help="Enable video capture")
    parser.add_argument("--output_file", type=str, help="Name of the video file to write to")
    args = parser.parse_args()

    device = int(args.device) if args.device == "0" or args.device == "1" or args.device == "2" else args.device

    main(device, capture=args.capture, output_file=args.output_file)
