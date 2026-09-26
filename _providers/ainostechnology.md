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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ainostechnology/refs/heads/main/security/ainostechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ainostechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eyenurse.net/
- group: company
  title: ''
  type: About
  url: https://www.eyenurse.net/pc/about
- group: company
  title: ''
  type: Newsroom
  url: https://www.eyenurse.net/pc/news
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.eyenurse.net/mobi/helpcenter
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/ainostechnology
coverage:
  checked: '2026-09-14'
  detail: 'Ainos Technology sells AI vision-screening systems to Chinese education bureaus, CDCs and eye hospitals, and its entire public surface is the eyenurse.net Vue single-page marketing site (products, solutions, cases, news, app downloads, a trial-request form and a customer login) whose shipped router — read straight out of https://eyenurse.net/js/app.3829f574.js — contains no developer, open-platform or documentation route at all, and whose 49 JavaScript chunks contain zero occurrences of 接口, 开发者 or 开放平台 (the 14 hits for 对接 are all about pairing the AI data-transfer module with 130+ third-party ophthalmic instruments, not about an API). The one API host the company operates, api.eyenurse.net, is the site''s own Spring Boot backend: its root serves the stock nginx welcome page and /newdeparture/v2/api-docs, /v3/api-docs, /doc.html, /swagger-ui.html and /swagger-resources all return Spring 404 JSON, so no contract is published there either. Every 200 on www.eyenurse.net is a soft
    404 — a control probe of /zz-api-evangelist-control-9f3a returns the same 8,071-byte SPA shell as /openapi.json, /graphql and /.well-known/agent-card.json — and docs./developer./open./portal.eyenurse.net exist only via a wildcard A record with no matching TLS certificate.'
  evidence:
  - status: 200
    url: https://www.eyenurse.net/
  - status: 200
    url: https://www.eyenurse.net/zz-api-evangelist-control-9f3a
  - status: 200
    url: https://www.eyenurse.net/openapi.json
  - status: 200
    url: https://www.eyenurse.net/.well-known/agent-card.json
  - status: 200
    url: https://api.eyenurse.net/
  - status: 404
    url: https://api.eyenurse.net/openapi.json
  - status: 404
    url: https://api.eyenurse.net/swagger.json
  - status: 404
    url: https://api.eyenurse.net/newdeparture/v3/api-docs
  - status: 404
    url: https://api.eyenurse.net/newdeparture/doc.html
  - status: 404
    url: https://api.eyenurse.net/graphql
  - status: 404
    url: https://api.eyenurse.net/.well-known/agent-card.json
  - status: 404
    url: https://api.eyenurse.net/.well-known/agent.json
  - status: 404
    url: https://api.eyenurse.net/llms.txt
  - status: 404
    url: https://m.eyenurse.net/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: Ainos Technology (北京爱诺斯科技有限公司, brand eYenurse) is a Beijing health-informatization company founded in 2016 that applies artificial intelligence to children's eye health and school health administration in China, selling to government and institutional buyers rather than to developers. Its products are a national vision and common-disease monitoring, early-warning and intervention system for education bureaus and schools, a student infectious-disease early-warning system, a 0-6 eye-health screening platform for maternal and child health institutions, AI screening hardware (smart visual-acuity charts and a module linking 130+ third-party ophthalmic instruments), and the eYenurse smart ophthalmology cloud platform. It reports deployments in all 31 provinces across 1,700+ institutions and is backed by Donghua Software (002065). It publishes no developer program, public API, SDK or machine-readable API contract.
image: https://www.eyenurse.net/img/logo.f7a8ff7d.svg
layout: provider
modified: '2026-09-14'
name: Ainos Technology
nav: Providers
network: true
overview: Ainos Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Public Health, and Vision Screening.
random_paper: 16
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ainostechnology Domain Security
  slug: ainostechnology-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ainostechnology
tags:
- Company
- Healthcare
- Artificial Intelligence
- Public Health
- Vision Screening
- Ophthalmology
- Education Technology
- Health Informatization
- China
website: https://www.eyenurse.net/
---
