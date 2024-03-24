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
0. Install prerequisites
    ```bash
    sudo apt-get update
    sudo apt-get install make
    ```
1. Clone the repo and sync the submodule
    ```bash
    git clone https://github.com/K-T-Ng/discord-bot-playground.git
    make sync-submodule
    ```
2. Create and activate virtual environment, install required python packages
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    make install-python-packages
    ```
3. Modify configuration file then export as environment variable
    ```bash
    cp .env_sample .env
    vim .env # Modify the configuration, with OTEL_ENABLE_INSTRUMENTATION=false
    set -o allexport && source .env
    ```
4. Launch the bot
    ```bash
    make run-bot
    ```

### Bot Monitoring
WIP