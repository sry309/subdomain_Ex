import os,sys

def print_():
    print('''
        Blog:http://www.f4ckweb.top
        bbs:https://www.0xNull.org
        github:https://www.github.com/XiaoTouMingyo
        version:0.1
        --------------------------------------------------------------------------------
    ''')

def include_plugin(filedir):
    plugin = []
    for i in os.listdir(filedir):
        if 'plugin' in i:
            plugin_name = i.split('.py')[0]
            plugin.append(plugin_name)
            import_str = 'import plugin.{name}'.format(name = plugin_name)
            exec(import_str)
    return plugin

def get_domain():
    return sys.argv[1]