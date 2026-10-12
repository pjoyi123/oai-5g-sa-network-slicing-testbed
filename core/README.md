# OpenAirInterface 5G Standalone Core

## Overview

This directory contains example OAI 5G Core configurations supporting
the reproducibility of our experimental 5G Standalone network slicing testbed.

The testbed supports three network slices:

| Slice | SST | SD |
|---|---|---|
| eMBB | 1 | 010203 |
| URLLC | 2 | 112233 |
| mMTC | 3 | 445566 |

The slices were evaluated sequentially.

## Directory Structure

- docker-compose.example.yaml: Example Docker deployment
- conf/config.template.yaml: Core configuration template
- database/oai_db_complete_example.sql: Example subscriber database
- healthscripts/mysql-healthcheck.sh: MySQL health-check script
- scripts/generate_core_config.py: Runtime configuration generator

## Prerequisites

- Ubuntu Linux
- Docker and Docker Compose
- Python 3
- PyYAML
- Compatible OpenAirInterface 5G Core container images

## Configuration

All commands below are run from the core directory.

### 1. Configure database credentials

Create a local `.env` file containing:

```dotenv
MYSQL_PASSWORD=replace_with_a_local_password
MYSQL_ROOT_PASSWORD=replace_with_a_different_local_root_password
```

Use your own strong passwords. Never commit the `.env` file.

### 2. Generate the runtime configuration

Load the environment variables:

```bash
set -a
source .env
set +a
```

Generate the runtime configuration:

```bash
python3 scripts/generate_core_config.py
```

This generates `conf/config.runtime.yaml`, which must remain private.

### 3. Validate Docker Compose

```bash
docker compose -f docker-compose.example.yaml config -q
```

### 4. Start the OAI Core

After reviewing the configuration and network settings:

```bash
docker compose -f docker-compose.example.yaml up -d
```

Check container status:

```bash
docker compose -f docker-compose.example.yaml ps
```

The complete example deployment has not yet been runtime-tested.

## Example Subscriber Database

The SQL file contains three illustrative test subscribers.

The example subscriber identities and authentication credentials are
not an exact reproduction of those used during the experiments.

The SQL initialization has not yet been validated through a complete
MySQL import and OAI Core startup.

## Network Configuration

The example Docker subnet is 172.28.10.0/26.

The external data-network container has a return route toward the UPF
that covers the configured UE address pools.

The UPF remote_n6_gw setting requires further verification.

## Reproducibility Limitations

- Docker Compose syntax validation passed.
- Runtime configuration generation passed basic validation.
- Complete OAI Core startup has not yet been verified.
- End-to-end UE connectivity has not yet been tested with this example.
- The original experiments evaluated slices sequentially.
- Concurrent slice isolation was not demonstrated.
- Differentiated QoS guarantees were not established.
- OAI development image tags may change over time.

## Security

Do not publish real subscriber authentication credentials,
database passwords, runtime configurations, or database backups.

Use the example files only in an authorised test environment.
