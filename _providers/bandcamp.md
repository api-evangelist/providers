---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
- acting_count: 12
  human_in_the_loop: 0
  name: Bandcamp Agentic Access
  operation_count: 12
  slug: bandcamp-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 7
apis:
- description: Account API for retrieving the list of bands a user manages and basic account metadata. OAuth 2.0 client credentials with token endpoint at /oauth_token; access tokens expire after one hour.
  name: Bandcamp Account API
  slug: account
- description: 'Sales Report API for labels: retrieves sales line items (digital, physical, merch, subscriptions) over a date range. Restricted to labels.'
  name: Bandcamp Sales Report API
  slug: sales-report
- description: 'Merch Orders API for fulfillment partners: list and update merchandise orders (mark shipped, set tracking). Restricted to merchandise fulfillment partners.'
  name: Bandcamp Merch Orders API
  slug: merch-orders
- description: Account and band information
  name: Bandcamp Account API
  slug: bandcamp-account-api
- description: Merchandise order management and fulfillment
  name: Bandcamp Merch Orders API
  slug: bandcamp-merch-orders-api
- description: OAuth 2.0 token issuance and refresh
  name: Bandcamp OAuth API
  slug: bandcamp-oauth-api
- description: Sales reporting for labels
  name: Bandcamp Sales API
  slug: bandcamp-sales-api
artifact_total: 15
collections:
- collection_type: open
  name: Bandcamp API
  slug: open-bandcamp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bandcamp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bandcamp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bandcamp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bandcamp-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bandcamp
- group: company
  title: ''
  type: Website
  url: https://bandcamp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bandcamp.com/developer
- group: commercial
  title: ''
  type: Plans
  url: plans/bandcamp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bandcamp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bandcamp-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.bandcamp.com/feed/
created: '2026-05-08'
description: Bandcamp is an artist-direct music marketplace and streaming platform. Its developer APIs are limited and gated to labels and merchandise fulfillment partners; access is granted on request and uses OAuth 2.0.
finops:
- name: Bandcamp Finops
  service_category: Music Marketplace
  slug: bandcamp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bandcamp.png
layout: provider
modified: '2026-05-08'
name: Bandcamp
nav: Providers
network: true
overview: 'Bandcamp publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Merch Orders API, OAuth API, and 1 more. Tagged areas include Music, Marketplace, Indie, Audio, and Sales.


  Bandcamp''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Bandcamp Plans Pricing
  plan_count: 2
  slug: bandcamp-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Bandcamp Rate Limits
  slug: bandcamp-rate-limits
scopes:
- name: Bandcamp Scopes
  scope_count: 0
  slug: bandcamp-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.9
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bandcamp/refs/heads/main/screenshots/bandcamp-2026-06-20T172941.png
security:
- kind: authentication
  name: Bandcamp Authentication
  slug: bandcamp-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Bandcamp Domain Security
  slug: bandcamp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bandcamp
tags:
- Music
- Marketplace
- Indie
- Audio
- Sales
- Merch
website: https://bandcamp.com/
---
