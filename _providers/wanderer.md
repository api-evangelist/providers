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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/wanderer/hosts/wanderer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wanderer-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wanderer.to/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://wanderer.to/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://wanderer.to/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://wanderer.to/run/installation/quick
- group: auth
  href: https://artifacts.apis.io/wanderer/security/wanderer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wanderer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wanderer.to/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found at the API host despite probing known paths.
  evidence:
  - status: 404
    url: https://api.wanderer.to/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'wanderer is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-28'
name: wanderer
nav: Providers
network: true
overview: 'wanderer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  wanderer''s developer surface includes changelog, API reference, getting-started guide, and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 26.8
    operational_transparency: 7.9
  previous_composite: 9.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wanderer/wanderer-2026-11-03T145959.png
security:
- kind: domain-security
  name: Wanderer Domain Security
  slug: wanderer-domain-security
  summary_line: TLSv1.3
slug: wanderer
tags:
- Company
website: https://wanderer.to/
---
