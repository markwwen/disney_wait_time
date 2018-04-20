import disney_api as api
import names
import time
import datetime
import influxdb
import os

def make_datas():
    datapoints = []
    for a in api.attractions():
        datapoint = {
            "measurement": "wait_minutes",
            "tags": {
                "name": a.name,
                "name_zh": names.translate(a.name),
            },
            "fields": {
                "value": a.wait_minutes,
            },
        }
        datapoints.append(datapoint)
        # print datapoint
    return datapoints


def get_influxdb():
    host = 'localhost'
    port = 8086
    user = 'root'
    password = os.environ['INFLUXDB_PWD']
    dbname = 'disney'

    db = influxdb.InfluxDBClient(host, port, user, password, dbname)
    db.create_database(dbname)
    return db


def crawl_one():
    db = get_influxdb()
    datapoints = make_datas()
    assert db.write_points(datapoints, database='disney', batch_size=50)

def crawl_loop():
    db = get_influxdb()
    while True:
        hour = datetime.datetime.now().hour
        if hour >= 7 and hour <= 20:
            datapoints = make_datas()
            assert db.write_points(datapoints, database='disney', batch_size=50)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(30)

if __name__ == '__main__':
    crawl_loop()