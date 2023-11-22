import requests
import settings
from datetime import datetime
import os
import logging
import schedule
import time

#Logger Settings
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('backup_bot_logger')
logger.setLevel(logging.DEBUG)

def create_json_file():
	# Get_testnet_state
	response = requests.post(f'{settings.NODE_URL}/v1/query/state')
	logger.info(f'Creating a new backup from {settings.NODE_URL} testnet validator')

	# Check if folder for testnet state backup exists and create it if not
	folder_path = "./testnet-state-backup"
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
		logger.info(f"{folder_path} - folder created.")

	# Create file with <<YYYY-MM-DD_HH:MM>>_state.json nomenclature
	current_datetime = datetime.now()
	formatted_datetime = current_datetime.strftime('%Y-%m-%d_%H:%M')
	file = open(f'{folder_path}/{formatted_datetime}_state.json', 'w')
	file.write(response.text)
	file.close()

	# Return the file's name (which is the same as the file's relative path in this case)
	return file.name


if __name__ == '__main__':
	schedule.every(2).hours.do(create_json_file)
	while True:
		schedule.run_pending()
		time.sleep(1)