---
title: "Your AI-Built App Is Probably Not Secure"
description: "AI builds things that work, but working and secure aren't the same thing. Here's where AI-generated code cuts corners on security and how to fix it."
pubDate: 2026-03-16
pubTime: "20:50"
tags: ["security", "ai", "supabase", "firebase", "rls"]
---

![A futuristic robot building a polished app with a visible open back door, oblivious to the security vulnerability](/blog/blog/securing-ai-apps-hero.webp)

You asked AI to build your app. It works. You deployed it. Users are signing up. Everything looks great until someone changes their own role to "admin" because your AI set up database policies that look correct but aren't. Now they have full access to every user's data, your admin dashboard, and whatever else that role unlocks.

AI builds things that work, but "works" and "secure" are not the same thing. The AI coding workflow has blind spots, and if you don't know where they are, your app is probably exposed right now.

Here's what to watch for and how to fix it.

## Your API Keys Are Showing

The most straightforward problem: AI puts secrets in client-side code.

AI grabs whichever key makes the code work. It doesn't think about where that code runs. A Supabase `service_role` key in your client code bypasses Row Level Security entirely. Game over. Same story with Firebase admin credentials or any third-party API key with broad permissions like a Stripe secret key.

```javascript
// AI does this more often than you'd think
const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SERVICE_ROLE_KEY // This bypasses ALL security
)
```

**The rule is simple: if a key is in code that ships to the browser, assume everyone has it.**

![A digital vault standing wide open with glowing API keys floating out into the void](/blog/blog/securing-ai-apps-keys.webp)

## The Anon Key Trap

"I'm using the anon key so I'm safe" is a false sense of security.

The anon key is public by design. It's in your JavaScript bundle. Everyone who visits your site has it. That's fine, because it's only supposed to work within the boundaries that Row Level Security sets.

The problem is when AI sets up RLS that's too loose. At that point the anon key can do almost everything, and your "public" key becomes a skeleton key. The anon key is only as safe as your RLS policies. If those policies have gaps, the anon key inherits every one of them.

## RLS Looks Right But Isn't

This is where it gets dangerous. RLS policies are rules that control who can read and write which rows in your database. AI generates these policies, they look reasonable at first glance, but they have critical gaps.

The most common mistake: users can update their own profile row, including the role column.

```sql
-- What AI typically generates
CREATE POLICY "Users can update own profile"
ON profiles FOR UPDATE
USING (auth.uid() = id);
-- Looks fine, right?
```

This policy lets a user run a simple update and own your entire app:

```sql
UPDATE profiles SET role = 'admin' WHERE id = 'my-user-id';
```

That's it. They're an admin now. Most people building with AI have custom tables with a concept of admin roles, and it's usually not locked down properly.

A better policy restricts which columns users can actually change:

```sql
-- Better: only allow updating safe columns
CREATE POLICY "Users can update own profile"
ON profiles FOR UPDATE
USING (auth.uid() = id)
WITH CHECK (
  role = (SELECT role FROM profiles WHERE id = auth.uid())
);
```

This ensures the role column stays unchanged. Even better: role changes should only happen through a server-side function that you control, never through direct client updates.

## Stop Rolling Your Own Auth

AI loves to build custom auth from scratch. You ask for login and signup, and it creates a users table with email, password hash, and a role column. It works, but it's missing everything that makes auth actually secure: rate limiting, session management, token rotation, password policies, email verification, brute force protection. Custom auth means custom vulnerabilities.

Use something battle-tested instead:

- <a href="https://www.better-auth.com/" target="_blank" rel="noopener noreferrer">better-auth</a> for TypeScript projects
- <a href="https://authjs.dev/" target="_blank" rel="noopener noreferrer">Auth.js</a> for Next.js
- Supabase Auth, which works with RLS out of the box
- Firebase Authentication

If you absolutely must keep custom auth: never let users write to their own role column, hash passwords with bcrypt or argon2, and use HTTP-only cookies for sessions.

## Context Slop and Round-Cornering

These two concepts explain why most of these issues happen in the first place.

**Context slop** is what happens as your AI conversation gets longer. You set up proper security in message 5, but by message 40 when you're adding a new feature, the AI has lost track of those constraints. It writes a new policy or endpoint that contradicts the security model it built earlier. The longer the conversation, the more your security model drifts.

**Round-cornering** is when AI hits a wall, like RLS blocking something or a permission denied error, and takes the shortest path to "working." That shortest path is almost always loosening security rather than writing a proper solution. AI doesn't flag this as a trade-off. It just does it and moves on.

Your prompts matter here. Be explicit about security requirements:

- Bad: "user need to be able to see their data in the dashboard."
- Good: "user need to be able to see their data in the dashboard, we need to setup the correct rls using userId and checks for columns that shouldnt be updated."

The more specific you are about security constraints, the less room AI has to cut corners.

![An AI robot casually cutting through a security wall with a laser instead of going around properly](/blog/blog/securing-ai-apps-corners.webp)

## Add a Security Audit to Your Workflow

You can't catch everything manually. A security audit skill acts as an automated red team for your codebase.

What ours does:

- Scans source code and build artifacts for exposed secrets and API keys
- Classifies findings and investigates actual permissions, not just pattern matching
- Checks dependencies against vulnerability databases for known CVEs
- Attempts to exploit found vulnerabilities to assess real severity
- Generates reports with severity ratings and remediation steps
- Can run as a pre-commit hook to catch issues before they ship

<a href="https://github.com/OrhayBenaim/blog/blob/main/.claude/skills/security-audit-skill/SKILL.md" target="_blank" rel="noopener noreferrer">Check out the security audit skill</a> and add it to your workflow.

## Ship Secure, Not Just Working

The AI workflow is powerful, but it optimizes for "working," not "secure." Every suggestion it makes is trying to get your code to run. That's a useful default until it starts quietly removing the guardrails you need.

The more aware you are of where AI cuts corners, the safer your apps will be. Be specific in your prompts, use battle-tested auth, lock down your RLS policies, and run a <a href="https://github.com/OrhayBenaim/blog/blob/main/.claude/skills/security-audit-skill/SKILL.md" target="_blank" rel="noopener noreferrer">security audit</a> before you deploy.
