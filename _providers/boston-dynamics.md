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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Spot SDK is an open-source SDK for developing applications and payloads for the Spot quadruped robot. Built on gRPC and Protocol Buffers, it provides Python and C++ libraries to control Spot, read
  name: Boston Dynamics Spot SDK
  slug: spot-sdk
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/boston-dynamics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boston-dynamics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bostondynamics.com/
- group: other
  title: ''
  type: Products
  url: https://bostondynamics.com/products/
- group: other
  title: ''
  type: SpotProductPage
  url: https://bostondynamics.com/products/spot/
- group: other
  title: ''
  type: AtlasProductPage
  url: https://bostondynamics.com/products/atlas/
- group: other
  title: ''
  type: StretchProductPage
  url: https://bostondynamics.com/products/stretch/
- group: other
  title: ''
  type: OrbitProductPage
  url: https://bostondynamics.com/products/orbit/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.bostondynamics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boston-dynamics
- group: operate
  title: ''
  type: Support
  url: https://support.bostondynamics.com/s/
- group: learn
  title: ''
  type: Training
  url: https://support.bostondynamics.com/s/bdu
- group: company
  title: ''
  type: Blog
  url: https://bostondynamics.com/blog/
- group: company
  title: ''
  type: News
  url: https://bostondynamics.com/news/
- group: other
  title: ''
  type: CaseStudies
  url: https://bostondynamics.com/case-studies/
- group: learn
  title: ''
  type: Videos
  url: https://bostondynamics.com/videos/
- group: company
  title: ''
  type: Partners
  url: https://bostondynamics.com/partners/
- group: operate
  title: ''
  type: ContactSales
  url: https://bostondynamics.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boston-dynamics/
created: '2026-05-23'
description: Boston Dynamics, a Hyundai Motor Group subsidiary, designs advanced mobile robots including Spot (agile quadruped for dynamic sensing and industrial inspection), Atlas (electric humanoid for manufacturing), Stretch (warehouse case-handling robot), and the Orbit enterprise fleet management platform. Boston Dynamics publishes a public, open-source Spot SDK (Python and C++) on GitHub built on gRPC and Protocol Buffers for developing applications and payloads for Spot; Atlas and Stretch are enterprise products without public APIs.
finops:
- name: Boston Dynamics Finops
  service_category: API
  slug: boston-dynamics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boston-dynamics.png
jsonld:
- class_count: 25
  name: Boston Dynamics Context
  property_count: 13
  slug: boston-dynamics-context
layout: provider
modified: '2026-05-23'
name: Boston Dynamics
nav: Providers
network: true
overview: 'Boston Dynamics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Atlas, Boston Dynamics, Fleet Management, gRPC, and Hardware.


  The Boston Dynamics catalog on APIs.io includes 1 JSON-LD context.


  Boston Dynamics'' developer surface includes support, training material, engineering blog, product news, and 15 more developer resources.'
plans:
- name: Boston Dynamics Plans Pricing
  plan_count: 1
  slug: boston-dynamics-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Boston Dynamics Rate Limits
  slug: boston-dynamics-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 26.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boston-dynamics/refs/heads/main/screenshots/boston-dynamics-2026-06-20T173614.png
security:
- kind: domain-security
  name: Boston Dynamics Domain Security
  slug: boston-dynamics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boston Dynamics Vulnerability Disclosure
  slug: boston-dynamics-vulnerability-disclosure
  summary_line: disclosure policy published
slug: boston-dynamics
tags:
- Atlas
- Boston Dynamics
- Fleet Management
- gRPC
- Hardware
- Humanoid Robots
- Industrial Inspection
- Quadrupedal Robots
- Robotics
- Spot
- Stretch
- Warehouse Automation
website: https://bostondynamics.com/
---
