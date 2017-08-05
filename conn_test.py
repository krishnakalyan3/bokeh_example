#!/usr/bin/env python3

import psycopg2
import json
from os.path import join
import os


def config_reader(read_path):
    with open(read_path, 'r') as input_file:
        conf_file = json.load(input_file)

    return conf_file

if __name__ == '__main__':
    FILE = join('creds', 'login.json')
    DIR = os.getcwd()
    PATH = join(DIR, FILE)

    login_info = config_reader(PATH)

    conn_string = "host={} port={} dbname={} user={} password={}".format(login_info['host'],
                                                                         login_info['port'],
                                                                 login_info['dbname'],
                                                                 login_info['user'],
                                                                 login_info['password'])
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("select time, tag from perftest_2 where  algo_comp = 'multinomial_data-gen_none_dense_10k_100';")
    rows = cursor.fetchall()
    print(rows)
