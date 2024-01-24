import nltk 
import json
## for the first time uncomment them
# nltk.download('punkt')
# nltk.download('stopwords')

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

text ="""Welcome to our website. If you continue to browse and use this website, you are agreeing to comply with and be bound by the following terms and conditions of use, which together with our privacy policy govern [business name]’s relationship with you in relation to this website. If you disagree with any part of these terms and conditions, please do not use our website.
The term ‘[business name]’ or ‘us’ or ‘we’ refers to the owner of the website whose registered office is [address]. Our company registration number is [company registration number and place of registration]. The term ‘you’ refers to the user or viewer of our website.
The use of this website is subject to the following terms of use:
The content of the pages of this website is for your general information and use only. It is subject to change without notice.
This website uses cookies to monitor browsing preferences. If you do allow cookies to be used, the following personal information may be stored by us for use by third parties: [insert list of information].
Neither we nor any third parties provide any warranty or guarantee as to the accuracy, timeliness, performance, completeness or suitability of the information and materials found or offered on this website for any particular purpose. You acknowledge that such information and materials may contain inaccuracies or errors and we expressly exclude liability for any such inaccuracies or errors to the fullest extent permitted by law.
Your use of any information or materials on this website is entirely at your own risk, for which we shall not be liable. It shall be your own responsibility to ensure that any products, services or information available through this website meet your specific requirements.
This website contains material which is owned by or licensed to us. This material includes, but is not limited to, the design, layout, look, appearance and graphics. Reproduction is prohibited other than in accordance with the copyright notice, which forms part of these terms and conditions.
All trademarks reproduced in this website, which are not the property of, or licensed to the operator, are acknowledged on the website.
Unauthorised use of this website may give rise to a claim for damages and/or be a criminal offence.
From time to time, this website may also include links to other websites. These links are provided for your convenience to provide further information. They do not signify that we endorse the website(s). We have no responsibility for the content of the linked"""
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text)

freqTable = dict() 

for word in words:
    word=word.lower()
    if word not in freqTable:
        freqTable[word]=1
    else:
        freqTable[word]+=1
        
# Creating a dictionary to keep the score
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 

for sentence in sentences: 
	for word, freq in freqTable.items(): 
		if word in sentence.lower(): 
			if sentence in sentenceValue: 
				sentenceValue[sentence] += freq 
			else: 
				sentenceValue[sentence] = freq 



sumValues = 0
for sentence in sentenceValue: 
	sumValues += sentenceValue[sentence] 

# Average value of a sentence from the original text 


average = 0

if len(sentenceValue) > 0:	
    sumValues = sum(sentenceValue.values())
    average = int(sumValues / len(sentenceValue))
else:
    print("Warning: No sentences found, setting average to 0.")

summary = '' 
for sentence in sentences: 
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.3 * average)): 
		summary += " " + sentence
  
for x in summary.split("."):
    print("*",x,end="\n\n")
    
def getSummary():
    summary=json.dumps({"summary":summary})
    return summary  