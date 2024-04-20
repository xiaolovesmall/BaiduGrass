import time
import requests
import hashlib
import urllib
import random
import json
import tkinter
from tkinter import ttk
import sv_ttk # type: ignore
import pyperclip as pc

def main():
    translation_language_list = [
        'zh',
        'en',
        'yue',
        'wyw',
        'jp',
        'kor',
        'fra',
        'spa',
        'th',
        'ara',
        'ru',
        'pt',
        'de',
        'it',
        'el',
        'nl',
        'pl',
        'bul',
        'est',
        'dan',
        'fin',
        'cs',
        'rom',
        'slo',
        'swe',
        'hu',
        'cht',
        'vie']
    
    root = tkinter.Tk()
    import ctypes

    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

    root.tk.call('tk', 'scaling', ScaleFactor/75)
    
    root.title("Graste")
    root.geometry('500x300+300+200')
    root.iconbitmap(r"graste.ico")
    root.minsize(700,500)	
    root.maxsize(1000,800)	
    def sun():
            if sv_ttk.get_theme() == "dark":
                sv_ttk.use_light_theme()
                sun_button.config(text="🌙") 

            elif sv_ttk.get_theme() == "light":
                sv_ttk.use_dark_theme()
                sun_button.config(text="☀")                 
    sun_button = ttk.Button(root,text="☀", command=sun,style="my.TButton")
    sun_button.pack(anchor="ne",pady=5,padx=5)
    tip1 = ttk.Label(root,text="翻译次数",font=('微软雅黑',15,'bold'))
    tip1.pack(anchor="w",pady=7,padx=15)
    time_box = ttk.Combobox(root, value=('5', '10', '15', '20'))
    time_box.pack(anchor="w",pady=7,padx=15)

    def after_button_pressed():
        out.configure(text="")
        number_of_translations = str(time_box.get())
        def text2grass(text = None):
            query = str(text)
        
            def getURL(toLang = None, q = None):
                appid = 'Your Baidudu Fanyi Apiid'
                secretKey = 'Your Baidudu Fanyi SecretKey'
                myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
                fromLang = 'auto'
                salt = random.randint(32768, 65536)
                sign = appid + q + str(salt) + secretKey
                sign = hashlib.md5(sign.encode()).hexdigest()
                myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
                return myurl

            
            def getResult(s = None):
                global query
                rand = random.randint(0, 27)
                URL = getURL(translation_language_list[rand], s)
                req = requests.get(URL)
                res = json.loads(req.text)
                query = res['trans_result'][0]['dst']
                time.sleep(1)
                return query
        
            for i in range(int(number_of_translations)):
                query = getResult(query)
                print(query)
            r = requests.get(getURL('zh', query))
            result = json.loads(r.text)['trans_result'][0]['dst']
            return(str(result))
    
        if str(number_of_translations) == '':
            out.configure(text="请先选择翻译次数")
        else:
            out.configure(text=text2grass(input.get()))
    tip2 = ttk.Label(root,text="输入要生草的内容",font=('微软雅黑',15,'bold'))
    tip2.pack(anchor="w",pady=7,padx=15)
    input = ttk.Entry(root,width=60)
    input.pack(anchor="w",pady=7,padx=15)
    grass_start_button = ttk.Button(root,text="开始", command=after_button_pressed, width=30)
    grass_start_button.pack(anchor="w",pady=7,padx=15)
    tip3 = ttk.Label(root,text="输出的草",font=('微软雅黑',15,'bold'))
    tip3.pack(anchor="w",pady=7,padx=15)
    out = ttk.Label(root,text="",font=('微软雅黑',12,'bold'))
    out.pack(anchor="w",pady=7,padx=15)

    def copy_out():
        pc.copy(out.cget("text"))
    copy_button = ttk.Button(root,text="复制", command=copy_out, width=30,style="my.TButton")
    copy_button.pack(anchor="w",pady=7,padx=15)

    sv_ttk.use_light_theme()
    root.mainloop()

main()
