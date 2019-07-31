import time

CLOCKS = {}


def start(name: str):
    if name not in CLOCKS:
        CLOCKS[name] = {"total": 0, "start": time.time()}
    else:
        CLOCKS[name]["start"] = time.time()


def stop(name: str):
    CLOCKS[name]["total"] += time.time() - CLOCKS[name]["start"]


def result():
    # total = CLOCKS["total"]["total"]
    total = sum([clock["total"] for clock in CLOCKS.values()])
    for name, clock in CLOCKS.items():
        print(f"{name}: {clock['total'] / total}")
