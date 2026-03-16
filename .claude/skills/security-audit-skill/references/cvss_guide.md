# CVSS Severity Rating Guide

## Severity Scale

| Severity | CVSS Score | Action Required | Description |
|----------|-----------|----------------|-------------|
| **Critical** | 9.0 - 10.0 | Immediate fix required | Actively exploitable, no special setup needed, high impact |
| **High** | 7.0 - 8.9 | Fix before next release | Exploitable but requires some conditions or setup |
| **Medium** | 4.0 - 6.9 | Plan fix in backlog | Requires significant setup or has limited impact |
| **Low** | 0.1 - 3.9 | Track and monitor | Theoretical risk, very difficult to exploit |
| **Info** | 0.0 | No action needed | Best practice recommendation, no direct security risk |

## CVSS v3.1 Vector Components

### Attack Vector (AV)
- **Network (N)**: Exploitable remotely via network
- **Adjacent (A)**: Requires same network segment
- **Local (L)**: Requires local system access
- **Physical (P)**: Requires physical device access

### Attack Complexity (AC)
- **Low (L)**: No special conditions needed
- **High (H)**: Requires specific configuration or race condition

### Privileges Required (PR)
- **None (N)**: No authentication needed
- **Low (L)**: Basic user privileges
- **High (H)**: Admin/elevated privileges

### User Interaction (UI)
- **None (N)**: No user action needed
- **Required (R)**: Victim must perform an action

### Scope (S)
- **Unchanged (U)**: Impact limited to vulnerable component
- **Changed (C)**: Impact extends beyond vulnerable component

### Impact (C/I/A - Confidentiality/Integrity/Availability)
- **High (H)**: Total loss
- **Low (L)**: Partial loss
- **None (N)**: No impact

## Common Finding Severity Mappings

### Critical (9.0-10.0)
- Exposed AWS Secret Key or GCP Service Account with broad permissions
- Exposed database connection strings to production databases
- Private keys (RSA, SSH) in source or build artifacts
- Hardcoded admin credentials
- Known RCE vulnerability in framework (confirmed exploitable)
- SQL injection in authentication endpoint
- CVSS: `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

### High (7.0-8.9)
- Exposed API keys with write/delete permissions (Stripe secret, SendGrid)
- Known framework vulnerability with public exploit (requires specific config)
- XSS in authenticated area with session stealing potential
- SSRF with internal network access
- Exposed JWT signing secret
- CVSS: `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Medium (4.0-6.9)
- Supabase anon key with weak RLS policies
- Framework vulnerability without public exploit
- Information disclosure (stack traces, debug endpoints)
- Missing security headers (CORS misconfiguration)
- Outdated dependency with known vulnerability (not directly exploitable in current config)
- CVSS: `AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:L/A:N`

### Low (0.1-3.9)
- Publishable/public keys that are designed to be client-facing
- Outdated dependency with theoretical vulnerability
- Missing non-critical security headers
- Verbose error messages in non-production builds
- CVSS: `AV:N/AC:H/PR:H/UI:R/S:U/C:L/I:N/A:N`

### Info (0.0)
- Dependencies approaching end-of-life
- Security best practice recommendations
- Configuration improvements

## Report Format Per Finding

Each finding in the report should include:

```
### [SEVERITY] Finding Title

**CVSS Score:** X.X
**CVSS Vector:** AV:X/AC:X/PR:X/UI:X/S:X/C:X/I:X/A:X
**Location:** file_path:line_number
**Category:** [Exposed Secret | Vulnerable Dependency | Code Vulnerability | Misconfiguration]

**Description:**
What was found and why it matters.

**Evidence:**
The specific match or proof.

**Remediation:**
Step-by-step fix instructions.

**References:**
- CVE links if applicable
- Documentation links
```
