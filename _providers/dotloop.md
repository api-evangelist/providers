---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Dotloop Agentic Access
  operation_count: 43
  slug: dotloop-agentic-access
  summary_line: 43 operations · 18 acting
api_count: 13
apis:
- description: The authenticated dotloop account.
  name: dotloop Account API
  slug: dotloop-account-api
- description: Read-only loop activity feed.
  name: dotloop Activities API
  slug: dotloop-activities-api
- description: The authenticated user's contacts (address book).
  name: dotloop Contacts API
  slug: dotloop-contacts-api
- description: Documents within a loop folder.
  name: dotloop Documents API
  slug: dotloop-documents-api
- description: Folders that organize documents within a loop.
  name: dotloop Folders API
  slug: dotloop-folders-api
- description: Structured detail fields of a loop.
  name: dotloop Loop Details API
  slug: dotloop-loop-details-api
- description: Single-call loop creation facade.
  name: dotloop Loop It API
  slug: dotloop-loop-it-api
- description: Reusable transaction blueprints under a profile.
  name: dotloop Loop Templates API
  slug: dotloop-loop-templates-api
- description: Loops (real estate transactions).
  name: dotloop Loops API
  slug: dotloop-loops-api
- description: Parties to a loop.
  name: dotloop Participants API
  slug: dotloop-participants-api
- description: Individual, team, and brokerage profiles that scope loops.
  name: dotloop Profiles API
  slug: dotloop-profiles-api
- description: Task lists and task items on a loop.
  name: dotloop Tasks API
  slug: dotloop-tasks-api
- description: Webhook subscriptions and delivered events.
  name: dotloop Webhooks API
  slug: dotloop-webhooks-api
artifact_total: 21
collections:
- collection_type: open
  name: dotloop Public API v2
  slug: open-dotloop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dotloop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dotloop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dotloop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dotloop-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotloop
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dotloop
- group: company
  title: ''
  type: Website
  url: https://www.dotloop.com
- group: docs
  title: ''
  type: Documentation
  url: https://dotloop.github.io/public-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dotloop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dotloop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dotloop-finops.yml
created: '2026-07-04'
description: dotloop is a real estate transaction management platform (owned by Zillow Group) that lets agents, teams, and brokerages create and manage transactions - called "loops" - end to end, including documents, e-signatures, tasks, participants, and compliance workflows. The dotloop Public API v2 is a documented, OAuth2-secured JSON REST API at https://api-gateway.dotloop.com/public/v2 that exposes accounts, profiles, loops and loop details, folders, documents, participants, tasks, activities, contacts, loop templates, and webhook subscriptions, plus a Loop-It facade for one-call loop creation.
finops:
- name: Dotloop Finops
  service_category: Business Applications
  slug: dotloop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dotloop.png
layout: provider
modified: '2026-07-04'
name: dotloop
nav: Providers
network: true
overview: 'dotloop publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Activities API, Contacts API, and 10 more. Tagged areas include Real Estate, Transaction Management, Loops, Documents, and E-Signature.


  dotloop''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Dotloop Plans Pricing
  plan_count: 4
  slug: dotloop-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Dotloop Rate Limits
  slug: dotloop-rate-limits
scopes:
- name: Dotloop Scopes
  scope_count: 8
  slug: dotloop-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: thin
  composite: 39.0
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.9
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dotloop/refs/heads/main/screenshots/dotloop-2026-07-25T212314.png
security:
- kind: authentication
  name: Dotloop Authentication
  slug: dotloop-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Dotloop Domain Security
  slug: dotloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dotloop
tags:
- Real Estate
- Transaction Management
- Loops
- Documents
- E-Signature
- Zillow Group
website: https://www.dotloop.com
---
