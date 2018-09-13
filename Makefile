manuscript = report
latexopt = -file-line-error -halt-on-error

# Build the PDF of the lab report from the source files
$(manuscript).pdf: $(manuscript).tex text/*.tex references.bib images/*.png
	pdflatex $(latexopt) $(manuscript).tex
	bibtex $(manuscript).aux
	bibtex $(manuscript).aux
	pdflatex $(latexopt) $(manuscript).tex
	pdflatex $(latexopt) $(manuscript).tex

# Get/download necessary data

data :
	curl -L -O https://www.dropbox.com/s/hutmwip3681xlup/lab0_spectral_data.txt

# Validate that downloaded data is not corrupted
validate :
	curl -L -O https://www.dropbox.com/s/amumdrm9zp1kn8d/lab0_spectral_data.md5
	md5sum lab0_spectral_data.txt
	md5sum -c lab0_spectral_data.md5

# Run tests on analysis code
test :
	nosetests --no-byte-compile test/*

# Automate running the analysis code
analysis :
	python code/spectrum_cal.py

clean :
	rm -f *.aux *.log *.bbl *.lof *.lot *.blg *.out *.toc *.run.xml *.bcf
	rm -f text/*.aux
	rm $(manuscript).pdf
	rm code/*.pyc

# Make keyword for commands that don't have dependencies
.PHONY : test data validate analysis clean
