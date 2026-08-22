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
  url: security/easyknock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.easyknock.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/easyknock_stock/
coverage:
  checked: '2026-08-12'
  detail: EasyKnock ceased operations on 2024-12-06; easyknock.com now serves only a static "EasyKnock has closed its doors" notice out of a Google Cloud Storage bucket, and the legacy api.easyknock.com host answers Cloudflare error 1016 because its origin DNS record has been deleted.
  evidence:
  - status: 200
    url: https://www.easyknock.com/
  - status: 530
    url: https://api.easyknock.com/openapi.json
  - status: 404
    url: https://www.easyknock.com/.well-known/api-catalog
  - status: 404
    url: https://api.github.com/orgs/easyknock
  reason: defunct
  state: none
created: '2026-08-12'
description: 'EasyKnock was a New York based residential real estate fintech, founded in 2016 by Jared Kessler, that pioneered consumer sale-leaseback in the United States: homeowners sold their house to EasyKnock for cash and stayed on as renting tenants with an option to repurchase. The company raised roughly $430 million in equity and debt and rolled up several proptech businesses — Ribbon Home, Onder, Balance Home, HomePace and FarmlandFinder — before consumer lawsuits and state attorney general and regulator actions in Massachusetts, Michigan, Connecticut, Texas, Maryland, South Carolina, Pennsylvania and Ohio over its sale-leaseback disclosures. EasyKnock announced it had closed its doors on December 6, 2024. Its website is now a single static shutdown notice, its api.easyknock.com host answers Cloudflare error 1016 (origin DNS deleted), and it never published a public developer program, API reference, SDK or machine-readable specification. This profile is retained as a historical
  record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-12'
name: EasyKnock
nav: Providers
network: true
overview: EasyKnock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Real Estate, PropTech, and Fintech.
random_paper: 2
score:
  band: minimal
  composite: 4.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Easyknock Domain Security
  slug: easyknock-domain-security
  summary_line: TLSv1.3 · DMARC
slug: easyknock
tags:
- Company
- Defunct
- Real Estate
- PropTech
- Fintech
- Sale Leaseback
- Home Equity
- Mortgage
- Consumer Finance
website: https://www.easyknock.com/
---
