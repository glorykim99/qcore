import os
import json
import platform

COMMON = {"ROOT": "/nesi/project/nesi00213",
          "GMT_DATA": "/nesi/project/nesi00213/PlottingData",
          "VEL_MOD": "/nesi/project/nesi00213/VelocityModel",
          "wallclock": "/nesi/project/nesi00213/share/wallclock.sqlite"}

OPT_DIR = "/nesi/project/nesi00213/opt"

HOSTNAME = platform.node()[:-2]  # maui01 --> maui


def get_host_config(bin_name, version, write=False):
    """
    return config data dict based on hostname
    write config file if 'write' is True
    :param bin_name: eg. emod3d
    :param version: eg. 3.4.0-gcc
    :param write: write the config_file or not
    :return: config data dict
    """
    basename = os.path.join('machine_config', 'config_{}.json'.format(HOSTNAME))
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), basename)
    bin_path = os.path.join(OPT_DIR, HOSTNAME, bin_name, version, 'bin')
    config_data = COMMON.update(tools_dir= bin_path)

    if write:
        with open(config_file, 'w') as f:
            json.dump(config_data, f)

    return config_data

