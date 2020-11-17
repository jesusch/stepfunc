def fanout(event, context):
    jobs = []
    for i in range(0,100):
        jobs.append({'job': i})
    return jobs

def mapJob(event:dict, context):
    event['result'] = True
    return event

def fanin(event, context):
    for job in event:
        if not job['result']:
            print(error)

if __name__ == "__main__":
    res = []
    for job in fanout(None,None):
        res.append(mapJob(job, None))
    fanin(res, None)
