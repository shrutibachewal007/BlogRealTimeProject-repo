from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):  #view-function
    #ss ----> multi-line-str with html-data/code
    print("welcome/ url is requested & display() is executed");
    ss='''
          <center>
                <h2 style="color:blue;">
                    Hello User, Welcome to Django First-Project
                    First-App
                </h2>
                <hr />
          </center>
       ''';
    return HttpResponse(ss);   
    
def show(request):
    ss='''
        <!--HTML Webpage to display 'WELCOME-MESSAGE' with different headings -->
<html>
	<head>
		<title>***Welcome2-Page***</title>
		<style>
		h1{
			color:red
		}
		h2{
			color:blue
		}
		h3{
			color:brown
		}
		h4{
			color:purple
		}
		h5{
			color:black 
		}
		h6{
			color:violet
		}
		h1,h3,h5{
			background-color:lightblue;
		}
		h2,h4,h6{
			background-color:yellow;
		</style>
	</head>
	<body>
		<center>
		<h1>Welcome To Django HTML webpage</h1>
		<hr color="green" width="90%"/>
		<h2>Welcome To Django HTML webpage</h2>
		<hr color="green" width="80%"/>
		<h3>Welcome To Django HTML webpage</h3>
		<hr color="green" width="70%"/>
		<h4>Welcome To Django HTML webpage</h4>
		<hr color="green" width="60%"/>
		<h5>Welcome To Django HTML webpage</h5>
		<hr color="green" width="50%"/>
		<h6>Welcome To Django HTML webpage</h6>
		<hr color="green" width="40%"/>
		</center>
	</body>
</html>
''';
    return HttpResponse(ss);
    
def hello(request):
    print("hello/ url is requested & hello() is executed")
    ss='''
        <html>
            <head>
            <title>Welcome-Page</title>
                <style>
                h1{
                    color:red;
                    width:60%;
                }
                h2{
                    color:green;
                    width:50%;
                }
                h3{
                    color:maroon;
                    width:40%;
                }
                h1,h2,h3{
                    background-color:lightpink;
                    border:2px black;
                }      
                </style>
            </head>
            <body>
                <center>
                    <h1>hello user..!!</h1>
                    <hr color="blue" width="75%"/>
                    <h2>welcome to django app</h2>
                    <hr color="blue" width="65%"/>
                    <h3>have a nice day</h3>
                    <hr color="blue" width="55%"/>
                </center>
            </body>
        </html>
    ''';
    return HttpResponse(ss);
    
import time;
def senddatetime(request):
    print("dtime/ url is requested & senddatetime() is executed");
    ct=time.ctime();
    print("client request date&time on server",ct);
    ss='''
        <html>
            <head>
            <title>date-time page</title>
                <style>
                h1{
                    color:red;
                    width:65%;
                }
                h2{
                    color:blue;
                    width:55%;
                }
                h3{
                    color:green
                    width:35%;
                }
                h1,h2,h3{
                    background-color:yellow;
                    border:2px solid brown;
                }      
                </style>
            </head>
            <body>
                <center>
                    <h1>hello django user..!!</h1>
                    <hr color="maroon" width="75%"/>
                    <h2>server date&time::</h2>
                    <hr color="maroon" width="60%"/>
                    <h3>''',ct,'''</h3>
                    <hr color="maroon" width="40%"/>
                </center>
            </body>
        </html>
    ''';
    return HttpResponse(ss);
    
def demo(request):
    print("multiple-requests-URLs same response");
    htmldata='''<center>
                    <h1>hello demo user..!!<h1>
                    <hr/>
                    <h2>this is same output for different-multiple-requests-urls</h2>
                    <hr/>
                    <h3>have a great day</h3>
                    <hr/>
               </center>
    '''
    return HttpResponse(htmldata);
    
def homepage(request):
    htmldata='''<center>
                    <h1>welcome to default home-page<h1>
                    <hr/>
                    <h2>your request page is not found</h2>
                    <hr/>
                    <h3>pls try other urls or links!!</h3>
                    <hr/>
               </center>
    '''
    return HttpResponse(htmldata);
    
