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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Buymeacoffee Agentic Access
  operation_count: 6
  slug: buymeacoffee-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: Server-push HTTP webhooks configured in the dashboard (Integrations - New webhook). Buy Me a Coffee POSTs a JSON event envelope to a subscriber URL for donation, membership / recurring-donation, extra
  name: Buy Me a Coffee Webhooks
  slug: buymeacoffee-webhooks-api
- description: Extras purchases (shop items and rewards). BETA.
  name: Buy Me a Coffee Extras API
  slug: buymeacoffee-extras-api
- description: Recurring memberships / subscriptions (members).
  name: Buy Me a Coffee Subscriptions API
  slug: buymeacoffee-subscriptions-api
- description: One-time supporters (tips / coffees) and their messages.
  name: Buy Me a Coffee Supporters API
  slug: buymeacoffee-supporters-api
artifact_total: 11
collections:
- collection_type: open
  name: Buy Me a Coffee API
  slug: open-buymeacoffee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/buymeacoffee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buymeacoffee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buymeacoffee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buymeacoffee
- group: company
  title: ''
  type: Website
  url: https://www.buymeacoffee.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.buymeacoffee.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/buymeacoffee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buymeacoffee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/buymeacoffee-finops.yml
created: '2026-07-05'
description: Buy Me a Coffee is a creator-support platform that lets fans tip creators ("buy a coffee"), subscribe to recurring memberships, and buy extras from a creator's shop. Its developer API is a read-only REST interface (base https://developers.buymeacoffee.com/api/v1) authenticated with a personal access Bearer token created self-serve in the Developer Dashboard. The API exposes a creator's own one-time supporters, memberships/subscriptions, and extra purchases, and the platform also delivers server-push webhooks for donation, membership, and shop events. Buy Me a Coffee charges a flat 5% platform fee on transactions with no monthly fee.
finops:
- name: Buymeacoffee Finops
  service_category: Creator Monetization and Payments
  slug: buymeacoffee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buymeacoffee.png
layout: provider
modified: '2026-07-05'
name: Buy Me a Coffee
nav: Providers
network: true
overview: 'Buy Me a Coffee publishes 3 APIs on the [APIs.io](https://apis.io/) network: Extras API, Subscriptions API, and Supporters API. Tagged areas include Creator Economy, Memberships, Subscriptions, Tips, and Payments.


  Buy Me a Coffee''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Buymeacoffee Plans Pricing
  plan_count: 2
  slug: buymeacoffee-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 3
  name: Buymeacoffee Rate Limits
  slug: buymeacoffee-rate-limits
score:
  band: thin
  composite: 33.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buymeacoffee/refs/heads/main/screenshots/buymeacoffee-2026-07-25T204126.png
security:
- kind: authentication
  name: Buymeacoffee Authentication
  slug: buymeacoffee-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Buymeacoffee Domain Security
  slug: buymeacoffee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buymeacoffee
tags:
- Creator Economy
- Memberships
- Subscriptions
- Tips
- Payments
- Donations
website: https://www.buymeacoffee.com
---
