"""
Interactive Data Science
Final Projecft

User Social Network

"""

import sys
import random
import numpy as np
import collections
import copy

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def count_users(inf, outf):
    """
    """
    date = []
    date_review = collections.defaultdict(int)
    fans = collections.defaultdict(int)
    line = inf.readline()
    count = 0
    d_strings = set()
    to_write = []
    new_line = ""
    new_line = line[2:-2]
    new_line = new_line.split(',"')
    new_line = [new_line[8]]+new_line[2:4]
    for word in new_line:
        word = word.split(':')
        to_write += [word[0][:-1]]
    outf.write(",".join(to_write)+"\n")
    to_write = []
    while line:
        line = line[2:-2]
        line = line.split(',"')
        # slice the original data
        line = [line[8]]+line[2:4]
        to_write = []
        for word in line[::-1]:
            word = word.split('":')
            if len(word) != 2:
                to_write = []
                break
            if word[0] == "yelping_since":
                dates = word[1].split('-')
                d = dates[0]+dates[1]
                d = int(d[1:])
                d_str = month[int(dates[1])-1]+" "+dates[0][1:]
                #date.append(d_str)
                #d_strings.add(d_str)
                d_strings.add(d)
                date.append(d)

            elif word[0] == "review_count":
                date_review[d] += int(word[1])
                #date_review[d_str] += int(word[1])
            else:
                fans[d] += int(word[1])
                #fans[d_str] += int(word[1])
        line = inf.readline()
        if to_write == []:
            continue
        if sum(map(int, to_write[-4:])) == 0:
            continue
        count += 1
    Count = collections.Counter(date)
    d_strings = sorted(list(d_strings))
    d_strings = map(str, d_strings)
    for key in Count:
        #outf.write("new_users"+","+str(key)+","+str(Count[key])+"\n")
        outf.write(str(Count[key])+", ")
    outf.write("\n")
    print len(Count)
    for key in date_review:
        #outf.write("review_count"+","+str(key)+","+str(date_review[key])+"\n")
        outf.write(str(date_review[key])+", ")
    outf.write("\n")
    print len(date_review)
    for key in fans:
        #outf.write("fans_count"+","+str(key)+","+str(fans[key])+"\n")
        outf.write(str(fans[key])+", ")


    outf.write("\n\n")
    print len(fans)
    s = 0
    for key in Count:
        #outf.write("new_users"+","+str(key)+","+str(Count[key])+"\n")
        s += Count[key]
        outf.write(str(s)+", ")
    outf.write("\n")
    s = 0
    for key in date_review:
        #outf.write("review_count"+","+str(key)+","+str(date_review[key])+"\n")
        s += date_review[key]
        outf.write(str(s)+", ")
    outf.write("\n")
    return Count, date_review, fans


def generate(inf, outf):
    """
    write the json data to csv
    """
    line = inf.readline()
    count = 0
    to_write = []
    new_line = ""
    new_line = line[2:-2]
    new_line = new_line.split(',"')
    new_line = new_line[5:10]
    for word in new_line:
        word = word.split(':')
        to_write += [word[0][:-1]]
    to_write += "feature"
    outf.write(",".join(to_write)+"\n")
    to_write = []
    while line:
        line = line[2:-2]
        line = line.split(',"')
        # slice the original data
        line = line[5:9]
        to_write = []
        for word in line:
            word = word.split('":')
            if len(word) != 2:
                to_write = []
                break
            if word[1].isdigit() or word[0] == 'average_stars':
                to_write += [word[1]]
            elif word[0] == "friends":
                to_write += ["__befriend__".join(word[1][1:-1].split(', '))]
            else:
                to_write += [word[1][1:-1]]
        line = inf.readline()
        if to_write == []:
            continue
        if not to_write[-4].isdigit() or not to_write[-3].isdigit() or not to_write[-2].isdigit() or not to_write[-1].isdigit():
            continue
        if sum(map(int, to_write[-4:])) == 0:
            continue
        max_feature = max(to_write[-4:])
        if max_feature == to_write[-4]:
            to_write += ["fun"]
        elif max_feature == to_write[-3]:
            to_write += ["funny"]
        elif max_feature == to_write[-2]:
            to_write += ["cool"]
        else:
            to_write += ["usefuls"]
        count += 1
        outf.write(",".join(to_write)+'\n')
    return count

def transform_slice(inf, outf):
    """
    write the json data to csv
    """
    line = inf.readline()
    count = 0
    to_write = []
    new_line = ""
    new_line = line[2:-2]
    new_line = new_line.split(',"')
    new_line = new_line[:11]
    for word in new_line:
        word = word.split(':')
        to_write += [word[0][:-1]]
    outf.write(",".join(to_write)+"\n")
    to_write = []
    while line:
        line = line[2:-2]
        line = line.split(',"')
        # slice the original data
        line = line[:11]
        to_write = []
        for word in line:
            word = word.split('":')
            if len(word) != 2:
                to_write = []
                break
            if word[1].isdigit() or word[0] == 'average_stars':
                to_write += [word[1]]
            elif word[0] == "friends":
                to_write += ["__befriend__".join(word[1][1:-1].split(', '))]
            else:
                to_write += [word[1][1:-1]]
        line = inf.readline()
        if to_write == []:
            continue
        if sum(map(int, to_write[-6:-2])) == 0:
            continue
        count += 1
        outf.write(",".join(to_write)+'\n')
    return count

def main():
    inf = open("user.json", 'r')
    outf = open("user_count_number.csv", 'w')

    #print transform(inf, outf)
    print count_users(inf, outf)




if __name__ == '__main__':
    main()