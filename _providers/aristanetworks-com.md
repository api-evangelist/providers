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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/aristanetworks-com/hosts/aristanetworks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aristanetworks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aristanetworks-com/vendors/aristanetworks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aristanetworks-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aristanetworks-com/security/aristanetworks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aristanetworks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arista.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.aristanetworks.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Arista Networks provides software-driven cloud networking solutions for large data centers, enterprises, and service providers. Founded to pioneer high-performance Ethernet switching, Arista offers the Extensible Operating System (EOS), CloudVision, and a portfolio spanning 10‑100 Gbps platforms, AI networking, SD‑WAN, and security services. The company serves industries such as cloud, finance, media, and government, delivering scalable, programmable networking with open APIs and automation capabilities.
layout: provider
modified: '2026-10-23'
name: Arista Networks
nav: Providers
network: true
overview: Arista Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Cloud, Enterprise, and OpenAPI.
random_paper: 5
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aristanetworks Com Domain Security
  slug: aristanetworks-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aristanetworks-com
tags:
- Company
- Networking
- Cloud
- Enterprise
- OpenAPI
website: https://www.arista.com/
---
