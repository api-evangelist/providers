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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/central-coast-agriculture-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ccagriculture.com/
- group: company
  title: ''
  type: About
  url: https://www.ccagriculture.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.ccagriculture.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ccagriculture.com/privacy-policy
- group: other
  title: ''
  type: Brand
  url: https://rawgarden.farm/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/centralcoastagriculturellc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/central-coast-agriculture_stock/
coverage:
  checked: '2026-08-09'
  detail: Central Coast Agriculture is a cannabis farm and CPG manufacturer whose corporate site is seven static pages (about, farming, genetics, brand guidelines, contact, privacy) with no developer section; ccagriculture.com answers HTTP 200 to /openapi.json, /graphql and every /.well-known/* path only because it serves its homepage as a catch-all — byte-identical to a control path — while the Raw Garden brand host genuinely 404s all of them.
  evidence:
  - status: 200
    url: https://www.ccagriculture.com/
  - status: 200
    url: https://www.ccagriculture.com/bogus-control-xyz
  - status: 200
    url: https://www.ccagriculture.com/openapi.json
  - status: 404
    url: https://rawgarden.farm/openapi.json
  - status: 404
    url: https://rawgarden.farm/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/Central-Coast-Agriculture
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'Central Coast Agriculture, Inc. (CCA) is a vertically integrated California cannabis cultivator and manufacturer headquartered in the Santa Ynez Valley north of Santa Barbara, best known for its Raw Garden brand of fresh-frozen concentrates, vapes and infused pre-rolls. The company describes itself as a progressive farm focused on utilizing science and sustainability to grow quality, modern crops, and operates its own farming, genetics/breeding and extraction programs. It is a physical agricultural and consumer-packaged-goods business: it publishes a corporate site, a consumer brand site and a wholesale ordering page, but no public API, developer portal, SDK or machine-readable specification of any kind.'
image: https://www.ccagriculture.com/files/mask-group-622x_53254.png
layout: provider
modified: '2026-08-09'
name: Central Coast Agriculture
nav: Providers
network: true
overview: Central Coast Agriculture is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Cannabis, Farming, and Consumer Packaged Goods.
random_paper: 2
score:
  band: minimal
  composite: 7.1
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Central Coast Agriculture Domain Security
  slug: central-coast-agriculture-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: central-coast-agriculture
tags:
- Company
- Agriculture
- Cannabis
- Farming
- Consumer Packaged Goods
- Manufacturing
- California
website: https://www.ccagriculture.com/
---
