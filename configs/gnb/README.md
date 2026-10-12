# OAI gNB Configuration

This directory contains the sanitized gNB configuration used for the 5G Standalone network slicing testbed.

## Radio configuration

- Band: n78
- Bandwidth: 106 PRBs
- Numerology: 1 (30 kHz)
- Radio simulation: OAI RF simulator
- MCC/MNC: 001/01
- TAC: 1

## Supported network slices

| Slice | SST | SD |
|---|---|---|
| eMBB | 1 | 010203 |
| URLLC | 2 | 112233 |
| mMTC | 3 | 445566 |

## Launch command

Run from the OAI build directory:

```bash
cd ~/openairinterface5g/cmake_targets/ran_build/build
./nr-softmodem -O /path/to/gnb.sa.band78.106prb.rfsim.conf --rfsim --log_config.global_log_options utc_time
```

The launch command was recovered from the original Bash history.

## Network configuration

The repository replaces the original AMF and gNB IP addresses with documentation addresses in the 192.0.2.0/24 range.

Before launching the gNB, replace these addresses with the actual IP addresses assigned to the gNB and AMF in your test environment. Ensure that the gNB can reach the AMF and that the user-plane interfaces are correctly configured.

## Reproducibility note

The configuration matches the recovered original gNB file except for the sanitized IP addresses. The exact software version and successful execution should be verified in the complete replication procedure.
