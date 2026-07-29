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
- acting_count: 14
  human_in_the_loop: 0
  name: Thumbtack Agentic Access
  operation_count: 21
  slug: thumbtack-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 10
apis:
- description: The Authentication API from Thumbtack — 1 operation(s) for authentication.
  name: Thumbtack Authentication API
  slug: thumbtack-authentication-api
- description: The Autocomplete API from Thumbtack — 1 operation(s) for autocomplete.
  name: Thumbtack Autocomplete API
  slug: thumbtack-autocomplete-api
- description: The Categories API from Thumbtack — 2 operation(s) for categories.
  name: Thumbtack Categories API
  slug: thumbtack-categories-api
- description: The Leads API from Thumbtack — 2 operation(s) for leads.
  name: Thumbtack Leads API
  slug: thumbtack-leads-api
- description: The Messages API from Thumbtack — 2 operation(s) for messages.
  name: Thumbtack Messages API
  slug: thumbtack-messages-api
- description: The Orders API from Thumbtack — 2 operation(s) for orders.
  name: Thumbtack Orders API
  slug: thumbtack-orders-api
- description: The Pro Profiles API from Thumbtack — 4 operation(s) for pro profiles.
  name: Thumbtack Pro Profiles API
  slug: thumbtack-pro-profiles-api
- description: The Pros API from Thumbtack — 2 operation(s) for pros.
  name: Thumbtack Pros API
  slug: thumbtack-pros-api
- description: The Reviews API from Thumbtack — 1 operation(s) for reviews.
  name: Thumbtack Reviews API
  slug: thumbtack-reviews-api
- description: The Testing API from Thumbtack — 1 operation(s) for testing.
  name: Thumbtack Testing API
  slug: thumbtack-testing-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thumbtack-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thumbtack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thumbtack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thumbtack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thumbtack-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thumbtack-inc.
- group: company
  title: ''
  type: Website
  url: https://www.thumbtack.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thumbtack.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/thumbtack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thumbtack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thumbtack-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://thumbtack.com/blog/feed/
created: '2026-07-03'
description: Thumbtack is a local services marketplace connecting homeowners with local service professionals (cleaning, home improvement, events, wellness, and more). There is no self-serve public API - Thumbtack operates an approval-gated Partner Platform (developers.thumbtack.com) with two documented API surfaces - a Demand API for marketplace integrations (pro search, categories, autocomplete, requests) and a Pro API for supply-side integrations (leads, messages, pro profiles, reviews) - plus low-code embeddable widgets. Access requires Thumbtack to approve a partner and issue OAuth 2.0 credentials; there is no public signup or API key self-service.
finops:
- name: Thumbtack Finops
  service_category: Local Services Marketplace
  slug: thumbtack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thumbtack.png
layout: provider
modified: '2026-07-03'
name: Thumbtack
nav: Providers
network: true
overview: 'Thumbtack publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Autocomplete API, Categories API, and 7 more. Tagged areas include Local Services, Marketplace, Home Services, Leads, and Partner API.


  Thumbtack''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Thumbtack Plans Pricing
  plan_count: 3
  slug: thumbtack-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Thumbtack Rate Limits
  slug: thumbtack-rate-limits
scopes:
- name: Thumbtack Scopes
  scope_count: 21
  slug: thumbtack-scopes
  summary_line: 21 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 36.7
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.7
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
  name: Thumbtack Authentication
  slug: thumbtack-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Thumbtack Domain Security
  slug: thumbtack-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Thumbtack Vulnerability Disclosure
  slug: thumbtack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: thumbtack
tags:
- Local Services
- Marketplace
- Home Services
- Leads
- Partner API
website: https://www.thumbtack.com
---
