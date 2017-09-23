.PHONY: *.py sync

%.py: sync
	@echo $@ && ssh -q raspberrypi.local "bash ~/.mysensehat/run.sh $@"

sync:
	@echo -n "Sync..." && (rsync -r . raspberrypi.local:.mysensehat/ > /dev/null 2>&1) && echo "done"
