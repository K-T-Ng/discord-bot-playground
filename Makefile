install-python-packages:
	pip install -r requirements.txt
	pip install -e \
		opentelemetry-python/opentelemetry-api \
		opentelemetry-python/opentelemetry-sdk \
		opentelemetry-python/opentelemetry-proto \
		opentelemetry-python/opentelemetry-semantic-conventions \
		opentelemetry-python/exporter/opentelemetry-exporter-otlp-proto-common \
		opentelemetry-python/exporter/opentelemetry-exporter-otlp-proto-http
