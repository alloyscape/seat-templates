# Seat templates

Cookie-cutter for AlloyScape tribe seats (think-server pattern).

## Live references (Hetzner)

| Seat | Port | Pattern |
|------|------|---------|
| Aegis | 8171 | Shield · full toolbelt |
| Sage | 8176 | Money/structure · force |
| Elysium | 8174 | 911 aftercare |
| Moros | 8173 | 911 pre-weight |

## Scaffold layout

```
templates/seat/
  soul.system.md
  start-SEAT-think.sh
  SEAT-home.html
  nginx.snippet.conf
  README.md
```

## Rules

- Collision-free THINK_PORT
- Probe-before-invite
- Soul file is identity source of truth
- No secrets in templates
