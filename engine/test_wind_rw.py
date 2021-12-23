import random
import numpy.random


def rough_binom(mean, spread):
	# mean should be an integer from -1000 to 1000
	# spread should be an integer from 0 to 1000
	assert not(mean < -1000 or mean > 1000 or spread < 0 or spread > 1000), "In rough_binom in env, got a mean of " + str(mean) + " and a spread of " + str(spread)

	binomial_n = (spread**2)*4
	binomial_rv = numpy.random.binomial(n = binomial_n, p = 0.5)
	print binomial_rv - binomial_n // 2 + mean
	return binomial_rv - binomial_n // 2 + mean



def run_sim(wind_avg, wind_volatility):
	wind_speed = wind_avg

	for i in range(100):
		wind_speed = wind_speed + rough_binom(wind_avg - wind_speed, wind_volatility)

		if wind_speed < 0:
			wind_speed = 0
		elif wind_speed > 999:
			wind_speed = 999

		print wind_speed,

		j = 0
		while j < wind_speed:
			if j == wind_avg:
				print '0',
			else:
				print '=',
			j += 10

		print


if __name__ == '__main__':

	run_sim(200, 200)