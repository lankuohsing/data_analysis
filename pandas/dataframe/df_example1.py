#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:44:57 2024

@author: guoxing.lan
"""
import pandas as pd
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                   index=['cobra', 'viper', 'sidewinder'],
                   columns=['max_speed', 'shield'])


a=df.loc['viper']#series
# In[]
b=df.loc[['viper']]#DataFrame
# In[]
c=df.loc[0]#会报错，无法用整数作为下标的方式获取
# In[]
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(mydict)

# In[]
a=df.iloc[[0]]

# In[]
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(mydict,index=[3,2,1])

# In[]
a=df.iloc[[0]]#这里是0是真实的序号0，不是label的index
