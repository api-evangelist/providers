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
api_count: 1
apis:
- description: BoltWise API provides quoting and sourcing capabilities for industrial distributors.
  name: BoltWise API
  slug: boltwise-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boltwise/refs/heads/main/llms/boltwise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boltwise-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boltwise/refs/heads/main/hosts/boltwise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boltwise-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boltwise/refs/heads/main/vendors/boltwise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boltwise-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getboltwise.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getboltwise.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getboltwise.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://getboltwise.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boltwise/refs/heads/main/security/boltwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boltwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getboltwise.com/
coverage:
  checked: '2026-10-02'
  detail: Main website returns a large JavaScript-rendered HTML page with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://getboltwise.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: BoltWise provides an AI‑powered quoting, sourcing and catalog‑management platform for industrial distributors. The SaaS solution automates RFQ processing, matches parts, integrates with ERP systems such as Epicor Prophet 21, INxSQL and Infor CloudSuite, and streamlines purchase‑order creation. Based in Denver, Colorado, BoltWise helps distributors accelerate quote turnaround by 3‑4×, reduce manual data entry, and improve procurement efficiency across the fastener and industrial supply chain.
image: https://cdn.prod.website-files.com/643e07a88d156000820b2e66/6a850eb74130f32f0706d509_boltwise-og-share-industrial.jpg
layout: provider
modified: '2026-10-02'
name: BoltWise
nav: Providers
network: true
overview: 'BoltWise publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Quoting, ERP Integration, and Industrial Distribution.


  BoltWise''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boltwise Domain Security
  slug: boltwise-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: boltwise
tags:
- Company
- Artificial Intelligence
- Quoting
- ERP Integration
- Industrial Distribution
website: https://getboltwise.com/
---
