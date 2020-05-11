import numpy as np 
import pandas as pd 

order = pd.read_csv('order_20200228.csv')
action = pd.read_csv('action_20200228.csv')
courier = pd.read_csv('courier_20200228.csv')
distance = pd.read_csv('distance_20200228.csv')

action_data = np.array(action)
l = [0,0]
a = [0,0]
b = [0,0]
pick = []
deliver = []
for i in range(len(action_data)):
    courier_id = action_data[i, 0]
    speed = courier.loc[courier['courier_id']==courier_id, 'speed'].item()
    wave_index = action_data[i, 1]
    tracking_id = action_data[i, 2]
    now_action = action_data[i, -2]

    e = action.loc[action['tracking_id']==tracking_id]
    expect_time = e.loc[e['action_type']=='PICKUP', 'expect_time'].item()
    print(i, expect_time, tracking_id)
    if now_action == 'PICKUP':
        estimate_pick_time = order.loc[order['tracking_id']==tracking_id, 'estimate_pick_time'].item()
        pick.append(expect_time - estimate_pick_time)
        l[0] += expect_time - estimate_pick_time
        if expect_time <= estimate_pick_time:
            a[0] += 1
        else:
            a[1] += 1
    else:
        promise_deliver_time = order.loc[order['tracking_id']==tracking_id, 'promise_deliver_time'].item()
        deliver.append(promise_deliver_time - expect_time)
        l[1] += promise_deliver_time - expect_time
        if expect_time <= promise_deliver_time:
            b[0] += 1
        else:
            b[1] += 1

l[0] /= len(action_data)
l[1] /= len(action_data)
print(pick)
print(deliver)
print(a, b)
print(l)






# import numpy as np

# #   estimate_pick_time  promise_deliver_time
# l1=[364.93819434678664, 877.0803684432569]
# l2=[419.7312018584179, 933.492052818193]
# l3=[276.09637561779243, 855.322556287754]
# l4=[495.70057840616965, 823.3314910025707]
# l5=[458.51756499682944, 909.821623335447]
# l6=[469.5477013021525, 905.644499069891]
# l7=[588.1756921575802, 866.6048298572997]
# l8=[819.39175856065, 864.3804991294254]
# l9=[630.0856820073731, 1099.208823879177]
# l10=[374.5370245329732, 1041.7071235651588]
# l11=[482.6857755303946, 1006.2636033857316]
# l12=[376.95839193624005, 1010.4096929207689]
# l13=[532.1939000347907, 980.0244694421895]
# l14=[536.9625153625564, 1192.3890482042877]
# l15=[408.98075877812806, 1043.422926405044]
# l16=[416.6010783082077, 1048.2478538525963]
# l17=[395.8933756805808, 1005.8259729784231]
# l18=[365.4246746987952, 982.9475662650602]
# l19=[406.7849255880941, 1001.729332693231]
# l20=[389.5541185103651, 953.8216382315171]
# l21=[329.26040464992457, 952.4147218031768]
# l22=[374.3490078018996, 970.1624406377205]
# l23=[318.9284716157205, 969.0897816593887]
# l24=[335.70363669259996, 937.0886104577528]
# l25=[284.54453650958055, 923.329147246677]
# l26=[254.35557095823947, 923.8357736960666]
# l27=[272.26331409057644, 917.8893405967965]
# l28=[373.83795351028743, 883.9548452960578]
# X = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28]
# l = [0,0]
# f = []
# for i in range(1, 29):
#     l[0] += X[i-1][0]
#     f.append(X[i-1][0])
# print(l[0]/28)
# f.sort()
# print(f)
# del f[0]
# del f[0]
# del f[-1]
# del f[-1]
# print(np.mean(f))