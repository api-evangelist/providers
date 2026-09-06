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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://xenesis.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xenesis-io/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/xenesisio
- group: operate
  title: ''
  type: Contact
  url: mailto:info@xenesis.io
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/xenesis_stock/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/company/xenesis/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xenesis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xenesis-llms.txt
coverage:
  checked: '2026-09-04'
  detail: Xenesis sells free-space optical terminals (the Xen-Hub) and planned satellite network capacity to government and commercial satellite operators — software is not the product — and its entire xenesis.io origin now answers HTTP 401 behind a Flywheel managed-WordPress site-wide password lock, so even the marketing site is unreadable; the last complete archived version of the site carried only Home, News and About Us in its navigation, with no developer portal, API, docs or SDK section.
  evidence:
  - status: 401
    url: https://xenesis.io/
  - status: 401
    url: https://xenesis.io/.well-known/security.txt
  - status: 401
    url: https://xenesis.io/openapi.json
  - status: 401
    url: https://xenesis.io/llms.txt
  - status: 200
    url: https://web.archive.org/web/20240910001501/https://xenesis.io/
  - status: 404
    url: https://registry.npmjs.org/xenesis
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Xenesis, Inc. is an optical satellite communications company founded in 2017 by Mark LaPenna and headquartered in Lisle, Illinois. It builds the Xen-Hub, a free-space optical (laser) communications terminal enabled by a technology transfer from NASA''s Jet Propulsion Laboratory and rated at greater than 10 Gbps, and plans Intercessor, a space-to-ground optical mesh network intended to backhaul high-bandwidth data with lower latency and higher capacity than radio-frequency or terrestrial fiber links. The company has taken Space Development Agency optical-terminal awards (Phase 1 in August 2022, a Phase 2 follow-on in December 2023) built to the SDA OCT v3.1 and v4.0 standards, signed a payload agreement with Airbus for a Bartolomeo demonstration slot on the International Space Station, and holds a $1.2M agreement with Georgia Tech for satellite optical communications work. Xenesis is a space hardware and telecommunications-infrastructure company, not a software vendor: as of
  this profiling pass it publishes no public API, developer portal, SDK, or machine-readable contract of any kind, and its own website is currently returning an HTTP 401 site-wide password lock.'
layout: provider
modified: '2026-09-04'
name: Xenesis
nav: Providers
network: true
overview: Xenesis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Satellite, Optical Communications, and Free Space Optics.
random_paper: 11
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Xenesis Domain Security
  slug: xenesis-domain-security
  summary_line: TLSv1.3
slug: xenesis
tags:
- Company
- Space
- Satellite
- Optical Communications
- Free Space Optics
- Laser Communications
- Telecommunications
- Aerospace
- Defense
- Connectivity
website: https://xenesis.io/
---
