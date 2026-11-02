# Seat templates

Minimal templates for an AlloyScape tribe seat using the think-server pattern.

## Scaffold layout

```text
templates/seat/
  README.md
  soul.system.md
  start-SEAT-think.sh
  SEAT-home.html
  nginx.snippet.conf
```

Copy `templates/seat/`, replace the documented placeholders, choose a unique
`THINK_PORT`, and validate the result before enabling the service or proxy.

## Rules

- Use a collision-free `THINK_PORT`.
- Probe the local service before exposing it through nginx.
- Treat `soul.system.md` as the seat identity source of truth.
- Keep credentials out of templates and committed files.
- Bind the think server to loopback; let the reverse proxy handle public traffic.

## Validation

```bash
python tools/validate_templates.py
bash -n templates/seat/start-SEAT-think.sh
```
