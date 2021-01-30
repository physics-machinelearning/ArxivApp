import datetime

dt_now = datetime.datetime.now()
dt_yesterday = dt_now - datetime.timedelta(days=1)

START = '20100101'
TODAY = dt_now.strftime('%Y%m%d')
YESTERDAY = dt_yesterday.strftime('%Y%m%d')

CATEGORIES = [
    'cs.AI', 'cs.AR', 'cs.CC', 'cs.CE', 'cs.CG', 'cs.CL',
    'cs.CR', 'cs.CV', 'cs.CY'
]