---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: TinEye provides an image search API allowing developers to integrate reverse image lookup, stock photo identification, and usage tracking.
  name: TinEye API
  slug: tineye-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/tineye/hosts/tineye-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tineye-hosts.yml
- group: other
  href: https://artifacts.apis.io/tineye/vendors/tineye-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tineye-vendors.yml
- group: build
  href: https://artifacts.apis.io/tineye/packages/tineye-packages.yml
  title: ''
  type: SDKs
  url: packages/tineye-packages.yml
- group: build
  href: https://artifacts.apis.io/tineye/packages/tineye-packages.yml
  title: ''
  type: Packages
  url: packages/tineye-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.tineye.com/category/168-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.tineye.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TinEye
- group: auth
  href: https://artifacts.apis.io/tineye/security/tineye-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tineye-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tineye.com/
coverage:
  checked: '2026-10-28'
  detail: Help site https://help.tineye.com/ returns HTML docs but no OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 404
    url: https://help.tineye.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'TinEye is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-28'
name: TinEye
nav: Providers
network: true
overview: 'TinEye is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  TinEye''s developer surface includes getting-started guide, documentation, and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 35.7
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tineye/tineye-2026-11-03T144800.png
security:
- kind: domain-security
  name: Tineye Domain Security
  slug: tineye-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tineye
tags:
- Company
website: https://tineye.com/
---
