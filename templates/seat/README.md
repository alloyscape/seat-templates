# `{{SEAT}}` seat template

Replace these placeholders before use:

- `{{SEAT}}`: the public seat name.
- `{{THINK_PORT}}`: a unique loopback port for the think server.

Then review `soul.system.md`, run `bash -n start-SEAT-think.sh`, start the
service locally, and confirm it responds on `127.0.0.1:{{THINK_PORT}}` before
installing the nginx snippet.

The templates intentionally contain no credentials. Supply runtime secrets
through the deployment environment.
