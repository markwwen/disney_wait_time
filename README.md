# Wait_Disney (等迪)

## What is this ?

Todo

## Installation

1. install influxdb
2. install grafana

```bash
$ git clone git://github.com/gtt116/wait4disney
$ cd wait_disney
$ pip install -r requirements.txt
$ python main.py
```
The influxdb configration was hard coded at main.py, please feel free to change
them to meet your environment.

You can setup a crontab job to update disney waiting queue every minute.
The grafana dashboard template locates at `wait4disney/doc/grafana.json`, you can
import it to give a try.

## Web Snapshot

![wait](./doc/demo_new.png)
