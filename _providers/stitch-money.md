---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Stitch Money Agentic Access
  operation_count: 1
  slug: stitch-money-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Stitch — 1 operation(s) for graphql.
  name: Stitch GraphQL API
  slug: stitch-money-graphql-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stitch GraphQL API
  slug: open-stitch-money-graphql-api
- collection_type: open
  name: Stitch GraphQL API
  slug: open-stitch-money
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stitch-money-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stitch-money-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stitch-money-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stitch-money-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stitch-Money
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stitchmoney
- group: company
  title: ''
  type: Website
  url: https://stitch.money/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stitch.money
- group: commercial
  title: ''
  type: Plans
  url: plans/stitch-money-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stitch-money-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stitch-money-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://stitch.money/blog/rss.xml
created: '2026-06-21'
description: Stitch is a South African payments and open-banking infrastructure company. Its single GraphQL API at https://api.stitch.money/graphql powers Pay By Bank (instant EFT) and LinkPay payment initiation, bank account verification, financial data access (accounts, transactions, balances), payouts and disbursements, refunds, and signed webhook subscriptions, authenticated via OAuth2 client-credentials Bearer tokens.
finops:
- name: Stitch Money Finops
  service_category: Financial Services
  slug: stitch-money-finops
graphqls:
- description: The [Stitch](https://stitch.money/) payments and open-banking platform is exposed through a
  name: Stitch GraphQL API
  slug: stitch-money-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stitch-money.png
layout: provider
modified: '2026-06-21'
name: Stitch
nav: Providers
network: true
overview: 'Stitch publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Payments, Open Banking, Pay By Bank, GraphQL, and Africa.


  Stitch''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Stitch Money Plans Pricing
  plan_count: 2
  slug: stitch-money-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 3
  name: Stitch Money Rate Limits
  slug: stitch-money-rate-limits
score:
  band: thin
  composite: 36.2
  delta: 0.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 62.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 22.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Stitch Money Authentication
  slug: stitch-money-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stitch Money Domain Security
  slug: stitch-money-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Stitch Money Vulnerability Disclosure
  slug: stitch-money-vulnerability-disclosure
  summary_line: security.txt
slug: stitch-money
tags:
- Payments
- Open Banking
- Pay By Bank
- GraphQL
- Africa
- South Africa
- Fintech
website: https://stitch.money/
---
