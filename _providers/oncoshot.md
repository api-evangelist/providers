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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/oncoshot/llms/oncoshot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oncoshot-llms.txt
- group: auth
  href: https://artifacts.apis.io/oncoshot/well-known/oncoshot-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/oncoshot-help-security.txt
- group: agent
  href: https://artifacts.apis.io/oncoshot/well-known/oncoshot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oncoshot-well-known.yml
- group: other
  href: https://artifacts.apis.io/oncoshot/hosts/oncoshot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oncoshot-hosts.yml
- group: other
  href: https://artifacts.apis.io/oncoshot/vendors/oncoshot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oncoshot-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.oncoshot.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://help.oncoshot.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Oncoshot
- group: auth
  href: https://artifacts.apis.io/oncoshot/security/oncoshot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oncoshot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oncoshot.com/
created: '2026-10-24'
description: 'Oncoshot is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by crane-venture-partners) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-24'
name: Oncoshot
nav: Providers
network: true
overview: 'Oncoshot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Oncoshot''s developer surface includes support, documentation, and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 26.8
    operational_transparency: 15.8
  provenance:
    mcp: unknown
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
  name: Oncoshot Domain Security
  slug: oncoshot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oncoshot
tags:
- Company
website: https://www.oncoshot.com/
---
