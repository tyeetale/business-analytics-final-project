
import numpy as np 
import pandas as pd 

order = pd.read_csv('order_20200229.csv')
action = pd.read_csv('action_20200229.csv')
courier = pd.read_csv('courier_20200229.csv')
distance = pd.read_csv('distance_20200229.csv')

action_data = np.array(action)
l = [0,0]
a = [0,0]
b = [0,0]
pick = []
deliver = []
for i in range(len(action_data)):
    courier_id = action_data[i, 1]
    # print(courier_id)
    # print(courier.loc[courier['courier_id']==courier_id])
    speed = courier.loc[courier['courier_id']==courier_id, 'speed'].item()
    wave_index = action_data[i, 2]
    tracking_id = action_data[i, 3]
    now_action = action_data[i, -2]

    e = action.loc[action['tracking_id']==tracking_id]
    expect_time = e.loc[e['action_type']=='PICKUP', 'expect_time'].item()
    if expect_time != 0:
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

# [3338, 3401] [6721, 18]
# [165.25810484951327, 547.4815575600608]
