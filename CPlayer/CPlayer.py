import os,sys,random,ctypes,winreg,chardet,platform
from threading import Thread
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu,QAction,QMessageBox,QApplication,QMainWindow,QSystemTrayIcon,QFileDialog,QDesktopWidget
from Ui_CPlayer import Ui_MainWindow
class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Tray()
        self.Listadd()
        self.step=0
        self.loop=0
        self.flag=self.listtag=self.fulltag=True
        self.player=vlc.MediaPlayer()
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.fp=fp
        if self.fp!=None:
            name=self.fp[self.fp.rfind('\\')+1:self.fp.rfind('.')]
            self.list.addItem(name)
            self.l.append(self.fp)
            self.Play()
    def Tray(self):
        self.tp=QSystemTrayIcon(self)
        self.tp.setIcon(QIcon(idirC))
        self.tp.activated.connect(self.Activated)
        self.tp.setToolTip('CPlayer')
        tpMenu=QMenu()
        a1=QAction((QIcon(idirC)),'显示主页面',self,triggered=(self.Showmain))
        a2=QAction((QIcon(idirC)),'隐藏主页面',self,triggered=(self.Min))
        a3=QAction((QIcon(idirabout)),'关于',self,triggered=(self.About))
        a4=QAction((QIcon(idirexit)),'退出',self,triggered=(self.Quit))
        tpMenu.addAction(a1)
        tpMenu.addAction(a2)
        tpMenu.addAction(a3)
        tpMenu.addAction(a4)
        self.tp.setContextMenu(tpMenu)
        self.tp.show()
    def closeEvent(self,event):
        event.ignore()
        self.hide()
    def Activated(self,reason):
        if reason==QSystemTrayIcon.MiddleClick:
            self.Min()
        else:
            if reason==QSystemTrayIcon.Trigger:
                self.Showmain()
    def Showmain(self):
        self.showNormal()
        self.activateWindow()
    def Min(self):
        self.hide()
    def About(self):
        QMessageBox.information(self,'关于','作者：cnzb\nGithub：https://github.com/cnzbpy/simplepy\nGitee：https://gitee.com/cnzbpy/simplepy')
    def Quit(self):
        self.tp=None
        app.exit()
    def resizeEvent(self,event):
        self.ratio()
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_P:
            self.Listhide()
        if event.key()==Qt.Key_T:
            self.Fastback()
        if event.key()==Qt.Key_L:
            self.Loop()
        if event.key()==Qt.Key_Space:
            self.Play()
        if event.key()==Qt.Key_S:
            self.Stop()
        if event.key()==Qt.Key_F:
            self.Full()
        if event.key()==Qt.Key_J:
            self.Fastforward()
        if event.key()==Qt.Key_M:
            self.Mute()
        if event.key()==Qt.Key_A:
            self.svolume.setValue(self.svolume.value()+1)
        if event.key()==Qt.Key_R:
            self.svolume.setValue(self.svolume.value()-1)
    def eventFilter(self,sender,event):
        if (event.type()==event.ChildRemoved):
            self.Moved()
        return False
    def Listmenu(self,position):
        lm=QMenu()
        addact=QAction("添加到播放列表",self,triggered=self.Add)
        removeact=QAction("从播放列表移除",self,triggered=self.Remove)
        renameact=QAction('重命名',self,triggered=self.Rename)
        clearact=QAction('清空播放列表',self,triggered=self.Clear)
        saveact=QAction('保存当前播放列表',self,triggered=self.Saved)
        lm.addAction(addact)
        if self.list.itemAt(position):
            lm.addAction(removeact)
            lm.addAction(renameact)
        lm.addAction(clearact)
        lm.addAction(saveact)
        lm.exec_(self.list.mapToGlobal(position))
    def Listadd(self):
        self.l=[]
        self.list.installEventFilter(self)
        if os.path.isfile('CPlayerlist.txt'):
            with open('CPlayerlist.txt','rb') as f:
                playencode=(chardet.detect(f.read()))['encoding']
            with open('CPlayerlist.txt',encoding=playencode,errors='ignore') as f:
                for i in f:
                    i=i.strip()
                    name=i[0:i.find(',')]
                    filelist=i[i.find(',')+1:len(i)]
                    self.list.addItem(name)
                    self.l.append(filelist)
    def Add(self):
        filelists,_=QFileDialog.getOpenFileNames(self,'添加到播放列表','.','媒体文件(*)')
        for filelist in filelists:
            name=filelist[filelist.rfind('/')+1:filelist.rfind('.')]
            self.list.addItem(name)
            self.l.append(filelist)
    def Remove(self):
        ltmp=[]
        for i in self.list.selectedIndexes():
            ltmp.append(i.row())
        ltmp.sort(reverse=True)
        for j in ltmp:
            self.list.takeItem(j)
            self.l.pop(j)
        self.list.setCurrentRow(self.list.currentRow())
        self.list.scrollToItem(self.list.currentItem(),hint=1)
    def Rename(self):
        item=self.list.item(self.list.currentRow())
        item.setFlags(item.flags()|Qt.ItemIsEditable)
        self.list.editItem(item)
    def Clear(self):
        self.l=[]
        self.list.clear()
        if os.path.isfile('CPlayerlist.txt'):
            os.remove('CPlayerlist.txt')
    def Drag(self):
        self.tmp1=[]
        self.tmp2=self.l[:]
        for i in range(self.list.count()):
            self.tmp1.append(self.list.item(i).text())
    def Moved(self):
        for i in range(self.list.count()):
            if self.list.item(i).text()==self.tmp1[i]:
                continue
            else:
                self.l[i]=self.tmp2[self.tmp1.index(self.list.item(i).text())]
    def Saved(self):
        if not os.path.isfile('CPlayerlist.txt'):
            file=open('CPlayerlist.txt','w')
            file.close()
        with open('CPlayerlist.txt','rb') as f:
            playencode=(chardet.detect(f.read()))['encoding']
        with open('CPlayerlist.txt','w',encoding=playencode,errors='ignore') as f:
            for i in range(self.list.count()):
                f.write('%s,%s\n'%(self.list.item(i).text(),self.l[i]))
        QMessageBox.information(self,'保存','播放列表保存成功！')
    def Listhide(self):
        if self.listtag:
            self.frame.hide()
            self.listtag=False
        else:
            self.frame.show()
            self.listtag=True
        self.ratio()
    def ratio(self):
        QApplication.processEvents()
        self.player.video_set_aspect_ratio('%s:%s'%(self.lmedia.width(),self.lmedia.height()))
    def Loop(self):
        self.loop+=1
        if self.loop>3:
            self.loop=0
        if self.loop==0:
            self.bloop.setIcon(QIcon(idirwithoutloop))
            self.bloop.setToolTip('无，快捷键“l”')
        elif self.loop==1:
            self.bloop.setIcon(QIcon(idirwithorderloop))
            self.bloop.setToolTip('顺序播放，快捷键“l”')
        elif self.loop==2:
            self.bloop.setIcon(QIcon(idirwithrandomloop))
            self.bloop.setToolTip('随机播放，快捷键“l”')
        else:
            self.bloop.setIcon(QIcon(idirwithloop))
            self.bloop.setToolTip('循环播放，快捷键“l”')
    def set_window(self,winid):
        if platform.system()=='Windows':
            self.player.set_hwnd(winid)
        elif platform.system()=='Linux':
            self.player.set_xwindow(winid)
        else:
            self.player.set_nsobject(winid)
    def Play(self):
        if self.flag:
            try:
                if self.fp!=None:
                    self.playitem=self.fp
                else:
                    if self.list.currentRow()==-1:
                        self.list.setCurrentRow(self.list.count()-1)
                    self.playitem=self.l[self.list.currentRow()]
                self.Loopplay()
            except:
                QMessageBox.warning(self,'错误','找不到要播放的文件！')
        else:
            if self.l[self.list.currentRow()]==self.playitem:
                if self.player.is_playing():
                    self.player.pause()
                    self.steptimer.stop()
                    self.bplay.setIcon(QIcon(idirplay))
                    self.bplay.setToolTip('播放，快捷键“Space”')
                else:
                    self.player.play()
                    self.steptimer.start()
                    self.bplay.setIcon(QIcon(idirpause))
                    self.bplay.setToolTip('暂停，快捷键“Space”')
            else:
                Thread(target=self.Threadstop,daemon=True).start()
                self.playitem=self.l[self.list.currentRow()]
                self.step=0
                self.stime.setValue(0)
                self.player.set_mrl("%s"%self.playitem)
                self.player.play()
                self.timer.start()
                self.steptimer.start()
                self.bplay.setIcon(QIcon(idirpause))
                self.bplay.setToolTip('暂停，快捷键“Space”')
    def Loopplay(self):
        self.step=0
        self.stime.setValue(0)
        self.player.set_mrl("%s"%self.playitem)
        self.set_window(int(self.lmedia.winId()))
        self.ratio()
        self.player.play()
        self.timer=QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.Show)
        self.steptimer=QTimer()
        self.steptimer.start(1000)
        self.steptimer.timeout.connect(self.Step)
        self.flag=False
        self.bplay.setIcon(QIcon(idirpause))
        self.bplay.setToolTip('暂停，快捷键“Space”')
    def Show(self):
        self.mediatime=self.player.get_length()/1000
        self.stime.setMaximum(int(self.mediatime))
        mediamin,mediasec=divmod(self.mediatime,60)
        mediahour,mediamin=divmod(mediamin,60)
        playmin,playsec=divmod(self.step,60)
        playhour,playmin=divmod(playmin,60)
        self.ltime.setText('%02d:%02d:%02d/%02d:%02d:%02d'%(playhour,playmin,playsec,mediahour,mediamin,mediasec))
    def Stop(self):
        if self.flag==False:
            Thread(target=self.Threadstop,daemon=True).start()
            self.timer.stop()
            self.steptimer.stop()
            self.step=0
            self.flag=True
            self.stime.setValue(0)
            self.ltime.setText('')
            self.bplay.setIcon(QIcon(idirplay))
            self.bplay.setToolTip('播放，快捷键“Space”')
    def Threadstop(self):
        self.player.stop()
    def Full(self):
        if self.fulltag:
            self.frame.hide()
            self.frame_2.hide()
            self.showFullScreen()
            self.bfull.setIcon(QIcon(idirexitfullscreen))
            self.bfull.setToolTip('退出全屏，快捷键“f”')
            self.fulltag=False
        else:
            self.frame.show()
            self.frame_2.show()
            self.showNormal()
            self.bfull.setIcon(QIcon(idirexpandfullscreen))
            self.bfull.setToolTip('全屏，快捷键“f”')
            self.fulltag=True
    def Curvol(self):
        self.curvol=self.svolume.value()
    def Mute(self):
        if self.flag==False:
            if self.player.audio_get_volume()!=0:
                self.player.audio_set_volume(0)
                self.bmute.setIcon(QIcon(idirwithoutvolume))
                self.bmute.setToolTip('取消静音，快捷键“m”')
                self.tag=False
            else:
                if self.svolume.value()!=0:
                    self.player.audio_set_volume(self.svolume.value())
                else:
                    self.player.audio_set_volume(self.curvol)
                    self.svolume.setValue(self.curvol)
                self.bmute.setIcon(QIcon(idirwithvolume))
                self.bmute.setToolTip('静音，快捷键“m”')
                self.tag=True
    def Volume(self):
        if self.flag==False:
            if self.svolume.value()==0:
                self.bmute.setIcon(QIcon(idirwithoutvolume))
                self.bmute.setToolTip('取消静音，快捷键“m”')
            else:
                self.bmute.setIcon(QIcon(idirwithvolume))
                self.bmute.setToolTip('静音，快捷键“m”')
            self.player.audio_set_volume(self.svolume.value())
    def Step(self):
        if self.step>=int(self.mediatime):
            self.step=int(self.mediatime)
            if self.loop==0:
                if not self.player.is_playing() and self.player.get_state()!=vlc.State.Paused:
                    self.Stop()
            else:
                if self.loop==1:
                    orderrow=self.list.currentRow()+1
                    if self.list.currentRow()==-1 or orderrow==self.list.count():
                        self.Stop()
                        QMessageBox.information(self,'播放完毕','当前播放列表播放完毕！')
                    else:
                        self.playitem=self.l[orderrow]
                        self.list.setCurrentRow(orderrow)
                        self.list.scrollToItem(self.list.item(orderrow),hint=1)
                        self.Loopplay()
                elif self.loop==2:
                    randomrow=random.randrange(self.list.count())
                    self.playitem=self.l[randomrow]
                    self.list.setCurrentRow(randomrow)
                    self.list.scrollToItem(self.list.item(randomrow),hint=1)
                    self.Loopplay()
                else:
                    self.Loopplay()
        else:
            self.step+=1
            self.stime.setValue(self.step)
    def Slidechanged(self):
        self.step=self.stime.value()
    def Slidemoved(self):
        if self.flag==False:
            self.player.set_position(self.step/int(self.mediatime))
    def Fastforward(self):
        if self.flag==False:
            self.step+=10
            if self.step>=int(self.mediatime):
                self.stime.setValue(int(self.mediatime))
            self.stime.setValue(self.step)
            self.player.set_position(self.step/int(self.mediatime))
    def Fastback(self):
        if self.flag==False:
            self.step-=10
            if self.step<=0:
                self.step=0
                self.stime.setValue(0)
            self.stime.setValue(self.step)
            self.player.set_position(self.step/int(self.mediatime))
if __name__=='__main__':
    if getattr(sys,'frozen',False):
        odir=sys._MEIPASS
    else:
        odir=os.path.dirname(os.path.abspath(__file__))
    os.environ['PYTHON_VLC_MODULE_PATH']=os.path.join(odir,'vlc')
    import vlc
    idirC=os.path.join(odir,'img\C.png')
    idirabout=os.path.join(odir,'img\gitee.png')
    idirexit=os.path.join(odir,'img\exit.png')
    idirwithoutloop=os.path.join(odir,'img\withoutloop.png')
    idirwithorderloop=os.path.join(odir,'img\withorderloop.png')
    idirwithrandomloop=os.path.join(odir,'img\withrandomloop.png')
    idirwithloop=os.path.join(odir,'img\withloop.png')
    idirpause=os.path.join(odir,'img\pause.png')
    idirplay=os.path.join(odir,'img\play.png')
    idirwithoutvolume=os.path.join(odir,'img\withoutvolume.png')
    idirwithvolume=os.path.join(odir,'img\withvolume.png')
    idirexpandfullscreen=os.path.join(odir,'img\expandfullscreen.png')
    idirexitfullscreen=os.path.join(odir,'img\exitfullscreen.png')
    exepath=sys.executable
    idirCPlayerpy=os.path.abspath(__file__)
    try:
        fp=sys.argv[1]
    except:
        fp=None
    if ctypes.windll.shell32.IsUserAnAdmin():
        menu_name='用CPlayer打开'
        if 'CPlayer.exe' in exepath:
            command=r'"%s"'%exepath
        else:
            command=r'"%s" "%s"'%(exepath,idirCPlayerpy)
        key1=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'*\\shell')
        winreg.SetValue(key1,menu_name,winreg.REG_SZ,menu_name)
        sub_key1=winreg.OpenKey(key1,menu_name)
        winreg.SetValue(sub_key1,'command',winreg.REG_SZ,command+' "%v"')
        winreg.CloseKey(sub_key1)
        winreg.CloseKey(key1)
        key2=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Directory\\shell')
        winreg.SetValue(key2,menu_name,winreg.REG_SZ,menu_name)
        sub_key2=winreg.OpenKey(key2,menu_name)
        winreg.SetValue(sub_key2,'command',winreg.REG_SZ,command+' "%v"')
        winreg.CloseKey(sub_key2)
        winreg.CloseKey(key2)
        key3=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Directory\\Background\\shell')
        winreg.SetValue(key3,menu_name,winreg.REG_SZ,menu_name)
        sub_key3=winreg.OpenKey(key3,menu_name)
        winreg.SetValue(sub_key3,'command',winreg.REG_SZ,command+' "%v"')
        winreg.CloseKey(sub_key3)
        winreg.CloseKey(key3)
        key4=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r'Drive\\shell')
        winreg.SetValue(key4,menu_name,winreg.REG_SZ,menu_name)
        sub_key4=winreg.OpenKey(key4,menu_name)
        winreg.SetValue(sub_key4,'command',winreg.REG_SZ,command+' "%v"')
        winreg.CloseKey(sub_key4)
        winreg.CloseKey(key4)
    else:
        tmp=ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,__file__,None,0)
        if tmp!=5:
            app=QApplication(sys.argv)
            QApplication.setQuitOnLastWindowClosed(False)
            win=Window()
            win.show()
            sys.exit(app.exec_())