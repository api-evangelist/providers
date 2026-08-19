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
  url: security/vancity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vancity.com/
- group: operate
  title: ''
  type: Support
  url: https://support.vancity.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vancity
created: '2026-07-23'
description: 'Vancity (Vancouver City Savings Credit Union) is a member-owned financial co-operative headquartered in Vancouver, British Columbia, and the largest community credit union in Canada, with over 543,000 members, roughly CA$35 billion in assets, and about 60 branches across the Lower Mainland and Vancouver Island. Founded in 1946 as an open-bond credit union, it is provincially chartered and cooperatively governed, offering retail and business banking, mortgages, foreign exchange, Visa cards, insurance, and investment advice, with values-based and impact-lending positioning. Vancity exposes no first-party public developer API portal: developer.vancity.com and developers.vancity.com do not resolve. It participates in Canada''s shared payment rails through Central 1 (its banking-technology and payments provider, including enhanced Interac e-Transfer real-time payments) and Payments Canada, while third-party consumer data access is provided through aggregators such as Plaid and Flinks.
  Canada''s federal Consumer-Driven Banking (open banking) framework is legislated but not yet operational, so any programmatic account access today is voluntary and aggregator-mediated rather than served by a documented Vancity API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Vancity
nav: Providers
network: true
overview: 'Vancity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Credit Union, and Co-operative.


  Vancity''s developer surface includes support and 3 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 2.4
  delta: -3.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Vancity Domain Security
  slug: vancity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vancity
tags:
- Financial Services
- Banking
- Canada
- Credit Union
- Co-operative
- Interac
- Payments
- Data Aggregation
website: https://www.vancity.com/
---
