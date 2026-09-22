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
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airwavzsolutions/refs/heads/main/security/airwavzsolutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airwavzsolutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airwavz.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airwavzsolutions/refs/heads/main/llms/airwavzsolutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airwavzsolutions-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://airwavz.com/news-highlights/
- group: company
  title: ''
  type: BlogRSS
  url: https://airwavz.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://airwavz.com/hyperwavz/
- group: operate
  title: ''
  type: Contact
  url: https://airwavz.com/contact/
coverage:
  checked: '2026-09-19'
  detail: 'Airwavz Solutions funds, builds and operates physical in-building wireless infrastructure (neutral-host DAS, ERRCS, managed Wi-Fi, fiber): airwavz.com is a WordPress marketing site whose 26-page sitemap has no developer, docs, API, privacy or terms page, every contract-discovery and /.well-known/ path 404s, no GitHub org or npm/PyPI package exists, and the only machine-readable surface is a company-description /llms.txt and the stock WordPress /wp-json/ CMS endpoint.'
  evidence:
  - status: 404
    url: https://airwavz.com/developers/
  - status: 404
    url: https://airwavz.com/api/
  - status: 404
    url: https://airwavz.com/openapi.json
  - status: 404
    url: https://airwavz.com/.well-known/api-catalog
  - status: 404
    url: https://airwavz.com/.well-known/agent-card.json
  - status: 200
    url: https://airwavz.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/airwavz
  reason: not-a-software-company
  state: none
created: '2026-09-19'
description: 'Airwavz Solutions is a Charlotte, North Carolina in-building wireless infrastructure company founded in 2013 that funds, designs, builds, owns and operates neutral-host distributed antenna systems (DAS), public safety emergency responder radio systems (ERRCS), managed Wi-Fi (sold as Hyperwavz), fiber backbones and private LTE/5G smart-building networks for commercial office, healthcare, hospitality, multifamily and event-venue properties across the United States, with over 154 million square feet under agreement and carrier agreements with AT&T, Verizon and T-Mobile. It is a physical wireless infrastructure operator rather than a software company: as of this profile it publishes no developer program, API documentation or machine-readable API contract, though it does serve an llms.txt describing the company for AI agents.'
image: https://airwavz.com/wp-content/uploads/2025/09/Airwavz-Logo.svg
layout: provider
modified: '2026-09-19'
name: Airwavz Solutions
nav: Providers
network: true
overview: 'Airwavz Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Wireless Infrastructure, Telecommunications, Distributed Antenna Systems, In-Building Wireless, and Public Safety.


  Airwavz Solutions'' developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airwavzsolutions Domain Security
  slug: airwavzsolutions-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airwavzsolutions
tags:
- Wireless Infrastructure
- Telecommunications
- Distributed Antenna Systems
- In-Building Wireless
- Public Safety
- Wi-Fi
- Fiber
- Private 5G
- Real-Estate
- United States
- Company
website: https://airwavz.com/
---
