WATCH_FILES= ag -l

test:
				nosetests -s

entr_warn:
				@echo "-------------------------------------------------"
				@echo " ! File watching functionality non-operational ! "
				@echo "																									"
				@echo " Install entr(1) to run tasks on file change.		"
				@echo " See http://entrproject.org/											"
				@echo "-------------------------------------------------"

watch_test:
				if command -v entr > /dev/null; then while sleep 1; do ${WATCH_FILES} | \
				entr -cd $(MAKE) test; done; else $(MAKE) test entr_warn; fi
