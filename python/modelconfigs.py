#!/usr/bin/python3
from typing import Dict, Any

ModelConfig = Dict[str,Any]

# version = 0 #V1 features, with old head architecture using crelus (no longer supported)
# version = 1 #V1 features, with new head architecture, no crelus
# version = 2 #V2 features, no internal architecture change.
# version = 3 #V3 features, selfplay-planned features with lots of aux targets
# version = 4 #V3 features, but supporting belief stdev and dynamic scorevalue
# version = 5 #V4 features, slightly different pass-alive stones feature
# version = 6 #V5 features, most higher-level go features removed
# version = 7 #V6 features, more rules support
# version = 8 #V7 features, asym, lead, variance time
# version = 9 #V7 features, shortterm value error prediction, inference actually uses variance time, unsupported now
# version = 10 #V7 features, shortterm value error prediction done properly

def get_version(config: ModelConfig):
  return config["version"]

def get_num_bin_input_features(config: ModelConfig):
  version = get_version(config)
  if version == 10:
    return 22
  else:
    assert(False)

def get_num_global_input_features(config: ModelConfig):
  version = get_version(config)
  if version == 10:
    return 19
  else:
    assert(False)

b2c16 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":16,
  "mid_num_channels":16,
  "regular_num_channels":8,
  "dilated_num_channels":8,
  "gpool_num_channels":8,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","gpool"],
  ],
  "p1_num_channels":8,
  "g1_num_channels":8,
  "v1_num_channels":8,
  "sbv2_num_channels":12,
  "num_scorebeliefs":2,
  "v2_size":12
}

b4c32 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":32,
  "mid_num_channels":32,
  "regular_num_channels":16,
  "dilated_num_channels":16,
  "gpool_num_channels":16,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","gpool"],
    ["rconv4","regular"],
  ],
  "p1_num_channels":12,
  "g1_num_channels":12,
  "v1_num_channels":12,
  "sbv2_num_channels":24,
  "num_scorebeliefs":4,
  "v2_size":24
}

b6c96 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":96,
  "mid_num_channels":96,
  "regular_num_channels":64,
  "dilated_num_channels":32,
  "gpool_num_channels":32,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","gpool"],
    ["rconv4","regular"],
    ["rconv5","gpool"],
    ["rconv6","regular"]
  ],
  "p1_num_channels":32,
  "g1_num_channels":32,
  "v1_num_channels":32,
  "sbv2_num_channels":48,
  "num_scorebeliefs":4,
  "v2_size":64
}

b10c128 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":128,
  "mid_num_channels":128,
  "regular_num_channels":96,
  "dilated_num_channels":32,
  "gpool_num_channels":32,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","gpool"],
    ["rconv6","regular"],
    ["rconv7","regular"],
    ["rconv8","gpool"],
    ["rconv9","regular"],
    ["rconv10","regular"]
  ],
  "p1_num_channels":32,
  "g1_num_channels":32,
  "v1_num_channels":32,
  "sbv2_num_channels":64,
  "num_scorebeliefs":6,
  "v2_size":80
}

b15c192 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":192,
  "mid_num_channels":192,
  "regular_num_channels":128,
  "dilated_num_channels":64,
  "gpool_num_channels":64,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","regular"],
    ["rconv7","gpool"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","regular"],
    ["rconv12","gpool"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"]
  ],
  "p1_num_channels":32,
  "g1_num_channels":32,
  "v1_num_channels":32,
  "sbv2_num_channels":80,
  "num_scorebeliefs":8,
  "v2_size":96
}

b20c256 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":256,
  "mid_num_channels":256,
  "regular_num_channels":192,
  "dilated_num_channels":64,
  "gpool_num_channels":64,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","regular"],
    ["rconv7","gpool"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","regular"],
    ["rconv12","gpool"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","regular"],
    ["rconv17","gpool"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"]
  ],
  "p1_num_channels":48,
  "g1_num_channels":48,
  "v1_num_channels":48,
  "sbv2_num_channels":96,
  "num_scorebeliefs":8,
  "v2_size":112
}

b30c320 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":320,
  "mid_num_channels":320,
  "regular_num_channels":224,
  "dilated_num_channels":96,
  "gpool_num_channels":96,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","gpool"],
    ["rconv7","regular"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","gpool"],
    ["rconv12","regular"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","gpool"],
    ["rconv17","regular"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"],
    ["rconv21","gpool"],
    ["rconv22","regular"],
    ["rconv23","regular"],
    ["rconv24","regular"],
    ["rconv25","regular"],
    ["rconv26","gpool"],
    ["rconv27","regular"],
    ["rconv28","regular"],
    ["rconv29","regular"],
    ["rconv30","regular"]
  ],
  "p1_num_channels":48,
  "g1_num_channels":48,
  "v1_num_channels":48,
  "sbv2_num_channels":112,
  "num_scorebeliefs":8,
  "v2_size":128
}

b40c256 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":256,
  "mid_num_channels":256,
  "regular_num_channels":192,
  "dilated_num_channels":64,
  "gpool_num_channels":64,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","gpool"],
    ["rconv7","regular"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","gpool"],
    ["rconv12","regular"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","gpool"],
    ["rconv17","regular"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"],
    ["rconv21","gpool"],
    ["rconv22","regular"],
    ["rconv23","regular"],
    ["rconv24","regular"],
    ["rconv25","regular"],
    ["rconv26","gpool"],
    ["rconv27","regular"],
    ["rconv28","regular"],
    ["rconv29","regular"],
    ["rconv30","regular"],
    ["rconv31","gpool"],
    ["rconv32","regular"],
    ["rconv33","regular"],
    ["rconv34","regular"],
    ["rconv35","regular"],
    ["rconv36","gpool"],
    ["rconv37","regular"],
    ["rconv38","regular"],
    ["rconv39","regular"],
    ["rconv40","regular"]
  ],
  "p1_num_channels":48,
  "g1_num_channels":48,
  "v1_num_channels":48,
  "sbv2_num_channels":112,
  "num_scorebeliefs":8,
  "v2_size":128
}

b40c384 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":384,
  "mid_num_channels":384,
  "regular_num_channels":256,
  "dilated_num_channels":128,
  "gpool_num_channels":128,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","gpool"],
    ["rconv7","regular"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","gpool"],
    ["rconv12","regular"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","gpool"],
    ["rconv17","regular"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"],
    ["rconv21","gpool"],
    ["rconv22","regular"],
    ["rconv23","regular"],
    ["rconv24","regular"],
    ["rconv25","regular"],
    ["rconv26","gpool"],
    ["rconv27","regular"],
    ["rconv28","regular"],
    ["rconv29","regular"],
    ["rconv30","regular"],
    ["rconv31","gpool"],
    ["rconv32","regular"],
    ["rconv33","regular"],
    ["rconv34","regular"],
    ["rconv35","regular"],
    ["rconv36","gpool"],
    ["rconv37","regular"],
    ["rconv38","regular"],
    ["rconv39","regular"],
    ["rconv40","regular"]
  ],
  "p1_num_channels":64,
  "g1_num_channels":64,
  "v1_num_channels":64,
  "sbv2_num_channels":128,
  "num_scorebeliefs":8,
  "v2_size":144
}


b60c320 = {
  "version":10,
  "support_japanese_rules":True,
  "norm_kind":"bnorm",
  "use_initial_conv_3":True,
  "trunk_num_channels":320,
  "mid_num_channels":320,
  "regular_num_channels":224,
  "dilated_num_channels":96,
  "gpool_num_channels":96,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","gpool"],
    ["rconv7","regular"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","gpool"],
    ["rconv12","regular"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","gpool"],
    ["rconv17","regular"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"],
    ["rconv21","gpool"],
    ["rconv22","regular"],
    ["rconv23","regular"],
    ["rconv24","regular"],
    ["rconv25","regular"],
    ["rconv26","gpool"],
    ["rconv27","regular"],
    ["rconv28","regular"],
    ["rconv29","regular"],
    ["rconv30","regular"],
    ["rconv31","gpool"],
    ["rconv32","regular"],
    ["rconv33","regular"],
    ["rconv34","regular"],
    ["rconv35","regular"],
    ["rconv36","gpool"],
    ["rconv37","regular"],
    ["rconv38","regular"],
    ["rconv39","regular"],
    ["rconv40","regular"],
    ["rconv41","gpool"],
    ["rconv42","regular"],
    ["rconv43","regular"],
    ["rconv44","regular"],
    ["rconv45","regular"],
    ["rconv46","gpool"],
    ["rconv47","regular"],
    ["rconv48","regular"],
    ["rconv49","regular"],
    ["rconv50","regular"],
    ["rconv51","gpool"],
    ["rconv52","regular"],
    ["rconv53","regular"],
    ["rconv54","regular"],
    ["rconv55","regular"],
    ["rconv56","gpool"],
    ["rconv57","regular"],
    ["rconv58","regular"],
    ["rconv59","regular"],
    ["rconv60","regular"],
   ],
  "p1_num_channels":64,
  "g1_num_channels":64,
  "v1_num_channels":64,
  "sbv2_num_channels":128,
  "num_scorebeliefs":8,
  "v2_size":144
}

config_of_name = {
  "b2c16": b2c16,
  "b4c32": b4c32,
  "b6c96": b6c96,
  "b10c128": b10c128,
  "b15c192": b15c192,
  "b20c256": b20c256,
  "b30c320": b30c320,
  "b40c256": b40c256,
  "b40c384": b40c384,
  "b60c320": b60c320,
}
