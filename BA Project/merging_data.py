import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

def read_data(file1, file2, file3, file4):
    action = pd.read_csv(file1)
    courier = pd.read_csv(file2)
    distance = pd.read_csv(file3)
    order = pd.read_csv(file4)
    return action, courier, distance, order

def merge_data(action, courier, diatance, order):
    action_and_courier = pd.merge(action[['courier_id', 'wave_index', 'tracking_id', 'action_type']], courier[['courier_id','speed','max_load']], on='courier_id', how = 'outer')
    print(action_and_courier.shape)
    action_courier_order = pd.merge(action_and_courier, order[['tracking_id', 'weather_grade', 'create_time', 'confirm_time', 'assigned_time', 'estimate_pick_time']], on='tracking_id', how = 'outer')
    print(action_courier_order.shape)
    action_courier_order_distance = pd.merge(action_courier_order, distance[['tracking_id', 'grid_distance']], on = 'tracking_id', how = 'outer')
    print(action_courier_order_distance.shape)
    return action_courier_order_distance

def real_action():
    pass

def check_line(data, i):
    print(data.loc[i])


if __name__ == "__main__":
    action, courier, distance, order = read_data('action_20200201.csv', 'courier_20200201.csv', 'distance_20200201.csv', 'order_20200201.csv')
    merged_data = merge_data(action, courier, distance, order)
    check_line(merged_data, 0)