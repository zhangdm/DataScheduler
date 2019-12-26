
# 运行方式

- 运行某一天

```bash
bash /data/DataScheduler/scheduler/scheduler.sh 2019-12-26

```

- 运行某一段时间


```bash
bash /data/DataScheduler/scheduler/set_days_run.sh 2019-10-01 2019-12-26

```

- 日常调度

```bash
bash /data/DataScheduler/scheduler/scheduler.sh $(date -d '-1 days' +%Y-%m-%d)

```


- 日志

日志打印在logs下，格式为run_运行时间，如run_2019-12-26.log