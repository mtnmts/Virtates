# Makefile
# 
# Converts Markdown to other formats (HTML, PDF, DOCX, RTF, ODT, EPUB) using Pandoc
# <http://johnmacfarlane.net/pandoc/>
#
# Run "make" (or "make all") to convert to all other formats
#
# Run "make clean" to delete converted files

# Convert all files in this directory that have a .md suffix
SOURCE_DOCS := $(wildcard src/*.rst)

EXPORTED_DOCS=\
 $(SOURCE_DOCS:.rst=.html)

RM=/bin/rm

PANDOC=/usr/bin/pandoc

PANDOC_OPTIONS=--smart --standalone

PANDOC_HTML_OPTIONS=--to html5

OUT_DIR =out/
# Pattern-matching Rules

%.html : %.rst
	@mkdir -p $(OUT_DIR)
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_HTML_OPTIONS) -o $@ $<
	mv $@ $(OUT_DIR)


# Targets and dependencies

.PHONY: all clean

all : $(EXPORTED_DOCS)
	

clean:
	- $(RM) $(OUT_DIR)*