# Replication checklist

- [x] Record current OAI Core container tags and image IDs (original experimental versions unconfirmed)
- [x] Document recovered gNB and UE launch commands (final measurement variant unconfirmed)
- [x] Add sanitized gNB, UE and core configuration files (full replication validation pending)
- [x] Describe subscriber provisioning without sharing keys
- [x] Document IP endpoints, traffic direction and likely iPerf3 server location (original server process unconfirmed; route details still require verification)
- [x] Document sequential profile selection (exact transition procedure unconfirmed)
- [x] Document available restart evidence and explicitly state that per-run restarts are unconfirmed
- [x] Add raw per-run RTT, throughput and jitter measurements
- [ ] Verify and document TCP retransmission records
- [x] Add original Docker CPU/memory records (30 observations per container per condition)
- [x] Document that original Docker statistics timestamps and sampling intervals could not be recovered
- [x] Confirm RTT, TCP throughput, UDP jitter and AMF/SMF/UPF CPU averages against raw data
- [x] Verify ICMP and UDP packet delivery against raw data; TCP retransmission totals recalculated, but manuscript discrepancy remains unresolved
- [ ] Remove secrets and seek CSIR publication approval
- [ ] Choose and add an approved open-source license
- [ ] Publish repository and record commit SHA / archived release DOI
