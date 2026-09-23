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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://agripedia.co.jp/
- group: company
  title: ''
  type: Newsroom
  url: https://agripedia.co.jp/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agripedia.co.jp/news/detail/privacy_policy
- group: company
  title: ''
  type: Blog
  url: https://note.com/agripedia
- group: company
  title: ''
  type: BlogRSS
  url: https://note.com/agripedia/rss
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgriPedia
- group: company
  title: ''
  type: Careers
  url: https://herp.careers/careers/companies/agripedia
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/agripedia/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agripedia/refs/heads/main/security/agripedia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agripedia-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agripedia/refs/heads/main/llms/agripedia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agripedia-llms.txt
coverage:
  checked: '2026-09-13'
  detail: 'Agripedia ships software only as closed end-user applications: its corporate site is a two-route Nuxt SPA (sitemap lists exactly / and /news) with no developer, docs, portal or integration link anywhere, kanri.agripedia.co.jp (AP管理システム) answers every path with a 401 "please register or sign in" body or a 302 to /users/sign_in, and connect.agripedia.co.jp calls itself "AgriPedia 社内向けSCMシステム" — an internal supply-chain tool — in its own meta description, so there is no public API being marketed and nothing gated behind a sales form either.'
  evidence:
  - status: 200
    url: https://agripedia.co.jp/
  - status: 200
    url: https://agripedia.co.jp/sitemap-static.xml
  - status: 200
    url: https://agripedia.co.jp/.well-known/zz-control-9f3a
  - status: 404
    url: https://material-sales.agripedia.co.jp/openapi.json
  - status: 404
    url: https://material-sales.agripedia.co.jp/graphql
  - status: 404
    url: https://material-sales.agripedia.co.jp/llms.txt
  - status: 404
    url: https://material-sales.agripedia.co.jp/.well-known/agent-card.json
  - status: 404
    url: https://material-sales.agripedia.co.jp/.well-known/api-catalog
  - status: 401
    url: https://kanri.agripedia.co.jp/openapi.json
  - status: 302
    url: https://kanri.agripedia.co.jp/api-docs
  - status: 200
    url: https://connect.agripedia.co.jp/openapi.json
  - status: 404
    url: https://registry.npmjs.org/agripedia
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: Agripedia (アグリぺディア株式会社) is a Tokyo agricultural technology company, founded in June 2019 and headquartered in Nishi-Gotanda, Shinagawa-ku, that connects mid- and large-scale Japanese farms and production areas with food-service and food-manufacturing buyers. It supports growers from GAP certification through to the sale of the certified produce, runs a B2B direct-sales channel for GAP-certified commercial agricultural products, sells crop-protection materials and fertilizer, and operates its own production management system for cultivation history and traceability. It holds JGAP group certification (March 2023) and is a GAP partner of Japan's Ministry of Agriculture, Forestry and Fisheries. Its software reaches farms, buyers and staff as closed, credentialed web applications; the company publishes no developer program, no public API, and no machine-readable contract on any host it operates.
image: https://storage.googleapis.com/production-os-assets/assets/b88741c2-9769-459d-8a72-ec63d33322a4
layout: provider
modified: '2026-09-13'
name: Agripedia
nav: Providers
network: true
overview: 'Agripedia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Farm Management, and Food Supply Chain.


  Agripedia''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 7.9
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agripedia Domain Security
  slug: agripedia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agripedia
tags:
- Company
- Agriculture
- AgTech
- Farm Management
- Food Supply Chain
- Traceability
- GAP Certification
- B2B Marketplace
- Japan
website: https://agripedia.co.jp/
---
