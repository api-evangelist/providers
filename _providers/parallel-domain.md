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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/parallel-domain/hosts/parallel-domain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/parallel-domain-hosts.yml
- group: other
  href: https://artifacts.apis.io/parallel-domain/vendors/parallel-domain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/parallel-domain-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paralleldomain.com/
- group: company
  title: ''
  type: Website
  url: https://paralleldomain.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://parallel-domain.github.io/pd-sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://parallel-domain.github.io/pd-sdk/
- group: docs
  title: ''
  type: APIReference
  url: https://parallel-domain.github.io/pd-sdk/paralleldomain/__index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://parallel-domain.github.io/pd-sdk/getting_started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parallel-domain
- group: company
  title: ''
  type: Blog
  url: https://paralleldomain.com/resources
- group: operate
  title: ''
  type: Support
  url: https://paralleldomain.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://app.paralleldomain.com/auth/login
- group: start
  title: ''
  type: Login
  url: https://app.paralleldomain.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paralleldomain.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paralleldomain.com/privacy-policy
- group: build
  href: https://artifacts.apis.io/parallel-domain/packages/parallel-domain-packages.yml
  title: ''
  type: Packages
  url: packages/parallel-domain-packages.yml
- group: build
  href: https://artifacts.apis.io/parallel-domain/packages/parallel-domain-packages.yml
  title: ''
  type: SDKs
  url: packages/parallel-domain-packages.yml
- group: auth
  href: https://artifacts.apis.io/parallel-domain/authentication/parallel-domain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/parallel-domain-authentication.yml
- group: agent
  href: https://artifacts.apis.io/parallel-domain/well-known/parallel-domain-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/parallel-domain-well-known.yml
- group: auth
  href: https://artifacts.apis.io/parallel-domain/security/parallel-domain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parallel-domain-domain-security.yml
coverage:
  checked: '2026-10-20'
  detail: Parallel Domain exposes its platform only through a Python SDK whose hosted docs (v1.0.4) remain live while the pd-sdk source repo now 404s, and no OpenAPI, GraphQL or MCP contract is served on paralleldomain.com, app.paralleldomain.com or status.paralleldomain.com.
  evidence:
  - status: 200
    url: https://parallel-domain.github.io/pd-sdk/
  - status: 404
    url: https://github.com/parallel-domain/pd-sdk
  - status: 404
    url: https://paralleldomain.com/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Parallel Domain is a synthetic-data and sensor-simulation platform for physical-AI and autonomy developers. It turns real-world drive and flight logs into photorealistic, simulation-ready digital replicas (PD Replica) and generates deterministic camera, lidar, and radar sensor data at scale (PD Sim), plus self-serve synthetic-data generation through its Data Lab service. The platform is driven through a first-party Python SDK (paralleldomain / pd-sdk) and an app console, integrating with existing autonomy stacks and CI/CD for training, testing, and regulatory validation of perception systems across automotive, trucking, drone, robotics, agriculture, and defense.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parallel-domain.png
layout: provider
modified: '2026-10-20'
name: Parallel Domain
nav: Providers
network: true
overview: 'Parallel Domain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Synthetic Data, Simulation, and Autonomous Vehicles.


  Parallel Domain''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 13 more developer resources.'
plans:
- name: Parallel Domain Plans Pricing
  plan_count: 0
  slug: parallel-domain-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 48.2
    operational_transparency: 21.1
  previous_composite: 27.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/parallel-domain/parallel-domain-2026-08-07T191422.png
security:
- kind: authentication
  name: Parallel Domain Authentication
  slug: parallel-domain-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Parallel Domain Domain Security
  slug: parallel-domain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parallel-domain
tags:
- Company
- Artificial Intelligence
- Synthetic Data
- Simulation
- Autonomous Vehicles
- Computer Vision
- Machine Learning
- Robotics
- SDK
website: https://paralleldomain.com
---
