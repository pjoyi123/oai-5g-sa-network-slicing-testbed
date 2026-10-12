# Replication checklist

- [ ] Add OAI Core container tags and image digests
- [ ] Add exact gNB and UE launch commands
- [ ] Add sanitized actual gNB, UE and core configs
- [ ] Describe subscriber provisioning without sharing keys
- [ ] Describe IP endpoints, route, traffic direction and iperf3 server
- [ ] Explain how profiles were changed between sequential runs
- [ ] Explain whether processes were restarted between measurement runs
- [x] Add raw per-run RTT, throughput and jitter measurements
- [ ] Verify and document TCP retransmission records
- [x] Add original Docker CPU/memory records (30 observations per container per condition)
- [ ] Recover or document Docker stats sampling timestamps and intervals
- [x] Confirm RTT, TCP throughput, UDP jitter and AMF/SMF/UPF CPU averages against raw data
- [ ] Verify packet delivery and TCP retransmission results against raw data
- [ ] Remove secrets and seek CSIR publication approval
- [ ] Choose and add an approved open-source license
- [ ] Publish repository and record commit SHA / archived release DOI
