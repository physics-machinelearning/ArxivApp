import argparse
import datetime

import pandas as pd
import arxiv

from db_tools import InteractArticle
from config import START, YESTERDAY, TODAY, CATEGORIES


def article_parser(START, END, categories):
    ia = InteractArticle()
    for category in categories:
        result_df = _article_parser_category(START, END, category)
        for index, row in result_df.iterrows():
            title = row['title']
            author = row['author']
            arxiv_url = row['arxiv_url']
            summary = row['summary']
            published = row['published']
            published = datetime.datetime.strptime(published, '%Y-%m-%dT%H:%M:%SZ')
            ia.insert_article(
                title, author, arxiv_url, summary, published, category
            )
        ia.save_article()


def _article_parser_category(START, END, category):
    query = "cat:{} AND submittedDate:[{} TO {}]".format(
        category, START, END
        )
    result = arxiv.query(query=query, sort_by='submittedDate')
    result_df = pd.io.json.json_normalize(result)
    return result_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1')
    args = parser.parse_args()

    if args.arg1 == 'all':
        article_parser(START, TODAY, CATEGORIES)
    elif args.arg1 == 'today':
        article_parser(YESTERDAY, TODAY, CATEGORIES)
    else:
        print('wrong argument')
