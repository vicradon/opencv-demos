import numpy as np
import cv2 as cv
import argparse 

def main(device, capture=False):
    cap = cv.VideoCapture(device)

    if not cap.isOpened():
        print("Error: Cannot open device")
        return
    
    if capture:
        frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv.CAP_PROP_FPS)) if cap.get(cv.CAP_PROP_FPS) > 0 else 30

        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height), isColor=False)
    
    while cap.isOpened():
        ret, frame = cap.read()
     
        # if frame is read correctly ret is True
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
    cv.destroyAllWindows()

if __name__ == "__main__":
    arg_parse = argparse.ArgumentParser(description="get args")
    arg_parse.add_argument("device")
    args = arg_parse.parse_args()

    if args.device == "0":
        main(int(args.device), capture=True)
    else:
        main(args.device)
