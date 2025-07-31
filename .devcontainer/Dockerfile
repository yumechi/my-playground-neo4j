FROM mcr.microsoft.com/devcontainers/python:3.11

# Install mise for package management
RUN curl https://mise.run | sh
ENV PATH="/root/.local/bin:$PATH"

# Install uv via mise
RUN mise install uv@latest
RUN mise use -g uv@latest

# Install additional tools
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
    podman \
    && rm -rf /var/lib/apt/lists/*

# Set up workspace
WORKDIR /workspace

# Copy project files
COPY . .

# Install Python dependencies
RUN /root/.local/bin/uv sync

# Ensure proper permissions
RUN chown -R vscode:vscode /workspace