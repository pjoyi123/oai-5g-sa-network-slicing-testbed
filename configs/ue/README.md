# OAI NR UE configurations

This directory contains sanitized NR UE configuration examples for the three network slice profiles evaluated in the IMITEC 2026 experiments.

## Network slice profiles

| Profile | Configuration | SST | SD | DNN |
|---|---|---|---|---|
| eMBB | `ue_embb.conf` | 1 | 010203 | oai |
| URLLC | `ue_urllc.conf` | 2 | 112233 | oai |
| mMTC | `ue_mmtc.conf` | 3 | 445566 | oai |

The configurations use test-network IMSIs and placeholder authentication credentials.

## Subscriber provisioning

Before launching a UE:

1. Replace `REPLACE_WITH_TEST_KEY` and `REPLACE_WITH_TEST_OPC` with credentials generated for your own test environment.
2. Provision the corresponding IMSI, authentication credentials, DNN and S-NSSAI in the OAI Core subscriber database.
3. Ensure that the gNB and Core configurations support the requested slice.

Do not commit actual subscriber authentication credentials to this repository.

## Experimental procedure

The eMBB, URLLC and mMTC profiles were evaluated sequentially.

Each profile was configured and tested separately using the OAI RF simulator. The experiments do not establish simultaneous multi-slice isolation.

The exact NR UE launch commands and process restart procedure must be verified against the original experimental records before this documentation is considered complete.

## Reproducibility notes

The configuration files are sanitized examples. They require locally generated authentication credentials and compatible network settings.

See the repository's main README for the experimental measurements and analysis scripts.

## NR UE launch commands

Run from the OAI build directory:

cd ~/openairinterface5g/cmake_targets/ran_build/build

### eMBB
sudo ./nr-uesoftmodem -r 106 -C 3619200000 --numerology 1 --band 78 --rfsim --rfsimulator.serveraddr 127.0.0.1 -O /path/to/ue_embb.conf

### URLLC
sudo ./nr-uesoftmodem -r 106 -C 3619200000 --numerology 1 --band 78 --rfsim --rfsimulator.serveraddr 127.0.0.1 -O /path/to/ue_urllc.conf

### mMTC
sudo ./nr-uesoftmodem -r 106 -C 3619200000 --numerology 1 --band 78 --rfsim --rfsimulator.serveraddr 127.0.0.1 -O /path/to/ue_mmtc.conf

These commands were recovered from Bash history. Replace /path/to/ with the actual configuration directory. Configure matching subscriber credentials before launching.
