import random

class Environment:

	# all rates are out of 1000

	def __init__(self, sunrise_time, sunset_time, wind_avg, wind_volatility, geothermal_rate, dust_rate, snow_rate, snap_rate):
		self.world_hour = 0 # Hour starts at 0, increments by 1 cycles mod 24
		self.world_day = 0  # Day starts at 0, increments by 1 every 24 hours

		self.sun_up = False
		self.sunrise_time = sunrise_time # Sun rises at hour 6 by default
		self.sunset_time = sunset_time # Sun sets at hour 20 by default
						# Solar panels only active while the sun is up

		self.wind_speed = wind_avg # wind speed out of 1000
		self.wind_avg = wind_avg # average wind speed
		self.wind_volatility = wind_volatility # tendency for the wind to change speed, random walk favoring moving back to average
						# also out of 1000
						# Doesn't have to be units of speed, can jump multiple speeds up or down in an hour
						# Wind should be more favored to picking up in the 1 hour radius around sunrise and 1 hour radius around sunset to reflect uneven surface heating

		self.geothermal_rate = geothermal_rate # median productivity, out of 1000, of a geothermal plant and roughly binomially distributed

		self.water_level = 10 # water content of atmosphere, which counts double at night
		self.oxygen_level = 2

		self.dust_rate = dust_rate # rate of dust storms
		self.snow_rate = snow_rate # rate of snow storms (CO2 snow)
		self.snap_rate = snap_rate # rate of cold snaps
		self.active_storm = None # object for the storm currently happening, None if no storm

	def update_conditions(self):

		def rough_binom(mean, spread):
			# mean should be an integer from -1000 to 1000
			# spread should be an integer from 0 to 1000
			assert not(mean < -1000 or mean > 1000 or spread < 0 or spread > 1000), "In rough_binom in env, got a mean of " + str(mean) + " and a spread of " + str(spread)
			



		# Time ===========

		self.world_hour += 1

		if self.world_hour == 24:
			self.world_hour = 0
			self.world_day += 1



		# Sun ============

		if self.world_hour == self.sunrise_time:
			self.sun_up = True
		elif self.world_hour == self.sunset_time:
			self.sun_up = False




		# Wind ===========

		# if dust storm is incoming, wind volatility should favor increase, and if dust storm passes, wind should return to average



		# Storm ==========

		# if active storm is not None, check if we should end the current storm

		# if no storms are active, roll the dice on each storm starting

			# if we start a storm, create a storm object with its starting and ending time and set active storm object
			# Time from now to starting time should depend on the amount of forewarning we get - high for dust, medium for snow, low to none for snap
 





if __name__ == '__main__':

	summer_env = Environment(sunrise_time = 6,
							 sunset_time = 20,
							 wind_avg = 200,
							 wind_volatility = 100,
							 geothermal_rate = 200, # should be default
							 dust_rate = 100,
							 snow_rate = 30,
							 snap_rate = 10
	)

	print summer_env.snow_rate