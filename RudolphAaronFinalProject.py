""" 
Author: Aaron Rudolph
Date Written: 02/27/2025 - 03/05/2025
Assignment: Final project
Desc: Short Pixar Personality test

"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
class PersonalityTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixar Personality Test")
        #Set window size
        self.root.geometry("800x600")
       
        #Set background color
        self.root.configure(bg = "lightblue")
        self.questions = ["You like making people laugh", "You find yourself forgetting a lot", 
                          "You are into fashion", "You are a leader", "You like discovery", 
                          "You take your job seriously", "You work very hard", "You are speed", "You like meeting new people",
                          "You like helping extraordinary people", "You are confident", "You value team work",
                          "You love to cook", "You value community", "You are stubborn", 
                          ]  #questions
        self.answers = []
        self.question_index = 0
        self.photo = None
        
        self.characters = {
            "Mike Wazowski": 0,
            "Dory": 0,
            "Edna Mode": 0,
            "Woody": 0,
            "Carl Fredricksen": 0,
            "Sully": 0,
            "Buzz Lightyear": 0,
            "Lightning McQueen": 0,
            "Remy": 0
        }
        
        self.character_traits = {
            "Mike Wazowski": "Funny, determined, loyal",
            "Dory": "Forgetful, friendly, adventurous",
            "Edna Mode": "Fashionable, confident, brilliant",
            "Woody": "Leader, brave, loyal",
            "Carl Fredricksen": "Adventurous, determined, caring",
            "Sully": "Strong, kind, protective",
            "Buzz Lightyear": "Brave, hardworking, loyal",
            "Lightning McQueen": "Fast, determined, competitive",
            "Remy": "Creative, passionate, hardworking"
        }
        
        self.character_images = {
            "Mike Wazowski": "C:\\Users\\rudol\\.vscode\\Mikey.jpg",
            "Dory": "C:\\Users\\rudol\\.vscode\\Doryy.jpg",
            "Edna Mode": "C:\\Users\\rudol\\.vscode\\Ednaa.jpg",
            "Woody": "C:\\Users\\rudol\\.vscode\\Woodyy.jpg",
            "Carl Fredricksen": "C:\\Users\\rudol\\.vscode\\Carlll.jpg",
            "Sully": "C:\\Users\\rudol\\.vscode\\Sullyy.jpg",
            "Buzz Lightyear": "C:\\Users\\rudol\\.vscode\\Buzz.jpg",
            "Lightning McQueen": "C:\\Users\\rudol\\.vscode\\lightninggg.jpg",
            "Remy": "C:\\Users\\rudol\\.vscode\\Remyy boi.jpg"
        }
        
        
        self.create_widgets()
        
    def create_widgets(self):
        """This method sets up the welcome frame and populates it with a welcome message,
    an image, a name entry field, and a button to start the test. The image is 
    loaded, resized, and displayed within the frame. """
        self.welcome_frame = tk.Frame(self.root, bg="lightblue")
        self.welcome_frame.pack(fill="both", expand=True)
        # Load and display the Pixar image
        pixar_image_path = "C:\\Users\\rudol\\.vscode\\Pixarr.jpg"  # Replace with the path to your Pixar image
        pixar_image = Image.open(pixar_image_path)
        pixar_image = pixar_image.resize((300, 150), Image.Resampling.LANCZOS)  # Resize the image if needed
        pixar_photo = ImageTk.PhotoImage(pixar_image)
        
        self.pixar_image_label = tk.Label(self.welcome_frame, image=pixar_photo, bg="lightblue")
        self.pixar_image_label.image = pixar_photo  # Keep a reference!
        self.pixar_image_label.pack(pady=20)
        
        self.welcome_label = tk.Label(self.welcome_frame, text="Welcome to the Pixar Personality Test",
                                      bg="lightblue", font=("Arial", 24))
        self.welcome_label.pack(pady=20)
        
        self.name_label = tk.Label(self.welcome_frame, text="Enter your name:",
                                   bg="lightblue", font=("Arial", 16))
        self.name_label.pack(pady=10)
        
        self.name_entry = tk.Entry(self.welcome_frame, font=("Arial", 16))
        self.name_entry.pack(pady=10)
        
        self.start_button = tk.Button(self.welcome_frame, text="Start Test", command=self.start_test, font=("Arial", 16))
        self.start_button.pack(pady=20)
        
        
    #create scale
    def start_test(self):
        """ This method retrieves the user's name from the name entry widget, destroys the welcome frame,
    and sets up the question frame along with the progress bar, question label, radio buttons
    for responses, and navigation buttons. """
        self.user_name = self.name_entry.get()
        self.welcome_frame.destroy()
        self.question_frame = tk.Frame(self.root, bg="lightblue")
        
        self.question_frame.pack(fill="both", expand=True)
        
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)
        self.progress["maximum"] = len(self.questions)
        
        self.question_label = tk.Label(self.root, text=self.questions[self.question_index],
                                       wraplength=400)
        self.question_label.pack(pady=20)
        
        
        self.var = tk.IntVar()
        
        #Buttons
        self.radio1 = tk.Radiobutton(self.root, text="Strongly Agree", variable=self.var, value=5)
        self.radio1.pack(anchor=tk.W)

        self.radio2 = tk.Radiobutton(self.root, text="Agree", variable=self.var, value=4)
        self.radio2.pack(anchor=tk.W)

        self.radio3 = tk.Radiobutton(self.root, text="Neutral", variable=self.var, value=3)
        self.radio3.pack(anchor=tk.W)

        self.radio4 = tk.Radiobutton(self.root, text="Disagree", variable=self.var, value=2)
        self.radio4.pack(anchor=tk.W)

        self.radio5 = tk.Radiobutton(self.root, text="Strongly Disagree", variable=self.var, value=1)
        self.radio5.pack(anchor=tk.W)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)
        
        self.back_button = tk.Button(self.root, text="Back", command=self.previous_question)
        self.back_button.pack(pady=20)
        
    def previous_question(self):
        """  Navigate to the previous question in the Pixar Personality Test.
    This method decreases the question index by one if it is greater than zero,
    effectively moving to the previous question. It then updates the question
    and the UI accordingly """
        if self.question_index > 0:
            self.question_index -= 1
            self.update_question()
            
    def update_question(self):
        """ Update the current question and progress in the Pixar Personality Test.
    This method updates the response variable, question label, and progress bar
    based on the current question index."""
        self.var.set(self.answers[self.question_index] if self.question_index < len(self.answers) else 0)
        self.question_label.config(text=self.questions[self.question_index])
        self.progress["value"] = self.question_index + 1
    
    def next_question(self):
        """ Update the current question and progress in the Pixar Personality Test.
    This method updates the response variable, question label, and progress bar
    based on the current question index."""
        response = self.var.get()
        self.answers.append(response)
        # Update character points based on the response
        if self.question_index == 0:  # "You like making people laugh"
            if response == 1: # Strongly disagree
                self.characters["Edna Mode"] += response
                self.characters["Carl Fredricksen"] += response
            elif response == 2: # Disagree
                self.characters["Lightning McQueen"] += response
                self.characters["Sully"] += response
            elif response == 3: # Neutral
                self.characters["Remy"] += response
                self.characters["Buzz Lightyear"] += response
            elif response == 4: # Agree
                self.characters["Woody"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Mike Wazowski"] += response
                self.characters["Dory"] += response
                
        elif self.question_index == 1:  # "You find yourself forgetting a lot"
            if response == 1:  # Strongly disagree
                self.characters["Woody"] += response
                self.characters["Sully"] += response
                self.characters["Remy"] += response * 2
            elif response == 2:  # Disagree
                self.characters["Buzz Lightyear"] += response
                self.characters["Mike Wazowski"] += response
            elif response == 3: # Neutral
                self.characters["Edna Mode"] += response
                self.characters["Carl Fredricksen"] += response
            elif response == 4: # Agree
                self.characters["Lightning McQueen"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Dory"] += response * 2
                
        elif self.question_index == 2:  # "You are into fashion"
            if response == 1: # Strongly Disagree
                self.characters["Buzz Lightyear"] += response * 2
            elif response == 2: # Disagree
                self.characters["Woody"] += response
            elif response == 3: # Neutral
                self.characters["Dory"] += response
                self.characters["Sully"] += response
            elif response == 4: # Agree
                self.characters["Mike Wazowski"] += response
                self.characters["Remy"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Edna Mode"] += response * 2
                self.characters["Lightning McQueen"] += response * 2
            
        elif self.question_index == 3:  # "You are a leader"
            if response == 1 or response == 2: # Disagree or Strongly Disagree
                self.characters["Mike Wazowski"] += response  * 2
                self.characters["Dory"] += response * 2
                self.characters["Edna Mode"] += response * 2
            elif response == 3: # Neutral
                self.characters["Carl Fredricksen"] += response
            elif response == 4: # Agree
                self.characters["Lightning McQueen"] += response
                self.characters["Remy"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Woody"] += response * 2
                self.characters["Buzz Lightyear"] += response * 2
                
        elif self.question_index == 4:  # "You like discovery"
            if response == 1: # Strongly Disagree
                self.characters["Woody"] += response * 2
            elif response == 2: # Disagree
                self.characters["Sully"] += response
                self.characters["Lightning McQueen"] += response
            elif response == 3: # Neutral
                self.characters["Mike Wazowski"] += response
            elif response == 4: # Agree
                self.characters["Dory"] += response
                self.characters["Carl Fredricksen"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Edna Mode"] += response * 2
                self.characters["Remy"] += response * 2
            
        elif self.question_index == 5:  # "You take your job seriously"
            if response == 1: # Strongly Disagree
                self.characters["Dory"] += response * 2
            elif response == 2: # Disagree
                self.characters["Sully"] += response
            elif response == 3: # Neutral
                self.characters["Carl Fredricksen"] += response
                self.characters["Remy"] += response
            elif response == 4: # Agree
                self.characters["Lightning McQueen"] += response * 2
            elif response == 5:  # Strongly Agree
                self.characters["Mike Wazowski"] += response
                self.characters["Edna Mode"] += response 
                self.characters["Woody"] += response
            
        elif self.question_index == 6:  # "You work very hard"
            if response == 1: # Strongly Disagree
                self.characters["Dory"] += response * 2
            elif response == 2: # Disagree
                self.characters["Remy"] += response
                self.characters["Woody"] += response
            elif response == 3: # Neutral
                self.characters["Carl Fredricksen"] += response * 2
            elif response == 4: # Agree
                self.characters["Lightning McQueen"] += response * 2
                self.characters["Sully"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Buzz Lightyear"] += response * 2
                self.characters["Edna Mode"] += response
                self.characters["Mike Wazowski"] += response
            
        elif self.question_index == 7:  # "You are speed"
            if response == 1: # Strongly Disagree
                self.characters["Woody"] += response
                self.characters["Buzz Lightyear"] += response * 2
            elif response == 2: # Disagree
                self.characters["Carl Fredricksen"] += response
                self.characters["Edna Mode"] += response
            elif response == 3: # Neutral
                self.characters["Dory"] += response
                self.characters["Remy"] += response
            elif response == 4: # Agree
                self.characters["Mike Wazowski"] += response
                self.characters["Sully"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Lightning McQueen"] += response * 2
                
        elif self.question_index == 8:  # "You like meeting new people"
            if response == 1: # Strongly Disagree
                self.characters["Woody"] += response
                self.characters["Edna Mode"] += response
            elif response == 2: # Disagree
                self.characters["Carl Fredricksen"] += response
            elif response == 3: # Neutral
                self.characters["Dory"] += response
            elif response == 4: # Agree
                self.characters["Lightning McQueen"] += response
                self.characters["Mike Wazowski"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Remy"] += response
                self.characters["Buzz Lightyear"] += response
                self.characters["Sully"] += response
            
        elif self.question_index == 9:  # "You like helping extraordinary people"
            if response == 1 or response == 2: # Disagree or Strongly Disagree
                self.characters["Buzz Lightyear"] += response * 2
                self.characters["Sully"] += response
                self.characters["Remy"] += response
            elif response == 3: # Neutral
                self.characters["Lightning McQueen"] += response
                self.characters["Woody"] += response
            elif response == 4: # Agree
                self.characters["Mike Wazowski"] += response
                self.characters["Carl Fredricksen"] += response
            elif response == 5:  # Strongly Agree     
                self.characters["Edna Mode"] += response * 2
                self.characters["Dory"] += response
                
        elif self.question_index == 10:  # "You are confident"
            if response == 1:  # Strongly disagree
                self.characters["Carl Fredricksen"] += response * 2
            elif response == 2:  # Disagree
                self.characters["Sully"] += response
            elif response == 3: # Neutral
                self.characters["Mike Wazowski"] += response
            elif response == 4: # Agree
                self.characters["Remy"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Lightning McQueen"] += response
                self.characters["Buzz Lightyear"] += response
                self.characters["Edna Mode"] += response
                
        elif self.question_index == 11:  # "You value team work"
            if response == 1: # Strongly disagree
                self.characters["Lightning McQueen"] += response
                self.characters["Edna Mode"] += response
            elif response == 2: # Disagree
                self.characters["Sully"] += response
            elif response == 3: # Neutral
                self.characters["Mike Wazowski"] += response
                self.characters["Buzz Lightyear"] += response * 2
            elif response == 4: # Agree
                self.characters["Carl Fredricksen"] += response
                self.characters["Dory"] += response
            elif response == 5:  # Strongly Agree  
                self.characters["Remy"] += response
                self.characters["Woody"] += response
                
        elif self.question_index == 12:  # "You love to cook"
            if response == 1:  # Strongly disagree
                self.characters["Edna Mode"] += response
            elif response == 2:  # Disagree
                self.characters["Sully"] += response
                self.characters["Carl Fredricksen"] += response
            elif response == 3: # Neutral
                self.characters["Woody"] += response
                self.characters["Dory"] += response
                self.characters["Buzz Lightyear"] += response
            elif response == 4: # Agree
                self.characters["Lightning McQueen"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Remy"] += response * 2
                self.characters["Mike Wazowski"] += response
                
        elif self.question_index == 13:  # "You value community"
            if response == 1:  # Strongly disagree
                self.characters["Edna Mode"] += response * 2
            elif response == 2:  # Disagree
                self.characters["Sully"] += response
                self.characters["Carl Fredricksen"] += response
            elif response == 3: # Neutral
                self.characters["Dory"] += response
                self.characters["Buzz Lightyear"] += response
            elif response == 4: # Agree
                self.characters["Mike Wazowski"] += response
                self.characters["Woody"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Lightning McQueen"] += response
                self.characters["Remy"] += response
                
        elif self.question_index == 14:  # "You are stubborn"
            if response == 1: # Strongly Disagree
                self.characters["Edna Mode"] += response
                self.characters["Woody"] += response
            elif response == 2: # Disagree
                self.characters["Mike Wazowski"] += response
                self.characters["Sully"] += response * 2
            elif response == 3: # Neutral
                self.characters["Dory"] += response
            elif response == 4: # Agree
                self.characters["Remy"] += response
                self.characters["Buzz Lightyear"] += response
            elif response == 5:  # Strongly Agree
                self.characters["Carl Fredricksen"] += response * 2
                self.characters["Lightning McQueen"] += response
            
        self.question_index += 1
        self.progress["value"] = self.question_index
        
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index])
            self.var.set(0)  # Reset the variable
        else:
            self.show_results()
    
    def show_results(self): 
        """ Display the results of the Pixar Personality Test.
    This method destroys the question-related widgets and frames, calculates the character
    with the highest score, and displays the results including the character's image and traits.
     """
        self.question_frame.destroy() 
        self.progress.destroy()
        self.next_button.destroy()
        self.back_button.destroy() 
        self.question_label.destroy()
        self.radio1.destroy()
        self.radio2.destroy()
        self.radio3.destroy()
        self.radio4.destroy()
        self.radio5.destroy()

        #show results
        self.result_frame = tk.Frame(self.root, bg="lightblue") 
        self.result_frame.pack(fill="both", expand=True) 
    
        #Determine the character with the highest score 
        highest_score = max(self.characters.values()) 
        chosen_character = [character for character, score in self.characters.items() 
                        if score == highest_score][0] 
        result_text = f"Thank you, {self.user_name}, for completing the test!\nYour Pixar character is: {chosen_character}" 
        self.result_label = tk.Label(self.result_frame, text=result_text, wraplength=600, bg="lightblue", font=("Arial", 16)) 
        self.result_label.pack(pady=20) 
    
    # Display character image 
        image_path = self.character_images[chosen_character] 
        image = Image.open(image_path) 
        image = image.resize((200, 200), Image.Resampling.LANCZOS) 
        self.photo = ImageTk.PhotoImage(image) 
        self.image_label = tk.Label(self.result_frame, image=self.photo, bg="lightblue")  
        self.image_label.pack(pady=10) 
    
    # Display character traits 
        traits_text = f"Character Traits: {self.character_traits[chosen_character]}" 
        self.traits_label = tk.Label(self.result_frame, text=traits_text, wraplength=800, bg="lightblue", font=("Arial", 16)) 
        self.traits_label.pack(pady=10)
         
        
def main():
    root = tk.Tk()
    app = PersonalityTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
