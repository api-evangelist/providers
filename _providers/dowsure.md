---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dowsure/well-known/dowsure-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dowsure-well-known.yml
- group: other
  href: https://artifacts.apis.io/dowsure/hosts/dowsure-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dowsure-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://world.dowsure.com/news/
- group: company
  title: ''
  type: Blog
  url: https://blog.dowsure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.dowsure.com/
- group: auth
  href: https://artifacts.apis.io/dowsure/security/dowsure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dowsure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://world.dowsure.com/en/
coverage:
  checked: '2026-10-24'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract discovered on any host.
  evidence:
  - status: 0
    url: https://api.dowsure.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Dowsure provides cross‑border e‑commerce financing solutions for sellers, platforms and financial institutions. It offers embedded financial services such as lines of credit, BNPL, term loans and merchant cash advances to meet multi‑currency capital needs of e‑commerce merchants across mainland China, Hong Kong, Singapore, Vietnam and other Asian markets. The company delivers these products through API technology and AI‑driven models, partnering with platforms like Amazon, Walmart and eBay and banks such as HSBC and SPDB.
image: https://world.dowsure.com/wp-content/uploads/2025/07/pretitle.png
layout: provider
modified: '2026-10-24'
name: Dowsure
nav: Providers
network: true
overview: 'Dowsure is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cross‑border E‑commerce Financing, Embedded Finance, and API Banking.


  Dowsure''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 41.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 9.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dowsure Domain Security
  slug: dowsure-domain-security
  summary_line: TLSv1.3
slug: dowsure
tags:
- Cross‑border E‑commerce Financing
- Embedded Finance
- API Banking
website: https://world.dowsure.com/en/
---
