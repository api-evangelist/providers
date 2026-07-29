---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 46
  human_in_the_loop: 46
  name: Momence Agentic Access
  operation_count: 73
  slug: momence-agentic-access
  summary_line: 73 operations · 46 acting · 46 human-in-the-loop
api_count: 8
apis:
- description: The auth API from Momence — 4 operation(s) for auth.
  name: Momence auth API
  slug: momence-auth-api
- description: The host API from Momence — 29 operation(s) for host.
  name: Momence host API
  slug: momence-host-api
- description: The host-checkout API from Momence — 3 operation(s) for host-checkout.
  name: Momence host-checkout API
  slug: momence-host-checkout-api
- description: The member-addresses API from Momence — 2 operation(s) for member-addresses.
  name: Momence member-addresses API
  slug: momence-member-addresses-api
- description: The member API from Momence — 11 operation(s) for member.
  name: Momence member API
  slug: momence-member-api
- description: The member-checkout API from Momence — 3 operation(s) for member-checkout.
  name: Momence member-checkout API
  slug: momence-member-checkout-api
- description: The member-host API from Momence — 5 operation(s) for member-host.
  name: Momence member-host API
  slug: momence-member-host-api
- description: The member-sessions API from Momence — 2 operation(s) for member-sessions.
  name: Momence member-sessions API
  slug: momence-member-sessions-api
artifact_total: 16
collections:
- collection_type: open
  name: Momence Public API
  slug: open-momence
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/momence-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/momence-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/momence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/momence-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/momence
- group: company
  title: ''
  type: Website
  url: https://momence.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.docs.momence.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/momence-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/momence-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/momence-finops.yml
created: '2026-07-04'
description: Momence is an all-in-one management platform for fitness, wellness, and experience-based businesses - studios, gyms, spas, and instructors - covering class and appointment scheduling, memberships and packages, point-of-sale and payments, marketing, and a branded member app. Momence exposes a documented public REST API (api.momence.com, /api/v2) split into a Host API for staff and back-office automation and a Member API scoped to the logged-in customer. The API is authenticated with OAuth2 (authorization code for customers, password grant for staff automation) using public API clients created in the Momence dashboard, and covers members, sessions and bookings, memberships, checkout and sales, reports, appointments, addresses, and saved payment methods.
finops:
- name: Momence Finops
  service_category: Business Management Software
  slug: momence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/momence.png
layout: provider
modified: '2026-07-04'
name: Momence
nav: Providers
network: true
overview: 'Momence publishes 8 APIs on the [APIs.io](https://apis.io/) network, including auth API, host API, host-checkout API, and 5 more. Tagged areas include Fitness, Wellness, Studio Management, Booking, and Scheduling.


  Momence''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Momence Plans Pricing
  plan_count: 3
  slug: momence-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 2
  name: Momence Rate Limits
  slug: momence-rate-limits
scopes:
- name: Momence Scopes
  scope_count: 0
  slug: momence-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.7
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Momence Authentication
  slug: momence-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Momence Domain Security
  slug: momence-domain-security
  summary_line: TLSv1.3 · DMARC
slug: momence
tags:
- Fitness
- Wellness
- Studio Management
- Booking
- Scheduling
- Memberships
- Payments
- Class Management
website: https://momence.com/
---
