#!/usr/bin/env python3

import os
from pathlib import Path
import yaml

base = Path(__file__).resolve().parent.parent

template = base / "conf/config.template.yaml"
output = base / "conf/config.runtime.yaml"

password = os.environ.get("MYSQL_PASSWORD")

if not password:
    raise SystemExit(
        "ERROR: MYSQL_PASSWORD is not configured."
    )

config = yaml.safe_load(template.read_text())

if config["database"].get("password") != "__MYSQL_PASSWORD__":
    raise SystemExit(
        "ERROR: Unexpected database password placeholder."
    )

config["database"]["password"] = password

# Restrict access to the generated file.
import os as operating_system

fd = operating_system.open(
    output,
    operating_system.O_WRONLY
    | operating_system.O_CREAT
    | operating_system.O_TRUNC,
    0o600
)

with operating_system.fdopen(fd, "w") as file:
    yaml.safe_dump(config, file, sort_keys=False)

output.chmod(0o600)

print("===== OAI CORE CONFIGURATION =====")
print("Runtime configuration generated:", output)
print("Database password configured: True")
print("File permissions: 600")
print("Password was not displayed.")
