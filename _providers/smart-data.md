---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.smart-data.com/software/byo-data-hosting/#pricing
  - https://demo.ndsmartdata.com/
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.smart-data.com/
- group: other
  title: ''
  type: Company
  url: https://nationaldrones.com.au/
- group: other
  title: ''
  type: Product
  url: https://www.smart-data.com/software/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smart-data.com/software/byo-data-hosting/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.ndsmartdata.com/accounts/register/
- group: start
  title: ''
  type: Login
  url: https://app.ndsmartdata.com/accounts/login/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/smart-data-sandbox.yml
- group: start
  title: ''
  type: Demo
  url: https://demo.ndsmartdata.com/
- group: operate
  title: ''
  type: Support
  url: https://www.smart-data.com/contact/
- group: operate
  title: ''
  type: Contact
  url: https://www.smart-data.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.smart-data.com/insights/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.smart-data.com/case-studies/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smart-data.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smart-data.com/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/smart-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smart-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smart-data-finops.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smart-data-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smart-data-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smart-data-llms.txt
coverage:
  checked: '2026-08-14'
  detail: SmartData is National Drones' end-user drone-data workspace and ships no developer surface at all - the 50-URL sitemap on www.smart-data.com has no /docs, /api or /developers page, api./docs./developer. subdomains do not resolve on either smart-data.com or ndsmartdata.com, and the only machine surface that exists is the Django REST backend the web app itself calls at app.ndsmartdata.com/api/v1/, which is undocumented and answers anonymous callers with 403 {"detail":"Authentication credentials were not provided."}.
  evidence:
  - status: 404
    url: https://www.smart-data.com/openapi.json
  - status: 404
    url: https://www.smart-data.com/docs/
  - status: 404
    url: https://www.smart-data.com/llms.txt
  - status: 404
    url: https://www.smart-data.com/.well-known/agent-card.json
  - status: 403
    url: https://app.ndsmartdata.com/api/v1/
  - status: 404
    url: https://app.ndsmartdata.com/api/v1/schema/
  - status: 404
    url: https://app.ndsmartdata.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-03-16'
description: 'SmartData is a hosted drone-data workspace built and operated by National Drones, a CASA ReOC holder and Registered Training Organisation headquartered at Level 34, 1 Eagle Street, Brisbane, Australia. Teams bring processed, viewer-ready outputs from DJI Terra, Agisoft Metashape or their own photogrammetry workflow into SmartData and share one secure browser workspace where clients and asset owners can inspect, measure, compare and sign off on the data instead of passing files around. The platform hosts orthomosaic views, Cesium 3D Tiles, tiled point clouds and Gaussian Splat packages, layers AI-assisted inspection review, measurements, change detection, reporting and role-based team governance over them, and is expanding into processing and analytics workflows for DJI L3 LiDAR, Elios confined-space data, powerline corridor analytics and forestry intelligence. It serves power and utilities, telecommunications, mining and resources, forestry and environment, and infrastructure
  and construction. SmartData is sold as an end-user SaaS product: it publishes pricing, a public demo sandbox and self-service signup, but no API, developer portal, SDK, webhook surface or machine-readable contract of any kind.'
finops:
- name: Smart Data Finops
  service_category: SaaS
  slug: smart-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smart-data.png
layout: provider
modified: '2026-08-14'
name: SmartData
nav: Providers
network: true
overview: 'SmartData is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Drone Data, Geospatial, Asset Inspection, Photogrammetry, and LiDAR.


  SmartData''s developer surface includes pricing, signup flow, sandbox, support, engineering blog, and 15 more developer resources.'
plans:
- name: Smart Data Plans Pricing
  plan_count: 4
  slug: smart-data-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 0
  name: Smart Data Rate Limits
  slug: smart-data-rate-limits
score:
  band: emerging
  composite: 20.2
  delta: 7.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/smart-data/refs/heads/main/screenshots/smart-data-2026-06-20T194035.png
security:
- kind: domain-security
  name: Smart Data Domain Security
  slug: smart-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smart-data
tags:
- Drone Data
- Geospatial
- Asset Inspection
- Photogrammetry
- LiDAR
- Point Cloud
- 3D Visualization
- Gaussian Splatting
- Computer Vision
- Infrastructure
- Utilities
- Mining
- Forestry
- Australia
website: https://www.smart-data.com/
---
