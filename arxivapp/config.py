import datetime

dt_now = datetime.datetime.now()
dt_yesterday = dt_now - datetime.timedelta(days=7)

START = '20100101'
TODAY = dt_now.strftime('%Y%m%d')
YESTERDAY = dt_yesterday.strftime('%Y%m%d')

CATEGORIES = {
    'Computer Science': ['cs.AI', 'cs.AR', 'cs.CC', 'cs.CE', 'cs.CG',
    'cs.CL', 'cs.CR', 'cs.CV', 'cs.CY'
    ],
    'Physics': [
        'astro-ph.CO', 'astro-ph.EP', 'astro-ph.GA', 'astro-ph.HE',
        'astro-ph.IM', 'astro-ph.SR'
    ]
}