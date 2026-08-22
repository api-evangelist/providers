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
  url: security/califia-farms-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/califia-farms-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.califiafarms.com/
- group: operate
  title: ''
  type: Support
  url: https://www.califiafarms.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.califiafarms.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.califiafarms.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Califia-Farms
- group: company
  title: ''
  type: Press
  url: https://www.califiafarms.com/press/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/califia-farms-stock
coverage:
  checked: '2026-08-08'
  detail: Califia Farms is a plant-based beverage manufacturer whose only public web presence is a Gatsby marketing and recipe site on Netlify; api., developer., developers. and docs.califiafarms.com do not resolve in DNS at all, and the company GitHub organization has zero public repositories.
  evidence:
  - status: 404
    url: https://www.califiafarms.com/openapi.json
  - status: 404
    url: https://www.califiafarms.com/.well-known/agent-card.json
  - status: 404
    url: https://www.califiafarms.com/llms.txt
  - status: 404
    url: https://www.califiafarms.co.uk/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/califia-farms
  reason: not-a-software-company
  state: none
created: '2026-08-08'
description: Califia Farms, LLC is a Los Angeles, California based plant-based beverage company founded in 2010 by Greg Steltenpohl and named for the mythical Queen Califia. It manufactures and distributes non-dairy oatmilks, almondmilks and organic soymilks, coffee creamers, barista blends, cold brew coffees and teas, and ready-to-drink creamy refreshers, sold through grocery retail, foodservice distribution and direct-to-consumer channels across North America and Europe. Its public web presence is a marketing, recipe and where-to-buy site built on Gatsby and hosted on Netlify; the company publishes no developer program, no API documentation, and no machine-readable API contract.
image: https://avatars.githubusercontent.com/u/101840768?v=4
layout: provider
modified: '2026-08-08'
name: Califia Farms
nav: Providers
network: true
overview: 'Califia Farms is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, Plant-Based, and Beverages.


  Califia Farms'' developer surface includes support and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.3
  delta: -0.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Califia Farms Domain Security
  slug: califia-farms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: califia-farms
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Plant-Based
- Beverages
- Retail
- Manufacturing
website: https://www.califiafarms.com/
---
