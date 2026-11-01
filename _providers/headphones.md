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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/headphones/vendors/headphones-vendors.yml
  title: ''
  type: Vendors
  url: vendors/headphones-vendors.yml
- group: other
  href: https://artifacts.apis.io/headphones/hosts/headphones-hosts.yml
  title: ''
  type: Hosts
  url: hosts/headphones-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/rembo10/headphones
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rembo10
coverage:
  checked: '2026-10-28'
  detail: Headphones.com is an e‑commerce storefront with no developer API.
  evidence:
  - status: 200
    url: https://headphones.com/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Headphones is a placeholder company identified during the API Evangelist harvest process. No official website, documentation, or API specifications have been located. The only known reference is a GitHub repository rembo10/headphones, which appears to be an open‑source project rather than an official corporate site. This entry exists to allow future profiling should the organization publish an API or related resources.
image: https://example.com/logo.png
layout: provider
modified: '2026-10-28'
name: Headphones
nav: Providers
network: true
overview: Headphones is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Stub, Placeholder, API, and Harvest.
plans:
- name: Headphones Plans Pricing
  plan_count: 0
  slug: headphones-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Headphones Rate Limits
  slug: headphones-rate-limits
scopes:
- name: Headphones Scopes
  scope_count: 0
  slug: headphones-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Headphones Authentication
  slug: headphones-authentication
  summary_line: 0 schemes
slug: headphones
tags:
- Company
- Stub
- Placeholder
- API
- Harvest
---
