PDF_NAME = presentation

all:
	pdflatex $(PDF_NAME).tex
	pdflatex $(PDF_NAME).tex
clean:
	- rm -f *.aux *.log *.out *.bbl *.blg 
	- rm -f *.nav *.toc *.vrb *.snm
pdfclean:
	- rm -f $(PDF_NAME).pdf
test:
	okular $(PDF_NAME).pdf
full: clean all test
