from motor_control import start_motor, stop_motor, slow_motor
from voice_recognition import capture_voice_command
from openai_api import interpret_command

def main():
    while True:
        command = capture_voice_command()
        if command:
            action = interpret_command(command)
            if "start" in action:
                start_motor()
            elif "stop" in action:
                stop_motor()
            elif "slow" in action:
                slow_motor()
            elif "exit" in action:
                print("Exiting...")
                break

if __name__ == "__main__":
    main()
