
VENV_DIR := venv
PYTHON := python3
PIP := $(VENV_DIR)/bin/pip
ACTIVATE := source $(VENV_DIR)/bin/activate

all: install run

install:
	@echo "🔧 Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "✅ Virtual environment created."

	@echo "📦 Installing dependencies from requirements.txt..."
	$(PIP) install -r requirements.txt
	@echo "✅ Dependencies installed."

run:
	@echo "🚀 Running the signature generator..."
	$(VENV_DIR)/bin/python generate_signatures.py
	@echo "✅ Signature generation completed."

clean:
	@echo "🧹 Cleaning environment..."
	rm -rf $(VENV_DIR)
	rm -rf __pycache__
	rm -rf signatures
	@echo "✅ Done."

.PHONY: all install run clean
