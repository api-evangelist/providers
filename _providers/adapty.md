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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Adapty Agentic Access
  operation_count: 12
  slug: adapty-agentic-access
  summary_line: 12 operations · 9 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Outbound webhooks that POST subscription lifecycle events (trial start, subscription started, renewed, billing issue, refund, access-level granted/revoked) to your endpoint in near real time for downs
  name: Adapty Webhooks
  slug: adapty-webhooks
- description: Grant and revoke access levels (entitlements) directly.
  name: Adapty Access Levels API
  slug: adapty-access-levels-api
- description: Attach third-party integration identifiers to a profile.
  name: Adapty Integrations API
  slug: adapty-integrations-api
- description: Read and update paywalls and their products.
  name: Adapty Paywalls API
  slug: adapty-paywalls-api
- description: Get, create, update, and delete end-user profiles.
  name: Adapty Profiles API
  slug: adapty-profiles-api
- description: Set transactions and validate store/Stripe purchases.
  name: Adapty Purchases API
  slug: adapty-purchases-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adapty Server-Side Access Levels API
  slug: open-adapty-access-levels-api
- collection_type: open
  name: Adapty Server-Side Access Levels Integrations API
  slug: open-adapty-integrations-api
- collection_type: open
  name: Adapty Server-Side Access Levels Paywalls API
  slug: open-adapty-paywalls-api
- collection_type: open
  name: Adapty Server-Side Access Levels Profiles API
  slug: open-adapty-profiles-api
- collection_type: open
  name: Adapty Server-Side Access Levels Purchases API
  slug: open-adapty-purchases-api
- collection_type: open
  name: Adapty Server-Side API
  slug: open-adapty
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adapty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adapty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adapty-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adaptyteam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adapty-io
- group: company
  title: ''
  type: Website
  url: https://adapty.io/
- group: docs
  title: ''
  type: Documentation
  url: https://adapty.io/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/adapty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adapty-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/adapty-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://adapty.io/blog
created: '2026-07-01'
description: Adapty is a mobile in-app subscription platform for iOS, Android, Flutter, React Native, and Unity apps. Its core is a client SDK for paywalls, A/B testing, remote config, and server-side receipt validation, backed by a supporting Server-Side REST API for programmatically managing profiles, purchases and transactions, access levels (entitlements), and paywalls, plus webhooks and integrations for streaming subscription events to downstream analytics and marketing tools.
finops:
- name: Adapty Finops
  service_category: Analytics and Monetization
  slug: adapty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adapty.png
layout: provider
modified: '2026-07-01'
name: Adapty
nav: Providers
network: true
overview: 'Adapty publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Access Levels API, Integrations API, Paywalls API, and 2 more. Tagged areas include Mobile, Subscriptions, In-App Purchases, Paywalls, and Analytics.


  Adapty''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Adapty Plans Pricing
  plan_count: 3
  slug: adapty-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Adapty Rate Limits
  slug: adapty-rate-limits
score:
  band: thin
  composite: 38.9
  delta: -0.1
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adapty/refs/heads/main/screenshots/adapty-2026-07-25T181605.png
security:
- kind: authentication
  name: Adapty Authentication
  slug: adapty-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Adapty Domain Security
  slug: adapty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adapty
tags:
- Mobile
- Subscriptions
- In-App Purchases
- Paywalls
- Analytics
website: https://adapty.io/
---
