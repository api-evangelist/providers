---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/waymo/llms/waymo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/waymo-llms.txt
- group: other
  href: https://artifacts.apis.io/waymo/hosts/waymo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/waymo-hosts.yml
- group: build
  href: https://artifacts.apis.io/waymo/packages/waymo-packages.yml
  title: ''
  type: SDKs
  url: packages/waymo-packages.yml
- group: build
  href: https://artifacts.apis.io/waymo/packages/waymo-packages.yml
  title: ''
  type: Packages
  url: packages/waymo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://waymo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://waymo.com/privacy/
- group: commercial
  href: https://artifacts.apis.io/waymo/plans/waymo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/waymo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/waymo/rate-limits/waymo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/waymo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/waymo/finops/waymo-finops.yml
  title: ''
  type: FinOps
  url: finops/waymo-finops.yml
- group: auth
  href: https://artifacts.apis.io/waymo/security/waymo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/waymo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waymo.com
- group: company
  title: ''
  type: AboutUs
  url: https://waymo.com/company/
- group: company
  title: ''
  type: Newsroom
  url: https://waymo.com/press/
- group: company
  title: ''
  type: Blog
  url: https://blog.waymo.com
- group: other
  title: ''
  type: Safety
  url: https://waymo.com/safety/
- group: other
  title: ''
  type: Research
  url: https://waymo.com/research/
- group: other
  title: ''
  type: OpenDataset
  url: https://waymo.com/open
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/waymo-research
- group: operate
  title: ''
  type: SupportCenter
  url: https://support.google.com/waymo
- group: company
  title: ''
  type: Careers
  url: https://careers.withwaymo.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/waymo
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Waymo
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Waymo
- group: other
  title: ''
  type: ProductPage
  url: https://github.com/waymo-research/waymax
coverage:
  checked: '2026-10-20'
  detail: Waymo publishes no public developer API; its developer-facing surface is the Waymo Open Dataset (waymo.com/open, PyPI toolkit, protobuf data formats) and the Waymax simulator on github.com/waymo-research, and the API/OpenAPI/MCP probes on waymo.com and api.waymo.com all missed.
  evidence:
  - status: 200
    url: https://waymo.com/open/
  - status: 404
    url: https://waymo.com/security/
  reason: no-developer-program
  state: none
created: '2026-05-23'
description: Waymo is the autonomous driving subsidiary of Alphabet, originally spun out of the Google Self-Driving Car Project. The company develops the Waymo Driver, a full Level 4 autonomous driving stack combining custom lidar, radar, and camera sensors with proprietary perception, prediction, and planning models. Waymo One operates a commercial robotaxi service in Phoenix, San Francisco, Los Angeles, Austin, and other expanding US markets, with announced launches in Tokyo and London. The company has logged tens of millions of rider-only miles and reports significantly fewer serious-injury crashes than human-driven benchmarks. Waymo does not publish a traditional public developer API. Its primary developer-facing artifacts are the Waymo Open Dataset, the Waymo Open Motion Dataset, the Waymax JAX-based driving simulator, and a robust research publication catalogue spanning perception, behaviour prediction, planning, simulation, and end-to-end driving. Consumer access is through the Waymo
  One mobile app.
finops:
- has_sources: false
  method: generated
  name: Waymo Finops
  primary_unit: ''
  service_category: API
  slug: waymo-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waymo.png
layout: provider
modified: '2026-07-25'
name: Waymo
nav: Providers
network: true
overview: 'Waymo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Vehicles, Self-Driving, Robotaxi, Ride Hailing, and Alphabet.


  Waymo''s developer surface includes engineering blog, YouTube channel, and 22 more developer resources.'
plans:
- name: Waymo Plans Pricing
  plan_count: 1
  slug: waymo-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Waymo Rate Limits
  slug: waymo-rate-limits
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 10.5
  previous_composite: 13.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/waymo/waymo-2026-06-20T201302.png
security:
- kind: domain-security
  name: Waymo Domain Security
  slug: waymo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: waymo
tags:
- Autonomous Vehicles
- Self-Driving
- Robotaxi
- Ride Hailing
- Alphabet
- LiDAR
- Computer Vision
- Open Dataset
- Simulation
- Mobility
website: https://waymo.com
---
