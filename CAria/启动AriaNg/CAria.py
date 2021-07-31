import os,sys,shutil,requests
import tkinter as tk
from tkinter import messagebox
from subprocess import Popen
class CAria:
    def Run(self):
        self.Update()
        Popen('start "" /b aria2c --conf-path=aria2.conf -D',shell=True)
        Popen('start "" /b "..\AriaNg\index.html"',shell=True)
    def Close(self):
        Popen('taskkill /f /t /im aria2c.exe',shell=True)
        Popen('taskkill /f /t /im chrome.exe',shell=True)
    def Closearia2c(self):
        Popen('taskkill /f /t /im aria2c.exe',shell=True)
    def Update(self):
        resp=requests.get('https://ngosang.github.io/trackerslist/trackers_best_ip.txt')
        tracker=resp.text.replace('\n\n',',')[:-1]
        with open('aria2.conf','r',encoding='utf-8') as conffile:
            with open('tmp.conf','w',encoding='utf-8') as tmpfile:
                for conf in conffile:
                    if 'bt-tracker=' in conf:
                        tmpfile.write('bt-tracker=%s\n'%tracker)
                    else:
                        tmpfile.write(conf)
        os.remove('aria2.conf')
        shutil.move('tmp.conf','aria2.conf')
    def Updatedone(self):
        self.Update()
        messagebox.showinfo('更新conf','更新conf完成！')
    def menuf(self,event,x,y):
        if event=='WM_RBUTTONDOWN':
            self.menu.tk_popup(x,y)
    def about(self):
        messagebox.showinfo('关于','作者：cnzb\nGithub：https://github.com/cnzbpy/simplepy\nGitee：https://gitee.com/cnzbpy/simplepy')
    def allquit(self):
        self.root.call('winico','taskbar','delete',self.icon)
        self.root.quit()
    def Root(self):
        self.root=tk.Tk()
        self.root.withdraw()
        self.root.iconbitmap(iicon)
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'CAria')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'启动AriaNg',command=self.Run)
        self.menu.add_command(label=u'关闭AriaNg',command=self.Close)
        self.menu.add_command(label=u'仅关闭aria2c',command=self.Closearia2c)
        self.menu.add_command(label=u'更新conf',command=self.Updatedone)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'退出',command=self.allquit)
        self.root.mainloop()
if getattr(sys,'frozen',False):
        odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'CAria.ico')
CAria().Root()