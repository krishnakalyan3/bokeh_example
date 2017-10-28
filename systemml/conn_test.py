#!/usr/bin/env python3

import psycopg2
import json
from os.path import join
import os
import itertools

def config_reader(read_path):
    with open(read_path, 'r') as input_file:
        conf_file = json.load(input_file)

    return conf_file


def get_backends(cursor):
    cursor.execute("select distinct exec from perftest_2;")
    backends = list(itertools.chain(*cursor.fetchall()))
    return backends


def get_algos(cursor):
    cursor.execute("select distinct algo_comp from perftest_2;")
    algos = list(itertools.chain(*cursor.fetchall()))
    return algos


def get_release_time(cursor, backend, algo):
    print('######')
    print(backend)
    print(algo)
    print('#####')
    exec_string = "select time, tag from perftest_2 where algo_comp = '{}' and exec='{}';".format(algo, backend)
    print(exec_string)
    cursor.execute(exec_string)
    rows = cursor.fetchall()
    x = map(lambda x: x[1], rows)
    y = map(lambda x: float(x[0]), rows)
    return list(x), list(y)

def init_connection():
    DIR = os.getcwd()
    FILE = join('creds', 'login.json')
    PATH = join(DIR, FILE)
    login_info = config_reader(PATH)
    conn_string = "host={} port={} dbname={} user={} password={}".format(
    login_info['host'], login_info['port'], login_info['dbname'], login_info['user'], login_info['password'])
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    return cursor

if __name__ == '__main__':
    conn = init_connection()
    #backend = get_backends(conn)
    #algos = get_algos(conn)
    x, y = get_release_time(conn, 'singlenode', 'multinomial_data-gen_none_dense_10k_100')
    print(x)
    print(y)
