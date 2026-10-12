# OAI 5G SA S-NSSAI Experimental Testbed

Reproducibility materials for **Implementation and Experimental Evaluation of End-to-End 5G Standalone Network Slicing Using OpenAir-Interface** (IMITEC 2026).

## Scope and limitations

The experiment evaluates **three S-NSSAI configurations sequentially**, representing eMBB, URLLC and mMTC. It validates UE registration, PDU session establishment and IP connectivity, and measures RTT, TCP throughput, UDP jitter, loss, retransmissions and selected core resource usage. **It does not demonstrate concurrent slice isolation or differentiated QoS guarantees.**

## Reported environment

| Item | Value |
| --- | --- |
| Host OS | Ubuntu 24.04.4 LTS |
| CPU | Intel Core i5-8365U, 8 logical CPUs |
| RAM | Approximately 15 GiB |
| OAI RAN branch | `2025.w46` |
| OAI RAN commit | `92980ceb` |
| OAI Core version/images | **TODO: record exact Docker image tags/digests** |
| RAN | OAI gNB and NR UE over RFsim |
| Band | NR n78 |
| PRBs | 106 |
| SCS | 30 kHz |
| TDD | 5 ms periodicity; 7 DL slots, 6 DL symbols, 2 UL slots, 4 UL symbols |
| DNN | `oai` |
| UE subnet | `10.0.0.0/24` |
| UPF | simple-switch with source NAT |

## S-NSSAI configurations

| Profile | SST | SD |
| --- | --- | --- |
| eMBB | 1 | `010203` |
| URLLC | 2 | `112233` |
| mMTC | 3 | `445566` |

These profiles were evaluated one at a time. The labels do not imply verified service-class guarantees.

## Experimental procedure

1. Deploy the recorded OAI 5G Core, gNB and UE configuration (actual sanitized configuration files must be supplied in `configs/`).
2. Activate one S-NSSAI profile and verify UE registration, PDU session establishment and IP connectivity using core logs and ICMP.
3. Conduct **five measurement runs per profile**: 100 ICMP echo requests per run; iPerf3 TCP and UDP tests lasting 20 seconds each; UDP offered load 10 Mbps.
4. Record RTT, TCP throughput, UDP jitter, ICMP/UDP loss and TCP retransmissions.
5. Monitor AMF, SMF and UPF with Docker statistics, 30 observations for baseline and active eMBB conditions.
6. Calculate mean and sample standard deviation across five runs for RTT, TCP throughput and UDP jitter.

**TODO:** Document exact UE launch commands, IP endpoints, iperf3 server location, run reset procedure, traffic direction, measurement sampling intervals, and container image versions. Do not claim bit-for-bit reproducibility until these details and original configurations are supplied.

## Directory structure

- `configs/`: placeholders for sanitized gNB, UE and core configuration files
- `scripts/`: Network performance measurement scripts
- `results/`: manuscript-level aggregate results; raw per-run data still needed
- `docs/`: replication checklist and reviewer response

## Manuscript results

See `results/aggregate_results.csv`, `results/packet_delivery.csv` and `results/core_cpu.csv`. These values were transcribed from the manuscript; they are **not raw measurements**.

## Reproducibility status

This is a **documentation starter**, not a complete reproducibility release. Before public release, add actual validated configuration files, raw per-run measurements, exact software versions, execution commands and a license approved by your organisation. Remove IMSIs, subscriber keys, credentials, internal addresses, private endpoints and proprietary material as appropriate.

## Citation

Joyi, P., Keetile, M., and Masonta, M. T., “Implementation and Experimental Evaluation of End-to-End 5G Standalone Network Slicing Using OpenAir-Interface,” IMITEC 2026 (accepted; publication details to be confirmed).
