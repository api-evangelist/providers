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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jawbone/refs/heads/main/vendors/jawbone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jawbone-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jawbone/refs/heads/main/hosts/jawbone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jawbone-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jawbone/refs/heads/main/packages/jawbone-packages.yml
  title: ''
  type: SDKs
  url: packages/jawbone-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jawbone/refs/heads/main/packages/jawbone-packages.yml
  title: ''
  type: Packages
  url: packages/jawbone-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Jawbone
- group: company
  title: ''
  type: Website
  url: https://www.jawbone.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jawbone/refs/heads/main/security/jawbone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jawbone-domain-security.yml
coverage:
  checked: '2026-10-12'
  detail: Jawbone ceased operations in 2017 and provides no active API.
  evidence:
  - status: 200
    url: https://www.jawbone.com
  reason: defunct
  state: none
created: '2026-10-12'
description: Jawbone was a consumer electronics company known for its wearable fitness trackers and Bluetooth headsets. Founded in 1999, the company focused on integrating health and activity monitoring into everyday accessories, offering products like the Jawbone UP series and the Jambox speaker. Although it ceased operations in 2017, its legacy includes pioneering the use of motion sensors and cloud-based data analytics in personal health devices, influencing the modern wearable market.
image: http://static1.squarespace.com/static/5c86c2f47eb88c1bb558b38e/t/5c86d0000852293752f1f113/1552338947641/jawbone_logo_black-01.jpg?format=1500w
layout: provider
modified: '2026-10-12'
name: Jawbone
nav: Providers
network: true
overview: Jawbone is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wearables, Consumer Electronics, Health Tech, and Bluetooth.
random_paper: 16
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jawbone Domain Security
  slug: jawbone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jawbone
tags:
- Company
- Wearables
- Consumer Electronics
- Health Tech
- Bluetooth
website: https://www.jawbone.com
---
