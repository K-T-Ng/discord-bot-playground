# discord-bot-playground
A discord bot for fun, learning aspect.

We want to learn the following things:
- [ ] A simple music bot that stream music from youtube
    - [ ] Audio format (`pcm`, `opus`)
- [ ] Application monitoring
    - [ ] Three pillars for monitoring (`Log`, `Metric`, `Trace`)
    - [ ] Data instrumenation via OpenTelemetry
    - [ ] Monitoring opensource solutions (`ElasticSearch`, `Prometheus`, `Jaeger`)
- [ ] Containerized and Kubernetes deployment

### Quick Start
To launch the bot quickly without any monitoring, you can follow the following steps
1. Install prerequisites
    ```bash
    sudo apt-get update
    sudo apt-get install make
    ```
2. Clone the repo and sync the submodule
    ```bash
    git clone https://github.com/K-T-Ng/discord-bot-playground.git
    make sync-submodule
    ```
3. Create and activate virtual environment, install required python packages
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    make install-python-packages
    ```
4. Modify configuration file then export as environment variable
    ```bash
    cp .env_sample .env
    vim .env # Modify the configuration, with OTEL_ENABLE_INSTRUMENTATION=false
    set -o allexport && source .env
    ```
5. Launch the bot
    ```bash
    make run-bot
    ```

### Bot Monitoring
Currently, we only provide OpenTelemetry instrumentation for generating the monitoring data and support push mode via HTTP only.

#### If you want to build a local monitoring stack...
If you are using Windows with WSL2, want to create a local monitoring stack, you may reference to [this repo](https://github.com/K-T-Ng/kubernetes-playground). We illustrate how to build the stack and integrate this bot here.
1. Make sure you have run `make sync-submodule` before and you can see some configuration file in `./kubernetes-playground`

2. Create the monitoring backed
    ```bash
    cd kubernetes-playground
    make install-prerequisite get-helm-charts
    make create-cluster
    make install-common check-common # This may need some time depends on your network (pull image)
    make install-monitor-backend check-monitor-backend # This may need some time depends on your network (pull image)
    ```

3. Add the following contents to the `C:\Windows\System32\drivers\etc\hosts` in Windows
    ```bash
    127.0.0.1 grafana.local prometheus.local jaeger.local otel-collector.local
    ```

4. Modify the configuration and exporter the environment variables again
    ```bash
    # Set OTEL_ENABLE_INSTRUMENTATION=true 
    # Set OTEL_OTLP_EXPORTER_HTTP_ENDPOINT=http://otel-collector.local
    vim .env

    # Export the environment again
    set -o allexport && source .env
    ```
5. Launch the bot again
    ```bash
    make run-bot
    ```
6. Visualize the result in
    ```txt
    Grafana: http://grafana.local
    Prometheus: http://prometheus.local
    Jaeger Query: http://jaeger.local
    ```

#### If you have OpenTelemetry Collector...
If you have the OpentTelemetry Collector with HTTP protocol enabled, you can simply issues the following steps.
1. Modify the configuration and exporter the environment variables again
    ```bash
    # Set OTEL_ENABLE_INSTRUMENTATION=true 
    # Set OTEL_OTLP_EXPORTER_HTTP_ENDPOINT=<your opentelemetry collector http endpoint>
    vim .env

    # Export the environment again
    set -o allexport && source .env
    ```
2. Launch the bot again
    ```bash
    make run-bot
    ```
