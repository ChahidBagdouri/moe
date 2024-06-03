# Author: Jacob Johnston

import cv2
import os
import random

# Directory where images are saved
save_dir = "database"

# List of negative emotions
negative_emotions = ['angry', 'disgust', 'fear', 'sad']

# Function to display the quiz
def quiz_user():
    images = [f for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))]
    
    if not images:
        print("No images found in the directory.")
        return
    
    score = 0
    total = len(images)
    
    for img_file in images:
        img_path = os.path.join(save_dir, img_file)
        img = cv2.imread(img_path)
        
        # Extract the correct emotion from the filename
        correct_emotion = img_file.split('_')[0]
        
        # Display the image
        cv2.imshow('Guess the Emotion', img)

        # Ensure the correct emotion is included in the choices
        remaining_emotions = [e for e in negative_emotions if e != correct_emotion]
        choices = random.sample(remaining_emotions, 3) + [correct_emotion]
        random.shuffle(choices)
        
        # Present the choices
        for idx, emotion in enumerate(choices):
            print(f"{idx + 1}. {emotion}")
        
        # Read input from the terminal
        # guess = input("Enter the number corresponding to the emotion: ")
        guess = cv2.waitKey(0) & 0xFF
        guess = chr(guess)
        
        # Close the image window
        cv2.destroyAllWindows()
        
        # Check the answer
        try:
            guess = int(guess) - 1
            if choices[guess] == correct_emotion:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct emotion was {correct_emotion}.")
        except:
            print(f"Invalid input. The correct emotion was {correct_emotion}.")
    
    # Print the final score
    print(f"Quiz finished! Your score: {score}/{total}")

if __name__ == "__main__":
    quiz_user()
