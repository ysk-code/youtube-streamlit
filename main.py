import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# st.title('Streamlit超入門')

# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# rand関数:正規分布を表すように乱数を生成する

# st.write(df)
# dataframeの方は引数を入れることができる
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0)) 行のmax値をハイライトする(pandasの機能)
# st.table(df.style.highlight_max(axis=0))

# # 以下マジックコマンド
# """
# # 章
# ## 節
# ### 項

# '''python
# import streamlit as st
# import numpy as np
# import pandas as pd
# '''
# """

# 以下チャート
# チャート基本
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# マットプロット
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

# 画像の表示

# st.title('Streamlit超入門')

# st.write('Display Image')

# img = Image.open('5apple.png')
# st.image(img, caption='5apples', use_column_width=True)
# _________________________________________________________
# 10_インタラクティブなウィジェット
# インタラクティブ=双方向に作用するもの

st.title('Streamlit超入門')

# st.write('Display Image')

# チェックボックス ありがTrue
# if st.checkbox('Show Image'):
#     img = Image.open('5apple.png')
#     st.image(img, caption='5apples', use_column_width=True)

# セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えてください.',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は、', option, 'です.'

# テキスト入力
# st.write('Interactive Widgets')

# # text = st.sidebar.text_input('あなたの趣味を教えてください')

# # 'あなたの趣味:', text

# # condition = st.sidebar.slider('あなたの今の調子は？', 0 ,100, 50)
# # 'コンディション:', condition
# ___________________________________________________
# 11_レイアウトを整える

# サイドバー
# st.write('Interactive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えてください')

# 'あなたの趣味:', text

# condition = st.sidebar.slider('あなたの今の調子は？', 0 ,100, 50)
# 'コンディション:', condition

# 2カラム

# st.write('Interactive Widgets')

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# エクスパンダー
# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')



# text = st.text_input('あなたの趣味を教えてください')

# 'あなたの趣味:', text

# condition = st.slider('あなたの今の調子は？', 0 ,100, 50)
# 'コンディション:', condition

# 12_プログレスバー

# st.write('プログレスバーの表示')
# 'Start!!'

# lastest_iteration = st.empty()
# bar = st.progress(0)


# for i in range(100):
#     lastest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)

# 'Done!!'

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# # エクスパンダー
# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')

# 13_Webアプリの公開

# 公開に必要なもの
# ・SteamShareの登録
# ・git
# ・


st.write('プログレスバーの表示')
'Start!!'

lastest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    lastest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# エクスパンダー
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
