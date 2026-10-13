# OAI 5G SA S-NSSAI Experimental Testbed

Reproducibility materials for **Implementation and Experimental Evaluation of End-to-End 5G Standalone Network Slicing Using OpenAir-Interface**.

## Scope and limitations

The experiment evaluates **three S-NSSAI configurations sequentially**, representing enhanced Mobile Broadband (eMBB), Ultra-Reliable Low-Latency Communications (URLLC), and massive Machine-Type Communications (mMTC). It validates UE registration, PDU session establishment, and IP connectivity, while measuring round-trip time (RTT), TCP throughput, UDP jitter, packet loss, TCP retransmissions, and selected 5G Core resource utilisation metrics. **Since the configurations were evaluated sequentially rather than concurrently, the experiment does not demonstrate concurrent network slice isolation or guaranteed QoS differentiation.**

## Reported environment

| Item | Value |
| --- | --- |
| Host OS | Ubuntu 24.04.4 LTS |
| CPU | Intel Core i5-8365U, 8 logical CPUs |
| RAM | Approximately 15 GiB |
| OAI RAN branch | `2025.w46` |
| OAI RAN commit | `92980ceb` |
| OAI Core version/images | Current deployment image IDs recorded in `docs/docker_image_versions.csv`; original experimental image versions not independently confirmed |
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

1. Deploy the recorded OAI 5G Core, gNB and UE configuration (sanitized configurations are provided in `configs/` and `core/`).
2. Activate one S-NSSAI profile and verify UE registration, PDU session establishment and IP connectivity using core logs and ICMP.
3. Conduct **five measurement runs per profile**: 100 ICMP echo requests per run; iPerf3 TCP and UDP tests lasting 20 seconds each; UDP offered load 10 Mbps.
4. Record RTT, TCP throughput, UDP jitter, ICMP/UDP loss and TCP retransmissions.
5. Monitor AMF, SMF and UPF with Docker statistics, 30 observations for baseline and active eMBB conditions.
6. Calculate mean and sample standard deviation across five runs for RTT, TCP throughput and UDP jitter.

**Remaining limitations:** The exact UE launch variant used for the final measurements, per-run restart procedure, original Docker statistics sampling interval, and original OAI Core image versions remain unconfirmed. Recovered commands, sanitized configurations, traffic endpoints and current Docker image IDs are documented. Complete testbed reproducibility has not yet been demonstrated.

## Directory structure

- `configs/`: sanitized gNB and UE configurations with launch instructions; see `core/` for the OAI Core configuration
- `scripts/`: Network performance measurement scripts
- `results/`: aggregate statistics, 45 original measurement files and generated performance figures
- `docs/`: replication checklist and reviewer response

## Manuscript results

See `results/aggregate_results.csv`, `results/packet_delivery.csv` and `results/core_cpu.csv`. The RTT, TCP throughput and UDP jitter statistics in `results/aggregate_results.csv` have been reproduced from the original measurements in `results/raw/`. AMF, SMF and UPF CPU averages and ICMP/UDP packet delivery have been independently verified against the preserved measurements. TCP retransmission totals were recalculated, but they differ from the manuscript values.

## Reproducibility status

The repository contains the experimental configurations, measurement scripts, raw data, and performance figures used in this study. The experimental measurements cover round-trip time (RTT), TCP throughput, UDP jitter, packet loss, TCP retransmissions, and selected 5G Core resource utilisation metrics.
The testbed was implemented using OpenAirInterface (OAI) 5G Standalone with an RFsim-based radio access network and a containerised 5G Core. Three S-NSSAI configurations representing eMBB, URLLC, and mMTC were evaluated sequentially. The experimental configurations and available deployment information are provided to support reproducibility and further research

## Verified traffic-generation parameters

The following parameters were recovered directly from all 30 original iPerf3 JSON measurement files.

| Parameter | TCP throughput | UDP jitter |
|---|---|---|
| Client IP | 10.0.0.2 | 10.0.0.2 |
| Server IP | 192.168.70.135 | 192.168.70.135 |
| Server port | 5201 | 5201 |
| Duration | 20 seconds | 20 seconds |
| Target bitrate | TCP default | 10 Mbps |
| Reverse mode | Disabled | Disabled |
| Runs per slice | 5 | 5 |

Traffic originated from the UE-side client and was directed toward the iPerf3 server. The same settings were recorded for eMBB, URLLC and mMTC.

The server IP is the original experimental address and must be replaced with the appropriate reachable server address in another deployment. The server address matches the current `oai-ext-dn` container, and recovered Bash history shows an iPerf3 server launch inside that container. However, the server process location during every original measurement remains unconfirmed.

## Network profile switching and process management

The eMBB, URLLC and mMTC profiles were evaluated sequentially using separate UE configurations.

Recovered Bash history confirms that OAI NR UE processes were stopped and relaunched during some experimental sessions. It also records multiple gNB launches and OAI Core deployment using Docker Compose.

The available records do not establish whether the gNB, UE or Core was restarted between every measurement run. Therefore, no fixed restart sequence is claimed for the original experiments.

For replication, researchers should activate the required UE profile, verify registration and PDU session establishment, confirm IP connectivity, and then execute the corresponding measurements.

## Citation

Joyi, P., Keetile, M., and Masonta, M. T., “Implementation and Experimental Evaluation of End-to-End 5G Standalone Network Slicing Using OpenAir-Interface,” (accepted for publication).

## Reproducing the experimental results

This repository contains 45 original experimental measurement files collected
from three S-NSSAI configurations: eMBB, URLLC and mMTC.

Each configuration was evaluated using five experimental runs.

### Python requirements

The analysis requires:

- Python 3
- NumPy
- Matplotlib

Install the required Python libraries:

```bash
python3 -m pip install numpy matplotlib
```

### Generate the experimental figures

From the root directory of the repository, execute:

```bash
python3 scripts/generate_figures.py
```

The script reads the original experimental measurements from `results/raw/`.

It calculates the mean and sample standard deviation for:

- ICMP round-trip time (RTT)
- TCP throughput
- UDP jitter

### Generated figures

The figures are automatically saved in `results/figures/`.

The generated files include:

- `latency_comparison.png` and `latency_comparison.pdf`
- `throughput_comparison.png` and `throughput_comparison.pdf`
- `jitter_comparison.png` and `jitter_comparison.pdf`

### Original experimental measurements

The original measurements are organised as follows:

- `results/raw/latency/`: 15 ICMP measurement files
- `results/raw/throughput/`: 15 TCP iPerf3 JSON files
- `results/raw/jitter/`: 15 UDP iPerf3 JSON files
- `results/raw/resources/docker_baseline_raw.csv`: 300 baseline Docker resource observations
- `results/raw/resources/docker_embb_traffic_raw.csv`: 300 Docker resource observations during active eMBB traffic

The Python analysis script has been successfully tested against these
measurements and reproduces the RTT, TCP throughput and UDP jitter
statistics reported in `results/aggregate_results.csv` to the stated precision.

AMF, SMF and UPF CPU averages and ICMP/UDP packet delivery have been
verified against the preserved measurements. TCP retransmission totals
have been recalculated, but their discrepancy with the manuscript remains
unresolved. Full testbed reproduction requires additional validation.

## Experimental traffic endpoints and topology

The original iPerf3 JSON measurement records identify the following endpoints:

| Parameter | Value |
|---|---|
| UE-side client IP | `10.0.0.2` |
| iPerf3 server IP | `192.168.70.135` |
| iPerf3 server port | `5201` |
| Traffic direction | UE-side client to server |
| TCP test duration | 20 seconds |
| UDP test duration | 20 seconds |
| UDP target bitrate | 10 Mbps |

The current `oai-ext-dn` container has IP address `192.168.70.135` and gateway `192.168.70.129`, matching the server address in the original measurement records.

Recovered Bash history includes the command `docker exec -it oai-ext-dn iperf3 -s`, indicating that an iPerf3 server was started inside the external data network container during testing. A host-based server command was also found.

The available records strongly support `oai-ext-dn` as the intended server location, but do not conclusively establish the server process location during every original measurement.

The recorded IP addresses describe the experimental environment and may need adjustment when reproducing the testbed on another host.

### UE tunnel interface and routing

The experimental latency measurements used the OAI NR UE tunnel interface `oaitun_ue1`.

The recorded ping command was:

```bash
ping -I oaitun_ue1 -c 100 -i 0.2 -W 2 10.0.0.1
```

Five runs were performed for each network slice, with a five-second pause between runs.

Recovered Bash history also contains the following routing commands:

```bash
ip route get 10.0.0.1
sudo ip route add 10.0.0.1 dev oaitun_ue1
```

These commands show that routing was inspected and a manual route was added during testing. However, the available records do not confirm whether the manual route was active during the final measurements.

The original iPerf3 records identify `10.0.0.2` as the client address and `192.168.70.135` as the server address.

The complete routing table used during the original measurements was not preserved.

Researchers reproducing the experiments should verify the UE tunnel address, routing table and end-to-end connectivity before collecting measurements.

### Docker resource monitoring and sampling limitations

Docker container CPU and memory utilisation were measured under baseline and active eMBB traffic conditions.

The original measurements are preserved in:

- `results/raw/resources/docker_baseline_raw.csv`
- `results/raw/resources/docker_embb_traffic_raw.csv`

Each file contains 30 observations per container, recording container name, CPU utilisation percentage and memory usage.

Recovered Bash history confirms that Docker statistics were inspected using `docker stats`, including the `--no-stream` option.

However, the original CSV files do not contain timestamps, and the exact sampling interval could not be independently recovered.

Consequently, the reported CPU and memory averages are descriptive statistics of the recorded observations. No specific sampling frequency or time-series interpretation is claimed.

### TCP retransmission verification

The TCP retransmission values reported in the manuscript do not fully agree with the totals obtained from the preserved iPerf3 JSON measurements.

| Network slice | Manuscript retransmissions | Sum from preserved TCP JSON records |
|---|---:|---:|
| eMBB | 212 | 492 |
| URLLC | 26 | 90 |
| mMTC | 164 | 162 |

The JSON totals were calculated across five TCP measurement runs per network slice.

The original calculation method or source records supporting the manuscript values have not been independently established.

These differences remain unresolved. The repository preserves the original measurement files without modifying their contents.

Researchers should distinguish the manuscript values from the totals calculated using the preserved JSON records.
