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
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mycotechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mycoiq.com/
- group: company
  title: ''
  type: About
  url: https://www.mycoiq.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.mycoiq.com/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://www.mycoiq.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mycoiq.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mycoiq.com/privacy-policy/
- group: other
  title: ''
  type: Products
  url: https://www.mycoiq.com/ingredients/
- group: other
  title: ''
  type: Resources
  url: https://www.mycoiq.com/resources/
- group: company
  title: ''
  type: Careers
  url: https://www.mycoiq.com/careers/
- group: other
  title: ''
  type: Patents
  url: https://www.mycoiq.com/patents/
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/mycotechnology_stock/
coverage:
  checked: '2026-08-04'
  detail: MycoTechnology sells mushroom-mycelium fermented food ingredients (ClearIQ, ClearHT, Zukora honey truffle sweet protein) to food manufacturers; its only web property is the WordPress marketing site at www.mycoiq.com, which has no developer section, and api./developer./docs./app.mycoiq.com resolve to no DNS records at all.
  evidence:
  - status: 404
    url: https://www.mycoiq.com/openapi.json
  - status: 404
    url: https://www.mycoiq.com/llms.txt
  - status: 404
    url: https://www.mycoiq.com/.well-known/agent-card.json
  - status: 404
    url: https://www.mycoiq.com/developers
  - status: 403
    url: https://forgeglobal.com/mycotechnology_stock/
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'MycoTechnology, Inc. is a Colorado-based food ingredient technology company that uses mushroom mycelial fermentation to create naturally derived ingredients for the food and beverage industry. Operating publicly as Myco (mycoiq.com), the company develops and manufactures flavor-modulation and sweetening ingredients — ClearIQ natural flavor, ClearHT natural flavor, and Zukora honey truffle sweet protein — used for bitterness masking, off-note mitigation, sugar reduction, and clean-label formulation in plant proteins, meat analogues, dairy alternatives, and health and wellness products. It also offers Fermentation as a Service (FaaS) and a MyCulinary culinary science program for food brands. This is an ingredient manufacturing and food science business, not a software or API company: it publishes no developer portal, no API documentation, and no machine-readable API contract.'
image: https://www.mycoiq.com/wp-content/uploads/2023/06/Mycotech-logo-header_203x71.svg
layout: provider
modified: '2026-08-04'
name: MycoTechnology
nav: Providers
network: true
overview: 'MycoTechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Ingredients, Fermentation, and Biotechnology.


  MycoTechnology''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 10.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mycotechnology/refs/heads/main/screenshots/mycotechnology-2026-08-07T184513.png
security:
- kind: domain-security
  name: Mycotechnology Domain Security
  slug: mycotechnology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mycotechnology
tags:
- Company
- Food
- Ingredients
- Fermentation
- Biotechnology
- Food Science
- Manufacturing
- Agriculture
website: https://www.mycoiq.com/
---
