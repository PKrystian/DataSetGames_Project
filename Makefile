install: requirements.txt
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements.txt

require: 
	./.venv/bin/pip freeze > requirements.txt
