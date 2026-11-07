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
  href: https://artifacts.apis.io/owntracks/hosts/owntracks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/owntracks-hosts.yml
- group: other
  href: https://artifacts.apis.io/owntracks/vendors/owntracks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/owntracks-vendors.yml
- group: auth
  href: https://artifacts.apis.io/owntracks/security/owntracks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/owntracks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://owntracks.org/
- group: docs
  title: ''
  type: Documentation
  url: https://owntracks.org/booklet/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/owntracks
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 404
    url: https://owntracks.org/booklet/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: OwnTracks provides open-source iOS and Android applications that let users publish their own location data to a server of their choice. The project emphasizes privacy and security, allowing individuals to keep a personal location diary or share selectively with family and friends. Documentation, guides, and a self‑hosted backend enable full control over data, while the apps integrate with MQTT and HTTP protocols for flexible deployments.
layout: provider
modified: '2026-10-28'
name: OwnTracks
nav: Providers
network: true
overview: 'OwnTracks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, Location Tracking, Privacy, and Mobile App.


  OwnTracks'' developer surface includes documentation and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.7
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/owntracks/owntracks-2026-11-03T140828.png
security:
- kind: domain-security
  name: Owntracks Domain Security
  slug: owntracks-domain-security
  summary_line: TLSv1.3
slug: owntracks
tags:
- Company
- Open Source
- Location Tracking
- Privacy
- Mobile App
website: https://owntracks.org/
---
