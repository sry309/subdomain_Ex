from lib import main_lib
import threading,sys,os,time

def start():
    main_lib.print_()
    domain_list = set()
    plugin_list = set()
    for i in os.listdir('./plugin'):
        if 'plugin' in i:
            plugin_name = i.split('.py')[0]
            plugin_list.add(plugin_name)
            import_str = 'import plugin.{name}'.format(name=plugin_name)
            exec(import_str)
    domain = main_lib.get_domain()
    for name in plugin_list:
        call_str = 'plugin.{name}.print_author()'.format(name=name)
        sys.stdout.write('Load:')
        exec(call_str)
        call_str = 'threading.Thread(target=plugin.{name}.return_domain,args=(domain,)).start()'.format(name=name)
        exec(call_str)
    while threading.active_count() != 1:
        pass
    print("执行完毕")
    for name in plugin_list:
        value_str = '[open("{filename}","a+").write(str(i)+"\\n") for i in set([a for a in plugin.{name}.domain_list])]'.format(name=name,filename=domain+'.txt')
        exec(value_str)

    print('[+] ' + domain + ' OK.')


if __name__ == '__main__':
    start()
