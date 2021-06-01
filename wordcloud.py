#スクレイピングした歌詞をwordcloudに適用し、hoshino_lyrics.pngを作成
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
stop_words = ['そう', 'よう', 'もの', 'こと', 'まま']
 # ワードクラウド作成
W = WordCloud(font_path='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
              width=640, height=480,
              background_color='white',
              colormap='bone',
              stopwords=set(stop_words)).generate(word_chain)

plt.imshow(W)
plt.axis('off')
plt.show()
