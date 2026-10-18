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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/farmonaut/refs/heads/main/llms/farmonaut-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/farmonaut-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/farmonaut/refs/heads/main/hosts/farmonaut-hosts.yml
  title: ''
  type: Hosts
  url: hosts/farmonaut-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/farmonaut/refs/heads/main/vendors/farmonaut-vendors.yml
  title: ''
  type: Vendors
  url: vendors/farmonaut-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/farmonaut/refs/heads/main/security/farmonaut-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/farmonaut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://farmonaut.com/
created: '2026-10-12'
description: 'Farmonaut is a company surfaced via the API Evangelist harvest backlog (source: space) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-12'
name: Farmonaut
nav: Providers
network: true
overview: Farmonaut is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 5
score:
  band: minimal
  composite: 2.0
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
    discoverability: 33.9
    operational_transparency: 0.0
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
  name: Farmonaut Domain Security
  slug: farmonaut-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: farmonaut
tags:
- Company
website: https://farmonaut.com/
---
