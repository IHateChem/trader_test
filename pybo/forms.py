from django import forms
import re
from datetime import datetime
import os
from .utils import db_controller
from collections import defaultdict as dd
class myForm(forms.Form):
    def __init__(self, user):
        self.user = user
        BASE = 'C:/users/이석우/proejcts' #BASE = '/home/fmsoft/project/trader_test'
        if os.path.isdir(BASE+f"/app/trader_test/user/{user}/models/"):
            self.models = os.listdir(BASE+f"/app/trader_test/user/{user}/models/")
            self.models.sort()
        else:
            self.models = []
            '''        if os.path.isfile(BASE+f"/app/trader_test/user/{user}/portfolio.txt"):
                        f = open(BASE+f"/app/trader_test/user/{user}/portfolio.txt", "r")
                        line=f.readline()
                        f.close()
                        self.portfolios = line.split("|")
            '''
        db_obj = db_controller("124.198.124.188", "root", "fmsoft1004", "history").get_cursor()
        db_obj.execute(f'SELECT PORTFOLIO FROM trader_test WHERE USER_ID="{user}" GROUP BY PORTFOLIO;')
        PORTFOLIO = list(map(lambda t: t["PORTFOLIO"], db_obj.fetchall()))
        db_obj.execute(f'SELECT PORTFOLIO, TICKER FROM trader_test WHERE USER_ID = "{user}" ORDER BY PORTFOLIO ASC;')
        self.portfolios = dd(list)
        for contents in db_obj.fetchall():self.portfolios[contents["PORTFOLIO"]].append(contents["TICKER"])
        self.portfolios = self.portfolios.items()
    today = datetime.now().strftime('%Y-%m-%d')
        
    
    my_date = forms.DateField(widget=forms.DateInput(attrs={'types':'date'}), input_formats=["%Y-%m-%d"])
    ticker = forms.DecimalField(label = "Ticker", max_digits=6)
