---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
- acting_count: 9
  human_in_the_loop: 0
  name: Zinrelo Agentic Access
  operation_count: 22
  slug: zinrelo-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 7
apis:
- description: Retrieve webhook event details by event ID.
  name: Zinrelo Events API
  slug: zinrelo-events-api
- description: Enroll, retrieve, update, block, and manage loyalty program members.
  name: Zinrelo Members API
  slug: zinrelo-members-api
- description: Award, deduct, and manage member point balances.
  name: Zinrelo Points API
  slug: zinrelo-points-api
- description: Redeem points for rewards and list a member's redemptions.
  name: Zinrelo Redemptions API
  slug: zinrelo-redemptions-api
- description: List and retrieve the rewards a program offers.
  name: Zinrelo Rewards API
  slug: zinrelo-rewards-api
- description: Retrieve loyalty tier configuration and a member's next tier.
  name: Zinrelo Tiers API
  slug: zinrelo-tiers-api
- description: Record purchases and returns and list loyalty transactions.
  name: Zinrelo Transactions API
  slug: zinrelo-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: Zinrelo Loyalty API
  slug: open-zinrelo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zinrelo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zinrelo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zinrelo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zinrelo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zinrelo
- group: company
  title: ''
  type: Website
  url: https://www.zinrelo.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.zinrelo.com/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://zinrelo.github.io/slate/
- group: commercial
  title: ''
  type: Plans
  url: plans/zinrelo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zinrelo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zinrelo-finops.yml
created: '2026-07-10'
description: Zinrelo is an enterprise SaaS loyalty and rewards platform that helps brands run holistic loyalty programs spanning transactional, social, advocacy, engagement, behavioral, and emotional loyalty across web, mobile, and in-store channels. Its documented REST Loyalty API lets you enroll and manage members, award and deduct points, record purchases and returns, list rewards, and redeem points for rewards. Every request is authenticated with a partner-id and an api-key sent as HTTP headers, both provisioned to a Zinrelo account. The API reference is public, but obtaining API credentials requires a Zinrelo account; pricing is quote-based via sales. Zinrelo is rebranding to TrueLoyal, and some documentation now lives under trueloyal.com domains.
finops:
- name: Zinrelo Finops
  service_category: Marketing and Loyalty
  slug: zinrelo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zinrelo.png
layout: provider
modified: '2026-07-10'
name: Zinrelo
nav: Providers
network: true
overview: 'Zinrelo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Events API, Members API, Points API, and 4 more. Tagged areas include Loyalty, Rewards, Points, Customer Retention, and Ecommerce.


  Zinrelo''s developer surface includes authentication, documentation, API reference, and 8 more developer resources.'
plans:
- name: Zinrelo Plans Pricing
  plan_count: 3
  slug: zinrelo-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 2
  name: Zinrelo Rate Limits
  slug: zinrelo-rate-limits
score:
  band: thin
  composite: 40.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 61.2
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Zinrelo Authentication
  slug: zinrelo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Zinrelo Domain Security
  slug: zinrelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zinrelo Trust Center
  slug: zinrelo-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: zinrelo
tags:
- Loyalty
- Rewards
- Points
- Customer Retention
- Ecommerce
- SaaS
website: https://www.zinrelo.com
---
