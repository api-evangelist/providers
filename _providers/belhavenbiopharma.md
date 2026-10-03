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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belhavenbiopharma/refs/heads/main/hosts/belhavenbiopharma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belhavenbiopharma-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belhavenbiopharma/refs/heads/main/vendors/belhavenbiopharma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/belhavenbiopharma-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belhavenbiopharma/refs/heads/main/security/belhavenbiopharma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belhavenbiopharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://belhavenbio.com
coverage:
  checked: '2026-09-27'
  detail: Belhaven Biopharma is a biotech company with no public API surface.
  evidence:
  - status: 200
    url: https://belhavenbio.com
  reason: not-a-software-company
  state: none
created: '2026-09-27'
description: 'Belhavenbiopharma is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-27'
name: Belhavenbiopharma
nav: Providers
network: true
overview: Belhavenbiopharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 2
score:
  band: minimal
  composite: 1.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Belhavenbiopharma Domain Security
  slug: belhavenbiopharma-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: belhavenbiopharma
tags:
- Company
website: https://belhavenbio.com
---
