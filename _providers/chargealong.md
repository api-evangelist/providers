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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Public EV charging site data API, free and keyless.
  name: ChargeAlong API
  slug: chargealong-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chargealong/refs/heads/main/conformance/chargealong-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chargealong-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chargealong/refs/heads/main/llms/chargealong-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chargealong-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chargealong/refs/heads/main/hosts/chargealong-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chargealong-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chargealong/refs/heads/main/vendors/chargealong-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chargealong-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/chargealong/refs/heads/main/packages/chargealong-packages.yml
  title: ''
  type: SDKs
  url: packages/chargealong-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/chargealong/refs/heads/main/packages/chargealong-packages.yml
  title: ''
  type: Packages
  url: packages/chargealong-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chargealong.io/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chargealong.io/en/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.chargealong.io</code
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chargealong
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chargealong/refs/heads/main/security/chargealong-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chargealong-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chargealong.io
- group: docs
  title: ''
  type: Documentation
  url: https://chargealong.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.chargealong.io/v1/openapi.json
created: '2026-10-02'
description: ChargeAlong provides free, keyless public EV charging site data across Australia and other countries. Users can query chargers by location, plug type, power, price and network without an API key, accessing up‑to‑date open data curated from official sources and driver contributions.
image: https://chargealong.io/og.png
layout: provider
modified: '2026-10-02'
name: Chargealong.io
nav: Providers
network: true
overview: 'Chargealong.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Vehicles, Charging, Data, and Public APIs.


  Chargealong.io''s developer surface includes documentation, API reference, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 73.2
    operational_transparency: 5.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chargealong Domain Security
  slug: chargealong-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chargealong
tags:
- Company
- Electric Vehicles
- Charging
- Data
- Public APIs
- Australia
website: https://chargealong.io
---
