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
artifact_total: 1
common:
- group: build
  href: https://artifacts.apis.io/nodar/cli/nodar-cli.yml
  title: ''
  type: CLI
  url: cli/nodar-cli.yml
- group: other
  href: https://artifacts.apis.io/nodar/hosts/nodar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nodar-hosts.yml
- group: other
  href: https://artifacts.apis.io/nodar/vendors/nodar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nodar-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.nodarsensor.com/blog/security
- group: build
  title: ''
  type: SDKs
  url: https://www.nodarsensor.com/sdk
- group: company
  title: ''
  type: Newsroom
  url: https://www.nodarsensor.com/media
- group: other
  title: ''
  type: Leadership
  url: https://www.nodarsensor.com/team
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nodarsensor.net/sdk/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nodarsensor
- group: auth
  href: https://artifacts.apis.io/nodar/security/nodar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nodar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nodarsensor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nodarsensor.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nodarsensor.net/
- group: operate
  title: ''
  type: Support
  url: https://www.nodarsensor.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.nodarsensor.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nodarsensor.com/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.nodarsensor.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Nodar develops advanced 3D sensor technology that transforms standard cameras into LiDAR alternatives, delivering dense point clouds up to 1,000 meters for autonomous vehicles, robotics, and industrial applications. Their stereo vision solutions enable intelligent machines to perceive depth with high accuracy, supporting a range of use cases from autonomous navigation to site inspection. Founded with backing from NEA, Nodar aims to accelerate adoption of affordable, high‑performance 3D sensing across industries.
image: https://framerusercontent.com/assets/CdtR2oeFKdZuxyr2PkKY4xhmFf0.jpg
layout: provider
modified: '2026-10-26'
name: Nodar
nav: Providers
network: true
overview: 'Nodar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sensor, 3DVision, AutonomousVehicles, and Robotics.


  Nodar''s developer surface includes CLI, getting-started guide, documentation, support, engineering blog, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 51.8
    operational_transparency: 15.8
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
- kind: domain-security
  name: Nodar Domain Security
  slug: nodar-domain-security
  summary_line: TLSv1.3 · HSTS
slug: nodar
tags:
- Company
- Sensor
- 3DVision
- AutonomousVehicles
- Robotics
website: https://www.nodarsensor.com/
---
