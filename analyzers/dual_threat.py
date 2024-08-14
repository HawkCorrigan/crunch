from .helper import *
from copy import deepcopy
from collections import Counter, OrderedDict
import matplotlib.pylab as plt
import random
import wcl

x = 0

def fmt_timestamp( timestamp ):
  timestamp_s = timestamp // 1000
  timestamp_m = timestamp_s // 60
  timestamp_h = timestamp_m // 60
  return f'{timestamp_h%60:02}:{timestamp_m%60:02}:{timestamp_s%60:02}.{timestamp%1000:03}'

def cb2( self, event):
  global x 
  x += 1

def cb3( self, event):
  global x 
  x -= 1


def cb( self, event ):

  if True:
    global x
    print( fmt_timestamp( event.get('timestamp') - self.params['startTime'] ), end=' ' )
    print( event.get( 'sourceID' ), end='\t')
    print( x)
    self.event_data.append(x)
    x = 0

def probability_at_count( report_codes ):
  global counter
  counter = 0
  t = Analyzer(
    report_codes,
    params={
      'limit': 25000,
      # 'filterExpression': "ability.id in (1, 451839) and source.name = 'Jfunk'"
      'filterExpression': "ability.id in (188389, 77762) and source.name = 'Bloodmallet'"
    },
    callbacks=[
      {
        'type': 'applybuff',
        'abilityGameID': [77762],
        'callback': cb
      },
      { 'type': 'damage',
        'abilityGameID': [188389],
        'callback': cb2},
      { 'type': 'cast',
        'abilityGameID': [188389],
        'callback': cb3}
        
    ],
    event_data=[],
  )

  def cum(list_of):
      sum_values = sum(list_of)
      F = []
      temp = 0
      for i in list_of:
          F.append(i/(sum_values-temp))
          temp += i
      return F

  import json
  # print(json.dumps( t.data, indent=2))

  thelist =sorted(Counter(t.event_data).items())
  x, y = zip(*thelist)
  print("Values:")
  print((x,y))
  y = cum(y)
  print
  print((x,y))
  
  plt.plot(x,y)
  plt.show()
