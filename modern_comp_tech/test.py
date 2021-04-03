# Предсказание пользовательской оценки отеля по тексту отзыва."
#"Мы собрали для вас отзывы по 1500 отелям из совершенно разных уголков мира. Что это за отели - секрет. Вам дан текст отзыва и пользовательская оценка отеля. 
# Ваша задача - научиться предсказывать оценку отеля по отзыву. Данные можно скачать (https://www.kaggle.com/c/hseds-texts-2020/data?select=train.csv
#  https://lh3.googleusercontent.com/a-/AOh14GgpsnUkWVfGko3j2nk8x35nG1-BYBW-eXEO56LN=s64
from google.colab import drive
drive.mount('/content/drive') 
# ["Главная метрика - Mean Absolute Error (MAE). Во всех частях домашней работы вам нужно получить значение MAE не превышающее 1. 
# В противном случае мы будем вынуждены не засчитать задание :( "]}, {"cell_type": "markdown", "metadata": {"id": "zhxSoae5HzQJ"}, "source": [
# "Для измерения качества вашей модели используйте разбиение данных на train и test и замеряйте качество на тестовой части."]}, 
#  ["#### Про данные:\n", "Каждое ревью состоит из двух текстов: positive и negative - плюсы и минусы отеля. 
# В столбце score находится оценка пользователя - вещественное число 0 до 10. Вам нужно извлечь признаки из этих текстов и предсказать по ним оценку.
# ["#### Использовать внешние данные для обучения строго запрещено. Можно использовать предобученные модели из torchvision."]}
#  "https://lh3.googleusercontent.com/a-/AOh14GgpsnUkWVfGko3j2nk8x35nG1-BYBW-eXEO56LN=s64",
PATH_TO_TRAIN_DATA = 'hseds-texts-2020/train.csv'
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/train-2.csv')
df.head()
import string
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
def process_text(text):
    return [word for word in word_tokenize(text.lower()) 
        if word not in string.punctuation]
    ['negative'] = df['negative'].apply(process_text)
    ['positive'] = df['positive'].apply(process_text) 

from sklearn.model_selection import train_test_split

#"Обучите логистическую регрессию на TF-IDF векторах текстов."]},
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
#Обучите логистическую регрессию на усредненных Word2Vec векторах.
#Усредняя w2v вектора, мы предполагаем, что каждое слово имеет равноценный вклад в смысл предложения, однако это может быть не совсем так. Теперь попробуйте воспользоваться другой концепцией и перевзвесить слова при получении итогового эмбеддинга текста. В качестве весов используйте IDF (Inverse document frequency)
# Проведите эксперименты с размерностью эмбеддинга. Для каждого из двух методов постройте график зависимости качества модели от размерности эмбеддинга.
# Сделайте выводы:
# "Теперь попробуйте обучить логистическую регрессию на любых других эмбеддингах размерности 300 и сравните качество с Word2Vec.\n", 
# # Выводы:
# "Теперь давайте воспользуемся более продвинутыми методами обработки текстовых данных, которые мы проходили в нашем курсе. Обучите RNN/Transformer для предсказания пользовательской оценки. 
# Получите ошибку меньше, чем во всех вышеперечисленных методах.
# "Если будете обучать RNN, попробуйте ограничить максимальную длину предложения. Некоторые отзывы могут быть слишком длинные относительно остальных.\n", 
# "Чтобы пользоваться DataLoader, все его элементы должны быть одинаковой размерности. Для этого вы можете добавить нулевой паддинг ко всем предложениям (см пример 
import torch
from torch import nn
from torch.nn import functional as F
WORDS = set()
for sent in list(df['positive']):
    for w in sent:
        WORDS.add(w)
        for sent in list(df['negative']):
            for w in sent:
                WORDS.add(w)
                int2word = dict(enumerate(tuple(WORDS)))
                word2int = {w: ii for ii, w in int2word.items()}
                MAX_LEN = max(max(df['positive'].apply(len)), max(df['negative'].apply(len)))
                MAX_LEN


from torch.nn.utils.rnn import pad_sequence
train_pos_pad = pad_sequence([torch.as_tensor([word2int[w] for w in seq][:MAX_LEN]) for seq in df_train['positive']]
batch_first=True)
class ReviewsDataset(torch.utils.data.Dataset):
    def __init__(self, df):
        
    def __len__(self):
    
    
    def __getitem__(self, idx):
        
        BATCH_SIZE = 1
        
        
train_dataset = ReviewsDataset(df_train)
test_dataset = ReviewsDataset(df_test)
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=BATCH_SIZE)
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=BATCH_SIZE)
NUM_EPOCHS = 1
for n in range(NUM_EPOCHS):
    model.train()
# Бонус. 10 баллов"Побейте качество 0.75 в [соревновании](https://www.kaggle.com/c/hseds-texts-2020/leaderboard). 
# Можете воспользоваться вышеперечисленными методами или попробовать что-нибудь еще.