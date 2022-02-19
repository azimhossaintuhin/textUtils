#custom fil
#packages of django
from django.http import HttpResponse
from django.shortcuts import render
#index This isthe main page
def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'AboutUs.html')

def contact_us(request):
    return render(request,"ContactUs.html")

def analyze(request):
    #get The text
    djtext    =  request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc','off')
    uppercase = request.POST.get('upercase','off')
    newLinerm = request.POST.get('newlinerm', 'off')
    extraspacerm = request.POST.get('sapcerm','off')
    
    #remove punction from text
    if removepunc == "on":
             punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
             analyzed = ""
            #analyze The Tex  
             for i in djtext:
                 if i not in punc:
                  analyzed = analyzed + i
             par = {'purpose' : "remove the punction" , 'analyze': analyzed }
             djtext = analyzed
                
             

     #COnvert Letter To the upppercase 
    if uppercase == 'on' :
                analyzed = ""
            #analyzed text
                for i in djtext:
                    analyzed  = analyzed + i.upper()
                par = {'purpose' : "remove to upper case" , 'analyze': analyzed }
                djtext = analyzed
    #new line charecter remove 
    if newLinerm == 'on':
                analyzed = ""
                
                for i in djtext:
                   if i !='\n' and i !='\r':
                    analyzed = analyzed + i
                    par = {'purpose' : "remove new lines" , 'analyze': analyzed }
                   #analyze The Tex             
                djtext = analyzed
    if extraspacerm == 'on':
        analyzed = ''
        for index , item in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + item
        par = {'purpose' : "remove new lines" , 'analyze': analyzed }
                   #analyze The Tex             
        djtext = analyzed
            
    if removepunc != "on" and uppercase!='on' and newLinerm !='on' and extraspacerm!='on': 
          return HttpResponse("error")
    
    return render(request,'analyze.html',par)