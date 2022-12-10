# 
# MODIFY get_data() AS YOU LIKE.
# DO NOT SEND THIS FILE TO US

import random
random.seed(111)  #remove hash-sign to get randomization seed we will be using at evaluation
#                    (if you fix the seed you get always the same probabilty choice sequence)




def get_data():
	"""Get the initial state of the individuals & the environment"""
	# @TODO: Update this function just for your own testing. We will use our own get_data().
	       #[M, N,   D,   K, LAMBDA, MU,    universal_sta
	return [100, 100, 5, 70, 30, 0.5, [[(37, 8), 6, 'notmasked', 'notinfected'], [(41, 8), 0, 'masked', 'infected'], [(44, 8), 0, 'notmasked', 'notinfected'], [(47, 8), 0, 'masked', 'infected'], [(50, 8), 0, 'notmasked', 'notinfected'], [(53, 8), 0, 'masked', 'infected'], [(55, 8), 0, 'notmasked', 'notinfected'], [(37, 11), 6, 'notmasked', 'infected'], [(55, 11), 2, 'masked', 'infected'], [(37, 13), 6, 'notmasked', 'notinfected'], [(55, 13), 2, 'notmasked', 'notinfected'], [(37, 16), 6, 'notmasked', 'infected'], [(55, 16), 2, 'masked', 'infected'], [(37, 18), 6, 'notmasked', 'notinfected'], [(54, 18), 2, 'notmasked', 'notinfected'], [(54, 21), 2, 'masked', 'infected'], [(37, 22), 6, 'notmasked', 'infected'], [(37, 25), 6, 'notmasked', 'notinfected'], [(54, 25), 2, 'notmasked', 'notinfected'], [(54, 28), 2, 'masked', 'infected'], [(37, 29), 6, 'notmasked', 'infected'], [(37, 32), 6, 'notmasked', 'notinfected'], [(54, 32), 2, 'notmasked', 'notinfected'], [(37, 35), 6, 'notmasked', 'infected'], [(54, 35), 2, 'masked', 'infected'], [(37, 37), 6, 'notmasked', 'notinfected'], [(53, 37), 2, 'notmasked', 'notinfected'], [(37, 40), 6, 'notmasked', 'infected'], [(53, 40), 3, 'masked', 'infected'], [(37, 43), 6, 'notmasked', 'notinfected'], [(53, 43), 2, 'notmasked', 'notinfected']]]
