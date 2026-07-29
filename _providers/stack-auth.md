---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Stack Auth Agentic Access
  operation_count: 45
  slug: stack-auth-agentic-access
  summary_line: 45 operations · 28 acting
api_count: 5
apis:
- description: REST API for managing users, sessions, OAuth providers, teams, organizations, permissions, and webhooks. Used by Stack Auth's own SDKs and available for custom backend integrations. JWT-based authenti
  name: Stack Auth REST API
  slug: rest-api
- description: Outbound webhook events for user lifecycle, team / organization membership, and permission changes. Customers register endpoint URLs and verify delivery via signed payloads.
  name: Stack Auth Webhooks
  slug: webhooks
- description: Frontend SDK distributed as @stackframe/stack on npm. Provides React components, hooks, and Next.js App Router middleware for sign-in, sign-up, account settings, and team / organization management. He
  name: Stack Auth React / Next.js SDK
  slug: sdk-react
- description: Project bootstrap CLI distributed as @stackframe/init-stack on npm, invoked with `npx @stackframe/init-stack@latest` to wire Stack Auth into a new or existing project.
  name: Stack Auth CLI
  slug: cli
- description: Open-source monorepo containing the Stack Auth backend (Next.js + Postgres) and dashboard. Deployable on customer infrastructure as an alternative to the hosted SaaS at app.stack-auth.com.
  name: Stack Auth Self-Hosted (stack-auth/stack)
  slug: self-hosted
artifact_total: 12
collections:
- collection_type: open
  name: Stack Auth REST API
  slug: open-stack-auth
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/stack-auth-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stack-auth-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stack-auth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stack-auth-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://stack-auth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stack-auth.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/stack-auth
- group: other
  title: ''
  type: Dashboard
  url: https://app.stack-auth.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://stack-auth.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://stack-auth.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.stack-auth.com/llms.txt
created: '2026-05-23'
description: Stack Auth is an open-source authentication and user management platform positioned as a self-hostable alternative to closed-source providers like Clerk and Auth0. It bundles password, OAuth / SSO, and two-factor sign-in flows with organizations, teams, role-based access control, impersonation, webhooks, and pre-built UI components built on shadcn/ui (or a headless SDK). Stack Auth is available as a hosted SaaS at app.stack-auth.com and as a self-hosted deployment from the stack-auth/stack monorepo on GitHub. Authentication is JWT-based. Y Combinator-backed.
finops:
- name: Stack Auth Finops
  service_category: API
  slug: stack-auth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-23'
name: Stack Auth
nav: Providers
network: true
overview: 'Stack Auth publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, User Management, Open Source, Self-Hosted, and Identity.


  Stack Auth''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Stack Auth Plans Pricing
  plan_count: 1
  slug: stack-auth-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 2
  name: Stack Auth Rate Limits
  slug: stack-auth-rate-limits
score:
  band: emerging
  composite: 25.1
  delta: -12.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/stack-auth/refs/heads/main/screenshots/stack-auth-2026-06-20T194441.png
security:
- kind: authentication
  name: Stack Auth Authentication
  slug: stack-auth-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Stack Auth Domain Security
  slug: stack-auth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stack-auth
tags:
- Authentication
- User Management
- Open Source
- Self-Hosted
- Identity
- Organizations
- RBAC
website: https://stack-auth.com/
---
