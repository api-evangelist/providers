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
  url: security/omnidian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.omnidian.com/
- group: company
  title: ''
  type: Blog
  url: https://www.omnidian.com/insights/
- group: operate
  title: ''
  type: Support
  url: https://www.omnidian.com/commercial-client-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.omnidian.com/HelpCenter/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.omnidian.com/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.omnidian.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omnidian
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/omnidian_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/omnidian-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Omnidian's production API gateway at api.service.omnidian.com (CNAME api-gateway-kube.service.omnidian.com) rejects every anonymous request with HTTP 401 — including /openapi.json, /graphql and every /.well-known/* path — and the only reachable human surfaces are the Client Portal SPA and a Salesforce Field Service Partner Portal login, while the marketing site's full page sitemap contains no developer, API or documentation page at all.
  evidence:
  - status: 401
    url: https://api.service.omnidian.com/openapi.json
  - status: 401
    url: https://api.service.omnidian.com/graphql
  - status: 404
    url: https://www.omnidian.com/.well-known/api-catalog
  - status: 200
    url: https://omnidian.my.site.com/OmnidianFieldServicePartnerPortal/s/
  reason: partner-login
  state: gated
created: '2026-08-04'
description: Omnidian, Inc. is a Seattle-based clean energy performance assurance company, founded in 2015, that protects and accelerates investments in residential and commercial solar and battery storage. Its proprietary, machine-learning driven software platform continuously monitors distributed solar assets, diagnoses hardware, communication and environmental faults such as soiling, shading and snow, dispatches a nationwide field service technician network across 48 states, Washington D.C. and Puerto Rico, and underwrites a 95% energy production guarantee that reimburses owners for covered shortfalls. Omnidian serves installers, EPCs, developers, IPPs, solar financing providers, commercial real estate owners and asset investors, and is a Certified B Corporation and a member of the SunSpec Alliance. Its monitoring platform, client portal and field service partner portal are operated as private, authenticated systems; Omnidian publishes no public developer program, API documentation, or
  machine-readable API contract.
image: https://www.omnidian.com/wp-content/uploads/2023/12/logo3x.png
layout: provider
modified: '2026-08-04'
name: Omnidian
nav: Providers
network: true
overview: 'Omnidian is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Solar, Clean Energy, and Renewable Energy.


  Omnidian''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.6
  delta: -1.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omnidian/refs/heads/main/screenshots/omnidian-2026-08-07T190149.png
security:
- kind: domain-security
  name: Omnidian Domain Security
  slug: omnidian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: omnidian
tags:
- Company
- Energy
- Solar
- Clean Energy
- Renewable Energy
- Asset Management
- Monitoring
- Performance Assurance
- Battery Storage
- Field Service
website: https://www.omnidian.com/
---
