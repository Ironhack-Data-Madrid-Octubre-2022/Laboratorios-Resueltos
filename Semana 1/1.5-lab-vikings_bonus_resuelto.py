from vikingsClasses import War, Soldier, Viking, Saxon
import time
from random import randint, choice

if __name__=='__main__':
    
    # First create a war object
    war = War()
    
    # This lines are for give a narrative elements to the game
    
    print('''Comienza el día en una playa de Weist y el ejercito Sajón se prepara para defender su patria del ataque de los normandos''')
    
    print('                                                             **')
    print('                                                            ****')
    print('                                                           ********')
    print('                                                           *******')
    print('   + + + + + + + + + + + + + + + + + + + + + + + +  + +     *****')
    print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print(' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    
    # This loop initialize the army of saxons
    
    for i in range(5):
        
        sax = Saxon(randint(50,100),randint(10,25))
        
        war.addSaxon(sax)
    
    time.sleep(2)
    
    print('Comienza el desembarco del ejercito invasor')
    
    # This loop initialize the viking´s army
    
    for i in range (5):
        
        time.sleep(2)
        
        # create a viking random, with a random name from a list of names and random health between (50-100) and strength between (10-25)
        
        vik = Viking(choice(['Haaland','Ragknar', 'Tobic', 'Toruck',
                            'Börj', 'Milnber', 'Äknior', 'Laguerza',
                            'Sven', 'Aleksi', 'Tob', 'Garek', 'Loki',
                            'Thor', 'Molnir', 'Milena', 'Malena', 'Kubrick']),
             randint(50,100),randint(10,25))
        
        print(f'{vik.name} se unio a la batalla')
        
        # Add created viking to viking´s Army
        
        war.addViking(vik)
        
        # Excute battleCry when the last viking was added to the army
        
        if i == 4:
            print(vik.battleCry())
            print('\n')
     
    for i in range (25):
        
        # This loop contains the logic of the game
        
        time.sleep(2)
        
        # First attack the saxon army because the are waiting for the attack from the vikings so i think the are in an advantage position
        
        print(war.saxonAttack())
        
        # after attack  the game will evaluate the state of the war
        if war.saxonArmy == [] or war.vikingArmy == []:
            print(war.showStatus())
            
            if war.saxonArmy == []:
                print(war.vikingArmy[0].battleCry())
                for e in war.vikingArmy:
                    print(f'{e.name} sobrevivió a la batalla le quedan {e.health} puntos de vida')
                break
            else:
                
                if len(war.saxonArmy) > 1: print(f'{len(war.saxonArmy)} saxons survived to the battle ')
                else:
                    print(f'{len(war.saxonArmy)} saxon survived to the battle')
                break
        
        # After the saxon attack execute the viking attack
        print(war.vikingAttack())
        print('\n')
        
        # the same after the saxon attack evaluate the state of the war
        
        if war.saxonArmy == [] or war.vikingArmy == []:
            print(war.showStatus())
            
            if war.saxonArmy == []:
                print(war.vikingArmy[0].battleCry())
                for e in war.vikingArmy:
                    print(f'{e.name} sobrevivió a la batalla le quedan {e.health} puntos de vida')
                break
            else:
                
                if len(war.saxonArmy) > 1: print(f'{len(war.saxonArmy)} saxons survived to the battle ')
                else:
                    print(f'{len(war.saxonArmy)} saxon survived to the battle')
                break
        
        if i == 24:
            print(war.showStatus())
