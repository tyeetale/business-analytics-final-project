import numpy as np 
import pandas as pd 

order = pd.read_csv('order_20200229.csv')
action = pd.read_csv('action_20200229.csv')
courier = pd.read_csv('courier_20200229.csv')
distance = pd.read_csv('distance_20200229.csv')

action_data = np.array(action)


# len(action_data)
for i in range(len(action_data)-2, -1, -1):
# for i in range(len(action_data)-2, len(action_data)-10, -1):
    if action_data[i, -1] == 0:
        courier_id = action_data[i, 1]
        speed = courier.loc[courier['courier_id']==courier_id, 'speed'].item()
        wave_index = action_data[i, 2]
        tracking_id = action_data[i, 3]
        now_action = action_data[i, -2]
        print(i, speed, tracking_id, now_action)
        # estimate_pick_time = order.loc[order['tracking_id']==tracking_id, 'estimate_pick_time'].item()
        # the first in the wavw
        j = i+1
        next_courier_id = action_data[j, 1]
        next_wave_index = action_data[j, 2]
        next_tracking_id = action_data[j, 3]
        next_action = action_data[j, -2]
        if next_wave_index != wave_index or next_courier_id != courier_id:
            # start_time = order.loc[order['tracking_id']==tracking_id, 'estimate_pick_time'].item()
            # if now_action != "PICKUP":
            #     print('error1')
            # x = distance.loc[distance['tracking_id']==tracking_id]
            # y = x.loc[x['source_type']=='ASSIGN']
            # z = y.loc[y['target_tracking_id']==tracking_id]
            # grid_distance = z.loc[z['target_type']=="PICKUP", 'grid_distance'].item()
            end_time = order.loc[order['tracking_id'] == tracking_id, 'promise_deliver_time'].item()
            grid_distance = 0
        else:
            end_time = action_data[j, -1]
            x = distance.loc[distance['tracking_id']==tracking_id]
            y = x.loc[x['source_type']==now_action]
            z = y.loc[y['target_tracking_id']==next_tracking_id]
            grid_distance = z.loc[z['target_type']==next_action, 'grid_distance'].item()
        action_data[i, -1] = int(np.round(end_time - grid_distance/speed))                      

# print(action_data[:2, :])      




out = pd.DataFrame(action_data)
out.to_csv('reverse_baseline3_result.csv', index = False)