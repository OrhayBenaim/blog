# API Key Detection Patterns

## Classification System

Keys are classified into two categories:

### OBVIOUS - Report Immediately (Critical/High)
Keys that should never appear in source or build artifacts. No investigation needed.

### INVESTIGATE - Check Permissions First
Keys that may be intentionally public (e.g., Supabase anon key, Firebase client config) but could have dangerous permissions attached.

---

## Pattern Definitions

### AWS

| Pattern | Regex | Classification |
|---------|-------|----------------|
| AWS Access Key ID | `AKIA[0-9A-Z]{16}` | OBVIOUS |
| AWS Secret Access Key | `(?i)aws_secret_access_key\s*[=:]\s*[A-Za-z0-9/+=]{40}` | OBVIOUS |
| AWS Session Token | `(?i)aws_session_token\s*[=:]\s*[A-Za-z0-9/+=]+` | OBVIOUS |

### Google Cloud / Firebase

| Pattern | Regex | Classification |
|---------|-------|----------------|
| GCP API Key | `AIza[0-9A-Za-z\-_]{35}` | OBVIOUS |
| GCP Service Account JSON | `"type"\s*:\s*"service_account"` | OBVIOUS |
| Firebase Client Config | `(?i)firebase(?:Config\|app).*apiKey` | INVESTIGATE |

### GitHub

| Pattern | Regex | Classification |
|---------|-------|----------------|
| GitHub Personal Access Token (classic) | `ghp_[0-9a-zA-Z]{36}` | OBVIOUS |
| GitHub Fine-Grained PAT | `github_pat_[0-9a-zA-Z_]{82}` | OBVIOUS |
| GitHub OAuth App Token | `gho_[0-9a-zA-Z]{36}` | OBVIOUS |
| GitHub App Installation Token | `ghs_[0-9a-zA-Z]{36}` | OBVIOUS |

### Stripe

| Pattern | Regex | Classification |
|---------|-------|----------------|
| Stripe Secret Key | `sk_live_[0-9a-zA-Z]{24,}` | OBVIOUS |
| Stripe Restricted Key | `rk_live_[0-9a-zA-Z]{24,}` | OBVIOUS |
| Stripe Publishable Key | `pk_live_[0-9a-zA-Z]{24,}` | INVESTIGATE |

### Supabase

| Pattern | Regex | Classification |
|---------|-------|----------------|
| Supabase Service Role Key | `(?i)supabase.*service.role.*eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+` | OBVIOUS |
| Supabase Anon Key | `(?i)supabase.*anon.*eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+` | INVESTIGATE |

### Database

| Pattern | Regex | Classification |
|---------|-------|----------------|
| PostgreSQL Connection String | `postgres(?:ql)?://[^:]+:[^@]+@[^/]+` | OBVIOUS |
| MongoDB Connection String | `mongodb(?:\+srv)?://[^:]+:[^@]+@` | OBVIOUS |
| Redis URL with Password | `redis://:[^@]+@` | OBVIOUS |
| MySQL Connection String | `mysql://[^:]+:[^@]+@` | OBVIOUS |

### Auth / JWT

| Pattern | Regex | Classification |
|---------|-------|----------------|
| Generic JWT Secret | `(?i)(?:jwt_secret\|jwt_key\|secret_key)\s*[=:]\s*["'][^"']{8,}["']` | OBVIOUS |
| Generic Private Key Block | `-----BEGIN (?:RSA\|EC\|DSA\|OPENSSH) PRIVATE KEY-----` | OBVIOUS |

### SendGrid / Mailgun / Twilio

| Pattern | Regex | Classification |
|---------|-------|----------------|
| SendGrid API Key | `SG\.[0-9A-Za-z\-_]{22}\.[0-9A-Za-z\-_]{43}` | OBVIOUS |
| Mailgun API Key | `key-[0-9a-zA-Z]{32}` | OBVIOUS |
| Twilio Auth Token | `(?i)twilio.*[0-9a-f]{32}` | OBVIOUS |

### OpenAI / Anthropic

| Pattern | Regex | Classification |
|---------|-------|----------------|
| OpenAI API Key | `sk-[0-9a-zA-Z]{20}T3BlbkFJ[0-9a-zA-Z]{20}` | OBVIOUS |
| OpenAI Project Key | `sk-proj-[0-9a-zA-Z_-]{80,}` | OBVIOUS |
| Anthropic API Key | `sk-ant-[0-9a-zA-Z_-]{80,}` | OBVIOUS |

### Slack

| Pattern | Regex | Classification |
|---------|-------|----------------|
| Slack Bot Token | `xoxb-[0-9]{10,}-[0-9a-zA-Z]{24,}` | OBVIOUS |
| Slack User Token | `xoxp-[0-9]{10,}-[0-9]{10,}-[0-9a-zA-Z]{24,}` | OBVIOUS |
| Slack Webhook URL | `https://hooks\.slack\.com/services/T[0-9A-Z]+/B[0-9A-Z]+/[0-9a-zA-Z]+` | OBVIOUS |

### Generic / Catch-all

| Pattern | Regex | Classification |
|---------|-------|----------------|
| Generic API Key Assignment | `(?i)(?:api_key\|apikey\|api_secret\|secret_key)\s*[=:]\s*["'][0-9a-zA-Z]{16,}["']` | INVESTIGATE |
| Generic Password Assignment | `(?i)(?:password\|passwd\|pwd)\s*[=:]\s*["'][^"']{8,}["']` | INVESTIGATE |
| Bearer Token in Code | `(?i)(?:authorization\|bearer)\s*[=:]\s*["']Bearer\s+[0-9a-zA-Z._-]+["']` | OBVIOUS |

---

## Investigation Procedures for INVESTIGATE Keys

### Supabase Anon Key
1. Decode the JWT payload (base64)
2. Check `role` claim - should be `anon`
3. Use curl to test RLS: `curl -H "apikey: <key>" -H "Authorization: Bearer <key>" <supabase_url>/rest/v1/<table>`
4. If RLS is disabled or overly permissive, escalate to CRITICAL
5. Check if key grants access to storage buckets, edge functions, or realtime channels

### Stripe Publishable Key
1. Publishable keys are designed to be public (used in frontend)
2. Check if the corresponding secret key is also exposed nearby
3. Verify it is not a test key being used in production context
4. Low risk unless paired with secret key exposure

### Firebase Client Config
1. Firebase client configs are semi-public by design
2. Check Firestore/RTDB security rules - if rules allow unauthenticated write, escalate
3. Check if Firebase Admin SDK key is also exposed
4. Test with curl: `curl https://firestore.googleapis.com/v1/projects/<project>/databases/(default)/documents/<collection>`

### Generic API Key / Password
1. Identify the service the key belongs to from surrounding code context
2. Check if the value looks like a placeholder (e.g., "YOUR_API_KEY", "changeme")
3. If real, attempt to identify the service and check permissions
4. Report with context about what the key appears to control
