def water_left(astronanunts, water_left, days_left):
	daily_usage = astronanunts*11
	total_urage = daily_usage*days_left
	total_water_left = water_left - total_urage
	if total_water_left<0:
		raise RuntimeError(f"There is no enough water for {astronanunts} astronaunts after {days_left} days ")
	return f"Total Water left after {days_left} days is: {total_water_left} liters"

try:
	water_left(5, 100, 2)
except RuntimeError as err:
	alert_navigation_system(err)
	