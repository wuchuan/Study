#incoding=utf8
import itchat
import commands
from itchat.content import TEXT

#""""""
#    node
#        normal 正常模式
#        cmd    命令行模式
#        auto   自动聊天模式
#'''

def mode_cmd(cmd):
    print('cmd=='+cmd)
    print commands.getstatusoutput(cmd)
    (status,rel)=commands.getstatusoutput(cmd)
    print(rel)
    return  'it.s ok'

#    return os.system(cmd)

@itchat.msg_register(TEXT)
def simple_reply(msg):
    msg=msg['Text']
    global mode
    if msg in 'cmd':
        mode='cmd'
        return
    elif msg in 'auto':
        mode='auto'
        return
    elif msg in 'normal':
        mode='normal'
        return
    print(mode)
    if mode in 'cmd':
	print(msg)
        if msg in 'wakeonlan':
            mode_cmd('wakeonlan 40:8d:5c:bc:52:7d')
            return 'wakeonlan'
        if msg in 'off':
	    mode_cmd('echo . | sudo -S pm-suspend')
	    return 'Computer is off'

        return mode_cmd(msg)

itchat.auto_login(hotReload=True)
itchat.run()
itchat.dump_login_status()
