import matplotlib.pyplot as plt
import random as rand

rand.seed()
y_offset = -5	# cm
num_sources = 100

x_range = 5
z_range = 5

counter = 1

with open('run_rand_sources.mac', 'w') as f:
    # start lines to set up simualation
    f.write('/run/initialize \n') 
    f.write('/control/verbose 0 \n')
    f.write('/run/verbose 0 \n')
    f.write('/event/verbose 0 \n')
    f.write('/tracking/verbose 0 \n')
    
    for i in range(0, num_sources):
    
        x_pos = rand.uniform(-x_range/2, x_range/2)
        z_pos = rand.uniform(-z_range/2, z_range/2)
        position_string = str(x_pos) + ' ' + str(y_offset) + ' ' + str(z_pos) + ' cm'
        
        x_dir = rand.uniform(-1, 1)
        y_dir = 1 #rand.random()
        z_dir = rand.uniform(-1, 1)
        direction_string = str(x_dir) + ' ' + str(y_dir) + ' ' + str(z_dir)
	
        f.write('\n# Particle source ' + str(counter) + '\n')
        f.write('/gps/particle e-\n')
        f.write('/gps/ene/min 100. keV \n')
        f.write('/gps/ene/max 10. MeV \n')
        f.write('/gps/position ' + position_string + '\n')
        f.write('/gps/direction ' + direction_string + '\n')
        f.write('/gps/pos/type Point \n')
        
        f.write('\n/run/beamOn 100 \n')

        counter = counter + 1

    
    f.close()

