import os 
from datetime import datetime
import webbrowser

def gnome_terminal():
    os.system('gnome-terminal')

def firefox():
    os.system('firefox')

def code():
    os.system('code')

def time():
    now = datetime.now()
    now = str(now.strftime("%H %M"))
    return now

def cs_class():
    webbrowser.open("https://meet.google.com/itn-mtng-eeg")

def chinese_class():
    webbrowser.open("https://meet.google.com/ske-gibo-azk")

def english_class():
    webbrowser.open("https://meet.google.com/kyg-tqrh-eqa")

def physics_class():
    webbrowser.open("http://meet.google.com/hzs-hqsg-iyn")

def math_class():
    webbrowser.open("https://us02web.zoom.us/j/7902010597?pwd=eWxDbWFYWU1HTkp6VUNqZTBtWEdSQT09")

def bm_class():
    webbrowser.open("https://sjcs.managebac.com/student/classes/11373953/calendar")

def tok_class():
    webbrowser.open("https://sjcs.managebac.com/student/classes/11373965/calendar")

def ee_class():
    webbrowser.open("https://meet.google.com/ndn-sson-mdx")

def hr_class():
    webbrowser.open("https://meet.google.com/knj-akem-awd")

def anime():
    webbrowser.open("https://4anime.to/")

def news():
    webbrowser.open("https://www.bbc.com/news/world")

