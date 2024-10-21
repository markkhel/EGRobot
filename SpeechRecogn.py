import speech_recognition as sr
import logging
from typing import Dict, Callable

class VoiceController:
    def __init__(self):
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Define commands and their corresponding actions
        self.commands = {
            "forward": self._move_forward,
            "back": self._move_backward,
            "left": self._move_left,
            "right": self._move_right,
            "stop": self._stop
        }
        
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Adjust for ambient noise
        with self.microphone as source:
            print("Adjusting for ambient noise... Please wait...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Ready!")

    def _move_forward(self) -> None:
        print("Moving forward")

    def _move_backward(self) -> None:
        print("Moving backward")

    def _move_left(self) -> None:
        print("Moving left")

    def _move_right(self) -> None:
        print("Moving right")

    def _stop(self) -> None:
        print("Stopping")

    def execute_command(self, command: str) -> None:
        """Execute the given voice command"""
        command = command.lower().strip()
        
        # Check each command keyword
        for key_word, action in self.commands.items():
            if key_word in command:
                action()
                return
        print(f"Command not recognized: {command}")

    def start_listening(self) -> None:
        """Start listening for voice commands"""
        print("Listening for commands... (Press Ctrl+C to stop)")
        
        while True:
            try:
                # Listen for audio input
                with self.microphone as source:
                    print("\nListening...")
                    audio = self.recognizer.listen(source)
                
                try:
                    # Try to recognize the speech
                    command = self.recognizer.recognize_google(audio)
                    print(f"Heard: {command}")
                    self.execute_command(command)
                    
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    
            except KeyboardInterrupt:
                print("\nStopping voice control system...")
                break
            except Exception as e:
                print(f"Error: {str(e)}")

def main():
    try:
        controller = VoiceController()
        controller.start_listening()
    except Exception as e:
        print(f"Failed to start voice controller: {str(e)}")

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 75c1376581e1557d1dd7d9925d21f0a8b257536b
