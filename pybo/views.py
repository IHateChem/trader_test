from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .docker_controller.filebuilder import dockerfile_builder, container_builder 
import docker 
import json
from .utils import log2dict, lineparser, db_controller
def get_info(request):  
    return redirect("/param/")

def parameters(request):
    user = "abc"
    form = myForm(user)
    if request.method == 'POST':
        result = {}
        # process user input here
        result["id"] = 'abc' #for test 
        result["memory"] = request.POST.get('memory')
        result["cpu"] = request.POST.get('cpu')
        result["gpu"] = request.POST.get('gpu')
        result["backend"] = request.POST.get('backend')
        result["mode"] = request.POST.get('mode')
        result["ticker"] = request.POST.get('ticker')
        result["net"] = request.POST.get('net')
        result["start_date"] = request.POST.get('start_date')
        result["end_date"] = request.POST.get('end_date')
        result["balance"] = request.POST.get('balance')
        result["lr"] = request.POST.get('lr')
        result["model"] = request.POST.get('model')
        return final(result)
    else:
        return render(request, 'pybo/parameters.html',{'form': form})
def final(result):
    dockerfile_builder(result)
    container_builder(result)
    return redirect("/result/")
def show_result(request):
    client = docker.from_env()
    user_id = 'abc' # for test 

    for container in client.containers.list(all=True):
        if user_id + "_" + "container" in container.name:
            break
    logs = container.logs(stream=False, follow=False)
    logs_stdout, log_data = lineparser(logs.decode("utf-8"))
    # Get the JSON data from somewhere
    data = log2dict(log_data)
    data_json = json.dumps(data)
    return render(request, 'pybo/result.html', {'logs': logs_stdout.split('\n'), 'data_json': data_json})

def popup(request):
    return render(request, 'pybo/popup.html')
def submit_url(request):
    user = "abc"
    tickers = []
    idx=  0
    if request.method == 'POST':
        while request.POST.get(f'ticker{idx}'):
            tickers.append(request.POST.get(f'ticker{idx}'))
            idx += 1  
        if tickers:
            db_obj = db_controller("124.198.124.188", "root", "fmsoft1004", "history") #db연결
            cur = db_obj.get_cursor()
            name = request.POST.get("portfolioname")
            n = len(tickers); USER_ID = [user]*n; PORTFOLIO = [name]*n
            query = "INSERT INTO trader_test (USER_ID, TICKER, PORTFOLIO) VALUES (%s,%s,%s)"
            cur.executemany(query, zip(USER_ID, tickers, PORTFOLIO))
            con = db_obj.get_conn()
            con.commit()
            con.close()
    return render(request, 'pybo/popup.html')