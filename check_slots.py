import requests
import time
import subprocess

# Function to send a macOS notification
def send_notification(title, message):
    subprocess.run([
        "osascript", "-e", f'display notification "{message}" with title "{title}"'
    ])

# Function to check slot availability
def check_slots(url):
    response = requests.get(url)
    data = response.json()
    
    if data['availableSlots']:
        # Extract the date from availableSlots
        date = data['availableSlots'][0]['startTimestamp'].split('T')[0]
        send_notification("Slot Available", date)
        subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])

# Main loop to continuously check every 2 seconds
def main():
    url = "http://ttp.cbp.dhs.gov/schedulerapi/slot-availability?locationId=5020"
    
    while True:
        check_slots(url)
        time.sleep(2)

if __name__ == "__main__":
    main()

