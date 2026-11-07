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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation is behind a login wall; no public contract discovered.
  name: D-EDGE API
  slug: d-edge-api
artifact_total: 2
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.d-edge.com/feed/
- group: agent
  href: https://artifacts.apis.io/d-edge/well-known/d-edge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/d-edge-well-known.yml
- group: other
  href: https://artifacts.apis.io/d-edge/hosts/d-edge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/d-edge-hosts.yml
- group: other
  href: https://artifacts.apis.io/d-edge/vendors/d-edge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/d-edge-vendors.yml
- group: build
  href: https://artifacts.apis.io/d-edge/packages/d-edge-packages.yml
  title: ''
  type: SDKs
  url: packages/d-edge-packages.yml
- group: build
  href: https://artifacts.apis.io/d-edge/packages/d-edge-packages.yml
  title: ''
  type: Packages
  url: packages/d-edge-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.d-edge.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.d-edge.com/product/price-monitoring/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.d-edge.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/d-edge
- group: auth
  href: https://artifacts.apis.io/d-edge/security/d-edge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/d-edge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.d-edge.com/
- group: company
  title: ''
  type: Blog
  url: https://www.d-edge.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.d-edge.com/contact
coverage:
  checked: 2026-09-23
  detail: API documentation requires login, returning a 302 redirect to a login page.
  evidence:
  - status: 302
    url: https://docs.d-edge.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: D-EDGE Hospitality Solutions provides a comprehensive suite of hotel technology and marketing solutions, including central reservation systems, channel management, booking engine, data intelligence, and digital marketing tools. Their platform helps hotels increase direct bookings, improve revenue management, and enhance guest experiences across multiple channels worldwide.
layout: provider
modified: '2026-10-06'
name: D-EDGE Hospitality Solutions
nav: Providers
network: true
overview: 'D-EDGE Hospitality Solutions is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Technology, Marketing, Software-as-a-Service, and Company.


  D-EDGE Hospitality Solutions'' developer surface includes pricing, documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 53.6
    operational_transparency: 2.6
  previous_composite: 15.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/d-edge/d-edge-2026-10-11T103446.png
security:
- kind: domain-security
  name: D Edge Domain Security
  slug: d-edge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: d-edge
tags:
- Hospitality
- Technology
- Marketing
- Software-as-a-Service
- Company
website: https://www.d-edge.com/
---
