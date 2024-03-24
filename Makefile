sync-submodule:
	# Get submodule that we need to use
	git submodule init
	git submodule update

install-python-packages:
	pip3 install -r requirements.txt
	pip3 install -e \
		opentelemetry-python/opentelemetry-api \
		opentelemetry-python/opentelemetry-sdk \
		opentelemetry-python/opentelemetry-proto \
		opentelemetry-python/opentelemetry-semantic-conventions \
		opentelemetry-python/exporter/opentelemetry-exporter-otlp-proto-common \
		opentelemetry-python/exporter/opentelemetry-exporter-otlp-proto-http

run-bot:
	python3 -m src.main