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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://percipient.ai/
- group: company
  title: ''
  type: Blog
  url: https://percipient.ai/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://percipient.ai/feed/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/percipient-ai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/percipient-ai-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/percipient-ai-plans-pricing.yml
coverage:
  checked: '2026-08-26'
  detail: 'Percipient.ai sells Mirage as a deployed analyst platform to US Government and intelligence customers, not as an integrable product: the entire public site is four WordPress pages (home, About Mirage, Meet Our Team, News) with no developer, docs, API or sign-up link anywhere in the navigation or footer, and the only other live host, the deployed Mirage FMV application at fmv-mirage.global.percipient.ai, serves a login SPA with a 404 on every contract and /.well-known/ path.'
  evidence:
  - status: 200
    url: https://percipient.ai/
  - status: 404
    url: https://percipient.ai/openapi.json
  - status: 404
    url: https://percipient.ai/.well-known/api-catalog
  - status: 200
    url: https://fmv-mirage.global.percipient.ai/
  - status: 404
    url: https://fmv-mirage.global.percipient.ai/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Percipient.ai is a Silicon Valley artificial intelligence, machine learning and computer vision company, founded in 2017 by Founder & CEO Balan Ayyar, that builds Mirage - an intelligence analysis platform for United States national security and intelligence missions. Mirage performs faster-than-real-time exploitation of unstructured multimedia, visual and multi-INT data across three modules: an FMV module for full motion video, still imagery and multi-INT sensor data supporting identity creation, network discovery, pattern-of-life analysis and geo-correlation; a cloud GSM geospatial module providing geo-fenced alerting, change detection, custom object detection and temporal analysis; and a VRM vehicle recognition module delivered as a mobile appliance for mobile and fixed surveillance with home-station cross-mission correlation. The platform is deployed both at the edge for live stream ingest and in the cloud at petabyte scale, and has been operationally procured by organizations
  in the US Intelligence Community and the National Geospatial-Intelligence Agency. Percipient.ai sells Mirage through federal contracting vehicles and is listed as Awardable on the CDAO Tradewinds Solutions Marketplace. It operates no public developer program: as of August 2026 it publishes no API, developer portal, API reference, SDK or machine-readable contract of any kind.'
image: https://percipient.ai/wp-content/uploads/2020/07/preview.png
layout: provider
modified: '2026-08-26'
name: Percipient.ai
nav: Providers
network: true
overview: 'Percipient.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine-Learning, Computer-Vision, National Security, and Defense.


  Percipient.ai''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Percipient Ai Plans Pricing
  plan_count: 0
  slug: percipient-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Percipient Ai Rate Limits
  slug: percipient-ai-rate-limits
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Percipient Ai Domain Security
  slug: percipient-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: percipient-ai
tags:
- Artificial Intelligence
- Machine-Learning
- Computer-Vision
- National Security
- Defense
- Intelligence Analysis
- Geospatial
- Video Analytics
- Government
website: https://percipient.ai/
---
