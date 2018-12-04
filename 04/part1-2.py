import re
from enum import Enum

class EventType(Enum):
    Begin = 1
    Sleep = 2
    Wake  = 3

def parse_timestamp(line):
    pattern = re.compile("\[(?P<year>\d*)\-(?P<month>\d*)\-(?P<day>\d*)\s*(?P<hour>\d*):(?P<minute>\d*)\]")
    match = pattern.match(line)
    year = int(match.group("year"))
    month = int(match.group("month"))
    day = int(match.group("day"))
    hour = int(match.group("hour"))
    minute = int(match.group("minute"))
    return { "year": year, "month": month, "day": day, "hour": hour, "minute": minute }

def parse_event(line):
    if "wakes" in line:
        return {"type": EventType.Wake, "id": -1 }
    if "falls" in line:
        return {"type": EventType.Sleep, "id": -1 }

    pattern = re.compile(".*?\]\s*Guard #(?P<id>\d*)")
    match = pattern.match(line)
    id = int(match.group("id"))
    return {"type": EventType.Begin, "id": id }

with open("input.txt") as f:
    lines = f.readlines()

log = []
for line in lines:
    ev = parse_event(line)
    ts = parse_timestamp(line)
    log += [{"timestamp": ts, "event": ev }]

log.sort(key=lambda x: (x["timestamp"]["year"], x["timestamp"]["month"], x["timestamp"]["day"], x["timestamp"]["hour"], x["timestamp"]["minute"]))

guards = {}
current_id = -1
sleep_start = 0
for event in log:
    if event["event"]["type"] == EventType.Begin:
        current_id = event["event"]["id"]
        if current_id not in guards:
            guards[current_id] = [0 for i in range(60)]
    if event["event"]["type"] == EventType.Sleep:
        sleep_start = event["timestamp"]["minute"]
    if event["event"]["type"] == EventType.Wake:
        sleep_end = event["timestamp"]["minute"]
        for i in range(sleep_start, sleep_end):
            guards[current_id][i] += 1
# part 1
best_guard = max(guards, key=lambda x: sum(guards[x]))
best_minute = guards[best_guard].index(max(guards[best_guard]))

print(best_guard * best_minute)

#part 2
best_guard = max(guards, key=lambda x: max(guards[x]))
best_minute = guards[best_guard].index(max(guards[best_guard]))

print(best_guard * best_minute)