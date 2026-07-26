PYTHON ?= python3

.PHONY: generate validate package-check serve release clean

generate:
	$(PYTHON) scripts/design_system.py generate

validate:
	$(PYTHON) scripts/design_system.py validate
	$(PYTHON) scripts/validate_package.py

package-check:
	$(PYTHON) scripts/validate_package.py

serve:
	$(PYTHON) scripts/design_system.py serve

release:
	$(PYTHON) scripts/design_system.py release
	$(PYTHON) scripts/validate_package.py release

clean:
	rm -rf dist __pycache__ scripts/__pycache__
