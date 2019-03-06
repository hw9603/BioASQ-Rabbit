all:
	make -C Expander
	make -C Ranker
	make -C Results
	make -C Splitter
	make -C Tiler