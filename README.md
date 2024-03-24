# discord-bot-playground
A discord bot for fun, learning aspect.

### Quick Start
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
    vim .env # Modify the configuration
    set -o allexport && source .env
    ```
4. Launch the bot
    ```bash
    make run-bot
    ```
