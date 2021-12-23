import random


def rough_binom(mean, spread):
	# mean should be an integer from -1000 to 1000
	# spread should be an integer from 0 to 1000
	assert not(mean < -1000 or mean > 1000 or spread < 0 or spread > 1000), "In rough_binom in env, got a mean of " + str(mean) + " and a spread of " + str(spread)

			


def run_sim(wind_avg, wind_volatility):
	wind_speed = wind_avg

	for i in range(100):
		wind_speed = wind_speed + rough_binom(wind_avg - wind_speed, wind_volatility)
		print wind_speed


if __name__ == '__main__':

	run_sim(200, 100)