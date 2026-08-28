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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pharmapacks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.packable.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.packable.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.packable.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.packable.com/contact-us/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pharmapacks-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Pharmapacks (Packable Holdings LLC) filed Chapter 11 on 2022-08-28 and ceased operations; pharmapacks.com is now a GoDaddy parked-domain lander that answers HTTP 200 with the same React parking shell for every path including /openapi.json and every /.well-known/*, and the live successor brand site www.packable.com is a WordPress marketing site with no developer section that 404s every spec, GraphQL and /.well-known probe.
  evidence:
  - status: 200
    url: https://pharmapacks.com/
  - status: 200
    url: https://pharmapacks.com/openapi.json
  - status: 404
    url: https://www.packable.com/openapi.json
  - status: 404
    url: https://www.packable.com/.well-known/agent-card.json
  - status: 404
    url: https://www.packable.com/graphql
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Pharmapacks was a New York-based e-commerce marketplace seller and third-party logistics operator, founded in 2010 in Long Island City, that grew into one of the largest independent sellers of health, beauty and personal-care goods on Amazon, eBay and Walmart Marketplace. The company rebranded as Packable Holdings LLC in 2021, agreed a SPAC merger with Highland Transcend Partners I Corp. that was abandoned in March 2022, and filed for Chapter 11 bankruptcy protection on 2022-08-28 before ceasing operations and liquidating substantially all of its assets. Its differentiator was an internal "Master Brain" marketplace-listing, repricing and fulfillment platform, but that technology was operated as an internal system and was never published as a public developer program: no developer portal, API reference, SDK, webhook catalog or machine-readable contract has ever been found on any host the company controlled. The pharmapacks.com domain is today a GoDaddy parking lander. A successor
  brand operating as Packable at packable.com, led by Pharmapacks/Packable co-founder Jonathan Webb, sells fulfillment, logistics and digital-enablement services and likewise publishes no public API.'
image: https://www.packable.com/wp-content/themes/packable_2023/assets/images/logo.svg
layout: provider
modified: '2026-08-26'
name: Pharmapacks
nav: Providers
network: true
overview: 'Pharmapacks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Fulfillment, and Logistics.


  Pharmapacks'' developer surface includes support and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Pharmapacks Domain Security
  slug: pharmapacks-domain-security
  summary_line: TLSv1.3
slug: pharmapacks
tags:
- Company
- E-Commerce
- Marketplace
- Fulfillment
- Logistics
- Retail
- Supply Chain
- Health and Beauty
- Distribution
- Defunct
website: https://www.packable.com/
---
