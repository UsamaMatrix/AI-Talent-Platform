# Security Policy

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Email: security@example.com (replace with real contact before going public)

We will respond within 72 hours and aim to release a fix within 14 days for critical issues.

## Supported versions

| Version | Supported |
|---|---|
| `main` | ✅ |

## Code execution warning

The Coding Interview module executes untrusted candidate code inside an isolated sandbox.

The sandbox enforces:
- Non-root user
- No privileged mode
- No host Docker socket mount
- Read-only root filesystem where possible
- Dropped Linux capabilities
- No outbound network
- CPU, memory, process, output and time limits
- Temporary isolated workspace per execution
- Cleanup after every run

Docker isolation alone is **not** considered a complete security boundary. The runner abstraction is designed to support Firecracker, gVisor, Kata Containers or a remote sandbox provider.

**Never execute candidate code in the API or worker container.**

## Input validation

All uploaded files, resumes, model responses, job descriptions and code submissions are treated as untrusted input. Validation includes file type, extension, MIME type and size checks.

## Prompt injection

All LLM inputs are validated and sanitized. System prompts are separated from user content. Model outputs are validated before use.

## Data privacy

Resume and interview data may contain personal information. See the data privacy section in the project rules for retention, deletion and export requirements.

## Dependency scanning

Dependencies are scanned on every pull request via GitHub Actions dependency review and Dependabot alerts.
