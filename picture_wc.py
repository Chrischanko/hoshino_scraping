#青白くした星野源にwordcloudを適用し、よく使われている歌詞を出力
#hoshinoface_lyrics.pngが作成される
from PIL import Image
import numpy as np
import MeCab
from matplotlib import pyplot as plt
from wordcloud import WordCloud
# テキストファイル読み込み
with open('hoshino_kashi.txt', mode='rt', encoding='utf-8') as fi:
    source_text = fi.read()
# MeCabの準備
tagger = MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(source_text)
# 名詞を取り出す
word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type == '名詞':
        word_list.append(node.surface)
    node = node.next
 # リストを文字列に変換
 word_chain = ' '.join(word_list)
 #無意味そうな単語除去
 stop_words = ['そう', 'よう', 'もの', 'こと', 'まま', 'これ', 'それ']
 def get_wordcrowd_mask( word_chain, imgpath ):
    img_color = np.array(Image.open( imgpath ))
    wc = WordCloud(font_path='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
                   mask=img_color,
                   collocations=False, # 単語の重複しないように
                   stopwords=set(stop_words),
                   background_color='white',
                   contour_width=3,
                   contour_color='black'
                  ).generate( word_chain )
  # show
    plt.figure(figsize=(6,6), dpi=200, facecolor='white')
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
