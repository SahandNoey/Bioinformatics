# import plotting modules 
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams["lines.linewidth"] = 0.9
from matplotlib import pyplot as plt
from matplotlib import gridspec
from matplotlib.ticker import MaxNLocator, FormatStrFormatter
from matplotlib.lines import Line2D
import seaborn as sns

# import statistical test modules
from statsmodels.stats.multitest import fdrcorrection
from scipy.stats import wilcoxon

# import miscellaneous
import numpy as np
import pandas as pd
import string
import os

# import core functions
from sys import path
path.append('../')
import core.graph

home_dir = '/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-2])
# result_fp = home_dir + '/my_results/my_main-results.tsv'
result_fp = home_dir + '/my_results/my_main-results.tsv'
mdlsel_result_fp = home_dir + '/results/mdlsel_result.tsv'
fig_dir = home_dir + '/my_figures_tables/'
network_dir = home_dir + '/data/networks/'
gsc_dir = home_dir + '/data/labels/'
prop_dir = home_dir + '/properties/'
alpha = 0.05

gsc_lst = ['GOBP', 'DisGeNet', 'BeFree', 'GWAS', 'MGI']
network_lst = ['BioGRID', 'STRING-EXP']
score_type_lst = ['auPRC', 'P@TopK', 'auROC']
method_lst = [
    'SL-A-LR',
    'SL-A-SVM',
    'SL-A-RF',
    'SL-E-LR',
    'SL-E',
    ]
prop_lst = ['Number of Genes', 'Edge Density', 'Segregation']
panel_annot_lst = list(string.ascii_uppercase)

valsplit_dict = {
	'Holdout': 'Holdout Validation', 
	'5FCV': '5-Fold Cross Validation'
}

gsc_group_dict = {
	'Function Prediction': ['GOBP'],
	'Disease and Trait Prediction': ['DisGeNet', 'BeFree', 'GWAS', 'MGI']
}

method_group_dict = {
	# 'Supervised Learning': ['LR-L2', 'SVM', 'LR-L1', 'RF'],
    'Supervised Learning': ['SL-A-LR', 'SL-A-SVM', 'SL-A-RF', 'SL-E-LR', 'SL-E'],
	'Label Propagation': ['LP-I55', 'LP-I65', 'LP-I75', 'LP-I85', 'LP-I95']
}

method_class_dict = {
	'SL': ['A', 'I'],
	'LP': ['A', 'I']
}

kw_dict = {
	'network': 'Network',
	'gsc': 'Geneset Collection',
	'valsplit': 'Validation Split',
	'geneset': 'Geneset',
	'score_type': 'Score Type',
	'method': 'Method'
}

# boxplot_color = {
# 	'LP-A': 'lightskyblue',
# 	'LP-I': 'dodgerblue',
# 	'SL-I': 'lightsalmon',
# 	'SL-A': 'tomato'
# }
boxplot_color = {
    'SL-A-LR': 'lightseagreen',   # Light Green for SL-A-LR
    'SL-A-SVM': 'mediumslateblue', # Blue for SL-A-SVM
    'SL-A-RF': 'darkorange',      # Orange for SL-A-RF
    'SL-E-LR': 'tomato',          # Red for SL-E-LR
    'SL-E': 'darkorchid',         # Purple for SL-E
}



network_color = {
	'BioGRID': 'blue',
	'STRING-EXP': 'orange',
	# 'InBioMap': 'green',
	# 'GIANT-TN': 'red',
	# 'STRING': 'purple'
}

gsc_color_dict = {
	'red': ['GOBP'],
	'blue': ['DisGeNet', 'BeFree'],
	'black': ['GWAS', 'MGI']
}

gsc_group_color_dict = {
	'red': 'Function Prediction',
	'blue': 'Disease Prediction',
	'black': 'Trait Prediction'
}

gsc_color = {
	# 'GOBPtmp': 'red',
	'GOBP': 'red',
	# 'KEGGBP': 'red',
	'DisGeNet': 'blue',
	'BeFree': 'blue',
	'GWAS': 'black',
	'MGI': 'black'
}

gsc_distinct_color = {
	# 'GOBPtmp': 'firebrick',
	'GOBP': 'red',
	# 'KEGGBP': 'orangered',
	'DisGeNet': 'blue',
	'BeFree': 'royalblue',
	'GWAS': 'grey',
	'MGI': 'silver'
}

gsc_marker = {
	# 'GOBPtmp': 'o',
	'GOBP': 'X',
	# 'KEGGBP': '*',
	'DisGeNet': 's',
	'BeFree': 'd',
	'GWAS': '^',
	'MGI': 'v'
}

import helperfun
