from django.http import HttpResponse
from django.shortcuts import render


def default(request): 
  return render(request, "home.html") 

def result(request):
  min_conf = eval(request.POST.get("min_conf"))  
  min_support = eval(request.POST.get("min_support"))
  min_lift = eval(request.POST.get("min_lift"))

  if(not( min_conf == None or min_lift == None or min_support == None )):

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    dataset = pd.read_csv('/home/sanket/App/Django-Apriori/app/ml_dataset/Market_Basket_Optimisation.csv', header = None)
    transactions = []
    for i in range(0, 7501):
      transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

    from apyori import apriori
    rules = apriori(transactions, min_support = min_support, min_confidence = min_conf, min_lift = min_lift, min_length = 2)
    # rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

    class Result:
      def __init__(self,support,confidence,rule):
        self.support = support
        self.confidence = confidence
        self.rule = rule

    new_result = []
    for obj in list(rules):
      new_result.append( Result("{:.4f}".format(obj.support),"{:.4f}".format(obj.ordered_statistics[0].confidence),', '.join(list(obj.items))) )

    return render(request, "result.html", {'min_sup':min_support, 'min_conf':min_conf, 'min_lift':min_lift, 'result':new_result})
