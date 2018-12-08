"""
Interactive Data Science
Final Projecft

User Social Network


data:
user_id,name,review_count,yelping_since,friends,useful,funny,cool,fans,average_stars


"""

import sys
import random
import numpy as np
import collections
import copy
import json
import math

colors = ["#e67e22", "#f1c40f", "#1abc9c", "#2980b9", "#9b59b6", "#e74c3c"]
N = 700
def read_write_node(inf, json_to_write):
    """
    write the json data to csv
    """
    users = dict()
    users_id = set()
    line = inf.readline()
    cnt = 0
    line = inf.readline()
    not_valid = 0
    values = []
    while line:
        line = line.split(',')
        if len(line) != 11:
            line = inf.readline()
            not_valid += 1
            continue
        new_user = dict()
        node = dict()

        new_user["id"] = line[0]
        new_user["index"] = cnt
        new_user["name"] = line[1]
        new_user["review_count"] = int(line[2])
        if int(line[2]) < N:
            line = inf.readline()
            not_valid += 1
            continue
        new_user["yelping_since"] = line[3]
        if line[4] == 'None':
            new_user["friends"] = []
        else:
            new_user["friends"] = line[4].split('__befriend__')

        new_user["feature"] = map(float, line[-6:-2])
        new_user["feature"] += [float(line[-1])]

        node["name"] = new_user["name"]

        # review count
        values.append(new_user["review_count"])

        if int(line[2]) > 1200:
            node["value"] = math.exp(5)
        else:
            node["value"] = 1
        node["color"] = colors[new_user["review_count"]%6]


        json_to_write["nodes"].append(node)
        users[new_user["id"]] = new_user
        users_id.add(line[0])

        line = inf.readline()
        cnt += 1
    valuef = open("values.txt", 'w')
    valuef.write("\n".join(map(str, sorted(values))))
    print cnt
    print not_valid
    return users, users_id

def write_link(users, users_id, json_to_write):
    """
    """
    not_found = 0
    s = 0
    for user_id in users:
        user = users[user_id]
        source_index = user["index"]
        for friend_id in user["friends"]:
            s += 1
            if friend_id not in users_id:
                not_found += 1
                continue
            target_index = users[friend_id]["index"]
            link = dict()
            link["source"] = source_index
            link["target"] = target_index

            # [TODO]
            link["value"] = 1
            json_to_write["links"].append(link)
    print "not found: "+str(not_found)
    print "s: "+str(s)
    return


def main():
    inf = open("user_slice.csv", 'r')
    outf = open("user_graph_small.json", 'w')
    json_to_write = dict()
    json_to_write["nodes"] = []
    json_to_write["links"] = []
    users, users_id = read_write_node(inf, json_to_write)
    write_link(users, users_id, json_to_write)
    json_str = json.dumps(json_to_write)
    outf.write(json_str)
    return





if __name__ == '__main__':
    main()