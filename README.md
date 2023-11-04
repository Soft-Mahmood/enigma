# THE ENIGMA

![alt text](https://www.google.com/imgres?imgurl=https%3A%2F%2Fpagoda-tech.com%2Fsite%2F1864pago%2FEnigma-plugboard-encryption.jpg&tbnid=SA8tZ4OC9R4S9M&vet=12ahUKEwjVsd3wyqqCAxWcW6QEHVgIBIEQMygIegQIARB_..i&imgrefurl=https%3A%2F%2Fpagoda-tech.com%2Fpagoda_blog%2Fthe_enigma_machine_a_window_into_the_history_of_encryption.en&docid=BIgYz6Xn4q9aDM&w=921&h=627&q=enigma&ved=2ahUKEwjVsd3wyqqCAxWcW6QEHVgIBIEQMygIegQIARB_)

### Description

Josef and Tu's Shell is a simple encryption program that reciprocates the enigma encryption algorithm with in a console.

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

these rotate so that each time they have input, they are in a different configuration. After 26 rotations of the first rotor, the next rotates once. and then the next like that. 

The program will use three rotors at a time and display their letter ordering when the user is selecting the rotor order and starting positions.

At the end of the three rotors will be a reflector which shall sent the output into the rotors once again from the last one to the first one.

#### Plugboard.
The plugboard will connect two letters to each other an swap one for the other whenever it gets that letter as input. 
If the letter is not among those connected, it will leave it unchanged.
The plugboard will have a maximum of 13 connections and a minimum of 8 connections.

### Accepted values.
The program for the start will be working with capital letters from A-Z for both its input and output

### Inbuilt functions.
The program has support for the following built-in commands:

| Command             | Definition                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------- |
| encrypt             | Exit the shell, with an optional exit status, n.                                          |
| decrypt             | Print the environment.                                                                    |
| Rotor [n] [rotor]   | Set an environment variable and value. If the variable exists, the value will be updated. |
| plug [l] [l]        | Remove an environment variable.                                                           |
| order ...,...,..    | Change the directory.                                                                     |
| help [built-in]     | Read documentation for a built-in.                                                        |

The following built-in commands may be supported in future versions:

| Command | Definition                     |
| ------- | ------------------------------ |
| alias   | Set an Alias.                  |
| history | View the history of the shell. |

#### Outside Programs

Our shell can run outside programs by typing their absolute paths (/bin/ls) or the executable name (ls), IF their directory is included in the PATH.

### Examples

```sh
$ ls -l
total 8
drwxrwxr-x 1 vagrant vagrant Apr 2 13:23 directory_1
drwxrwxr-x 2 vagrant vagrant Apr 2 20:30 directory_2
```

```sh
$ /bin/pwd
/home/vagrant/shell
```

```sh
$ hello world
./hsh: 1: hello: not found
```

```sh
$ help env
env: env
	Print the environment.
```

### Included Files

- main.c - functions for calling the shell and initializing the shell struct
- shell.c - functions for running the basic shell logic
- shell_helpers.c - functions for helping the shell run
- split_string.c - functions for splitting string from the user
- string_helpers1.c - functions for manipulating strings
- string_helpers2.c - functions for manipulating strings
- built_ins.c - functions for built-ins
- built_in_helpers.c - functions for helping the built-in functions
- help.c - functions for the help built-in
- help2.c - functions for the help built-in
- cd.c - functions for the cd built-in
- cd2.c - functions for the cd built-in
- \_getenv.c - functions for getting elements from the environment
- env.c - functions for the env, setenv, and unsetenv built-ins
- llfuncs1.c - linked list functions
- llfuncs2.c - linked list functions
- expansions.c - functions for dealing with the $? and $\$ expansions
- check_path.c - functions for checking the path of an executable
- error_handler.c - functions for dealing with errors
- free.c - functions for freeing allocated memory
- holberton.h - header file

### Credits

All code written by [Tu Vo](https://github.com/tuvo1106) and [Josef Goodyear](https://github.com/JosefGoodyear).

