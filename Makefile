
SHELL:=/bin/bash
NOISE=0.2
LENGTH=40
CHECKER_NOISE=05 10 15 20 25
CORRECTOR_NOISE=05 10 15
NOISE_VALUES=$(CHECKER_NOISE)
LENGTH_VALUES=20 40 60 80 100
EXPERIMENT_VALUES=2000 4000 6000 8000 10000

experiment:
	@for L in $(EXPERIMENT_VALUES); do echo -n $$L; $$(which time) -p make -s test LENGTH=$$L 2>&1 | grep user | cut -c5- ; done

test-length:
	@for L in $(LENGTH_VALUES); do make -s test-noise LENGTH=$$L || exit $$?; done

test-noise:
	@for I in $(NOISE_VALUES); do make -s test-average NOISE=0.$$I || exit $$?; done

test-average:
	@for X in `seq 10`; do make -s test || exit $$?; done | grep -v Entering | grep -v Leaving | cut -c11- | ./mean.py > mean.txt
	@echo -n $(LENGTH) $(NOISE)" "; cat mean.txt

test:
#@echo Length $(LENGTH)
#@echo Noise $(NOISE)
	@./plumbus.py $(LENGTH) | tee original.txt | ./senderscribe.py | tee sent.txt | ./vitiet.py $(NOISE) | tee noisy.txt | ./receiverscribe.py > result.txt
	@./checker.py original.txt sent.txt noisy.txt result.txt

zip:
	zip nayox.zip plumbus.py vitiet.py senderscribe.py receiverscribe.py checker.py mean.py Makefile
