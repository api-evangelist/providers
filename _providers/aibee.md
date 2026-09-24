---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-09-24'
api_count: 2
apis:
- description: The hosted map-data surface behind Aibee's indoor map and wayfinding products. It is not documented as a public API and has no published reference or specification; it is recorded here because Aibee's
  name: Aibee BMap Indoor Map Data
  slug: aibee-bmap-indoor-map-data
- description: Aibee's all-scene AR indoor-wayfinding SDK for web and WeChat mini-programs, published with a full public reference (quickstart, constructor, events, methods, and the map, camera, model and particle c
  name: Aibee AR Navigation SDK
  slug: aibee-ar-navigation-sdk
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/security/aibee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aibee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aibee.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://map.aibee.cn/sdk-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://map.aibee.cn/sdk-docs/bmap/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://map.aibee.cn/sdk-docs/pages/guide/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/packages/aibee-packages.yml
  title: ''
  type: Packages
  url: packages/aibee-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/packages/aibee-packages.yml
  title: ''
  type: SDKs
  url: packages/aibee-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/components/aibee-components.yml
  title: ''
  type: Components
  url: components/aibee-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/conventions/aibee-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aibee-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/errors/aibee-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/aibee-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/lifecycle/aibee-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aibee-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/conformance/aibee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aibee-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/plans/aibee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aibee-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/rate-limits/aibee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aibee-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aibee/refs/heads/main/llms/aibee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aibee-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.aibee.cn/news.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aibee.cn/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aibee.cn/clause.html
created: '2026-09-13'
description: 'Aibee (爱笔智能, 爱笔（北京）智能科技有限公司) is a Beijing-based artificial-intelligence company founded in November 2017 by Dr. Yuanqing Lin, the former head of Baidu Research, that digitizes and automates physical commercial space. It fuses computer vision, multi-modal sensing, indoor positioning, 3D reconstruction, speech and big-data analytics into AI Mall OS and AI Parking OS — indoor 3D "reality maps", AR wayfinding, smart parking and find-my-car, and precise footfall/customer-flow analytics — deployed across shopping malls, parking garages, office towers, bank branches, automotive 4S dealerships, chain retail stores, airports, scenic areas and high-speed-rail stations. Its public developer surface is client-side rather than a REST platform: a first-party @aibee npm scope of indoor-map, AR-navigation and React Native navigation SDKs, and a public SDK reference at map.aibee.cn. No OpenAPI, GraphQL SDL, MCP server or agent card is published.'
image: https://www.aibee.cn/logo-blue.9fb45835.png
layout: provider
modified: '2026-09-13'
name: Aibee
nav: Providers
network: true
overview: 'Aibee publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer Vision, Indoor Mapping, and Indoor Navigation.


  Aibee''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Aibee Plans Pricing
  plan_count: 0
  slug: aibee-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Aibee Rate Limits
  slug: aibee-rate-limits
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 18.7
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aibee Domain Security
  slug: aibee-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: aibee
tags:
- Company
- Artificial Intelligence
- Computer Vision
- Indoor Mapping
- Indoor Navigation
- Augmented Reality
- Retail Technology
- Commercial Real Estate
- Smart Parking
- Location Services
- SDK
- China
website: https://www.aibee.cn/
---
