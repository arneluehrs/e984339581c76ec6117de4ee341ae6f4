#! /usr/bin/python

"""

Settings files for TEITS demo project


"""

# Authentication settings. 
SECURE_MODE = False
USERNAME = "mapr"
PASSWORD = "mapr"
PEM_FILE = "/opt/mapr/conf/ssl_truststore.pem"


ACTIVE_DRONES = 1 # Number of pilot processes launched
NUMBER_OF_PROCESSORS = 3 # Each processor can analyse 2 to 3 images / second
DRONE_MODE = "live"    # "video" : plays video files, "live": send data from drones.
NO_FLIGHT = False  # when True, the flight commands aren't sent to the drones.
REMOTE_MODE = False # When True, drones pilots are supposed to be far from the main cluster. 
                   # Images are then sent using a direct connection to a DB buffer in the main cluster

# Video settings
STREAM_FPS = 10.0 # FPS sent by the pilot to the datastore
REPLAYER_FPS = 30.0 # FPS replayed from recording

# Drone settings
DIRECTIONAL_MODE = "LINEAR" # LINEAR (only x & y moves), OPTIMIZED (minimizes turns) or FORWARD (turns and forward) or DIRECT (no turn, just moveto the point)
FORWARD_COEF = 3 # Time taken to move 1m - used to wait between move instructions
ANGULAR_COEF = 8.0 # Time taken to rotate 360 deg - used to wait between move instructions

# Utilities

def get_cluster_name():
  with open('/opt/mapr/conf/mapr-clusters.conf', 'r') as f:
    first_line = f.readline()
    return first_line.split(' ')[0]

def get_cluster_ip():
  with open('/opt/mapr/conf/mapr-clusters.conf', 'r') as f:
    first_line = f.readline()
    return first_line.split(' ')[2].split(':')[0]


# Cluster information
CLUSTER_NAME = get_cluster_name()
CLUSTER_IP = get_cluster_ip()


# Project folders
PROJECT_FOLDER = "/teits/" # Project folder from the cluster root
ROOT_PATH = '/mapr/' + CLUSTER_NAME + PROJECT_FOLDER
DATA_FOLDER = ROOT_PATH + "data/" # Folder to store the data
RECORDING_FOLDER = DATA_FOLDER + "recording/" # Folder to store the recordings
LOG_FOLDER = ROOT_PATH + "logs/" # Folder to store the data


# Table names
ZONES_TABLE = DATA_FOLDER + 'zones_table' # Table for storing informations about predefined zones
CONTROLS_TABLE = DATA_FOLDER + 'controls_table' # Table for storing informations about interactive flight instructions
DRONEDATA_TABLE = DATA_FOLDER + 'dronedata_table'  # Table for storing informations about each drone
PROCESSORS_TABLE = DATA_FOLDER + 'processors_table'  # Table for storing info about processors
RECORDING_TABLE = DATA_FOLDER + 'recording_table' # Table to excahnge informations while recording


# Stream names
POSITIONS_STREAM = DATA_FOLDER + 'positions_stream'   # Stream for storign drone movements
PROCESSORS_STREAM = DATA_FOLDER + 'processors_stream'   # Stream to feed the processors
VIDEO_STREAM = DATA_FOLDER + 'video_stream' # Stream for the video frames metadata 
RECORDING_STREAM = DATA_FOLDER + 'recording_stream' # Stream for the video frames recording metadata 


# Generic Settings
ALLOWED_LAG = 2 # Allowed lag between real time events and processed events
OFFSET_RESET_MODE = 'latest' # latest for running the demo, earliest can be used for replaying existing streams
DISPLAY_STREAM_NAME = "processed" # source or processed- which default stream is displayed in the UI

# Drone control keys
controls = {
    'z' : "forward",
    's' : "backward",
    'q' : "left",
    'd' : "right",
    'ArrowUp' : "up",
    'ArrowDown' : "down",
    'ArrowRight' : "clockwise",
    'ArrowLeft' : "counter_clockwise",
    'f' : "flip",
    'Tab' : "takeoff",
    'Backspace' : "land" 
}



