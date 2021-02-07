import datetime

dt_now = datetime.datetime.now()
dt_yesterday = dt_now - datetime.timedelta(days=7)

START = '20100101'
TODAY = dt_now.strftime('%Y%m%d')
YESTERDAY = dt_yesterday.strftime('%Y%m%d')

CATEGORIES = {
    'Astrophysics': [
        'astro-ph', 'astro-ph.CO', 'astro-ph.EP', 'astro-ph.GA'
        'astro-ph.HE', 'astro-ph.IM', 'astro-ph.SR'
    ],
    'Condensed Matter': [
        'cond-mat.dis-nn', 'cond-mat.mes-hall', 'cond-mat.mtrl-sci', 'cond-mat.other',
        'cond-mat.quant-gas', 'cond-mat.soft', 'cond-mat.stat-mech', 'cond-mat.str-el'
        'cond-mat.supr-con'
    ],
    'Computer Science': [
        'cs.AI', 'cs.AR', 'cs.CC', 'cs.CE', 'cs.CG',
        'cs.CL', 'cs.CR', 'cs.CV', 'cs.CY', 'cs.DB', 'cs.DC', 'cs.DL',
        'cs.DM', 'cs.DS', 'cs.ET', 'cs.FL', 'cs.GL', 'cs.GR', 'cs.GT',
        'cs.HC', 'cs.IR', 'cs.IT', 'cs.LG', 'cs.LO', 'cs.MA', 'cs.MM',
        'cs.MS', 'cs.NA', 'cs.NE', 'cs.NI', 'cs.OH', 'cs.OS', 'cs.PF',
        'cs.PL', 'cs.RO', 'cs.SC', 'cs.SD', 'cs.SE', 'cs.SI', 'cs.SY'
    ],
    'Economics': ['econ.EM'],
    'Signal Processing': [
        'eess.AS', 'eess.IV', 'eess.SP'
    ],
    'Physics': [
        'gr-qc', 'hep-ex', 'hep-lat', 'hep-ph', 'hep-th',
        'physics.acc-ph', 'physics.ao-ph', 'physics.app-ph', 'physics.atm-clus',
        'physics.atom-ph', 'physics.bio-ph', 'physics.chem-ph', 'physics.class-ph',
        'physics.comp-ph', 'physics.data-an', 'physics.ed-ph', 'physics.flu-dyn',
        'physics.gen-ph', 'physics.geo-ph', 'physics.hist-ph', 'physics.ins-det,',
        'physics.med-ph', 'physics.optics', 'physics.plasm-ph', 'physics.pop-ph',
        'physics.soc-ph', 'physics.space-ph', 'quant-ph',
    ],
    'Math': [
        'math.AC', 'math.AG', 'math.AP', 'math.AT', 'math.CA',
        'math.CO', 'math.CT', 'math.CV', 'math.DG', 'math.DS',
        'math.FA', 'math.GM', 'math.GN', 'math.GR', 'math.GT',
        'math.HO', 'math.IT', 'math.KT', 'math.LO', 'math.MG',
        'math.MP', 'math.NA', 'math.NT', 'math.OA', 'math.OC',
        'math.PR', 'math.QA', 'math.RA', 'math.RT', 'math.SG',
        'math.SP', 'math.ST', 'math-ph
    ],
    'Nonlinear Sciences': [
        'nlin.AO', 'nlin.CD', 'nlin.CG', 'nlin.PS', 'nlin.SI'
    ],
    'Nucliear Experiment': [
        'nucl-ex', 'nucl-th'
    ],
    'Quantitative Biology': [
        'q-bio.BM', 'q-bio.CB', 'q-bio.GN', 'q-bio.MN', 'q-bio.NC', 'q-bio.OT',
        'q-bio.PE', 'q-bio.QM', 'q-bio.SC', 'q-bio.TO'
    ],
    'Quantitative Finance': [
        'q-fin.CP', 'q-fin.EC', 'q-fin.GN', 'q-fin.MF', 'q-fin.PM',
        'q-fin.PR', 'q-fin.RM', 'q-fin.ST', 'q-fin.TR'
    ],
    'Statistics': [
        'stat.AP', 'stat.CO', 'stat.ME', 'stat.ML', 'stat.OT', 'stat.TH'
    ],
}