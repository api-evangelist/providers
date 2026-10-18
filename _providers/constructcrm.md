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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/constructcrm/refs/heads/main/well-known/constructcrm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/constructcrm-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/constructcrm/refs/heads/main/hosts/constructcrm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/constructcrm-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/constructcrm/refs/heads/main/vendors/constructcrm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/constructcrm-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://constructcrm.com/terms-of-service
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/constructcrm/refs/heads/main/security/constructcrm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constructcrm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constructcrm.com/
- group: other
  title: ''
  type: Coverage
  url: https://constructcrm.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://constructcrm.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: 'ConstructCRM is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-10'
name: ConstructCRM
nav: Providers
network: true
overview: ConstructCRM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Constructcrm Domain Security
  slug: constructcrm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: constructcrm
tags:
- Company
website: https://constructcrm.com/
---
