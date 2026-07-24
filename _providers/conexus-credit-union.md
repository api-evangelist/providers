---
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conexus-credit-union-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conexus-credit-union-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.conexus.ca/
- group: other
  title: ''
  type: OnlineBanking
  url: https://banking.online.conexus.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conexus-credit-union
- group: company
  title: ''
  type: Blog
  url: https://www.conexus.ca/about-us/meet-conexus/news/member-news
- group: operate
  title: ''
  type: Support
  url: https://www.conexus.ca/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.conexus.ca/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conexus.ca/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.conexus.ca/security
created: '2026-07-23'
description: Conexus Credit Union is Saskatchewan's largest credit union, a member-owned cooperative financial institution headquartered in Regina with over $10 billion in consolidated assets under management, more than 140,000 members, roughly 30 branches, and over 800 employees across the province. As a provincially regulated Saskatchewan credit union it operates under a cooperative charter, with member deposits guaranteed by the Credit Union Deposit Guarantee Corporation (CUDGC). In November 2024 Conexus announced its intent to explore a merger with Cornerstone and Synergy credit unions. Conexus does not publish a first-party public developer API or a developer portal; developer.conexus.ca does not resolve, and /developer and /api on the corporate site return 404. Consumer financial-data access is provided through third-party aggregators (notably Plaid in Canada) via screen-scraping and connection-based data sharing rather than a first-party API. Digital and online banking are delivered
  through core-banking and fintech partners (banking.online.conexus.ca), and investing runs through the credit-union system's Aviso Wealth / Qtrade and Thrive Wealth partners. Canada's federal Consumer-Driven Banking (open banking) framework, overseen by the Financial Consumer Agency of Canada (FCAC), is legislated but not yet operational, so Conexus's open-finance access remains voluntary and aggregator-mediated today.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Conexus Credit Union
nav: Providers
network: true
overview: 'Conexus Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Credit Union, and Cooperative.


  Conexus Credit Union''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 16.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 10.5
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-23'
security:
- kind: domain-security
  name: Conexus Credit Union Domain Security
  slug: conexus-credit-union-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conexus-credit-union
tags:
- Financial Services
- Banking
- Canada
- Credit Union
- Cooperative
- Saskatchewan
- Data Aggregation
- Open Banking
website: https://www.conexus.ca/
---
