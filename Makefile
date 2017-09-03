.PHONY: *.py sync

%.py: sync
	@echo $@ && ssh -q pi3.local 'sudo python ~/.mysensehat/$@'

sync:
	@echo -n "Sync..." && (rsync -r . pi3.local:.mysensehat/ > /dev/null 2>&1) && echo "done"