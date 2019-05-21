###########################################################################
# This file simply binds the two configuration files together, overriding #
# generic configuration with environment-specific configuration values.   #
###########################################################################

from env import envConfig
from generic import genericConfig

# Change this varaible to something dynamic (inherited from GDM)
env = 'my-environment-name'

config = dict()
config.update(genericConfig)
config.update(envConfig[env])
