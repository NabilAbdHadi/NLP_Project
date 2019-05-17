# NLP_Project - Mohamad Nabil bin Abdul Hadi

## PreProcess.py
commit by MuhdMujibRahman
form this class export the output to "new file2"

## language_detection.py
1 lang_ratio Method:  
    1.1 separate the punctution and word from input  
    1.2 detect the language of the word  
    1.3 turn the ratios of all present language  
2 detect_language Method:  
    2.1 input the output from lang_ratio  
    2.2 the highest ratio language will be consider as the main language of the input  
    2.3 return the language  

## tokenization sentences
1 import language_detection  
2 initialize the counter for malay, english, mixed language and other  
3 initialize the empty array to insert the other word  
4 import file "new file2" as f  
  4.1 for index, sentence in f:  
    4.1.1 initialize the malay and english counter  
    4.1.2 tokenize the sentence as row  
    4.1.3 for word in row:  
            4.1.3.1 detect the word language  
            4.1.3.2 increases the counter of malay and english language  
		4.1.4 analysis the sentences is in which language  
5 print the frequency of the language in "new file2"
6 remove the repetitive element in others array
7 print others array  

## Problem
problem 1 : the language_detection doesnt malay language however its detect the indonesian language. 
	since the malay language and the indonesian doesnt have much different so i consider the indonesian is the malay  
Problem 2 : some of the element in others array contain malay and english word however the language_detection.py 
	detect these word in other language for example "bijak" was detect as arabic  
Problem 3 : most of elements in others array is the punctuation. also, some element is the combination of few words
	that make the language_detection misunderstanding. the short form of the real form word
	ansd the combination of text and punctuation also make it difficult to analysis
