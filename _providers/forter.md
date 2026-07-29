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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Forter Agentic Access
  operation_count: 8
  slug: forter-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 4
apis:
- description: Send order and checkout information to receive a real-time fraud or abuse decision (approve / decline / not-reviewed), with optional payment optimization and abuse-policy recommendations. Includes the
  name: Forter Order Decision API
  slug: forter-order-decision-api
- description: Protect the account lifecycle - submit registration details at signup to get a fraud or abuse decision, and submit login attempt details to get an account takeover (ATO) decision. Built on Forter's cr
  name: Forter Account Protection API
  slug: forter-account-protection-api
- description: Report customer-initiated disputes (chargebacks) to feed Forter's decision model and enable chargeback recovery, and submit customer requests for compensation - refunds or reships, at the order or ite
  name: Forter Chargeback and Compensation API
  slug: forter-chargeback-compensation-api
- description: Data-subject profile access endpoint used to support privacy and compliance workflows (for example, access requests) against the identity data Forter holds for an account.
  name: Forter Data Privacy API
  slug: forter-data-privacy-api
artifact_total: 11
collections:
- collection_type: open
  name: Forter API
  slug: open-forter
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/forter-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forter-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forter
- group: company
  title: ''
  type: Website
  url: https://www.forter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.forter.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/forter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/forter-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.forter.com/blog/
created: '2026-07-12'
description: Forter is a fraud prevention and digital identity platform for online commerce. Its Decision API returns real-time trust-or-not decisions for orders, payments, account signups, and logins, drawing on a global identity graph and machine learning trained across a large network of merchants. Beyond fraud management, Forter covers chargeback recovery, abuse prevention, payment optimization, 3DS orchestration, and identity protection. Access is enterprise / contact-sales - API credentials (a per-account site ID and API key) are provisioned by Forter during onboarding, and requests are sent to a dedicated per-tenant host.
finops:
- name: Forter Finops
  service_category: Fraud Prevention and Identity
  slug: forter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-12'
name: Forter
nav: Providers
network: true
overview: 'Forter publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Order Decision API, Account Protection API, Chargeback and Compensation API, and 1 more. Tagged areas include Fraud Detection, Fraud Prevention, Identity, Trust, and Payments.


  Forter''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Forter Plans Pricing
  plan_count: 1
  slug: forter-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 2
  name: Forter Rate Limits
  slug: forter-rate-limits
score:
  band: thin
  composite: 28.6
  delta: -7.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 40.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/forter/refs/heads/main/screenshots/forter-2026-07-25T215001.png
security:
- kind: authentication
  name: Forter Authentication
  slug: forter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Forter Domain Security
  slug: forter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: forter
tags:
- Fraud Detection
- Fraud Prevention
- Identity
- Trust
- Payments
- Chargebacks
- Account Protection
- E-commerce
- Risk
- Machine Learning
website: https://www.forter.com/
---
