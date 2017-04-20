import sys
import io
import getopt
import select_data
import os

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfdevice import TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.utils import set_debug_logging

'''
args = 'cs_aeca.pdf'

caching = True
scale = 1
layoutmode = 'normal'
laparams = LAParams()
outdir = None
debug = False
outfile = None

rsrcmgr = PDFResourceManager(caching=caching)

if outfile:
    outfp = io.open(outfile, 'wt', encoding='unicode', errors='ignore')
    close_outfp = True
else:
    outfp = sys.stdout
    close_outfp = False

device = HTMLConverter(rsrcmgr, outfp, scale=scale, layoutmode=layoutmode,
            laparams=laparams, outdir=outdir, debug=debug)

for fname in args:
    fp = io.open(fname, 'rb')
    process_pdf(rsrcmgr, device, fp, caching=caching, check_extractable=True)
    fp.close()
device.close()
if close_outfp:
    outfp.close()
'''
'''
L =[]
result = select_data.query_pdflink()

for i in result:
    i = i.replace('/plantguide/pdf/', '')
    j = i.replace('.pdf','')
    L.append(j)

for line in L:
    if line!= "NULL":
        line = 'python pdf2txt.py -t html -o "E:\pdf\p\%s.html" "E:\pdf\plant_guide\%s.pdf" ' % (line, line)
        print(line)
        os.system(line)
'''
L =[]
result2 = select_data.query_pdflink2()
for i in result2:
    i = i.replace('/factsheet/pdf/', '')
    j = i.replace('.pdf', '')
    L.append(j)

for line in L:
    if line != "None":
        line = 'python pdf2txt.py -t html -o "E:\pdf\\f\%s.html" "E:\pdf\\fact_sheet\%s.pdf" ' % (line, line)
        print(line)
        os.system(line)