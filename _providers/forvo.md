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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/forvo/plans/forvo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/forvo-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/forvo/hosts/forvo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/forvo-hosts.yml
- group: other
  href: https://artifacts.apis.io/forvo/vendors/forvo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/forvo-vendors.yml
- group: build
  href: https://artifacts.apis.io/forvo/packages/forvo-packages.yml
  title: ''
  type: SDKs
  url: packages/forvo-packages.yml
- group: build
  href: https://artifacts.apis.io/forvo/packages/forvo-packages.yml
  title: ''
  type: Packages
  url: packages/forvo-packages.yml
- group: auth
  href: https://artifacts.apis.io/forvo/security/forvo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forvo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forvo.com/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI or other machine-readable contract found; attempts to fetch https://api.forvo.com/openapi.json returned HTTP 403.
  evidence:
  - status: 403
    url: https://api.forvo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'Forvo is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-28'
name: Forvo
nav: Providers
network: true
overview: Forvo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Forvo Plans Pricing
  plan_count: 3
  slug: forvo-plans-pricing
random_paper: 4
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 12.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 26.8
    operational_transparency: 0.0
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
  name: Forvo Domain Security
  slug: forvo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: forvo
tags:
- Company
website: https://forvo.com/
---
