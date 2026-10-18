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
  href: https://raw.githubusercontent.com/api-evangelist/mouser/refs/heads/main/hosts/mouser-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mouser-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mouser/refs/heads/main/vendors/mouser-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mouser-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mouser/refs/heads/main/packages/mouser-packages.yml
  title: ''
  type: SDKs
  url: packages/mouser-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mouser/refs/heads/main/packages/mouser-packages.yml
  title: ''
  type: Packages
  url: packages/mouser-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mouser/refs/heads/main/security/mouser-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mouser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mouser.com
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI or other machine‑readable contract was found; attempts to fetch https://api.mouser.com/openapi.json returned HTTP 302 redirects with no content.
  evidence:
  - status: 302
    url: https://api.mouser.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: 'Mouser Electronics is a company surfaced via the API Evangelist harvest backlog (source: tag-qc) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-14'
name: Mouser Electronics
nav: Providers
network: true
overview: Mouser Electronics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 7
score:
  band: minimal
  composite: 2.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 26.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mouser Domain Security
  slug: mouser-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mouser
tags:
- Company
website: https://www.mouser.com
---
