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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Anaimo provides AI-driven automation solutions but no public machine‑readable API specification was found.
  name: Anaimo API
  slug: anaimo-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/anaimo/hosts/anaimo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anaimo-hosts.yml
- group: build
  href: https://artifacts.apis.io/anaimo/packages/anaimo-packages.yml
  title: ''
  type: Packages
  url: packages/anaimo-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.anaimo.com/
- group: build
  title: ''
  type: SDKs
  url: https://anaimo.com/sdk/
- group: start
  title: ''
  type: Login
  url: https://anaimo.com/login/
- group: auth
  href: https://artifacts.apis.io/anaimo/security/anaimo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anaimo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anaimo.com/
- group: company
  title: ''
  type: Blog
  url: https://anaimo.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anaimo.com/politica-de-privacidad
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anaimo.com/aviso-legal
coverage:
  checked: '2026-10-16'
  detail: Anaimo's website provides no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable API spec despite open homepage.
  evidence:
  - status: 404
    url: https://anaimo.com/openapi.json
  - status: 404
    url: https://anaimo.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Anaimo is a Spanish AI company offering virtual assistants and AI-driven automation solutions for retail, industry, academia and other sectors. Their platform provides tools for real‑time product classification, quality‑control defect detection, and customizable virtual employee assistants. Anaimo aims to streamline operations, reduce costs, and enhance customer experiences through artificial intelligence.
layout: provider
modified: '2026-10-15'
name: Anaimo
nav: Providers
network: true
overview: 'Anaimo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Virtual Assistant, and Retail.


  Anaimo''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 14.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anaimo Domain Security
  slug: anaimo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anaimo
tags:
- Company
- Artificial Intelligence
- Automation
- Virtual Assistant
- Retail
website: https://anaimo.com/
---
