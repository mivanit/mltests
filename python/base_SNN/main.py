import learning
import brain
import sys
import gym 

#John Balis 2019
#for support email balisujohn@gmail.com



#parameterizations for various evaluation environments


def set_space_invaders_params():
	brain.Mutation_params.input_count = 128
	brain.Mutation_params.output_count = 3
	brain.Mutation_params.upper_input_bounds = [1] * 128
	brain.Mutation_params.lower_input_bounds = [-1] * 128

def set_pong_params():
	brain.Mutation_params.input_count = 128
	brain.Mutation_params.output_count = 3
	brain.Mutation_params.upper_input_bounds = [1] * 128
	brain.Mutation_params.lower_input_bounds = [-1] * 128


def set_cart_pole_params():
	brain.Mutation_params.input_count = 4
	brain.Mutation_params.output_count = 1
	brain.Mutation_params.upper_input_bounds = [.00000001] * 4
	brain.Mutation_params.lower_input_bounds = [-.000000001] * 4


def set_xor_params():
	brain.Mutation_params.input_count = 2
	brain.Mutation_params.output_count = 1
	brain.Mutation_params.upper_input_bounds = [1] * 2
	brain.Mutation_params.lower_input_bounds = [-1] * 2


def set_berzerk_params():
	brain.Mutation_params.input_count = 128
	brain.Mutation_params.output_count = 5
	brain.Mutation_params.upper_input_bounds = [1] * 128
	brain.Mutation_params.lower_input_bounds = [-1] * 128


def set_chopper_params():
	brain.Mutation_params.input_count = 128
	brain.Mutation_params.output_count = 5
	brain.Mutation_params.upper_input_bounds = [1] * 128
	brain.Mutation_params.lower_input_bounds = [-1] * 128

def set_stress_test_params():
	brain.Mutation_params.input_count = 100
	brain.Mutation_params.output_count = 100
	brain.Mutation_params.upper_input_bounds = [.000000001] * 100
	brain.Mutation_params.lower_input_bounds = [-.000000001] * 100


environments ={
'invaders':learning.evaluate_space_invaders_performance,
'cartpole':learning.evalute_pendulum_cart_performance,
'xor':learning.evaluate_xor_performance,
'berzerk':learning.evaluate_berzerk_performance,
'chopper':learning.evaluate_chopper_performance,
'pong':learning.evaluate_pong_performance
}

environment_settings= {
'invaders':set_space_invaders_params,
'cartpole':set_cart_pole_params,
'xor':set_xor_params,
'berzerk':set_berzerk_params,
'chopper':set_chopper_params,
'pong':set_pong_params

}



#core user interface dialouge

if len(sys.argv) == 3 and sys.argv[1] == 'stress':
	mutation_count = int(sys.argv[2])
	set_stress_test_params()
	b = brain.Brain(1)
	b.mutation_stress_test(mutation_count)

elif len(sys.argv) == 3 and sys.argv[1] == 'train':
	param_setup = environment_settings[sys.argv[2]]
	param_setup()
	result = learning.learn(environments[sys.argv[2]])

elif len(sys.argv) == 4 and sys.argv[1] == 'analyze':
	load_brain = brain.load_brain_from_file(sys.argv[3])
	param_setup = environment_settings[sys.argv[2]]
	param_setup()
	learning.visualize_performance(load_brain, environments[sys.argv[2]])

elif len(sys.argv) == 4 and sys.argv[1] == 'improve':
	load_brain = brain.load_brain_from_file(sys.argv[3])
	param_setup = environment_settings[sys.argv[2]]
	param_setup()
	result = learning.learn_from_existing(load_brain, environments[sys.argv[2]])
else:
	print('INVALID USAGE')
	
