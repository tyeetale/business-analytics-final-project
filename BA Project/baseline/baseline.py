import numpy as np 
import pandas as pd 

order = pd.read_csv('order_20200229.csv')
action = pd.read_csv('action_20200229.csv')

action_data = np.array(action)

for i in range(len(action_data)):
    if action_data[i, -1] == 0:
        # courier_id = action_data[i, 1]
        # wave_index = action_data[i, 2]
        tracking_id = action_data[i, 3]
        action = action_data[i, -2]
        print(i, tracking_id, action)
        if action == 'PICKUP':
            action_data[i, -1] = order.loc[order['tracking_id'] == tracking_id, 'estimate_pick_time'].item()
        else:
            action_data[i, -1] = order.loc[order['tracking_id'] == tracking_id, 'promise_deliver_time'].item()

out = pd.DataFrame(action_data)
out.to_csv('baseline_result.csv', index = False)