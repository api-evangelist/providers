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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aosongelectronics/refs/heads/main/hosts/aosongelectronics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aosongelectronics-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aosongelectronics/refs/heads/main/security/aosongelectronics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aosongelectronics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aosong.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://aosong.com/en/Products/list.aspx?lcid=164
- group: operate
  title: ''
  type: Support
  url: https://aosong.com/en/Contact/index.aspx
- group: start
  title: ''
  type: SignUp
  url: https://aosong.com/en/Login/index.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beian.miit.gov.cn/
coverage:
  checked: '2026-09-25'
  detail: The company's website is a JavaScript‑rendered site with no machine‑readable API specifications discovered.
  evidence:
  - status: 200
    url: https://aosong.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Aosongelectronics, operating under the brand ASAIR, is a Chinese semiconductor company specializing in MEMS smart sensor solutions. It offers a broad portfolio including temperature & humidity sensors, oxygen sensors, flow meters, pressure gauges, gas sensors, and related instrumentation. The company serves global markets with high‑precision, reliable sensor products for industrial, environmental, and consumer applications, emphasizing stability, low leakage, and long‑term performance.
layout: provider
modified: '2026-09-25'
name: Aosongelectronics
nav: Providers
network: true
overview: 'Aosongelectronics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Electronics, Manufacturing, and IoT.


  Aosongelectronics'' developer surface includes getting-started guide, support, signup flow, and 4 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aosongelectronics Domain Security
  slug: aosongelectronics-domain-security
  summary_line: no transport/DNS hardening detected
slug: aosongelectronics
tags:
- Company
- Technology
- Electronics
- Manufacturing
- IoT
website: https://aosong.com/en/
---
