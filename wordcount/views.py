from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') # 확장의 경로를 새로 써줘야 하는 것 같다.
   # 3개의 인자까지 돌아갔다 (request , html 인자를 , 사전형 객체 dictionary 형을 받게된다.) 

def about(request):
    return render(request, 'about.html') # 'wordcount/about.html' 에 있는 형식에 대하여 디렉토리 설정을해주면 좋다는 것을의마한다.

def method(request):
    return render(request, 'method.html') 

def count(request):
    full_text = request.GET['fulltext'] # 원문의 글자체를 말하는 것을 의미한다. ''
    word_list = full_text.split() # 약간의 메소드의 형태로 말하면된다.
    word_dictionary = word_dictionary = {} # 단어 : 몇번, 단어 : 몇번 , 쌍들을 보내고 싶다. 

    for word in word_list:
        if word in word_dictionary:
             #increase
            word_dictionary[word] += 1
        else:
             # add to dictionary
            word_dictionary[word] = 1

    return render(request, 'count.html',{'fulltext' : full_text, 'total': len(word_list), 'dictionary':word_dictionary.items()}) # result 로 반환한다는 것을 말한다. 3번째인자를 사용한다 
    # , {'full' : text, 'total' : len(words), 'dictionary': word_dictionary.items()}

