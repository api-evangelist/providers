---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/cobalt-pe/hosts/cobalt-pe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cobalt-pe-hosts.yml
- group: other
  href: https://artifacts.apis.io/cobalt-pe/vendors/cobalt-pe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cobalt-pe-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cobalt-pe/security/cobalt-pe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cobalt-pe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cobalt.pe/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://cobalt.pe/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: 'Cobalt is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by techstars) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-29'
name: Cobalt
nav: Providers
network: true
overview: Cobalt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Cobalt Pe Plans Pricing
  plan_count: 3
  slug: cobalt-pe-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Cobalt Pe Rate Limits
  slug: cobalt-pe-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 35.0
    catalog_earned_first_party: 20.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 21.1
  provenance:
    mcp: first-party
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
- kind: authentication
  name: Cobalt Pe Authentication
  slug: cobalt-pe-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cobalt Pe Domain Security
  slug: cobalt-pe-domain-security
  summary_line: DMARC
- kind: trust-center
  name: Cobalt Pe Trust Center
  slug: cobalt-pe-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
slug: cobalt-pe
tags:
- Company
website: https://cobalt.pe/
---
