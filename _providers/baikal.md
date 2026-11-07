---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/baikal/authentication/baikal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/baikal-authentication.yml
- group: other
  href: https://artifacts.apis.io/baikal/hosts/baikal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baikal-hosts.yml
- group: other
  href: https://artifacts.apis.io/baikal/vendors/baikal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baikal-vendors.yml
- group: auth
  href: https://artifacts.apis.io/baikal/security/baikal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baikal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sabre.io/
- group: company
  title: ''
  type: Blog
  url: https://sabre.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://sabre.io/dav
- group: operate
  title: ''
  type: Support
  url: https://sabre.io/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sabre-io
coverage:
  checked: '2026-10-27'
  detail: Documentation pages exist but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://sabre.io/dav
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Baikal is currently a stub entry in the API Evangelist network, created from a new‑submission harvest. The company’s public presence and API offerings have not yet been documented, and no dedicated website or API specifications are available. This placeholder entry records basic metadata while the profiling process seeks to discover official resources, documentation, and endpoints for Baikal.
layout: provider
modified: '2026-10-27'
name: Baikal
nav: Providers
network: true
overview: 'Baikal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, Calendar, and CardDAV.


  Baikal''s developer surface includes authentication, engineering blog, documentation, support, and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 35.7
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/baikal/baikal-2026-11-03T121519.png
security:
- kind: authentication
  name: Baikal Authentication
  slug: baikal-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Baikal Domain Security
  slug: baikal-domain-security
  summary_line: TLSv1.3
slug: baikal
tags:
- Company
- Open Source
- Calendar
- CardDAV
website: https://sabre.io/
---
