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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Churnkey Agentic Access
  operation_count: 9
  slug: churnkey-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 7
apis:
- description: Client-side embed surface for personalized Cancel Flows. The JavaScript SDK is initialized with window.churnkey.init(), passing an appId, customerId, subscriptionId, provider, and a server-computed HM
  name: Churnkey Cancel Flow Embed
  slug: churnkey-cancel-flow-embed
- description: Reactivation (win-back) campaigns that re-engage churned or paused customers with targeted offers. Reactivations are a documented Churnkey product, but a dedicated public REST endpoint set is not publ
  name: Churnkey Reactivation API
  slug: churnkey-reactivation-api
- description: Billing-contact management for Failed Payment Recovery.
  name: Churnkey Billing Contacts API
  slug: churnkey-billing-contacts-api
- description: Customer and B2B user attribute updates.
  name: Churnkey Customers API
  slug: churnkey-customers-api
- description: GDPR access and deletion requests (Data API).
  name: Churnkey Data Subject Requests API
  slug: churnkey-data-subject-requests-api
- description: Customer event tracking and passive data enrichment.
  name: Churnkey Events API
  slug: churnkey-events-api
- description: Cancel Flow session data and aggregations (Data API).
  name: Churnkey Sessions API
  slug: churnkey-sessions-api
artifact_total: 15
collections:
- collection_type: open
  name: Churnkey API
  slug: open-churnkey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/churnkey-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/churnkey-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/churnkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/churnkey-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/churnkey
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/churnkey
- group: company
  title: ''
  type: Website
  url: https://churnkey.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.churnkey.co
- group: commercial
  title: ''
  type: Plans
  url: plans/churnkey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/churnkey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/churnkey-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://churnkey.co/pricing
created: '2026-07-10'
description: Churnkey is retention and growth infrastructure for subscription companies. It provides personalized Cancel Flows that intercept subscription cancellations with pauses, discounts, plan changes and surveys; Failed Payment Recovery (dunning) that recovers involuntary churn; and Reactivation campaigns that win back churned customers. Churnkey embeds via a JavaScript SDK authenticated with a server-computed HMAC authHash, and exposes REST APIs for session/analytics data, event tracking, customer updates, billing-contact management, and GDPR data-subject requests, plus signed webhooks. It integrates with Stripe, Chargebee, Paddle, Braintree, and Maxio.
finops:
- name: Churnkey Finops
  service_category: Retention and Subscription Management
  slug: churnkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/churnkey.png
layout: provider
modified: '2026-07-10'
name: Churnkey
nav: Providers
network: true
overview: 'Churnkey publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Billing Contacts API, Customers API, Data Subject Requests API, and 2 more. Tagged areas include Churn Prevention, Retention, Cancellation Flows, Failed Payment Recovery, and Dunning.


  Churnkey''s developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Churnkey Plans Pricing
  plan_count: 4
  slug: churnkey-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 4
  name: Churnkey Rate Limits
  slug: churnkey-rate-limits
score:
  band: thin
  composite: 40.5
  delta: -3.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/churnkey/refs/heads/main/screenshots/churnkey-2026-07-25T205328.png
security:
- kind: authentication
  name: Churnkey Authentication
  slug: churnkey-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Churnkey Domain Security
  slug: churnkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Churnkey Trust Center
  slug: churnkey-trust-center
  summary_line: SOC 2, GDPR
slug: churnkey
tags:
- Churn Prevention
- Retention
- Cancellation Flows
- Failed Payment Recovery
- Dunning
- Reactivation
- Subscriptions
- SaaS
website: https://churnkey.co
---
