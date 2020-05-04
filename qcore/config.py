import json
import os
import platform

def determine_machine_config(hostname=platform.node()):
    """
    Manages multiple configurations for different machines.
    Determines the machine name eg: nodes ni0002 and maui01 belong to maui.
    :return: machine name, config file
    """
    if (hostname.startswith("ni") and len(hostname) == 8) or hostname.startswith(
        "maui"
    ):
        machine = "maui"
        basename = os.path.join("machine_config", "config_maui.json")

    elif (hostname.startswith("wb") and len(hostname) == 6) or hostname.startswith(
        "mahuika"
    ):
        machine = "mahuika"
        basename = os.path.join("machine_config", "config_mahuika.json")
    elif hostname.find('stampede') > -1:
        machine = "stampede2"
        basename = "config.json"
    elif (hostname.startswith("login") or hostname.startswith("node") or hostname.startswith('nurion')):
        machine = "nurion"
        basename = os.path.join("machine_config", "config_nurion.json")
    else:
        machine = "default"
        basename = "config.json"
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), basename)
    return machine, config_path


def get_machine_config(hostname=platform.node()):
    _, config_path = determine_machine_config(hostname=hostname)
    with open(config_path, "r") as machine_config_file:
        return json.load(machine_config_file)


host, config_file = determine_machine_config()


qconfig = get_machine_config()

