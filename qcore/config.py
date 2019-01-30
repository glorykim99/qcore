import os
import json
import platform

COMMON_CONFIG = {"ROOT": "/nesi/project/nesi00213",
          "GMT_DATA": "/nesi/project/nesi00213/PlottingData",
          "VEL_MOD": "/nesi/project/nesi00213/VelocityModel",
          "wallclock": "/nesi/project/nesi00213/share/wallclock.sqlite"}

OPT_DIR = "/nesi/project/nesi00213/opt"


def get_host_config(bin_name='emod3d', version='3.0.4-gcc', write=False):
    """
    return config data dict based on hostname
    write config file if 'write' is True
    :param bin_name: eg. emod3d
    :param version: eg. 3.4.0-gcc
    :param write: write the config_file or not
    :return: config data dict
    """
    config_data = COMMON_CONFIG
    hostname = platform.node()

    if hostname.startswith("ni") and len(hostname) == 8:  # maui
        basename = os.path.join('machine_config', 'config_maui.json')
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), basename)
        tools_dir = os.path.join(OPT_DIR, 'maui', bin_name, version, 'bin')
   
    elif hostname.startswith("mahuika") and len(hostname) == 6: # mahuika
        basename = os.path.join('machine_config', 'config_mahuika.json')
        tools_dir = os.path.join(OPT_DIR, 'mahuika', bin_name, version, 'bin')
   
    else:  # default
        basename = 'config.json'
        tools_dir = os.path.join(COMMON_CONFIG['ROOT'], 'tools')

    config_data['tools_dir'] = tools_dir

    if write:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), basename)
        with open(config_file, 'w') as f:
            json.dump(config_data, f)

    return config_data






