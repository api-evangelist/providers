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
  href: https://artifacts.apis.io/availink/hosts/availink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/availink-hosts.yml
- group: build
  href: https://artifacts.apis.io/availink/packages/availink-packages.yml
  title: ''
  type: SDKs
  url: packages/availink-packages.yml
- group: build
  href: https://artifacts.apis.io/availink/packages/availink-packages.yml
  title: ''
  type: Packages
  url: packages/availink-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.availink.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/availink
- group: auth
  href: https://artifacts.apis.io/availink/security/availink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/availink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://availink.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.availink.com/mcp
  - status: 403
    url: https://doc.availink.com/mcp
  - status: 200
    url: https://availink.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Availink is a technology company providing connectivity solutions for IoT and telecom operators. It offers hardware modules, cloud services, and APIs that enable remote device management, data collection, and network optimization. The company focuses on secure, scalable communication platforms for enterprises and developers.
layout: provider
modified: '2026-10-22'
name: Availink
nav: Providers
network: true
overview: 'Availink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Telecommunications, Connectivity, and Device Management.


  Availink''s developer surface includes documentation and 6 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 35.7
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/availink/availink-2026-11-03T121419.png
security:
- kind: domain-security
  name: Availink Domain Security
  slug: availink-domain-security
  summary_line: TLSv1.3 · DMARC
slug: availink
tags:
- IoT
- Telecommunications
- Connectivity
- Device Management
website: https://availink.com
---
