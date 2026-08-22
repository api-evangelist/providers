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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pc-financial-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pc-financial-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.pcfinancial.ca/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pcoptimum.ca/presidents-choice-financial-legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pcoptimum.ca/presidents-choice-financial-legal
- group: operate
  title: ''
  type: Support
  url: https://www.pcfinancial.ca/en/contact-us/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pcfinancial.ca/en/faqs/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/president's-choice-financial
created: '2026-07-23'
description: PC Financial (President's Choice Financial) is the financial-services brand of Canadian grocery giant Loblaw Companies Limited. Its personal banking and Mastercard credit-card products are issued by President's Choice Bank, a federally chartered Schedule I bank and CDIC member, while insurance is offered through PC Financial Insurance. The digital-first, branchless brand centers on the no-fee PC Money Account (a Mastercard-network everyday spending account launched September 2020), a line of PC Financial and PC World Elite Mastercard credit cards, and deep integration with the PC Optimum loyalty program across Loblaw's grocery, pharmacy, and retail banners. Consumer banking (chequing, savings, mortgages) was transferred to CIBC's Simplii Financial in 2017, so PC Financial today is a rewards-linked digital banking arm rather than a full-service bank. In December 2025 Equitable Bank (EQB) agreed to acquire PC Financial from Loblaw for roughly $800 million. On open finance, PC
  Financial runs NO public first-party developer portal or API; Canada's Consumer-Driven Banking framework is legislated but not yet operational, so consumer account access today is aggregator/screen-scraping-based via providers such as Plaid and Finicity (Mastercard). The bank supports Interac e-Transfer on the PC Money Account as shared payments-rail participation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: PC Financial
nav: Providers
network: true
overview: 'PC Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Schedule I Bank, and Digital Banking.


  PC Financial''s developer surface includes support, documentation, and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.4
  delta: -3.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pc-financial/refs/heads/main/screenshots/pc-financial-2026-08-07T191717.png
security:
- kind: domain-security
  name: Pc Financial Domain Security
  slug: pc-financial-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: pc-financial
tags:
- Financial Services
- Banking
- Canada
- Schedule I Bank
- Digital Banking
- Credit Cards
- Loyalty
- Interac
- Data Aggregation
website: https://www.pcfinancial.ca/en/
---
