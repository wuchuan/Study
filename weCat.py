import itchat
import commands
from itchat.content import TEXT

mode=normal
#""""""
#    node
#        normal 正常模式
#        cmd    命令行模式
#        auto   自动聊天模式
#'''

def mode_cmd(cmd):
    return   commands.getstatusoutput(cmd)
#    return os.system(cmd)

@itchat.msg_register(TEXT)
def simple_reply(msg):
    msg=msg['Text']
    if msg in 'cmd':
        mode='cmd'
        return
    elif msg in 'auto':
        mode='auto'
        return
    else :
        mode='normal'
        return

    if mode in 'cmd':
        return mode_cmd(msg['Text'])

itchat.auto_login(hotReload=True)
itchat.run()
itchat.dump_login_status()
