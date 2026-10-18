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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Car IQ payment platform
  name: Car IQ API
  slug: car-iq-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/car-iq/refs/heads/main/hosts/car-iq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/car-iq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/car-iq/refs/heads/main/vendors/car-iq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/car-iq-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cariqpay.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.cariqpay.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/car-iq/refs/heads/main/security/car-iq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/car-iq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cariqpay.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI or other machine‑readable contract found on any discovered host.
  evidence:
  - status: 404
    url: https://api.cariqpay.com/openapi.json
  - status: 404
    url: https://www.cariqpay.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Car IQ provides a modern, card‑less vehicle payments platform that enables fleets, merchants and drivers to transact seamlessly. Their solution replaces traditional fuel cards with digital payments, offering real‑time receipts, fraud prevention, and streamlined back‑office operations. Car IQ’s technology integrates with banks and telematics to deliver secure, efficient payments across local, short‑haul, and national fleets.
image: https://cdn.prod.website-files.com/6564327980f3c207d70b5922/67d3f15313eafafc4aa0ce2b_67c804fd38d37c39d174f182_OGI%20-%20Home%20page.jpg
layout: provider
modified: '2026-10-06'
name: Car IQ
nav: Providers
network: true
overview: 'Car IQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fleet Management, and Fintech.


  Car IQ''s developer surface includes documentation and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Car Iq Domain Security
  slug: car-iq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: car-iq
tags:
- Company
- Payments
- Fleet Management
- Fintech
website: https://www.cariqpay.com
---
