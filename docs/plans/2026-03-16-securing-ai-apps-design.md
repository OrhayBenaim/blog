# Securing AI-Built Apps - Blog Post Design

## Meta

- **Date:** 2026-03-16
- **Type:** Blog post
- **Target length:** ~1570 words
- **Audience:** Non-technical builders, vibe coders, people using AI to build apps without a security background
- **Tone:** Practical with story-driven elements
- **Assets:** 3 nanobanana-generated images, code snippets, prompt examples

## Title

TBD - something like "Your AI-Built App Is Probably Not Secure"

## Structure

### 1. Hook (~150 words)

Short relatable scenario: You asked AI to build your app. It works. You deployed it. Users are signing up. But someone just changed their own role to "admin" because your AI set up RLS policies that look correct but aren't.

Core message: **AI builds things that work, but "works" and "secure" are not the same thing.** The AI coding workflow has blind spots, and if you don't know where they are, your app is probably exposed right now.

Transition: "Here's what to watch for and how to fix it."

**Image:** Nanobanana - futuristic app with a visible crack/vulnerability, or a robot building a house with an open back door.

### 2. "Your API Keys Are Showing" (~200 words)

The straightforward problem: AI puts secrets in client-side code.

Key points:
- AI grabs whichever key makes the code work. It doesn't think about where that code runs.
- Supabase `service_role` key in client = bypasses RLS entirely. Game over.
- Firebase admin credentials in client = full database access.
- Same applies to any third-party API key with broad permissions (Stripe secret key, etc.)
- **Rule: if a key is in code that ships to the browser, assume everyone has it.**

Short example showing a service_role key sitting in client code.

**Image:** Nanobanana - exposed keys / open vault concept.

### 3. "The Anon Key Trap" (~200 words)

The subtler problem: you used the right key but your RLS makes it irrelevant.

Key points:
- "I'm using the anon key so I'm safe" is a false sense of security
- The anon key is public by design. It's in your JS bundle. Everyone has it.
- It's only safe because RLS is supposed to restrict what it can do
- AI sets up RLS that's too loose, so the anon key can do almost everything
- **The anon key is only as safe as your RLS policies**

Transitions into RLS deep-dive.

### 4. "RLS Looks Right But Isn't" (~350 words)

The meat of the post. RLS explained in plain terms: rules that control who can read/write what rows in your database.

Key points:
- AI generates RLS policies that look correct but have critical gaps
- Most common mistake: users can update their own profile row, **including the role column**. A simple `UPDATE profiles SET role = 'admin' WHERE id = my_id` and they own your app.
- Most people rolling their own auth have custom tables with a concept of admin, and it's usually not set up right
- Context slop and round-cornering (explained in section 6) are why this happens

Code examples (short, not full snippets):
- A bad RLS policy that lets users update their own row (including role)
- A better policy that excludes the role column from user updates
- Note that role changes should only happen through a server-side function

### 5. "Stop Rolling Your Own Auth" (~200 words)

AI loves to build custom auth. You ask for login/signup and it creates a users table with email, password hash, and a role column. It works, but it's missing everything that makes auth actually secure.

Key points:
- AI-generated auth typically misses: rate limiting, session management, token rotation, password policies, email verification, brute force protection
- Custom auth means custom vulnerabilities

Battle-tested alternatives (with links):
- [better-auth](https://www.better-auth.com/) for TypeScript projects
- Supabase Auth (built-in, works with RLS out of the box)
- Firebase Authentication
- [Auth.js](https://authjs.dev/) for Next.js

- If you must keep custom auth: never let users write to their own role column, hash passwords with bcrypt/argon2, use HTTP-only cookies for sessions

### 6. "Context Slop and Round-Cornering" (~250 words)

The *why* behind most of the issues. These two concepts explained in plain language.

**Context slop:**
- AI has a conversation window. As your chat gets longer, earlier context fades.
- You set up proper security in message 5, but by message 40 when adding a new feature, the AI has lost track of those constraints.
- It writes a new policy or endpoint that contradicts the security model it built earlier.

**Round-cornering:**
- When AI hits a wall (RLS blocking something, permission denied), it takes the shortest path to "working."
- That shortest path is almost always loosening security rather than writing a proper solution.
- AI doesn't flag this as a trade-off. It just does it and moves on.

**Prompt examples:**
- Bad: "user need to be able to see their data in the dashboard."
- Good: "user need to be able to see their data in the dashboard, we need to setup the correct rls using user id."

**Image:** Nanobanana - AI cutting corners or taking shortcuts around a security wall.

### 7. "Add a Security Audit to Your Workflow" (~120 words)

You can't catch everything manually. A security audit skill acts as an automated red team.

What ours does (bullet points):
- Scans source code and build artifacts for exposed secrets and API keys
- Classifies findings and investigates actual permissions (not just pattern matching)
- Checks dependencies against vulnerability databases for known CVEs
- Attempts to exploit found vulnerabilities to assess real severity
- Generates reports with severity ratings and remediation steps
- Can run as a pre-commit hook to catch issues before they ship

**Link to the security audit skill** + "Add it to your workflow and run it before you deploy."

### 8. Closing (~100 words)

The AI workflow is powerful but it optimizes for "working," not "secure." The more aware you are of where it cuts corners, the safer your apps will be.

Link back to the security audit skill.
