from voice_recognition import recognize_speech
from motor_control import move_forward, stop_motor, move_slow
from openai_api import process_command
from camera_follow import detect_objects

def main():
    while True:
        command = recognize_speech()
        if command:
            print("Processing command...")
            response = process_command(command)
            print(f"AI Response: {response}")

            if "follow me" in command:
                print("Moving forward...")
                move_forward()
            elif "stop here" in command:
                print("Stopping...")
                stop_motor()
            elif "run slow" in command:
                print("Slowing down...")
                move_slow()
            elif "scan object" in command:
                print("Scanning...")
                detect_objects()
            elif "exit" in command:
                print("Exiting program...")
                stop_motor()
                break

if __name__ == "__main__":
    main()
