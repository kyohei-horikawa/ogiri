import collections
from termextract import japanese_plaintext
from termextract import core

# ファイルを読み込む
text = open("sample.txt", "r", encoding="utf-8").read()

# 複合語を抽出し、重要度を算出
frequency = japanese_plaintext.cmp_noun_dict(text)
LR = core.score_lr(frequency,
                   ignore_words=japanese_plaintext.IGNORE_WORDS,
                   lr_mode=1, average_rate=1
                   )
term_imp = core.term_importance(frequency, LR)

# 重要度が高い順に並べ替えて出力
data_collection = collections.Counter(term_imp)
for cmp_noun, value in data_collection.most_common():
    print(core.modify_agglutinative_lang(cmp_noun), value, sep="\t")
