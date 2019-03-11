from datetime import datetime
import pytz
import argparse
import os

# parse arguments
parser = argparse.ArgumentParser(description='Convert time from UNIX to UTC and CERN local time')
parser.add_argument('input', help='path to the input file')

args = parser.parse_args()

def convert(file, zone='UTC'):
	"""
	input:
		file: str, path to .h5 file
		zone: 'UTC' or 'CERN'
	output:
		return: datetime object, converted UNIX time
	"""

	# get time and convert to seconds
	unix_time = int(os.path.basename(file).split('.')[0].split('_')[0]) / 1e10

	if zone == 'UTC':
		time = datetime.utcfromtimestamp(unix_time).replace(tzinfo=pytz.utc)
	elif zone == 'CERN':
		time = datetime.fromtimestamp(unix_time, pytz.timezone('CET'))
	else:
		raise ValueError("zone argument can be 'UTC' or 'CERN'.")

	return time 

print('UTC time: ', convert(args.input, zone='UTC'))
print('CERN local time: ', convert(args.input, zone='CERN'))