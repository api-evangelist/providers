---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-tech-federal-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-tech-federal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-tech-federal-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.firsttechfed.com/
- group: operate
  title: ''
  type: Support
  url: https://www.firsttechfed.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firsttechfed.com/help/consumer-privacy
- group: company
  title: ''
  type: Blog
  url: https://www.firsttechfed.com/learn/article-gallery
- group: commercial
  title: ''
  type: Pricing
  url: https://www.firsttechfed.com/rates
- group: start
  title: ''
  type: Login
  url: https://banking.firsttechfed.com/Authentication
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-tech-federal-credit-union
created: '2026-07-23'
description: First Tech Federal Credit Union is a federally chartered, member-owned, not-for-profit financial cooperative headquartered in San Jose, California, and one of the largest credit unions in the United States. It was founded to serve employees of the technology industry and their families, and its membership is drawn heavily from workers at major technology employers. As an NCUA-insured credit union, First Tech offers consumer and business deposit accounts, lending, mortgages, credit cards, and wealth services delivered primarily through its website and mobile apps. Like the vast majority of US credit unions, First Tech publishes no first-party public developer portal or documented open API; consumer-permissioned financial data sharing is handled through third-party data aggregators (such as Plaid, MX, Finicity, and Akoya) rather than a directly documented first-party API surface. US open finance is voluntary and fragmented — the Financial Data Exchange (FDX) standard and the CFPB
  Section 1033 Personal Financial Data Rights rule are still emerging — and no first-party FDX-conformant data-access API or published Section 1033 posture was found for First Tech during this review.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: First Tech Federal Credit Union
nav: Providers
network: true
overview: 'First Tech Federal Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Credit Union, and Open Finance.


  First Tech Federal Credit Union''s developer surface includes support, engineering blog, pricing, and 7 more developer resources.'
random_paper: 75
score:
  band: emerging
  composite: 14.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-tech-federal/refs/heads/main/screenshots/first-tech-federal-2026-07-25T214611.png
security:
- kind: domain-security
  name: First Tech Federal Domain Security
  slug: first-tech-federal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: first-tech-federal
tags:
- Financial Services
- Banking
- United States
- Credit Union
- Open Finance
- Data Aggregation
website: https://www.firsttechfed.com/
---
