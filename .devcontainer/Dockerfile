FROM mcr.microsoft.com/devcontainers/python:3.12

# Install additional tools as root first
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    vim \
    htop \
    tree \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install podman for Neo4j container management
RUN apt-get update && apt-get install -y \
    podman podman-compose \
    && rm -rf /var/lib/apt/lists/*

# Switch to vscode user
USER vscode

# Install mise for vscode user
RUN curl https://mise.run | sh
ENV PATH="/home/vscode/.local/bin:$PATH"

# Install uv via mise
# RUN /home/vscode/.local/bin/mise install uv@latest
# RUN /home/vscode/.local/bin/mise use -g uv@latest

# Set up workspace
WORKDIR /workspace

# Copy project files and set ownership
COPY --chown=vscode:vscode . .

# インストールは手動で行う
# Install Python dependencies
# RUN /home/vscode/.local/bin/mise exec -- uv sync