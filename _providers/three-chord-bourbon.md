---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/three-chord-bourbon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://threechordbourbon.com/
- group: company
  title: ''
  type: About
  url: https://threechordbourbon.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://threechordbourbon.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://threechordbourbon.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://threechordbourbon.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://threechordbourbon.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/three-chord-bourbon-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Three Chord Bourbon, Inc. is a whiskey blending house selling bottled spirits through distributors and a WooCommerce/age-gated online store; every contract-discovery path returned a real 404 and the only machine-readable endpoint on the domain is the stock WordPress /wp-json/ index that ships with the CMS, not an API the company published.
  evidence:
  - status: 404
    url: https://threechordbourbon.com/openapi.json
  - status: 404
    url: https://threechordbourbon.com/.well-known/agent-card.json
  - status: 404
    url: https://threechordbourbon.com/.well-known/api-catalog
  - status: 404
    url: https://store.threechordbourbon.com/openapi.json
  - status: 307
    url: https://store.threechordbourbon.com/graphql
  - status: 200
    url: https://threechordbourbon.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: 'Three Chord Bourbon, Inc. is an American whiskey blending house founded in 2017 by Rock & Roll Hall of Fame guitarist, producer and songwriter Neil Giraldo, who serves as founder, creative director and chairman. The company blends straight bourbon whiskeys aged a minimum of four years using a proprietary process it calls "Perfectly Tuned Taste," and has extended the line into rye and cask-finished expressions including a pinot noir cask finish and the Amplify rye. Product is co-packed at Ugly Dog Distillery in Chelsea, Michigan, and the corporate office is in Clarence, New York. The brand sells through wholesale distribution and a direct-to-consumer online store at store.threechordbourbon.com. It is a consumer packaged goods company: it publishes no developer portal, no API documentation, no SDKs and no machine-readable API contract of any kind.'
image: https://threechordbourbon.com/wp-content/uploads/3Chord-record-logo-cream.svg
layout: provider
modified: '2026-08-30'
name: Three Chord Bourbon
nav: Providers
network: true
overview: 'Three Chord Bourbon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Food and Beverage, Alcoholic Beverages, and Whiskey.


  Three Chord Bourbon''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Three Chord Bourbon Domain Security
  slug: three-chord-bourbon-domain-security
  summary_line: TLSv1.3
slug: three-chord-bourbon
tags:
- Company
- Consumer Packaged Goods
- Food and Beverage
- Alcoholic Beverages
- Whiskey
- Bourbon
- Spirits
- Retail
- E-Commerce
- Direct to Consumer
website: https://threechordbourbon.com/
---
