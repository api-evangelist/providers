---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: Core TypeScript library distributed as the `better-auth` npm package. Configured in the application backend to expose sign-in / sign-up / session endpoints that the developer mounts under their own do
  name: Better Auth Library
  slug: library
- description: Project initialization and schema-migration CLI invoked with `npx @better-auth/cli` (or `npx auth init`). Generates database schema, configures the auth route handler, and scaffolds plugin wiring.
  name: Better Auth CLI
  slug: cli
- description: First-party plugin ecosystem covering two-factor authentication, passkeys, magic link, organizations and teams, API keys, generic OAuth, JWT, OpenAPI, admin, and SSO (SAML / OIDC). Plugins extend both
  name: Better Auth Plugins
  slug: plugins
- description: Optional managed dashboard at dash.better-auth.com. Adds user management UI, audit logs, security signals (breached-password lookups, bot protection, brute-force detection), and enterprise features su
  name: Better Auth Dashboard (Managed)
  slug: dashboard
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/better-auth/better-auth/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/better-auth/better-auth/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/better-auth/better-auth/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/better-auth/better-auth/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/better-auth/better-auth/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/better-auth/better-auth/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/better-auth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.better-auth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.better-auth.com/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/better-auth/better-auth
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/better-auth
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/better-auth
- group: other
  title: ''
  type: Dashboard
  url: https://dash.better-auth.com
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/better-auth
- group: company
  title: ''
  type: Blog
  url: https://better-auth.com/blog/rss.xml
created: '2026-05-23'
description: Better Auth is a framework-agnostic authentication and authorization library for TypeScript. Unlike hosted identity providers, Better Auth runs inside the developer's own application against their own database (Postgres, MySQL, SQLite, MongoDB via adapters). The core library supports credential, social, magic-link, OTP, passkey, and SSO sign-in, with plugins for organizations / teams / RBAC, API keys, two-factor authentication, JWT, generic OAuth, SAML / SSO, and SCIM. It integrates with Next.js, Nuxt, SvelteKit, Astro, Hono, and 20+ other frameworks. An optional managed dashboard with audit logs, breached-password detection, bot-protection, and self-service enterprise SSO is available at dash.better-auth.com.
finops:
- name: Better Auth Finops
  service_category: API
  slug: better-auth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/better-auth.png
layout: provider
modified: '2026-05-23'
name: Better Auth
nav: Providers
network: true
overview: 'Better Auth publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Authorization, TypeScript, Library, and Open Source.


  Better Auth''s developer surface includes documentation, GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Better Auth Plans Pricing
  plan_count: 1
  slug: better-auth-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Better Auth Rate Limits
  slug: better-auth-rate-limits
score:
  band: emerging
  composite: 20.9
  delta: -2.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 23.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Better Auth Domain Security
  slug: better-auth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: better-auth
tags:
- Authentication
- Authorization
- TypeScript
- Library
- Open Source
- SSO
- Passkeys
website: https://www.better-auth.com/
---
