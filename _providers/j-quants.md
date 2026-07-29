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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: J Quants Agentic Access
  operation_count: 21
  slug: j-quants-agentic-access
  summary_line: 21 operations · 2 acting
api_count: 10
apis:
- description: The J-Quants API (V2) is a data distribution service operated by Japan Exchange Group (JPX) that makes it easy to obtain cleansed financial data such as Japanese stock prices and financials in histori
  name: J-Quants API
  slug: j-quants-api
- description: The Derivatives API from J-Quants — 2 operation(s) for derivatives.
  name: J-Quants Derivatives API
  slug: j-quants-derivatives-api
- description: The Equities API from J-Quants — 1 operation(s) for equities.
  name: J-Quants Equities API
  slug: j-quants-equities-api
- description: The Fins API from J-Quants — 4 operation(s) for fins.
  name: J-Quants Fins API
  slug: j-quants-fins-api
- description: The Indices API from J-Quants — 1 operation(s) for indices.
  name: J-Quants Indices API
  slug: j-quants-indices-api
- description: The Listed API from J-Quants — 1 operation(s) for listed.
  name: J-Quants Listed API
  slug: j-quants-listed-api
- description: The Markets API from J-Quants — 7 operation(s) for markets.
  name: J-Quants Markets API
  slug: j-quants-markets-api
- description: The Option API from J-Quants — 1 operation(s) for option.
  name: J-Quants Option API
  slug: j-quants-option-api
- description: The Prices API from J-Quants — 2 operation(s) for prices.
  name: J-Quants Prices API
  slug: j-quants-prices-api
- description: The Token API from J-Quants — 2 operation(s) for token.
  name: J-Quants Token API
  slug: j-quants-token-api
artifact_total: 17
collections:
- collection_type: open
  name: J-Quants API
  slug: open-j-quants
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/j-quants-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/j-quants-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/j-quants-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/J-Quants
- group: company
  title: ''
  type: Website
  url: https://jpx-jquants.com/
- group: docs
  title: ''
  type: Documentation
  url: https://jpx-jquants.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://jpx-jquants.com/llms.txt
created: '2025-02-12'
description: J-Quants is a financial data API service operated by Japan Exchange Group (JPX) that makes it easy for retail investors to obtain cleansed financial data such as stock prices and financials in historical format. The service democratizes access to raw financial data for investment analysis.
finops:
- name: J Quants Finops
  service_category: API
  slug: j-quants-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/j-quants.png
layout: provider
modified: '2026-04-28'
name: J-Quants
nav: Providers
network: true
overview: 'J-Quants publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Derivatives API, Equities API, Fins API, and 6 more. Tagged areas include Financial Data, Investment, Japan, and Stock Market.


  J-Quants'' developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: J Quants Plans Pricing
  plan_count: 3
  slug: j-quants-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: J Quants Rate Limits
  slug: j-quants-rate-limits
score:
  band: thin
  composite: 36.6
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.0
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/j-quants/refs/heads/main/screenshots/j-quants-2026-06-20T183644.png
security:
- kind: authentication
  name: J Quants Authentication
  slug: j-quants-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: J Quants Domain Security
  slug: j-quants-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: j-quants
tags:
- Financial Data
- Investment
- Japan
- Stock Market
website: https://jpx-jquants.com/
---
