# THE ENIGMA PROGRAM
### Description

The enigma program is a simple encryption program that reciprocates the enigma encryption algorithm with in a console.

### Installation

Clone this repository into your working directory and run:
```
python3 enigma
```

### Usage
The program runs on a number of pre-set settings to encrpt the information provided. 

The settings include the following
1. Rotor Order.
2. Ring settings.
3. Rotor starting positions.
4. Plugboard configurations.

### How it works.

In this program, the user input or file is read letter by letter, each letter is sent to the plugboard where it could be swapped with another letter or not depending on the plugboard configuration, then the output of the plugboard goes to the rotors which each swap the letters depending on the rotor settings. the output is then sent to the plugboard again and swapped or not before being output.

The program will have options for encryption and decryption.

### Component description.
#### Rotors.

These rotate so that each time they have input, they are in a different configuration. After 26 rotations of the first rotor, the next rotates once. and then the next like that. 

The program will use three rotors at a time and display their letter ordering when the user is selecting the rotor order and starting positions.

At the end of the three rotors will be a reflector which shall send the output into the rotors once again from the last one to the first one.

#### Plugboard.
The plugboard will connect two letters to each other and swap one for the other whenever it gets that letter as input. 
If the letter is not among those connected, it will leave it unchanged.
The plugboard will have a maximum of 13 connections and a minimum of 8 connections.
These connections will be set during the initial plugboard configuration settings of the program.

### Accepted values.
The program for the start will be working with capital letters from A-Z for both its input and output

### Inbuilt functions.
The program has support for the following built-in commands:

| Command             | Definition                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------- |
| encrypt             | Encrypt the information using the settings added.                                         |
| decrypt             | Decrypt the information using the settings added.                                         |
| Rotor [n] [rotor]   | Add a rotor to the settings. n stands for rotot number and rotor stands for the rotor name|
| plug [l] [l]        | Connect the first letter to the second in the plugboard |
| start [rotor] [v]   | Set the rotor starting positions at  given value v                       |
| help [built-in]     | Read documentation for a built-in command                                                 |

### Future versions:

For future versions, all ascii characters will be included including numbers, A-Z, and a-z plus special characters.

##### This project will be as an exercise to utilise what i have learned in the ALX software engineering class.
