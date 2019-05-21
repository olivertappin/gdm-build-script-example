import sys
import yaml

sys.path.insert(0, 'config')

from config import config

def GenerateConfig(config):
  resources = []
  resources.append({
      'name': 'vm',
      'type': 'compute.v1.instance',
      'properties': {
          'zone': config['zone'],
          'machineType': ''.join(['zones/', config['zone'], '/machineTypes/', config['instance-size']]),
      }
  })
  return {'resources': resources}

# For GDM Templates, we would change the config parameter to become context, as GDM passes this in directly.
# We would then use the config variable globally to use all the required mappings which would be inherited
# using environment-specific configuration overrides, with the parent being the generic config.

print yaml.dump(GenerateConfig(config), default_flow_style=False)
