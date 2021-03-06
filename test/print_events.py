from conf.configuration import Configuration
from injection.schedule import Scheduler

if __name__ == "__main__":
    config = Configuration("config.json")
    config.load()
    sched = Scheduler()
    sched.load_injections(config.get_injections())

    ev = sched.next_event()
    while ev is not None:
        print(ev)
        ev = sched.next_event()