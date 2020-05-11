import numpy as np 
import pandas as pd 

order = pd.read_csv('order_20200229.csv')
action = pd.read_csv('action_20200229.csv')
courier = pd.read_csv('courier_20200229.csv')
distance = pd.read_csv('distance_20200229.csv')

action_data = np.array(action)


# len(action_data)
for i in range(len(action_data)):
    if action_data[i, -1] == 0:
        courier_id = action_data[i, 1]
        speed = courier.loc[courier['courier_id']==courier_id, 'speed'].item()
        wave_index = action_data[i, 2]
        tracking_id = action_data[i, 3]
        now_action = action_data[i, -2]
        print(i, speed, tracking_id, now_action)
        # estimate_pick_time = order.loc[order['tracking_id']==tracking_id, 'estimate_pick_time'].item()
        # the first in the wavw
        if i == 0:
            if now_action != "PICKUP":
                print('error1')
            x = distance.loc[distance['tracking_id']==tracking_id]
            # print(x)
            y = x.loc[x['source_type']=='ASSIGN']
            # print(y)
            z = y.loc[y['target_tracking_id']==tracking_id]
            # print(z)
            w = z.loc[z['target_type']=="PICKUP"]
            # print(w)
            grid_distance = w['grid_distance'].item()
        else:
            j = i-1
            previous_courier_id = action_data[j, 1]
            previous_wave_index = action_data[j, 2]
            previous_tracking_id = action_data[j, 3]
            previous_action = action_data[j, -2]
            if previous_wave_index != wave_index or previous_courier_id != courier_id:
                if now_action != "PICKUP":
                    print('error1')
                x = distance.loc[distance['tracking_id']==tracking_id]
                y = x.loc[x['source_type']=='ASSIGN']
                z = y.loc[y['target_tracking_id']==tracking_id]
                grid_distance = z.loc[z['target_type']=="PICKUP", 'grid_distance'].item()
            else:
                x = distance.loc[distance['tracking_id']==previous_tracking_id]
                y = x.loc[x['source_type']==previous_action]
                z = y.loc[y['target_tracking_id']==tracking_id]
                grid_distance = z.loc[z['target_type']==now_action, 'grid_distance'].item()
        action_data[i, -1] = int(np.round(estimate_pick_time + grid_distance/speed))                      

# print(action_data[:2, :])      




out = pd.DataFrame(action_data)
out.to_csv('baseline2_result.csv', index = False)