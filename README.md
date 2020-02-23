# Adjust test tasks

1. Please write a simple CLI application in the language of your choice that does the following:
    - Print the numbers from 1 to 10 in random order to the terminal.
    - Please provide a README, that explains detailed how to run the program on MacOS and Linux.
2. Imagine a server with the following specs:
    - 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
    - 64GB of ram
    - 2 tb HDD disk space
    - 2 x 10Gbit/s nics
    The server is used for SSL offloading and proxies around 25000 requests per second.
    Please let us know which metrics are interesting to monitor in that specific case and how would you do that? What are the challenges of monitoring this?
    Also, some information was added by request:
    - the server is using Haproxy.
    - switches assume: Arista 7060CX2-32S
    - network cards assume: Intel Corporation Ethernet Controller 10-Gigabit X540-AT2
    - firewall assume: Cisco ASA 5515-X


## Coding part

For installing and executing this project you need to have python >3.5 installed.

### Installation
```sh
~ pip install pip install git+https://github.com/beastea/adjust_test_task.git
```
### Execution
```sh
randomizer
```
Will return you something like
```sh
~ 7 10 1 4 9 6 5 3 2 8
```

## Theoretical questions part

Some very highly structured thought on what ideally should(could) be monitored (or where data(metrics) could be taken from for the monitoring purposes).

1. Firewall
   1. Bandtwidth monitoring
   2. RAM+CPU+SSD(health+space) usage on device
   3. Number of connections per second
   4. Queues fullfilment, errors, collisions, drops
   5. Packet loss, round trip average
2. Switch
   1. Latency
   2. Packet Buffer Memory
   3. CPU+RAM+Temperature
   4. Port monitoring(utilization, packets loss)
   5. RTT,RTA
3. Network Card
   1. ethtool -S (should look for values with “drop”, “buffer”, “miss”, etc in the label)
   2. or sysfs (e.g `cat /sys/class/net/eth0/statistics/rx_dropped`, counter values will be split into files like `collisions`, `rx_dropped`, `rx_errors`, `rx_missed_errors`, etc.)
   3. `/proc/net/dev`
   4. Monitoring `/proc/softirqs` (give you an idea of how your network receive (NET_RX) processing is currently distributed across your CPUs)
   5. Check hardware interrupt stats `/proc/interrupts`.
   6. IP protocol statistics `/proc/net/snmp` + `/proc/net/netstat`.
   7. UDP protocol statistics `/proc/net/snmp` + `/proc/net/udp`
4. HaProxy
   1. Frontend
      1. `req_rate` - requests per second
      2. `rate` - sessions created per second
      3. `session utilization` - sessions used
      4. `ereq` - request errors
      5. `dreq` - denied requests (ACL)
      6. `hrsp_4xx` - client errors
      7. `hrsp_5xx` - server errors
      8. `bin` - bytes received
      9. `bout` - bytes sent
   2. Backend
      1. `rtime` - backend response time (in ms) for the last 1024 requests
      2. `econ` - requests that encountered an error attempting to connect to a backend server
      3. `dresp` - responses denied (ACL)
      4. `eresp` - requests whose responses yielded an error
      5. `qcur` - number of requests unassigned in queue
      6. `qtime` - time spent in queue (in ms) for the last 1,024 requests
      7. `wredis` - times a request was redispatched to a different backend
      8. `wretr` - times a connection was retried
   3. Health
      1. `check` directive in config knows how to check(monitor) from L2 to L7 so you can monitor the availability not port only but http session to your app.

Gathering this metrics could be achieved in any way from gathering data with snmp OIDs and up to agent-based or prometheus-like exporter. The exact technology doesn't bring a lot of sense here.
