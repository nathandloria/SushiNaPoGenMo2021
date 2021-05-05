import re
import random
import news_scraper as ns
import pos_tokenizer as tok

def filter_chars_and_normalize(str_data: str):
    pattern = re.compile(r"\W+")
    return pattern.sub(" ", str_data).lower()

def main():
    search_term = input("Please enter the desired search term: ")
    results = ns.get_search_results(search_term)
    cont = []
    pos = {}

    for x in results:
        cont += ns.scrape_article(f"https://{x['link']}")

    for s in cont:
        tok_res = tok.pos_tokenize(filter_chars_and_normalize(s))[0]
        if len(pos) == 0:
            pos = tok_res
        else:
            for x in tok_res:
                try:
                    for el in tok_res[x]:
                        if el not in pos[x]:
                            pos[x].append(el)
                except:
                    pos[x] = tok_res[x]

    print(f"\n+---+ Your poem from the news surrounding {search_term} +---+")
    print(
        f"\n{random.choice(pos['DT']).capitalize()} {random.choice(pos['NN'])}.\n{random.choice(pos['JJ']).capitalize()} {random.choice(pos['CC'])} {random.choice(pos['JJ'])}.\n{random.choice(pos['VB']).capitalize()} {random.choice(pos['CC'])} {random.choice(pos['VB'])}.\n{random.choice(pos['RB']).capitalize()}.\n{random.choice(pos['NN']).capitalize()}."
    )


main()
