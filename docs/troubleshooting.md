
# Troubleshooting

## GENERATE_SYNTHETIC_DATA not found

Cause:
Snowflake native synthetic generation is unavailable.

Fix:
Use fallback empirical generation.

---

## Internal SQL execution error 370001

Cause:
Unsupported object complexity.

Fix:
Use fallback mode.

---

## TOK_STAR unsupported

Cause:
Unsupported SQL constructs.

Fix:
Materialize complex views.

---

## Empty _SYN table

Cause:
Insert/type mismatch issue.

Fix:
Validate datatype casting.
