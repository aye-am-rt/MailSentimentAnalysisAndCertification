import os
import string
import sys
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer


class AnalyzedSentence:
    def __init__(self, sent, polarity, isAppriciatory):
        self.polarity = polarity
        self.sentence = sent
        self.isAppreciatory = isAppriciatory

    def check_sentiment(self):
        if self.polarity > 0.05:
            return 1
        elif -0.05 <= self.polarity <= 0.05:
            return 0
        else:
            return -1


stop_words = {'their', 'then', 'not', 'ma', 'here', 'other', 'won', 'up', 'weren', 'being', 'we', 'those', 'an', 'them',
              'which', 'him', 'so', 'yourselves', 'what', 'own', 'has', 'should', 'above', 'in', 'myself', 'against',
              'that', 'before', 't', 'just', 'into', 'about', 'most', 'd', 'where', 'our', 'or', 'such', 'ours', 'of',
              'doesn', 'further', 'needn', 'now', 'some', 'too', 'hasn', 'more', 'the', 'yours', 'her', 'below', 'same',
              'how', 'very', 'is', 'did', 'you', 'his', 'when', 'few', 'does', 'down', 'yourself', 'i', 'do', 'both',
              'shan', 'have', 'itself', 'shouldn', 'through', 'themselves', 'o', 'didn', 've', 'm', 'off', 'out', 'but',
              'and', 'doing', 'any', 'nor', 'over', 'had', 'because', 'himself', 'theirs', 'me', 'by', 'she', 'whom',
              'hers', 're', 'hadn', 'who', 'he', 'my', 'if', 'will', 'are', 'why', 'from', 'am', 'with', 'been', 'its',
              'ourselves', 'ain', 'couldn', 'a', 'aren', 'under', 'll', 'on', 'y', 'can', 'they', 'than', 'after',
              'wouldn', 'each', 'once', 'mightn', 'for', 'this', 'these', 's', 'only', 'haven', 'having', 'all', 'don',
              'it', 'there', 'until', 'again', 'to', 'while', 'be', 'no', 'during', 'herself', 'as', 'mustn', 'between',
              'was', 'at', 'your', 'were', 'isn', 'wasn'}

l1 = ["admire", "accomplish", "accomplishment", "achievement", "achievement", "appealing", "attractive", "awesome",
      "beautiful", "bravo", "brilliant", "beneficial", "charming", "creative", "champion", "delightful", "delight",
      "ecstatic", "effective", "efficient", "electrifying", "encouraging", "enthusiastic", "exciting", "excellent",
      "exquisite"]
l2 = ["fabulous", "fantastic", "genius", "glamorous", "happy", "honored", "impressive", "imaginative", "innovate",
      "innovative",
      "congratulation", "intelligent", "inventive", "legendary", "lovely", "marvelous", "masterful", "miraculous",
      "motivating"]
l3 = ["productive", "prominent", "proud", "quality", "reassuring", "reliable", "remarkable", "respected", "reward",
      "robust",
      "satisfactory", "skilled", "skillful", "stunning", "special", "sparkling", "success", "successful", "super",
      "superb"]
l4 = ["thank", "helpful", "indebted", "thanks", "appreciate", "inspiration", "grateful", "great", "novel", "optimistic",
      "perfect", "phenomenal", "pleasant", "positive", "powerful", "terrific", "thrilling", "transforming", "unreal",
      "outstanding", "valued", "vibrant", "victorious", "victory", "vital", "well", "wonderful", "wow"]

lemmatizer = WordNetLemmatizer()
os.chdir('../../../../../resources')


def read_and_analyze():
    count_neg_Nonappr = listOfAnalyzedObjects = count_pos_appr = count_neg_appr = count_pos_Nonappr = count_neutral_sentence = count_positive_sentence = count_negative_sentence = 0
    try:
        lineList = []
        listOfAnalyzedObjects = []
        f = open('appreciate.txt')
        line = f.readline()
        while line:
            line = line.strip('\n')
            if len(str(line)) > 1:
                lineList.append(line)
            line = f.readline()
        f.close()
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    print("*******************************************")
    print(lineList)

    for eachLine in lineList:

        print(eachLine)
        sentenceList = sent_tokenize(eachLine)
        print("sentenceList in line  ###########  " + str(sentenceList))
        for sentence in sentenceList:
            isAppreciatory = False
            filtered_sent = []
            analysis = TextBlob(sentence)
            print(analysis.sentiment_assessments)
            sentence = str(sentence).lower().translate(str.maketrans('', '', string.punctuation))
            tokenized_words = word_tokenize(sentence)
            for w in tokenized_words:
                if w not in stop_words:
                    filtered_sent.append(w)

            for word in filtered_sent:
                word = lemmatizer.lemmatize(str(word))
                if word in l1 or word in l2 or word in l3 or word in l4:
                    isAppreciatory = True
                    break

            analyzedSentence = AnalyzedSentence(sentence, analysis.sentiment.polarity, isAppreciatory)
            listOfAnalyzedObjects.append(analyzedSentence)

    for obj in listOfAnalyzedObjects:
        if obj.check_sentiment() == 1 and obj.isAppreciatory:
            count_pos_appr += 1
        elif obj.check_sentiment() == -1 and obj.isAppreciatory:
            count_neg_appr += 1
        elif obj.check_sentiment() == 1 and not obj.isAppreciatory:
            count_pos_Nonappr += 1
        elif obj.check_sentiment() == -1 and not obj.isAppreciatory:
            count_neg_Nonappr += 1
        if obj.check_sentiment() == 0:
            count_neutral_sentence += 1
        if obj.check_sentiment() == 1:
            count_positive_sentence += 1
        if obj.check_sentiment() == -1:
            count_negative_sentence += 1

    print("count_pos_appr= ", count_pos_appr)
    print("count_neg_appr= ", count_neg_appr)
    print("count_pos_Nonappr= ", count_pos_Nonappr)
    print("count_neg_Nonappr= ", count_neg_Nonappr)
    print("count_positive_sentence= ", count_positive_sentence)
    print("count_negative_sentence= ", count_negative_sentence)
    print("count_neutral_sentence= ", count_neutral_sentence)

    if count_positive_sentence > count_negative_sentence and count_pos_appr > count_neg_appr:
        if (count_pos_appr / (count_pos_appr + count_neg_appr)) >= 0.7:
            return 1
        else:
            return -1
    else:
        return -1

