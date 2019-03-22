# Quantum Computing with Python
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://bitbucket.org/lbesson/ansi-colors) 
[![Generic badge](https://img.shields.io/badge/Docker-Compatible-blue.svg)](https://docker.com)
[![Github license](https://github.com/wsdt/QuantumComputing_Python.svg)](https://github.com/wsdt/QuantumComputing_Python/blob/master/LICENSE)

I basically just played around. 

## Programs
This repo contains following programs. 

### Quantum Dice
The source-folder contains a program for a quantum dice which has more sides than usual. 
This program uses the Rigetti Api/VM to execute the program.   

#### Run
To run e.g. quantum_dice.py which uses the rigetti api, you can use the 
Docker-Compose-File like this:
 
`docker-compose up --build rigetti_qapp rigetti_qvm`


### Quantum String Generator (Real Randomness)
This program generates a truly randomized string via QBits. You can easily change the length of the
string in the python-file. 

#### Run
If you want the qiskit-applications like _quantum_true_randomstring_generator.py_ 
you can use the following command: 

`docker-compose up --build qiskit_qapp` 

## Docker
I strongly recommend you to use the Docker images/Docker-compose file. 
It avoids a lot of pain and headache :)

I provided a Dockerfile for both programs as they use different dependencies, libraries and 
even APIs. For that reason I created a docker-compose file too, as e.g. the Rigetti VM depends
on another container. 
