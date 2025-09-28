from bssid import *
from paths import *
from locations import *
from graph import *

bssid = get_bssid_windows()
if bssid:
    print("Connected BSSID:", bssid)
else:
    print("No BSSID found or not connected to Wi-Fi.")

dest = landmark_to_index["Food Court"]
src = bssid_to_index["34:AC:55:77:22:B1"]
_,path_indices = dijkstra_all_paths(graph,src,dest)
path_names = [vertices[i][0] for i in path_indices]  # ["Gym", "Library", "Food Court"]
path_codes = [vertices[i][1] for i in path_indices]  # ["88:FE:12:99:77:C3", ...]
