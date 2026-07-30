---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Xoxoday Agentic Access
  operation_count: 4
  slug: xoxoday-agentic-access
  summary_line: 4 operations · 3 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: API for creating and sending personalized reward links via email, SMS, or chat. Supports campaign management, link generation, and link delivery without requiring recipients to have a Xoxoday account.
  name: Xoxoday Reward Links API
  slug: reward-links-api
- description: API for distributing, tracking, and managing loyalty and engagement points programs. Supports sending points to users, canceling points transactions, and fetching points balances for loyalty and recog
  name: Xoxoday Reward Points API
  slug: reward-points-api
- description: API for embedding a white-labeled reward storefront into existing applications via SSO/SAML. Enables end-users to browse and redeem rewards from a branded marketplace without leaving the host applicat
  name: Xoxoday Storefront Integration API
  slug: storefront-integration-api
- description: Token generation, validation, and refresh
  name: Xoxoday Authentication API
  slug: xoxoday-authentication-api
- description: Account balance retrieval
  name: Xoxoday Balance API
  slug: xoxoday-balance-api
- description: Browse and order gift card vouchers
  name: Xoxoday Gift Cards API
  slug: xoxoday-gift-cards-api
- description: Order placement, tracking, and history
  name: Xoxoday Orders API
  slug: xoxoday-orders-api
- description: Payment report and transaction history
  name: Xoxoday Payments API
  slug: xoxoday-payments-api
- description: Generate and send personalized reward links
  name: Xoxoday Reward Links API
  slug: xoxoday-reward-links-api
- description: Send, fetch, and cancel reward points
  name: Xoxoday Reward Points API
  slug: xoxoday-reward-points-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xoxoday-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/xoxoday-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xoxoday-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xoxoday-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xoxoday-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xoxoday-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.xoxoday.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.xoxoday.com/docs/overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/xoxoday
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xoxoday/
- group: company
  title: ''
  type: Blog
  url: https://blog.xoxoday.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://plum.xoxoday.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xoxoday.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/thexoxoday
- group: commercial
  title: ''
  type: Plans
  url: plans/xoxoday-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xoxoday-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/xoxoday-finops.yml
created: '2026-06-13'
description: Xoxoday is an AI-powered enterprise platform for rewards, loyalty, and incentive operations. Its Plum Rewards API enables organizations to programmatically distribute digital rewards including gift cards, merchandise, experiences, travel, mobile top-ups, and charitable donations across 150+ countries. The platform supports employee recognition workflows, sales incentive programs, customer loyalty campaigns, and channel partner rewards through REST APIs, webhook integrations, and a white-labeled storefront.
finops:
- name: Xoxoday Finops
  service_category: ''
  slug: xoxoday-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xoxoday.png
jsonld:
- class_count: 16
  name: Xoxoday Context
  property_count: 0
  slug: xoxoday
layout: provider
modified: '2026-06-13'
name: Xoxoday
nav: Providers
network: true
overview: 'Xoxoday publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Balance API, Gift Cards API, and 4 more. Tagged areas include Rewards, Employee Engagement, Gift Cards, Incentives, and Loyalty.


  The Xoxoday catalog on APIs.io includes 1 JSON-LD context.


  Xoxoday''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Xoxoday Plans Pricing
  plan_count: 0
  slug: xoxoday-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 0
  name: Xoxoday Rate Limits
  slug: xoxoday-rate-limits
scopes:
- name: Xoxoday Scopes
  scope_count: 2
  slug: xoxoday-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 37.6
  delta: -2.3
  facets:
    commercial_clarity: 26.3
    contract_quality: 71.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xoxoday/refs/heads/main/screenshots/xoxoday-2026-06-20T201711.png
security:
- kind: authentication
  name: Xoxoday Authentication
  slug: xoxoday-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Xoxoday Domain Security
  slug: xoxoday-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Xoxoday Vulnerability Disclosure
  slug: xoxoday-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Xoxoday Trust Center
  slug: xoxoday-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: xoxoday
tags:
- Rewards
- Employee Engagement
- Gift Cards
- Incentives
- Loyalty
- Recognition
- Digital Rewards
- Points Programs
- Redemption
- Fintech
website: https://www.xoxoday.com/
---
