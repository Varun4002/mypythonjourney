ep1 = {122 :45,
      123:68,
      566:90,
      543:23}

ep2 = {222:91,
       334:76,
       125:56}

ep1.update(ep2)
print(ep1)
ep1.pop(122)
print(ep1)

del ep1[566]
print(ep1)