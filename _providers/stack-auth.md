---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://stack-auth.com/'', ''status'': 308, ''note'': ''declared website redirects to https://www.hexclave.com/ — a different registrable domain (stack-auth.com -> hexclave.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Stack Auth Agentic Access
  operation_count: 45
  slug: stack-auth-agentic-access
  summary_line: 45 operations · 28 acting
api_count: 1
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
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Auth API from Stack Auth — 4 operation(s) for auth.
  name: Stack Auth Auth API
  slug: stack-auth-auth-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Connected Accounts API from Stack Auth — 1 operation(s) for connected accounts.
  name: Stack Auth Connected Accounts API
  slug: stack-auth-connected-accounts-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Contact Channels API from Stack Auth — 4 operation(s) for contact channels.
  name: Stack Auth Contact Channels API
  slug: stack-auth-contact-channels-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Emails API from Stack Auth — 2 operation(s) for emails.
  name: Stack Auth Emails API
  slug: stack-auth-emails-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Sessions API from Stack Auth — 3 operation(s) for sessions.
  name: Stack Auth Sessions API
  slug: stack-auth-sessions-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Stack Auth REST API API from Stack Auth — 1 operation(s) for stack auth rest api.
  name: Stack Auth Stack Auth REST API API
  slug: stack-auth-stack-auth-rest-api-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Team Api Keys API from Stack Auth — 3 operation(s) for team api keys.
  name: Stack Auth Team Api Keys API
  slug: stack-auth-team-api-keys-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Team Memberships API from Stack Auth — 1 operation(s) for team memberships.
  name: Stack Auth Team Memberships API
  slug: stack-auth-team-memberships-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Team Permissions API from Stack Auth — 1 operation(s) for team permissions.
  name: Stack Auth Team Permissions API
  slug: stack-auth-team-permissions-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Teams API from Stack Auth — 2 operation(s) for teams.
  name: Stack Auth Teams API
  slug: stack-auth-teams-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The User Api Keys API from Stack Auth — 3 operation(s) for user api keys.
  name: Stack Auth User Api Keys API
  slug: stack-auth-user-api-keys-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Users API from Stack Auth — 2 operation(s) for users.
  name: Stack Auth Users API
  slug: stack-auth-users-api
- baseURL: https://api.stack-auth.com
  baseurl_source: declared
  description: The Webhooks API from Stack Auth — 1 operation(s) for webhooks.
  name: Stack Auth Webhooks API
  slug: stack-auth-webhooks-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stack REST Auth API
  slug: open-stack-auth-auth-api
- collection_type: open
  name: Stack REST Auth Connected Accounts API
  slug: open-stack-auth-connected-accounts-api
- collection_type: open
  name: Stack REST Auth Contact Channels API
  slug: open-stack-auth-contact-channels-api
- collection_type: open
  name: Stack REST Auth Emails API
  slug: open-stack-auth-emails-api
- collection_type: open
  name: Stack REST Auth Sessions API
  slug: open-stack-auth-sessions-api
- collection_type: open
  name: Stack REST Auth Stack Auth REST API API
  slug: open-stack-auth-stack-auth-rest-api-api
- collection_type: open
  name: Stack REST Auth Team Api Keys API
  slug: open-stack-auth-team-api-keys-api
- collection_type: open
  name: Stack REST Auth Team Memberships API
  slug: open-stack-auth-team-memberships-api
- collection_type: open
  name: Stack REST Auth Team Permissions API
  slug: open-stack-auth-team-permissions-api
- collection_type: open
  name: Stack REST Auth Teams API
  slug: open-stack-auth-teams-api
- collection_type: open
  name: Stack REST Auth User Api Keys API
  slug: open-stack-auth-user-api-keys-api
- collection_type: open
  name: Stack REST Auth Users API
  slug: open-stack-auth-users-api
- collection_type: open
  name: Stack REST Auth Webhooks API
  slug: open-stack-auth-webhooks-api
- collection_type: open
  name: Stack Auth REST API
  slug: open-stack-auth
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/stack-auth/stack/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/stack-auth/stack/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/hexclave/hexclave/blob/dev/CONTRIBUTING.md
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
overview: 'Stack Auth publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Connected Accounts API, Contact Channels API, and 10 more. Tagged areas include Authentication, User Management, Open-Source, Self-Hosted, and Identity.


  Stack Auth''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Stack Auth Plans Pricing
  plan_count: 1
  slug: stack-auth-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Stack Auth Rate Limits
  slug: stack-auth-rate-limits
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 1.8
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
- Open-Source
- Self-Hosted
- Identity
- Organization
- RBAC
website: https://stack-auth.com/
---
