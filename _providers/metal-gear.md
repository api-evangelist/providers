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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/metal-gear/hosts/metal-gear-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metal-gear-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.metalgear.xyz/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.metalgear.xyz/Payouts/First steps/gettingStarted
- group: docs
  title: ''
  type: Documentation
  url: https://doc.metalgear.xyz/
- group: auth
  href: https://artifacts.apis.io/metal-gear/security/metal-gear-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metal-gear-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metalgear.xyz/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://metalgear.xyz/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Metal Gear is a technology and defense solutions company specializing in advanced cyber‑physical systems, secure communications, and embedded hardware platforms. Founded to bridge the gap between cutting‑edge research and real‑world defense applications, Metal Gear offers a suite of APIs for device management, telemetry ingestion, and secure data exchange. The company collaborates with industry partners to deliver scalable, high‑integrity solutions for critical infrastructure and defense operations, emphasizing security, reliability, and compliance with international standards.
image: https://framerusercontent.com/images/NWRFa8N2gGUxNCIRPgniwSI09RA.png
layout: provider
modified: '2026-10-24'
name: Metal Gear
nav: Providers
network: true
overview: 'Metal Gear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Technology, Defense, Cyber-Physical, APIs, and Embedded Systems.


  Metal Gear''s developer surface includes getting-started guide, documentation, and 4 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Metal Gear Domain Security
  slug: metal-gear-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: metal-gear
tags:
- Technology
- Defense
- Cyber-Physical
- APIs
- Embedded Systems
website: https://metalgear.xyz/
---
