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
  band: agent-aware
  dimensions:
    agent_card: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Snov Agentic Access
  operation_count: 37
  slug: snov-agentic-access
  summary_line: 37 operations · 22 acting
api_count: 10
apis:
- description: The Authentication API from Snov.io — 1 operation(s) for authentication.
  name: Snov.io Authentication API
  slug: snov-authentication-api
- description: The Campaigns API from Snov.io — 5 operation(s) for campaigns.
  name: Snov.io Campaigns API
  slug: snov-campaigns-api
- description: The Domain Search API from Snov.io — 9 operation(s) for domain search.
  name: Snov.io Domain Search API
  slug: snov-domain-search-api
- description: The Email Finder API from Snov.io — 4 operation(s) for email finder.
  name: Snov.io Email Finder API
  slug: snov-email-finder-api
- description: The Email Verifier API from Snov.io — 2 operation(s) for email verifier.
  name: Snov.io Email Verifier API
  slug: snov-email-verifier-api
- description: The Enrichment API from Snov.io — 3 operation(s) for enrichment.
  name: Snov.io Enrichment API
  slug: snov-enrichment-api
- description: The Prospects API from Snov.io — 4 operation(s) for prospects.
  name: Snov.io Prospects API
  slug: snov-prospects-api
- description: The Sender Accounts API from Snov.io — 3 operation(s) for sender accounts.
  name: Snov.io Sender Accounts API
  slug: snov-sender-accounts-api
- description: The User API from Snov.io — 1 operation(s) for user.
  name: Snov.io User API
  slug: snov-user-api
- description: The Warm-up API from Snov.io — 2 operation(s) for warm-up.
  name: Snov.io Warm-up API
  slug: snov-warm-up-api
artifact_total: 18
collections:
- collection_type: open
  name: Snov.io API
  slug: open-snov
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snov-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/snov-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snov-io
- group: company
  title: ''
  type: Website
  url: https://snov.io
- group: docs
  title: ''
  type: Documentation
  url: https://snov.io/api
- group: commercial
  title: ''
  type: Plans
  url: plans/snov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/snov-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://snov.io/blog
created: '2026-07-01'
description: Snov.io is a sales engagement platform providing email finder, email verification, prospect and list management, multichannel drip campaigns, sender account and warm-up management, and a lightweight sales CRM. Its REST API uses an OAuth2 client_credentials access token and mixes form-encoded v1 endpoints with a v2 asynchronous start/result (task_hash) pattern for search and verification.
finops:
- name: Snov Finops
  service_category: Sales and Marketing
  slug: snov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snov.png
layout: provider
modified: '2026-07-01'
name: Snov.io
nav: Providers
network: true
overview: 'Snov.io publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Campaigns API, Domain Search API, and 7 more. Tagged areas include Sales Engagement, Email Finder, Email Verification, Prospecting, and Drip Campaigns.


  Snov.io''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Snov Plans Pricing
  plan_count: 5
  slug: snov-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 4
  name: Snov Rate Limits
  slug: snov-rate-limits
scopes:
- name: Snov Scopes
  scope_count: 0
  slug: snov-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.9
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Snov Authentication
  slug: snov-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Snov Domain Security
  slug: snov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snov
tags:
- Sales Engagement
- Email Finder
- Email Verification
- Prospecting
- Drip Campaigns
- CRM
- Lead Generation
website: https://snov.io
---
