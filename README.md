# Quantum Computing with Python
Exemplary Python3-Programs programmed for quantum computers.

## Docker
I strongly recommend you to use the Docker images/Docker-compose file. 
It avoids a lot of pain and headache :)


## Run
To run e.g. quantum_dice.py which uses the rigetti api, you can use the 
Docker-Compose-File like this: 
`docker-compose up --build rigetti_qapp rigetti_qvm`

If you want the qiskit-applications like _quantum_true_randomstring_generator.py_ 
you can use the following command: 
`docker-compose up --build qiskit_qapp` 