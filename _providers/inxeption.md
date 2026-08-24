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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-23'
  detail: Inxeption shut down on 2024-08-15 and the company's namespace is gone — every developer-facing host (api., docs., developer., developers., support., app., platform.inxeption.com) is NXDOMAIN, the github.com/inxeption organization still exists but holds zero public repositories, and no package named inxeption exists on npm, PyPI, RubyGems, crates.io or Packagist; the only host left is the apex, which now returns a serp.domains "premium aged domain" for-sale listing whose SPA catch-all answers HTTP 200 with the same HTML shell for /openapi.json, /llms.txt and every /.well-known/ path, and the Wayback record shows inxeption.com going 404 in September 2024 with no API reference or developer portal ever archived under it.
  evidence:
  - status: 200
    url: https://inxeption.com/
  - status: 200
    url: https://inxeption.com/openapi.json
  - status: 200
    url: https://inxeption.com/.well-known/agent-card.json
  - status: 200
    url: https://inxeption.com/llms.txt
  - status: 0
    url: https://api.inxeption.com/
  - status: 0
    url: https://docs.inxeption.com/
  - status: 0
    url: https://developer.inxeption.com/
  - status: 0
    url: https://support.inxeption.com/
  - status: 200
    url: https://api.github.com/orgs/inxeption/repos
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=inxeption
  reason: defunct
  state: none
created: '2026-08-23'
description: 'Inxeption was a B2B "industrial commerce" software company founded in 2017 by serial entrepreneur Farzad Dibachi and headquartered in Silicon Valley (San Jose / Cupertino, California). It sold a cloud commerce platform that let manufacturers, distributors and wholesalers stand up a branded online storefront and digital product catalog, then manage quoting, contract-specific pricing, purchase orders, bulk and multimodal orders, freight and logistics, returns, payments and sales analytics from one place — a category it marketed as the "Industrial Commerce SuperApp". Its best-known product was Inxeption Zippy, launched in March 2019 with UPS after an equity investment from the UPS Strategic Enterprise Fund, which bundled UPS as the shipper of choice into the storefront. The company raised roughly $186M across its rounds, including a $125M Series E in January 2022. Inxeption shut down on 2024-08-15. It never operated a public developer program: no developer portal, API reference,
  OpenAPI/AsyncAPI/GraphQL contract, SDK or package was ever published, and its integration story was bespoke customer and EDI connections delivered under contract. Today only the apex domain resolves, and it no longer belongs to the company — it is listed for sale on the serp.domains domain marketplace. This profile is retained as a historical company record.'
layout: provider
modified: '2026-08-23'
name: Inxeption
nav: Providers
network: true
overview: Inxeption is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ecommerce, B2B Ecommerce, Supply Chain, and Logistics.
random_paper: 3
score:
  band: minimal
  composite: 4.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
slug: inxeption
tags:
- Company
- Ecommerce
- B2B Ecommerce
- Supply Chain
- Logistics
- Freight
- Industrial
- Manufacturing
- Marketplace
- Order Management
---
