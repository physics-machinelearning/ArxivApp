import argparse

import pandas as pd
import arxiv

from db_tools import InteractArticle
from config import START, YESTARDAY, TODAY, CATEGORIES


def article_parser(START, END, categories):
    ida = InteractArticle()
    for category in categories:
        result_df = _article_parser_category(START, END, category)
        for index, row in result_df.iterrows():
            title = row['title']
            author = row['author']
            arxiv_url = row['arxiv_url']
            summary = row['summary']
            published = row['published']
            idb.insert_article(
                title, author, arixv_url, summary, published
            )
        idb.save_article()


def _article_parser_category(START, END, category):
    query = "cat:{} AND subittedDATE:[{} TO {}]".format(
        category, START, END
        )
    result = arxiv.query(query=query, sort_by='submittedDate')
    result_df = pd.io.json.json_normalize(result)
    return result_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_artument('arg1')
    args = parser.parse_args()

    if args.arg1 == 'all':
        article_parser(START, TODAY, CATEGORIES)
    elif args.arg1 == 'today':
        article_parser(YESTARDAY, TODAY, CATEGORIES)
    else:
        print('wrong argument')
