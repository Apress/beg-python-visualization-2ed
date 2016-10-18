# creating an INI (config) file
import configparser
options = configparser.ConfigParser()
options['User Options'] = {}
options['User Options']['all_data'] = 'Y'
options['User Options']['graph'] = '1'
options['Plot'] = {}
options['Plot']['grid'] = 'Y'
f = open('../data/options.ini', 'w')
options.write(f)
f.close()