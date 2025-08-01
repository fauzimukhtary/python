import cv2

reference = cv2.CascadeClassifier('reference.xml')
cap = cv2.VideoCapture(0)

def detect(frame):
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = reference.detectMultiScale(optimized_frame,
                                       scaleFactor=1.1,
                                       minNeighbors=5, minSize=(100, 100)
                                       )
    return faces

def drawer_box(frame):
    for x, y, w, h in detect(frame):
        cv2.rectangle(frame, (x , y), (x + w, y + h),
                      (125, 150, 20), 6)

def close():
    cap.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = cap.read() 
        drawer_box(frame)
        cv2.imshow('ZEE CAMERA FACE DETECTION', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if chr(key).lower() == 'q':
            close()

if __name__ == "__main__":
    main()