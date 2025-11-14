import json
from datetime import datetime

# Load contributors
with open("contributors.json", "r") as f:
    contributors = json.load(f)

# Rotate order
contributors = contributors[1:] + [contributors[0]]

# Save updated list
with open("contributors.json", "w") as f:
    json.dump(contributors, f, indent=2)

# Log mutation
with open("mutation_log.md", "a") as log:
    log.write(f"\n## Mutation #{len(contributors)+39}: Contributor Rotation\n")
    log.write(f"**Date**: {datetime.utcnow().isoformat()}Z\n")
    log.write(f"**Rotated to**: {contributors[0]['name']}\n")
    log.write("> “The wheel turned. The next builder stepped forward.”\n")
