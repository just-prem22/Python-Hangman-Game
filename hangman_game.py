import random
lives=6
word_list=["winner","brothers","programming","coding","building","apple","banana","tiger","elephant","guitar",
"mountain","river","ocean","pencil","notebook",
"window","bottle","garden","butterfly","rainbow",
"castle","forest","desert","island","rocket",
"camera","pillow","blanket","cookie","chocolate",
"diamond","engine","flower","hammer","jungle",
"ladder","mirror","pocket","shadow","silver",
"spoon","sunshine","thunder","village","whisper"]
chosen_word=random.choice(word_list)
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)
game_over=False
correct_letters=[]
while not game_over:
    guess=input("Guess the letter...").lower()
    display=""
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
    print("Total lives left: ",lives)
    print(display)
    if lives==6:
        print('''
             
 +---+
 |   |
     |
     |
     |
     |

======
             ''' )
    elif lives==5:
        print('''
             
 +---+
 |   |
 o   |
     |
     |
     |

======
            '''  )
    elif lives==4:
        print('''
+---+
|   |
o   |
|   |
    |
    |

======     
              
              ''')
    elif lives==3:
        print('''
              
+---+
|   |
o   |
|\\  |
|   |
    |
 
======
              ''')
    elif lives==2:
        print('''
    +---+
    |   |
    o   |
   /|\\  |
    |   |
        |
    
  ======  
              ''')
    elif lives==1:
        print('''
    +---+
    |   |
    o   |
   /|\\  |
    |   |
     \\  |
    
 ======   
              ''')
    elif lives==0:
        print('''
    +---+
    |   |
    o   |
   /|\\  |
    |   |
   / \\  |
    
  ======
              
              ''')
        print("You Lose")
        print("The word was:", chosen_word)
        game_over=True
    if "_" not in display:
        game_over=True
        print("You Won")



