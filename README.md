# call_watch
Monitor BrandMeister Network for a list of callsigns and give an OS notification.

20230803 - added call_watch_pm.py - for partial matches e.g. find out with TGs VK3's hang out on.

Usage:
python call_watch.py

Note:

        #Comment out the next line if you don't want to see all calls on the console
        
        print(f"{source_id} - {source_call} - {source_name} - {destination_id}")

Dependancies:

pip install "python-socketio[client]"

pip install notify-py
