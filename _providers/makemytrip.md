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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/makemytrip/refs/heads/main/llms/makemytrip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/makemytrip-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/makemytrip/refs/heads/main/hosts/makemytrip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/makemytrip-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/makemytrip/refs/heads/main/vendors/makemytrip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/makemytrip-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/makemytrip/refs/heads/main/security/makemytrip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/makemytrip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.makemytrip.com/
created: '2026-09-22'
description: MakeMyTrip is a leading Indian online travel company that provides a comprehensive platform for booking flights, hotels, holiday packages, and rail tickets. Founded in 2000, it offers a user-friendly interface and mobile apps, serving millions of customers across India and abroad. The company exposes APIs for partners to integrate travel search, pricing, and booking functionalities, enabling developers to build travel solutions and services. This profile expands the stub with a detailed description for the API Evangelist network.
layout: provider
modified: '2026-09-22'
name: MakeMyTrip
nav: Providers
network: true
overview: MakeMyTrip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Booking, and India.
random_paper: 13
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Makemytrip Domain Security
  slug: makemytrip-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: makemytrip
tags:
- Company
- Travel
- Booking
- India
website: https://www.makemytrip.com/
---
