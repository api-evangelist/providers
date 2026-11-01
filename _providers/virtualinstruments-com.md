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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Virtual Instruments platform providing virtual sensor data and analytics.
  name: Virtual Instruments API
  slug: virtual-instruments-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/virtualinstruments-com/well-known/virtualinstruments-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/virtualinstruments-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/virtualinstruments-com/well-known/virtualinstruments-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/virtualinstruments-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/virtualinstruments-com/vendors/virtualinstruments-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/virtualinstruments-com-vendors.yml
- group: other
  href: https://artifacts.apis.io/virtualinstruments-com/hosts/virtualinstruments-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/virtualinstruments-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.virtana.com/trust/
- group: operate
  title: ''
  type: Support
  url: https://www.virtana.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.virtana.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtana.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.virtana.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.virtana.com/company/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.virtana.com/blog/
- group: company
  title: ''
  type: Website
  url: https://virtualinstruments.com
- group: auth
  href: https://artifacts.apis.io/virtualinstruments-com/security/virtualinstruments-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/virtualinstruments-com-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider’s documented docs host.
  evidence:
  - status: 200
    url: https://docs.virtana.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Virtual Instruments provides a platform for virtual instrumentation and data acquisition, enabling developers to integrate hardware-like measurement capabilities into software applications via APIs. The company focuses on delivering scalable, cloud‑native solutions for test and measurement, supporting a range of industries including manufacturing, research, and IoT. Their services include virtual sensor data streams, real‑time analytics, and SDKs for multiple programming languages, aiming to simplify complex instrumentation workflows for modern developers.
image: https://www.virtana.com/wp-content/uploads/2x_Virtana-Wordmark-Two-Stripes-Three-Color-Dark-Blue.jpg
layout: provider
modified: '2026-10-29'
name: Virtual Instruments
nav: Providers
network: true
overview: 'Virtual Instruments is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Virtual Instruments, Data Acquisition, Instrumentation, and Cloud Services.


  Virtual Instruments'' developer surface includes support, engineering blog, and 11 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 60.7
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Virtualinstruments Com Domain Security
  slug: virtualinstruments-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: virtualinstruments-com
tags:
- Company
- Virtual Instruments
- Data Acquisition
- Instrumentation
- Cloud Services
website: https://virtualinstruments.com
---
