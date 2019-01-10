# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

"""Collection of available datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


# Path to data dir
_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Required dataset entry keys
_IM_DIR = 'image_directory'
_ANN_FN = 'annotation_file'

# Optional dataset entry keys
_IM_PREFIX = 'image_prefix'
_DEVKIT_DIR = 'devkit_directory'
_RAW_DIR = 'raw_dir'
_ODOM_DIR = 'odom_directory'
_CAM_CAL = 'camera_calibration'

# Available datasets
_DATASETS = {
    
    #training sets
    'mobilityaids_RGB_train': {
        _IM_DIR:
            _DATA_DIR + '/mobility-aids/Images_RGB',
        _ANN_FN:
            _DATA_DIR + '/mobility-aids/annotations/train_RGB.json',
    },
    'mobilityaids_Depthjet_train': {
        _IM_DIR:
            _DATA_DIR + '/mobility-aids/Images_DepthJet',
        _ANN_FN:
            _DATA_DIR + '/mobility-aids/annotations/train_DepthJet.json',
    },
    
    #test set 1: detections
    'mobilityaids_RGB_test': {
        _IM_DIR:
            _DATA_DIR + '/mobility-aids/Images_RGB',
        _ANN_FN:
            _DATA_DIR + '/mobility-aids/annotations/test_RGB.json',
    },
    'mobilityaids_Depthjet_test': {
        _IM_DIR:
            _DATA_DIR + '/mobility-aids/Images_DepthJet',
        _ANN_FN:
            _DATA_DIR + '/mobility-aids/annotations/test_DepthJet.json',
    },
    
    #test set 2: with occlusions and odometry, tracking
    'mobilityaids_RGB_test2_seq1': {
        _IM_DIR:
            _DATA_DIR + '/mobility-aids/Images_RGB',
        _ANN_FN:
            _DATA_DIR + '/mobility-aids/annotations/test2_RGB_seq1.json',
        _ODOM_DIR:
            _DATA_DIR + '/mobility-aids/odometry_TestSet2',
        _CAM_CAL:
            _DATA_DIR + '/mobility-aids/camera_calibration.txt',
    }
}


def datasets():
    """Retrieve the list of available dataset names."""
    return _DATASETS.keys()


def contains(name):
    """Determine if the dataset is in the catalog."""
    return name in _DATASETS.keys()


def get_im_dir(name):
    """Retrieve the image directory for the dataset."""
    return _DATASETS[name][_IM_DIR]


def get_ann_fn(name):
    """Retrieve the annotation file for the dataset."""
    return _DATASETS[name][_ANN_FN]

def get_odom_dir(name):
    """Retrieve the odometry directory for the dataset. """
    return _DATASETS[name][_ODOM_DIR] if _ODOM_DIR in _DATASETS[name] else None

def get_im_prefix(name):
    """Retrieve the image prefix for the dataset."""
    return _DATASETS[name][_IM_PREFIX] if _IM_PREFIX in _DATASETS[name] else ''

def get_camera_calibration(name):
    if _CAM_CAL in _DATASETS[name]:
        
        cam_calib = {}
        with open(_DATASETS[name][_CAM_CAL]) as f:
            for line in f:
                splits = line.split('=')
                if len(splits) == 2:
                    cam_calib[splits[0]] = float(splits[1])
        return cam_calib
    
    else:
        return None
    
def get_devkit_dir(name):
    """Retrieve the devkit dir for the dataset."""
    return _DATASETS[name][_DEVKIT_DIR]


def get_raw_dir(name):
    """Retrieve the raw dir for the dataset."""
    return _DATASETS[name][_RAW_DIR]
