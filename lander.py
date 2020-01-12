# Dean Blank; ID:db3226; Lecture Section: CS171-A; Lab section: CS-171-063

import sys

gravity = {'Moon': -1.622,  # dictionary for gravity values
           'Earth': -9.81,
           'Pluto': -0.42,
           'Neptune': -14.07,
           'Uranus': -10.67,
           'Saturn': -11.08,
           'Jupiter': -25.95,
           'Mars': -3.77,
           'Venus': -8.87,
           'Mercury': -3.59,
           'Sun': -274.13}

levels = {1: 'Moon',  # dictionary for levels
          2: 'Earth',
          3: 'Pluto',
          4: 'Neptune',
          5: 'Uranus',
          6: 'Saturn',
          7: 'Jupiter',
          8: 'Mars',
          9: 'Venus',
          10: 'Mercury',
          11: 'Sun'}

level_fuel = {'Moon': 150,  # dictionary for fuel values
              'Earth': 5000,
              'Pluto': 5000,
              'Neptune': 5000,
              'Uranus': 5000,
              'Saturn': 5000,
              'Jupiter': 5000,
              'Mars': 5000,
              'Venus': 5000,
              'Mercury': 5000,
              'Sun': 5000}

altitude = 50  # altitude in meters
velocity = 0  # initial velocity (m/s)
seconds = 1  # num of seconds passed
thruster = 0.10  # thruster acceleration (m/s^2)


def ask_fuel(current_fuel, fuel):  # Function to ask for fuel
    while True:
        try:
            fuel_use = int(input('Enter units of fuel to use: '))  # fuel input must be integer value
            if fuel_use >= 0:  # fuel input cannot be negative number
                if fuel_use <= current_fuel:  # fuel input must be less than or equal to available fuel
                    return fuel_use
                else:
                    print('Not enough fuel. Max fuel:', fuel)
            else:
                print('Cannot Use Negative Fuel')
        except ValueError:
            print('Please Enter Integer Value.')


def play_level(name, G, fuel):  # function to play game

    global level
    play_option = input('Do you want to play level {}? (yes/no) '.format(level))

    if play_option == 'yes':  # if input = 'yes' then play game
        global altitude
        global velocity
        global seconds
        global thruster
        seconds = 0
        print('\nEntering Level', level)  # print details of level
        print('Landing on the', name)
        print('Gravity is', G, 'm/s^2')
        print('Initial Altitude:', altitude, 'meters')
        print('Initial Velocity', velocity, 'm/s')
        print('Burning a unit of fuel causes 0.10 m/s slowdown.')
        print('Initial Fuel Level:', fuel, 'units')

        print('\nGO')

        while altitude > 0:  # while the altitude is above surface (>0) then continue to ask for fuel
            fuel_ask = ask_fuel(fuel, fuel)  # ask for fuel
            fuel = fuel - fuel_ask  # current fuel is the current fuel - fuel just asked for
            velocity = velocity + (G) + (thruster * fuel_ask)  # velocity = current velocity * gravity + (the units of fuel * thruster effect of .10)
            altitude = altitude + velocity  # current altitude = altitude + negative velocity
            seconds += 1  # increment seconds for fuel_ask
            if altitude < 0:  # if the altitude is negative than convert altitude to 0
                print('After {} seconds Altitude is {:.2f} meters, velocity is {:.2f}m/s.'.format(seconds, 0, velocity))
                print('Remaining Fuel: {} units.'.format(fuel))
            else:  # if altitude > 0 than print current altitude along with velocity and reaming fuel
                print('After {} seconds Altitude is {:.2f} meters, velocity is {:.2f}m/s.'.format(seconds, altitude, velocity))
                print('Remaining Fuel: {} units.'.format(fuel))
        if altitude <= 0:  # if altitude is less than or equal to zero and velocity is between -2m/s and 2m/s, then you landed successfully
            if -2 < velocity < 2:
                print('Landed Successfully!')
                return 'Landed Successfully!'
            else:
                print('Crashed!')  # if don't land between -2m/s and 2m/s then you crash

    elif play_option == 'no':  # if input is 'no' to play game, then exit program
        print('You made it past {} levels.\nThank you for Playing.'.format(level - 1))
        sys.exit()
    else:
        print('Invalid input')


print('Welcome to the Lunar Lander Game')  # intro

level = 1  # set initial level to zero
name = levels[level]  # pull name of level from levels dictionary
while True:  # run while loop to continue asking to play game
    if play_level(name, gravity[name], level_fuel[name]) == 'Landed Successfully!':  # continue on to next level
        level += 1  # increment to next level
        name = levels[level]  # next level's name
        altitude = 50  # restart altitude
        velocity = 0  # restart velocity
        play_level(name, gravity[name], level_fuel[name])  # play game again with new level parameters
    else:  # if you crash, then ask to play same level again
        altitude = 50  # restart altitude
        velocity = 0  # restart velocity
        if play_level(name, gravity[name], level_fuel[name]) == 'Landed Successfully!':  # continue on to next level
            level += 1  # increment to next level
            name = levels[level]  # next level name
            altitude = 50  # restart altitude
            velocity = 0  # restart velocity
