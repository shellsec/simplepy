import os,re,sys,json,random,base64,js2py,hashlib,requests
import tkinter as tk
from threading import Thread
from tkinter import messagebox
class Tr:
    def Bd(self):
        try:
            if not self.rootbd.winfo_exists():
                self.Rbd()
        except:
            self.Rbd()
    def Rbd(self):
        self.rootbd=tk.Toplevel()
        self.rootbd.iconbitmap(iicon)
        self.rootbd.title('百度翻译')
        panel1=tk.Frame(self.rootbd)
        xgd1=tk.Scrollbar(panel1,orient='horizontal')
        ygd1=tk.Scrollbar(panel1)
        xgd1.pack(side='bottom',fill='x')
        ygd1.pack(side='right',fill='y')
        self.textbd1=tk.Text(panel1,wrap='none',xscrollcommand=xgd1.set,yscrollcommand=ygd1.set)
        self.textbd1.pack(fill='both')
        panel1.pack(fill='both')
        xgd1.config(command=self.textbd1.xview)
        ygd1.config(command=self.textbd1.yview)
        panel2=tk.Frame(self.rootbd)
        self.btbdr=tk.Button(panel2,text='百度翻译(B)',font=('',16),command=lambda:self.Bdr(None))
        self.btbdr.pack(side='left')
        tk.Button(panel2,text='清屏',font=('',16),command=self.Bdc).pack(side='left')
        panel2.pack()
        panel3=tk.Frame(self.rootbd)
        xgd2=tk.Scrollbar(panel3,orient='horizontal')
        ygd2=tk.Scrollbar(panel3)
        xgd2.pack(side='bottom',fill='x')
        ygd2.pack(side='right',fill='y')
        self.textbd2=tk.Text(panel3,wrap='none',xscrollcommand=xgd2.set,yscrollcommand=ygd2.set)
        self.textbd2.pack(fill='both')
        panel3.pack(fill='both')
        xgd2.config(command=self.textbd2.xview)
        ygd2.config(command=self.textbd2.yview)
        self.rootbd.bind('<Alt-b>',self.Bdr)
    def Bdr(self,event):
        Thread(target=self.Bdg,daemon=True).start()
    def Bdg(self):
        self.btbdr.config(text='正在翻译...')
        strings=(self.textbd1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','Cookie':'BAIDUID=4650B0B34048BBAA1E0B909B42F5A564:FG=1;BIDUPSID=4650B0B34048BBAA1E0B909B42F5A564;PSTM=1537177909;BDUSS=w0VmEzUFFWTTh0bld5VWVhNVo5MEEyV2ZKdTk3U2stMGZmWVQ1TTRuSnVkOHBiQVFBQUFBJCQAAAAAAAAAAAEAAAD0GzcNaG9uZ3F1YW4xOTkxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG7qoltu6qJbTk;pgv_pvi=6774493184;uc_login_unique=19e6fd48035206a8abe89f98c3fc542a;uc_recom_mark=cmVjb21tYXJrXzYyNDU4NjM%3D;MCITY=-218%3A;cflag=15%3A3;SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02893452711;locale=zh;Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1539333192;from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D;REALTIME_TRANS_SWITCH=1;FANYI_WORD_SWITCH=1;HISTORY_SWITCH=1;SOUND_SPD_SWITCH=1;SOUND_PREFER_SWITCH=1;to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D;Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1539333307'}
                html=requests.get('https://fanyi.baidu.com',headers=headers)
                gtk=re.findall("window.gtk = '(.*?)';",html.text)[0]
                js=js2py.EvalJs()
                js.execute('function a(r,o){for(var t=0;t<o.length-2;t+=3){var a=o.charAt(t+2);a=a>="a"?a.charCodeAt(0)-87:Number(a),a="+"===o.charAt(t+1)?r>>>a:r<<a,r="+"===o.charAt(t)?r+a&4294967295:r^a}return r}var C=null;var hash=function(r,_gtk){var o=r.length;o>30&&(r=""+r.substr(0,10)+r.substr(Math.floor(o/2)-5,10)+r.substr(-10,10));var t=void 0,t=null!==C?C:(C=_gtk||"")||"";for(var e=t.split("."),h=Number(e[0])||0,i=Number(e[1])||0,d=[],f=0,g=0;g<r.length;g++){var m=r.charCodeAt(g);128>m?d[f++]=m:(2048>m?d[f++]=m>>6|192:(55296===(64512&m)&&g+1<r.length&&56320===(64512&r.charCodeAt(g+1))?(m=65536+((1023&m)<<10)+(1023&r.charCodeAt(++g)),d[f++]=m>>18|240,d[f++]=m>>12&63|128):d[f++]=m>>12|224,d[f++]=m>>6&63|128),d[f++]=63&m|128)}for(var S=h,u="+-a^+6",l="+-3^+b+-f",s=0;s<d.length;s++)S+=d[s],S=a(S,u);return S=a(S,l),S^=i,0>S&&(S=(2147483647&S)+2147483648),S%=1e6,S.toString()+"."+(S^h)}')
                sign=js.hash(string,gtk)
                token=re.findall("token: '(.+)',",html.text)[0]
                landata={'query':string}
                lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
                lan=lanhtml.json()['lan']
                if lan=='zh':
                    to='en'
                else:
                    to='zh'
                data={'from':lan,'to':to,'query':string,'sign':'%s'%sign,'token':'%s'%token}
                resp=requests.post('https://fanyi.baidu.com/v2transapi',data=data,headers=headers)
                result=resp.json()['trans_result']['data'][0]['dst']+'\n'
                self.textbd2.insert('end',result)
        self.textbd2.delete(self.textbd2.index('end-1c'),'end')
        self.btbdr.config(text='翻译完成')
        self.btbd.config(text='翻译完成')
        try:
            self.boolnum+=1
        except:
            pass
    def Bdc(self):
        self.textbd1.delete(1.0,'end')
        self.textbd2.delete(1.0,'end')
        self.btbdr.config(text='百度翻译(B)')
        self.btbd.config(text='百度翻译')
    def Bdfy(self):
        self.Bd()
        self.textbd1.insert('end',self.textjh.get(1.0,'end').strip())
        self.Bdr(None)
    def Cy(self):
        try:
            if not self.rootcy.winfo_exists():
                self.Rcy()
        except:
            self.Rcy()
    def Rcy(self):
        self.rootcy=tk.Toplevel()
        self.rootcy.iconbitmap(iicon)
        self.rootcy.title('彩云翻译')
        panel1=tk.Frame(self.rootcy)
        xgd1=tk.Scrollbar(panel1,orient='horizontal')
        ygd1=tk.Scrollbar(panel1)
        xgd1.pack(side='bottom',fill='x')
        ygd1.pack(side='right',fill='y')
        self.textcy1=tk.Text(panel1,wrap='none',xscrollcommand=xgd1.set,yscrollcommand=ygd1.set)
        self.textcy1.pack(fill='both')
        panel1.pack(fill='both')
        xgd1.config(command=self.textcy1.xview)
        ygd1.config(command=self.textcy1.yview)
        panel2=tk.Frame(self.rootcy)
        self.btcyr=tk.Button(panel2,text='彩云翻译(C)',font=('',16),command=lambda:self.Cyr(None))
        self.btcyr.pack(side='left')
        tk.Button(panel2,text='清屏',font=('',16),command=self.Cyc).pack(side='left')
        panel2.pack()
        panel3=tk.Frame(self.rootcy)
        xgd2=tk.Scrollbar(panel3,orient='horizontal')
        ygd2=tk.Scrollbar(panel3)
        xgd2.pack(side='bottom',fill='x')
        ygd2.pack(side='right',fill='y')
        self.textcy2=tk.Text(panel3,wrap='none',xscrollcommand=xgd2.set,yscrollcommand=ygd2.set)
        self.textcy2.pack(fill='both')
        panel3.pack(fill='both')
        xgd2.config(command=self.textcy2.xview)
        ygd2.config(command=self.textcy2.yview)
        self.rootcy.bind('<Alt-c>',self.Cyr)
    def Cyr(self,event):
        Thread(target=self.Cyg,daemon=True).start()
    def Cyg(self):
        self.btcyr.config(text='正在翻译...')
        strings=(self.textcy1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                encrypt=hashlib.md5()
                encrypt.update(''.join(random.choices('qweasdzxcrtyfghvbnuiopjklm1234567890',k=10)).encode())
                brower_id=encrypt.hexdigest()
                authdata={'browser_id':brower_id}
                authdata=json.dumps(authdata)
                authheaders={'X-Authorization':'token:qgemv4jr1y38jyq6vhvi','Content-Type':'application/json;charset=UTF-8'}
                html=requests.post('https://api.interpreter.caiyunai.com/v1/user/jwt/generate',data=authdata,headers=authheaders)
                auth=html.json()['jwt']
                landata={'query':string}
                lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
                lan=lanhtml.json()['lan']
                if lan=='zh':
                    to='en'
                else:
                    to='zh'
                data={'browser_id':brower_id,'detect':'true','source':string,'trans_type':'auto2%s'%to}
                data=json.dumps(data)
                headers={'T-Authorization':auth}
                resp=requests.post('https://api.interpreter.caiyunai.com/v1/translator',data=data,headers=headers)
                preresult=json.loads(resp.text)['target']
                t='NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
                o='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
                s=[]
                for i in list(preresult):
                    index=o.find(i)
                    if index>-1:
                        s.append(t[index])
                    else:
                        s.append(i)
                result=base64.b64decode(''.join(s)).decode('utf-8')+'\n'
                self.textcy2.insert('end',result)
        self.textcy2.delete(self.textcy2.index('end-1c'),'end')
        self.btcyr.config(text='翻译完成')
        self.btcy.config(text='翻译完成')
        try:
            self.boolnum+=1
        except:
            pass
    def Cyc(self):
        self.textcy1.delete(1.0,'end')
        self.textcy2.delete(1.0,'end')
        self.btcyr.config(text='彩云翻译(C)')
        self.btcy.config(text='彩云翻译')
    def Cyfy(self):
        self.Cy()
        self.textcy1.insert('end',self.textjh.get(1.0,'end').strip())
        self.Cyr(None)
    def Gg(self):
        try:
            if not self.rootgg.winfo_exists():
                self.Rgg()
        except:
            self.Rgg()
    def Rgg(self):
        self.rootgg=tk.Toplevel()
        self.rootgg.iconbitmap(iicon)
        self.rootgg.title('谷歌翻译')
        panel1=tk.Frame(self.rootgg)
        xgd1=tk.Scrollbar(panel1,orient='horizontal')
        ygd1=tk.Scrollbar(panel1)
        xgd1.pack(side='bottom',fill='x')
        ygd1.pack(side='right',fill='y')
        self.textgg1=tk.Text(panel1,wrap='none',xscrollcommand=xgd1.set,yscrollcommand=ygd1.set)
        self.textgg1.pack(fill='both')
        panel1.pack(fill='both')
        xgd1.config(command=self.textgg1.xview)
        ygd1.config(command=self.textgg1.yview)
        panel2=tk.Frame(self.rootgg)
        self.btggr=tk.Button(panel2,text='谷歌翻译(G)',font=('',16),command=lambda:self.Ggr(None))
        self.btggr.pack(side='left')
        tk.Button(panel2,text='清屏',font=('',16),command=self.Ggc).pack(side='left')
        panel2.pack()
        panel3=tk.Frame(self.rootgg)
        xgd2=tk.Scrollbar(panel3,orient='horizontal')
        ygd2=tk.Scrollbar(panel3)
        xgd2.pack(side='bottom',fill='x')
        ygd2.pack(side='right',fill='y')
        self.textgg2=tk.Text(panel3,wrap='none',xscrollcommand=xgd2.set,yscrollcommand=ygd2.set)
        self.textgg2.pack(fill='both')
        panel3.pack(fill='both')
        xgd2.config(command=self.textgg2.xview)
        ygd2.config(command=self.textgg2.yview)
        self.rootgg.bind('<Alt-g>',self.Ggr)
    def Ggr(self,event):
        Thread(target=self.Ggg,daemon=True).start()
    def Ggg(self):
        self.btggr.config(text='正在翻译...')
        strings=(self.textgg1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                js=js2py.EvalJs()
                js.execute('function TL(a){var k="";var b=406644;var b1=3293161072;var jd=".";var $b="+-a^+6";var Zb="+-3^+b+-f";for(var e=[],f=0,g=0;g<a.length;g++){var m=a.charCodeAt(g);128>m?e[f++]=m:(2048>m?e[f++]=m>>6|192:(55296==(m&64512)&&g+1<a.length&&56320==(a.charCodeAt(g+1)&64512)?(m=65536+((m&1023)<<10)+(a.charCodeAt(++g)&1023),e[f++]=m>>18|240,e[f++]=m>>12&63|128):e[f++]=m>>12|224,e[f++]=m>>6&63|128),e[f++]=m&63|128)}a=b;for(f=0;f<e.length;f++)a+=e[f],a=RL(a,$b);a=RL(a,Zb);a^=b1||0;0>a&&(a=(a&2147483647)+2147483648);a%=1E6;return a.toString()+jd+(a^b)};function RL(a,b){var t="a";var Yb="+";for(var c=0;c<b.length-2;c+=3){var d=b.charAt(c+2),d=d>=t?d.charCodeAt(0)-87:Number(d),d=b.charAt(c+1)==Yb?a>>>d:a<<d;a=b.charAt(c)==Yb?a+d&4294967295:a^d}return a}')
                tk=js.TL(string)
                landata={'query':string}
                lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
                lan=lanhtml.json()['lan']
                if lan=='zh':
                    to='en'
                else:
                    to='zh-CN'
                resp=requests.get('https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&pc=1&otf=1&ssel=0&tsel=0&kc=1&tk=%s&q=%s'%(to,tk,string))
                result=resp.json()[0][0][0]+'\n'
                self.textgg2.insert('end',result)
        self.textgg2.delete(self.textgg2.index('end-1c'),'end')
        self.btggr.config(text='翻译完成')
        self.btgg.config(text='翻译完成')
        try:
            self.boolnum+=1
        except:
            pass
    def Ggc(self):
        self.textgg1.delete(1.0,'end')
        self.textgg2.delete(1.0,'end')
        self.btggr.config(text='谷歌翻译(G)')
        self.btgg.config(text='谷歌翻译')
    def Ggfy(self):
        self.Gg()
        self.textgg1.insert('end',self.textjh.get(1.0,'end').strip())
        self.Ggr(None)
    def Sg(self):
        try:
            if not self.rootsg.winfo_exists():
                self.Rsg()
        except:
            self.Rsg()
    def Rsg(self):
        self.rootsg=tk.Toplevel()
        self.rootsg.iconbitmap(iicon)
        self.rootsg.title('搜狗翻译')
        panel1=tk.Frame(self.rootsg)
        xgd1=tk.Scrollbar(panel1,orient='horizontal')
        ygd1=tk.Scrollbar(panel1)
        xgd1.pack(side='bottom',fill='x')
        ygd1.pack(side='right',fill='y')
        self.textsg1=tk.Text(panel1,wrap='none',xscrollcommand=xgd1.set,yscrollcommand=ygd1.set)
        self.textsg1.pack(fill='both')
        panel1.pack(fill='both')
        xgd1.config(command=self.textsg1.xview)
        ygd1.config(command=self.textsg1.yview)
        panel2=tk.Frame(self.rootsg)
        self.btsgr=tk.Button(panel2,text='搜狗翻译(S)',font=('',16),command=lambda:self.Sgr(None))
        self.btsgr.pack(side='left')
        tk.Button(panel2,text='清屏',font=('',16),command=self.Sgc).pack(side='left')
        panel2.pack()
        panel3=tk.Frame(self.rootsg)
        xgd2=tk.Scrollbar(panel3,orient='horizontal')
        ygd2=tk.Scrollbar(panel3)
        xgd2.pack(side='bottom',fill='x')
        ygd2.pack(side='right',fill='y')
        self.textsg2=tk.Text(panel3,wrap='none',xscrollcommand=xgd2.set,yscrollcommand=ygd2.set)
        self.textsg2.pack(fill='both')
        panel3.pack(fill='both')
        xgd2.config(command=self.textsg2.xview)
        ygd2.config(command=self.textsg2.yview)
        self.rootsg.bind('<Alt-s>',self.Sgr)
    def Sgr(self,event):
        Thread(target=self.Sgg,daemon=True).start()
    def Sgg(self):
        self.btsgr.config(text='正在翻译...')
        strings=(self.textsg1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                fsheaders={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,image/apng,*/*;''q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
                html=requests.get('https://fanyi.sogou.com',headers=fsheaders)
                FUV=html.cookies.get_dict()['FUV']
                SNUID=html.cookies.get_dict()['SNUID']
                landata={'query':string}
                lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
                lan=lanhtml.json()['lan']
                if lan=='zh':
                    to='en'
                else:
                    to='zh-CHS'
                sign=lan+to+string+'109984457'
                m=hashlib.md5()
                m.update(sign.encode('utf-8'))
                data={'from':lan,'s':m.hexdigest(),'text':string,'to':to}
                headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)''AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/83.0.4103.97 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;''q=0.9,image/webp,image/apng,*/*;''q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8','Cookie':'FUV=%s;SNUID=%s'%(FUV,SNUID)}
                resp=requests.post('https://fanyi.sogou.com/api/transpc/text/result',data=data,headers=headers)
                result=resp.json()['data']['translate']['dit']+'\n'
                self.textsg2.insert('end',result)
        self.textsg2.delete(self.textsg2.index('end-1c'),'end')
        self.btsgr.config(text='翻译完成')
        self.btsg.config(text='翻译完成')
        try:
            self.boolnum+=1
        except:
            pass
    def Sgc(self):
        self.textsg1.delete(1.0,'end')
        self.textsg2.delete(1.0,'end')
        self.btsgr.config(text='搜狗翻译(S)')
        self.btsg.config(text='搜狗翻译')
    def Sgfy(self):
        self.Sg()
        self.textsg1.insert('end',self.textjh.get(1.0,'end').strip())
        self.Sgr(None)
    def Tx(self):
        try:
            if not self.roottx.winfo_exists():
                self.Rtx()
        except:
            self.Rtx()
    def Rtx(self):
        self.roottx=tk.Toplevel()
        self.roottx.iconbitmap(iicon)
        self.roottx.title('腾讯翻译')
        panel1=tk.Frame(self.roottx)
        xgd1=tk.Scrollbar(panel1,orient='horizontal')
        ygd1=tk.Scrollbar(panel1)
        xgd1.pack(side='bottom',fill='x')
        ygd1.pack(side='right',fill='y')
        self.texttx1=tk.Text(panel1,wrap='none',xscrollcommand=xgd1.set,yscrollcommand=ygd1.set)
        self.texttx1.pack(fill='both')
        panel1.pack(fill='both')
        xgd1.config(command=self.texttx1.xview)
        ygd1.config(command=self.texttx1.yview)
        panel2=tk.Frame(self.roottx)
        self.bttxr=tk.Button(panel2,text='腾讯翻译(T)',font=('',16),command=lambda:self.Txr(None))
        self.bttxr.pack(side='left')
        tk.Button(panel2,text='清屏',font=('',16),command=self.Txc).pack(side='left')
        panel2.pack()
        panel3=tk.Frame(self.roottx)
        xgd2=tk.Scrollbar(panel3,orient='horizontal')
        ygd2=tk.Scrollbar(panel3)
        xgd2.pack(side='bottom',fill='x')
        ygd2.pack(side='right',fill='y')
        self.texttx2=tk.Text(panel3,wrap='none',xscrollcommand=xgd2.set,yscrollcommand=ygd2.set)
        self.texttx2.pack(fill='both')
        panel3.pack(fill='both')
        xgd2.config(command=self.texttx2.xview)
        ygd2.config(command=self.texttx2.yview)
        self.roottx.bind('<Alt-t>',self.Txr)
    def Txr(self,event):
        Thread(target=self.Txg,daemon=True).start()
    def Txg(self):
        self.bttxr.config(text='正在翻译...')
        strings=(self.texttx1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                html=requests.post('https://fanyi.qq.com/api/reauth1232f')
                qtv=html.json()['qtv']
                qtk=html.json()['qtk']
                landata={'query':string}
                lanhtml=requests.post('https://fanyi.baidu.com/langdetect',data=landata)
                lan=lanhtml.json()['lan']
                if lan=='zh':
                    to='en'
                else:
                    to='zh'
                data={'source':'auto','target':to,'sourceText':string,'qtv':'%s'%qtv,'qtk':'%s'%qtk}
                headers={'Referer':'https://fanyi.qq.com/'}
                resp=requests.post('https://fanyi.qq.com/api/translate',data=data,headers=headers)
                result=resp.json()['translate']['records'][0]['targetText']+'\n'
                self.texttx2.insert('end',result)
        self.texttx2.delete(self.texttx2.index('end-1c'),'end')
        self.bttxr.config(text='翻译完成')
        self.bttx.config(text='翻译完成')
        try:
            self.boolnum+=1
        except:
            pass
    def Txc(self):
        self.texttx1.delete(1.0,'end')
        self.texttx2.delete(1.0,'end')
        self.bttxr.config(text='腾讯翻译(T)')
        self.bttx.config(text='腾讯翻译')
    def Txfy(self):
        self.Tx()
        self.texttx1.insert('end',self.textjh.get(1.0,'end').strip())
        self.Txr(None)
    def Yd(self):
        try:
            if not self.rootyd.winfo_exists():
                self.Ryd()
        except:
            self.Ryd()
    def Ryd(self):
        self.rootyd=tk.Toplevel()
        self.rootyd.iconbitmap(iicon)
        self.rootyd.title('有道翻译')
        panel1=tk.Frame(self.rootyd)
        xgd1=tk.Scrollbar(panel1,orient='horizontal')
        ygd1=tk.Scrollbar(panel1)
        xgd1.pack(side='bottom',fill='x')
        ygd1.pack(side='right',fill='y')
        self.textyd1=tk.Text(panel1,wrap='none',xscrollcommand=xgd1.set,yscrollcommand=ygd1.set)
        self.textyd1.pack(fill='both')
        panel1.pack(fill='both')
        xgd1.config(command=self.textyd1.xview)
        ygd1.config(command=self.textyd1.yview)
        panel2=tk.Frame(self.rootyd)
        self.btydr=tk.Button(panel2,text='有道翻译(Y)',font=('',16),command=lambda:self.Ydr(None))
        self.btydr.pack(side='left')
        tk.Button(panel2,text='清屏',font=('',16),command=self.Ydc).pack(side='left')
        panel2.pack()
        panel3=tk.Frame(self.rootyd)
        xgd2=tk.Scrollbar(panel3,orient='horizontal')
        ygd2=tk.Scrollbar(panel3)
        xgd2.pack(side='bottom',fill='x')
        ygd2.pack(side='right',fill='y')
        self.textyd2=tk.Text(panel3,wrap='none',xscrollcommand=xgd2.set,yscrollcommand=ygd2.set)
        self.textyd2.pack(fill='both')
        panel3.pack(fill='both')
        xgd2.config(command=self.textyd2.xview)
        ygd2.config(command=self.textyd2.yview)
        self.rootyd.bind('<Alt-y>',self.Ydr)
    def Ydr(self,event):
        Thread(target=self.Ydg,daemon=True).start()
    def Ydg(self):
        self.btydr.config(text='正在翻译...')
        strings=(self.textyd1.get(1.0,'end')).split('\n')
        for string in strings:
            if string=='':
                continue
            else:
                data={'doctype':'json','i':string}
                resp=requests.post('http://fanyi.youdao.com/translate',data=data)
                result=resp.json()['translateResult'][0][0]['tgt']+'\n'
                self.textyd2.insert('end',result)
        self.textyd2.delete(self.textyd2.index('end-1c'),'end')
        self.btydr.config(text='翻译完成')
        self.btyd.config(text='翻译完成')
        try:
            self.boolnum+=1
        except:
            pass
    def Ydc(self):
        self.textyd1.delete(1.0,'end')
        self.textyd2.delete(1.0,'end')
        self.btydr.config(text='有道翻译(Y)')
        self.btyd.config(text='有道翻译')
    def Ydfy(self):
        self.Yd()
        self.textyd1.insert('end',self.textjh.get(1.0,'end').strip())
        self.Ydr(None)
    def Fy(self,event):
        self.btjh.config(text='正在翻译...')
        self.boolnum=self.countnum=0
        if self.var1.get()==True:
            self.btbd.config(text='正在翻译...')
            self.countnum+=1
            self.Bdfy()
        if self.var2.get()==True:
            self.btcy.config(text='正在翻译...')
            self.countnum+=1
            self.Cyfy()
        if self.var3.get()==True:
            self.btgg.config(text='正在翻译...')
            self.countnum+=1
            self.Ggfy()
        if self.var4.get()==True:
            self.btsg.config(text='正在翻译...')
            self.countnum+=1
            self.Sgfy()
        if self.var5.get()==True:
            self.bttx.config(text='正在翻译...')
            self.countnum+=1
            self.Txfy()
        if self.var6.get()==True:
            self.btyd.config(text='正在翻译...')
            self.countnum+=1
            self.Ydfy()
        self.done()
    def done(self):
        loop=self.root.after(100,self.done)
        if self.boolnum==self.countnum:
            self.btjh.config(text='翻译完成')
            self.root.after_cancel(loop)
    def Clear(self,event):
        try:
            self.textbd1.delete(1.0,'end')
        except:
            pass
        try:
            self.textbd2.delete(1.0,'end')
        except:
            pass
        try:
            self.textcy1.delete(1.0,'end')
        except:
            pass
        try:
            self.textcy2.delete(1.0,'end')
        except:
            pass
        try:
            self.textgg1.delete(1.0,'end')
        except:
            pass
        try:
            self.textgg2.delete(1.0,'end')
        except:
            pass
        try:
            self.textsg1.delete(1.0,'end')
        except:
            pass
        try:
            self.textsg2.delete(1.0,'end')
        except:
            pass
        try:
            self.texttx1.delete(1.0,'end')
        except:
            pass
        try:
            self.texttx2.delete(1.0,'end')
        except:
            pass
        try:
            self.textyd1.delete(1.0,'end')
        except:
            pass
        try:
            self.textyd2.delete(1.0,'end')
        except:
            pass
        try:
            self.btbdr.config(text='百度翻译(B)')
        except:
            pass
        try:
            self.btcyr.config(text='彩云翻译(C)')
        except:
            pass
        try:
            self.btggr.config(text='谷歌翻译(G)')
        except:
            pass
        try:
            self.btsgr.config(text='搜狗翻译(S)')
        except:
            pass
        try:
            self.bttxr.config(text='腾讯翻译(T)')
        except:
            pass
        try:
            self.btydr.config(text='有道翻译(Y)')
        except:
            pass
        self.textjh.delete(1.0,'end')
        self.btbd.config(text='百度翻译')
        self.btcy.config(text='彩云翻译')
        self.btgg.config(text='谷歌翻译')
        self.btsg.config(text='搜狗翻译')
        self.bttx.config(text='腾讯翻译')
        self.btyd.config(text='有道翻译')
        self.btjh.config(text='聚合翻译(A)')
    def menuf(self,event,x,y):
        if event=='WM_RBUTTONDOWN':
            self.menu.tk_popup(x,y)
        if event=='WM_LBUTTONDOWN':
            self.root.deiconify()
        if event=='WM_MBUTTONDOWN':
            self.root.withdraw()
    def about(self):
        messagebox.showinfo('关于','作者：cnzb\nGithub：https://github.com/cnzbpy/simplepy\nGitee：https://gitee.com/cnzbpy/simplepy')
    def allquit(self):
        self.root.call('winico','taskbar','delete',self.icon)
        self.root.quit()
    def Root(self):
        self.root=tk.Tk()
        self.root.iconbitmap(iicon)
        self.root.title('聚合翻译')
        self.root.call('package','require','Winico')
        self.icon=self.root.call('winico','createfrom',iicon)
        self.root.call('winico','taskbar','add',self.icon,'-callback',(self.root.register(self.menuf),'%m','%x','%y'),'-pos',0,'-text',u'聚合翻译')
        self.menu=tk.Menu(self.root,tearoff=0)
        self.menu.add_command(label=u'显示主页面',command=self.root.deiconify)
        self.menu.add_command(label=u'关于',command=self.about)
        self.menu.add_command(label=u'隐藏主页面',command=self.root.withdraw)
        self.menu.add_command(label=u'退出',command=self.allquit)
        panel1=tk.Frame(self.root)
        xgd=tk.Scrollbar(panel1,orient='horizontal')
        ygd=tk.Scrollbar(panel1)
        xgd.pack(side='bottom',fill='x')
        ygd.pack(side='right',fill='y')
        self.textjh=tk.Text(panel1,wrap='none',xscrollcommand=xgd.set,yscrollcommand=ygd.set)
        self.textjh.pack(fill='both',expand=1)
        panel1.pack(fill='both',expand=1)
        xgd.config(command=self.textjh.xview)
        ygd.config(command=self.textjh.yview)
        panel2=tk.Frame(self.root)
        self.btjh=tk.Button(panel2,text='聚合翻译(A)',font=('',16),command=lambda:self.Fy(None))
        self.btjh.pack(side='left')
        self.var1=tk.BooleanVar()
        tk.Checkbutton(panel2,text='百度翻译',font=('',12),variable=self.var1).pack(side='left')
        self.var2=tk.BooleanVar()
        self.var2.set(True)
        tk.Checkbutton(panel2,text='彩云翻译',font=('',12),variable=self.var2).pack(side='left')
        self.var3=tk.BooleanVar()
        self.var3.set(True)
        tk.Checkbutton(panel2,text='谷歌翻译',font=('',12),variable=self.var3).pack(side='left')
        self.var4=tk.BooleanVar()
        tk.Checkbutton(panel2,text='搜狗翻译',font=('',12),variable=self.var4).pack(side='left')
        self.var5=tk.BooleanVar()
        tk.Checkbutton(panel2,text='腾讯翻译',font=('',12),variable=self.var5).pack(side='left')
        self.var6=tk.BooleanVar()
        tk.Checkbutton(panel2,text='有道翻译',font=('',12),variable=self.var6).pack(side='left')
        panel2.pack()
        panel3=tk.Frame(self.root)
        tk.Button(panel3,text='清屏(C)',font=('',16),command=lambda:self.Clear(None)).pack(side='left')
        self.btbd=tk.Button(panel3,text='百度翻译',font=('',16),command=self.Bd)
        self.btbd.pack(side='left')
        self.btcy=tk.Button(panel3,text='彩云翻译',font=('',16),command=self.Cy)
        self.btcy.pack(side='left')
        self.btgg=tk.Button(panel3,text='谷歌翻译',font=('',16),command=self.Gg)
        self.btgg.pack(side='left')
        self.btsg=tk.Button(panel3,text='搜狗翻译',font=('',16),command=self.Sg)
        self.btsg.pack(side='left')
        self.bttx=tk.Button(panel3,text='腾讯翻译',font=('',16),command=self.Tx)
        self.bttx.pack(side='left')
        self.btyd=tk.Button(panel3,text='有道翻译',font=('',16),command=self.Yd)
        self.btyd.pack(side='left')
        panel3.pack()
        self.root.bind('<Alt-a>',self.Fy)
        self.root.bind('<Alt-c>',self.Clear)
        self.root.mainloop()
if getattr(sys,'frozen',False):
        odir=sys._MEIPASS
else:
    odir=os.path.dirname(os.path.abspath(__file__))
iicon=os.path.join(odir,'聚合翻译.ico')
Tr().Root()