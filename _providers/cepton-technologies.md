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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cepton-technologies/refs/heads/main/hosts/cepton-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cepton-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cepton-technologies/refs/heads/main/vendors/cepton-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cepton-technologies-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cepton-technologies/refs/heads/main/packages/cepton-technologies-packages.yml
  title: ''
  type: SDKs
  url: packages/cepton-technologies-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cepton-technologies/refs/heads/main/packages/cepton-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/cepton-technologies-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.cepton.com/lets-talk/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cepton.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.cepton.com/company-2024/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cepton.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cepton
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cepton-technologies/refs/heads/main/security/cepton-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cepton-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cepton.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cepton.com/learn/announcements
- group: company
  title: ''
  type: Blog
  url: https://www.cepton.com/learn/blog
- group: company
  title: ''
  type: AboutUs
  url: https://www.ceptot.com/company-2024/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.cepton.com/company-2024/careers
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.cepton.com/
  - status: 403
    url: https://forgeglobal.com/cepton-technologies_stock/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cepton Technologies develops advanced lidar sensors and perception software for autonomous vehicles, robotics, and safety-critical applications. Their products include Vista Ultra, Nova Ultra, and Helius platforms, delivering high-resolution, long-range detection for a variety of industries. The company focuses on safe, reliable, and scalable sensing solutions to enable autonomous transportation and intelligent machines.
layout: provider
modified: '2026-10-07'
name: Cepton Technologies
nav: Providers
network: true
overview: 'Cepton Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LiDAR, Autonomous Vehicles, Robotics, and Sensors.


  Cepton Technologies'' developer surface includes support, documentation, engineering blog, and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 46.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cepton Technologies Domain Security
  slug: cepton-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cepton-technologies
tags:
- Company
- LiDAR
- Autonomous Vehicles
- Robotics
- Sensors
website: https://www.cepton.com/
---
