# This code takes care of daylight savings

import pytz
from datetime import datetime
shanghai_tz = pytz.timezone('America/Los_Angeles')
local_time = datetime.strptime('2023-03-13 00:00:00', '%Y-%m-%d %H:%M:%S')
local_time = shanghai_tz.localize(local_time)
local_time.astimezone(pytz.utc)
