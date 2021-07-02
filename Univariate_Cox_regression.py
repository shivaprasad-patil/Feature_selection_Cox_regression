import sys
import click
import numpy as np
import pandas as pd
import rpy2.robjects as ro
#from rpy2.rinterface_lib.embedded import RRuntimeError
from rpy2.rinterface import RRuntimeError
from rpy2.robjects import pandas2ri, Formula
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import importr

base = importr('base')
stats = importr('stats')
survival = importr('survival',lib_loc='')
writexl = importr('writexl', lib_loc='')


data = pd.read_excel("filename.xlsx")
data = data.drop(['ID'], axis=1)

coxph = survival.coxph

genes = list(data.columns[2:])
results_cox = pd.DataFrame()
results_cox['Gene_symbol'] = genes #The column name can be changed to your liking
results_cox = results_cox.set_index('Gene_symbol')

with localconverter(ro.default_converter + pandas2ri.converter):
    r_results_cox = ro.conversion.py2ri(results_cox)

for col in data.columns[2:]:
    data_col = (data[[col, 'survivaltime', 'event']]
        
    with localconverter(ro.default_converter + pandas2ri.converter):
        r_data_col = ro.conversion.py2ri(data_col)
    cox = coxph(ro.Formula("Surv(survivaltime, event) ~ ."), data = r_data_col)
    results = ro.r.coef(ro.r.summary(cox))
    r_results_cox = ro.r.rbind(r_results_cox, results)
    writexl.write_xlsx(r_results_cox, ro.r.paste("cox_output.xlsx"))


df = pd.read_excel("cox_output.xlsx")
df.insert(loc=0, column='Gene_symbol', value=genes)
df.to_excel("cox_output_gene.xlsx", index=0) 
