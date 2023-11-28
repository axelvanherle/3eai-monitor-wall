import cv2
import time

# Receive from all possible IPs on port 5000
stream_url = "http://0.0.0.0:5000/"

# Number of retries
max_retries = 3

# Retry interval in seconds
retry_interval = 5

retry_attempt = 1

while retry_attempt <= max_retries:
    try:
        cap = cv2.VideoCapture(stream_url)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to receive frame. Retrying...")
                break

            cv2.imshow('Video Stream', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        time.sleep(retry_interval)
        retry_attempt += 1

print("Maximum number of retries reached. Exiting.")
