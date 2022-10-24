# In rock this rock paper scissors game, youll give your choice to compete against the computers choice. Either of you have an equal chance of winning. Good luck!!
import random

# let the computer choose between the three options
choices = ['r', 'p', 's']
rps = random.choice(choices)

# both users and computer start with 10 points
user_stars = 10
computer_stars = 10

guess_list = ['r', 'p', 's'] # to ensure user's select one of r, p and c
while user_stars > 0 and computer_stars > 0:
    user_guess = input('\nenter your guess: r, p OR s (lowecase) ?: (press q to quit game) Both of us are at 10 points!!\n')

    if user_guess == 'q': 
        print('Bye bye!! Quitters never win though \n') #quits the game and breaks out!
        break

    elif user_guess in guess_list:
        if user_guess == rps: # there might be a tie which doesn't count

            print(f'We tied!! We both chose {rps}')
            rps = random.choice(choices)
        
        #checks whether user is the winner or else computer and assigns the necessary scores and picks a new guess
        elif (user_guess == 'r' and rps == 's') or (user_guess == 'p' and rps == 'r') or (user_guess == 's' and rps == 'p'):
            user_stars += 5
            computer_stars -= 5
            print(f'Genius! Your points increased to {user_stars} and my points decreased to {computer_stars} bcoz I chose {rps}')
            rps = random.choice(choices)

        #where user gets beaten by computer
        else:
            user_stars -= 5
            computer_stars += 5
            if user_stars > 5:
                print(f'Nop! {user_guess} cannot beat {rps}! {user_stars} stars left till you\'re out! I am at {computer_stars}\n')
                rps = random.choice(choices)

            # Just to warn the user of their last chance
            elif user_stars == 5:
                print(f'Danger, one more fail and youre out. As for me, I have {computer_stars} points now!')
                rps = random.choice(choices)

            else:
                print(f'you have now {user_stars} lives left and I now have {computer_stars} left :)')
                rps = random.choice(choices)
            
    else: # choice not r, p or s
        print('try again, make a correct selection this time')


# congratulating the winner, they deserved it!
if computer_stars == 0:
    print('---------------')
    print(f'\nYou WON with {user_stars} stars! Mehn youre tough')
    print('---------------')
elif user_stars == 0:
    print('---------------')
    print(f'sorry, you lost and I won with {computer_stars} stars')
    print('---------------')