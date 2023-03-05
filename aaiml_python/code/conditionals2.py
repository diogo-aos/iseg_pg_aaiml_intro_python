traffic_light = "green"
action = None
if traffic_light == "green":
    action = "accelerate"
elif traffic_light == "yellow":
    action = "deaccelerate"
elif traffic_light == "red":
    action = "stop"
else:
    # unknown color
    action = "proceed_carefully"
