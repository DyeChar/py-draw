# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:58:18 2019

@author: zhady
"""


import pandas as pd
data = pd.read_excel(r'D:\Users\zhady\Desktop\tmp.xlsx')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.pyplot import MultipleLocator
import matplotlib.dates as mdates
from datetime import datetime


plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来正常显示中文标签
fmt ='%.2f%%'
font = {'family':'SimHei'} #设置使用的字体（需要显示中文的时候使用）
plt.rc('font',**font) #设置显示中文，与字体配合使用
fig ,ax=plt.subplots(3,sharex=True,figsize=(12,9)) 
fig.suptitle(r'低佣房型',fontsize=20, y=0.92)

ax[0].bar(data['d'], data['直采非直连房型数'],label='房型数', color='orange',width=12) 
ax[0].yaxis.set_major_locator(mtick.MultipleLocator(50000))
ax[0].set_ylabel(r"房型数",{'size':15})
ax[0].tick_params(labelsize=15)
ax[0].legend(loc=1,bbox_to_anchor=(1,0.89))

ax01 = ax[0].twinx()
ax01.plot(data['d'], data['直采非直连房型占比']*100,label='占  比',color='r',linewidth=2) 
ax01.set_ylabel(r"占  比",{'size':15})
ax01.tick_params(labelsize=15)
ax01.yaxis.set_major_formatter(mtick.FormatStrFormatter(fmt))
ax01.legend(loc=1,bbox_to_anchor=(1,1))
for a,b in zip(data['d'],data['直采非直连房型占比']*100):
    ax01.text(a, b+0.0002, fmt % b, ha='center', va= 'bottom',fontsize=14)
ax[0].set_title('直采非直连',fontsize=16,y=-0.16)


ax[1].bar(data['d'], data['直采直连房型数'],label='房型数', color='orange',width=12) 
ax[1].yaxis.set_major_locator(mtick.MultipleLocator(50000))
ax[1].set_ylabel(r"房型数",{'size':15})
ax[1].tick_params(labelsize=15)
ax[1].legend(loc=1,bbox_to_anchor=(1,0.89))

ax11 = ax[1].twinx()
ax11.plot(data['d'], data['直采直连房型占比']*100,label='占  比',color='r',linewidth=2) 
ax11.set_ylabel(r"占  比",{'size':15})
ax11.tick_params(labelsize=15)
ax11.yaxis.set_major_formatter(mtick.FormatStrFormatter(fmt))
ax11.legend(loc=1,bbox_to_anchor=(1,1))
for a,b in zip(data['d'],data['直采直连房型占比']*100):
    ax11.text(a, b, fmt % b, ha='center', va= 'bottom',fontsize=14)
ax[1].set_title('直采直连',fontsize=16,y=-0.16)


ax[2].bar(data['d'], data['代理房型数'],label='房型数', color='orange',width=12) 
ax[2].yaxis.set_major_locator(mtick.MultipleLocator(5000000))
ax[2].set_ylabel(r"房型数",{'size':15})
ax[2].tick_params(labelsize=15)
ax[2].legend(loc=1,bbox_to_anchor=(1,0.89))

ax21 = ax[2].twinx()
ax21.plot(data['d'], data['代理房型占比']*100,label='占  比',color='r',linewidth=2) 
ax21.set_ylabel(r"占  比",{'size':15})
ax21.tick_params(labelsize=15)
ax21.yaxis.set_major_formatter(mtick.FormatStrFormatter(fmt))
ax21.legend(loc=1,bbox_to_anchor=(1,1))
for a,b in zip(data['d'],data['代理房型占比']*100):
    ax21.text(a, b, fmt % b, ha='center', va= 'bottom',fontsize=14)
ax[2].set_title('代理',fontsize=16,y=-0.16)
r'''
ax[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))  
x_major_locator=MultipleLocator(30)
ax[2].xaxis.set_major_locator(x_major_locator)
#ax[2].set_xticks([datetime.strptime(d, '%Y-%m-%d') for d in data['d']]  )
ax[2].axes.set_xticklabels(data['d'])
print  (data['d'])
'''
fig.autofmt_xdate()
plt.savefig(r'D:\Users\zhady\Desktop\低佣房型变化.png')
plt.show()






plt.rcParams['font.sans-serif']=['Microsoft YaHei'] #用来正常显示中文标签
fmt ='%.2f%%'
font = {'family':'SimHei'} #设置使用的字体（需要显示中文的时候使用）
plt.rc('font',**font) #设置显示中文，与字体配合使用
fig ,ax=plt.subplots(3,sharex=True,figsize=(12,9)) 
fig.suptitle(r'低佣酒店',fontsize=20, y=0.92)

ax[0].bar(data['d'], data['直采非直连酒店数'],label='酒店数', color='orange',width=12) 
ax[0].yaxis.set_major_locator(mtick.MultipleLocator(500))
ax[0].set_ylabel(r"酒店数",{'size':15})
ax[0].tick_params(labelsize=15)
ax[0].legend(loc=1,bbox_to_anchor=(1,0.89))

ax01 = ax[0].twinx()
ax01.plot(data['d'], data['直采非直连酒店占比']*100,label='占  比',color='r',linewidth=2) 
ax01.set_ylabel(r"占  比",{'size':15})
ax01.tick_params(labelsize=15)
ax01.yaxis.set_major_formatter(mtick.FormatStrFormatter(fmt))
ax01.legend(loc=1,bbox_to_anchor=(1,1))
for a,b in zip(data['d'],data['直采非直连酒店占比']*100):
    ax01.text(a, b+0.0002, fmt % b, ha='center', va= 'bottom',fontsize=14)
ax[0].set_title('直采非直连',fontsize=16,y=-0.16)


ax[1].bar(data['d'], data['直采直连酒店数'],label='酒店数', color='orange',width=12) 
ax[1].yaxis.set_major_locator(mtick.MultipleLocator(50))
ax[1].set_ylabel(r"酒店数",{'size':15})
ax[1].tick_params(labelsize=15)
ax[1].legend(loc=1,bbox_to_anchor=(1,0.89))

ax11 = ax[1].twinx()
ax11.plot(data['d'], data['直采直连酒店占比']*100,label='占  比',color='r',linewidth=2) 
ax11.set_ylabel(r"占  比",{'size':15})
ax11.tick_params(labelsize=15)
ax11.yaxis.set_major_formatter(mtick.FormatStrFormatter(fmt))
ax11.legend(loc=1,bbox_to_anchor=(1,1))
for a,b in zip(data['d'],data['直采直连酒店占比']*100):
    ax11.text(a, b, fmt % b, ha='center', va= 'bottom',fontsize=14)
ax[1].set_title('直采直连',fontsize=16,y=-0.16)


ax[2].bar(data['d'], data['代理酒店数'],label='酒店数', color='orange',width=12) 
ax[2].yaxis.set_major_locator(mtick.MultipleLocator(25000))
ax[2].set_ylabel(r"酒店数",{'size':15})
ax[2].tick_params(labelsize=15)
ax[2].legend(loc=1,bbox_to_anchor=(1,0.89))

ax21 = ax[2].twinx()
ax21.plot(data['d'], data['代理酒店占比']*100,label='占  比',color='r',linewidth=2) 
ax21.set_ylabel(r"占  比",{'size':15})
ax21.tick_params(labelsize=15)
ax21.yaxis.set_major_formatter(mtick.FormatStrFormatter(fmt))
ax21.legend(loc=1,bbox_to_anchor=(1,1))
for a,b in zip(data['d'],data['代理酒店占比']*100):
    ax21.text(a, b, fmt % b, ha='center', va= 'bottom',fontsize=14)
ax[2].set_title('代理',fontsize=16,y=-0.16)
# plt.xlim('2018-11-20', '2019-12-20')

ax[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))  
# x_major_locator=MultipleLocator(1)
# ax[2].xaxis.set_major_locator(x_major_locator)

fig.autofmt_xdate()
plt.savefig(r'D:\Users\zhady\Desktop\低佣酒店变化.png')
plt.show()

