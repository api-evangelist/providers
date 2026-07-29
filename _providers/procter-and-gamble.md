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
- acting_count: 0
  human_in_the_loop: 0
  name: Procter And Gamble Agentic Access
  operation_count: 3
  slug: procter-and-gamble-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Manage and track orders.
  name: Procter & Gamble Orders API
  slug: procter-and-gamble-orders-api
- description: Access P&G product catalog and data.
  name: Procter & Gamble Products API
  slug: procter-and-gamble-products-api
- description: Integration with P&G supply chain operations.
  name: Procter & Gamble Supply Chain API
  slug: procter-and-gamble-supply-chain-api
artifact_total: 11
collections:
- collection_type: open
  name: Procter & Gamble API Marketplace
  slug: open-procter-and-gamble-api-marketplace
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/procter-and-gamble-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/procter-and-gamble-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/procter-and-gamble-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/procter-and-gamble-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/procter-gamble
created: '2026-03-21'
description: Procter & Gamble (P&G) is one of the world's largest consumer goods companies, with a portfolio of trusted brands across beauty, grooming, health care, fabric and home care, and baby, feminine, and family care. P&G operates an API Marketplace at developer.pg.com that provides partners, suppliers, and developers with programmatic access to P&G systems for integrating with the company's supply chain, product data, and business operations.
finops:
- name: Procter And Gamble Finops
  service_category: Consumer Goods
  slug: procter-and-gamble-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/procter-and-gamble.png
layout: provider
modified: '2026-05-19'
name: Procter & Gamble
nav: Providers
network: true
overview: 'Procter & Gamble publishes 3 APIs on the [APIs.io](https://apis.io/) network: Orders API, Products API, and Supply Chain API. Tagged areas include Consumer Goods, Manufacturing, Retail, Supply Chain, and Fortune 100.


  Procter & Gamble''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Procter And Gamble Plans Pricing
  plan_count: 1
  slug: procter-and-gamble-plans-pricing
press:
- date: '2026-05-25'
  title: How P&G Transforms Business Through Technology
  url: https://us.pg.com/blogs/innovation-at-scale-transforming-business-through-technology/
- date: '2026-05-25'
  title: How Procter & Gamble Uses AI to Unlock New Insights ...
  url: https://sloanreview.mit.edu/article/how-procter-gamble-uses-ai-to-unlock-new-insights-from-data/
- date: '2026-05-25'
  title: 'Procter & Gamble Uses AI Agents: 10 Ways to ...'
  url: https://www.klover.ai/procter-gamble-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025/
- date: '2026-05-25'
  title: Google Cloud Helps Power More Personalized Experience ...
  url: https://www.googlecloudpresscorner.com/2020-07-14-Google-Cloud-Helps-Power-More-Personalized-Experience-for-Procter-Gamble-Consumers
- date: '2026-05-25'
  title: How Procter & Gamble is Leveraging AI to Democratize ...
  url: https://www.youtube.com/watch?v=DjxguIe1tqc
random_paper: 20
rate_limits:
- limit_count: 1
  name: Procter And Gamble Rate Limits
  slug: procter-and-gamble-rate-limits
score:
  band: thin
  composite: 31.9
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.5
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/procter-and-gamble/refs/heads/main/screenshots/procter-and-gamble-2026-06-20T192133.png
security:
- kind: authentication
  name: Procter And Gamble Authentication
  slug: procter-and-gamble-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Procter And Gamble Domain Security
  slug: procter-and-gamble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Procter And Gamble Vulnerability Disclosure
  slug: procter-and-gamble-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: procter-and-gamble
tags:
- Consumer Goods
- Manufacturing
- Retail
- Supply Chain
- Fortune 100
---
