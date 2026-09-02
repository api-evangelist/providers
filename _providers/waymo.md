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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
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
created: '2026-05-23'
description: Waymo is the autonomous driving subsidiary of Alphabet, originally spun out of the Google Self-Driving Car Project. The company develops the Waymo Driver, a full Level 4 autonomous driving stack combining custom lidar, radar, and camera sensors with proprietary perception, prediction, and planning models. Waymo One operates a commercial robotaxi service in Phoenix, San Francisco, Los Angeles, Austin, and other expanding US markets, with announced launches in Tokyo and London. The company has logged tens of millions of rider-only miles and reports significantly fewer serious-injury crashes than human-driven benchmarks. Waymo does not publish a traditional public developer API. Its primary developer-facing artifacts are the Waymo Open Dataset, the Waymo Open Motion Dataset, the Waymax JAX-based driving simulator, and a robust research publication catalogue spanning perception, behaviour prediction, planning, simulation, and end-to-end driving. Consumer access is through the Waymo
  One mobile app.
finops:
- name: Waymo Finops
  service_category: API
  slug: waymo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waymo.png
layout: provider
modified: '2026-07-25'
name: Waymo
nav: Providers
network: true
overview: 'Waymo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Vehicles, Self-Driving, Robotaxi, Ride Hailing, and Alphabet.


  Waymo''s developer surface includes engineering blog, YouTube channel, and 13 more developer resources.'
plans:
- name: Waymo Plans Pricing
  plan_count: 1
  slug: waymo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Waymo Rate Limits
  slug: waymo-rate-limits
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 14.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waymo/refs/heads/main/screenshots/waymo-2026-06-20T201302.png
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
- Computer-Vision
- Open Dataset
- Simulation
website: https://waymo.com
---
