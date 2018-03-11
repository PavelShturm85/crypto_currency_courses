from redis import Redis
from rq_scheduler import Scheduler
from datetime import datetime
from tasks import save_exchange_rates

redis_conn = Redis()
scheduler = Scheduler(connection=redis_conn) 

scheduler.schedule(
    datetime.utcnow(),
    save_exchange_rates, 
    interval=10,                  
    repeat=None,                    
)