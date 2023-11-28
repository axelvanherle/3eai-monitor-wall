import cv2

# Receive from all possible IPs on port 5000
stream_url = "http://0.0.0.0:5000/"

cap = cv2.VideoCapture(stream_url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to receive frame. Exiting...")
        break

    cv2.imshow('Video Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()