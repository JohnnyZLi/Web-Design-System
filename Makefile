PYTHON ?= python3

.PHONY: generate validate serve release clean

generate:
	$(PYTHON) scripts/design_system.py generate

validate:
	$(PYTHON) scripts/design_system.py validate

serve:
	$(PYTHON) scripts/design_system.py serve

release:
	$(PYTHON) scripts/design_system.py release

clean:
	rm -rf dist __pycache__ scripts/__pycache__
