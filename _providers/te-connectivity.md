---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/te-connectivity-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TEConnectivity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/te-connectivity
- group: company
  title: ''
  type: Website
  url: https://www.te.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/te-connectivity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/te-connectivity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/te-connectivity-finops.yml
created: '2026-05-06'
description: TE Connectivity is a global manufacturer of connectors and sensors headquartered in Galway, Ireland with operational headquarters in Berwyn, Pennsylvania. TE provides electrical connectivity and sensor solutions for transportation, industrial, and communications markets, with strong automotive Tier 1 supply relationships.
finops:
- name: Te Connectivity Finops
  service_category: Industrial / Connectors
  slug: te-connectivity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/te-connectivity.png
layout: provider
modified: '2026-05-06'
name: TE Connectivity
nav: Providers
network: true
overview: TE Connectivity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Connectors, Sensors, Automotive, Industrial, and Tier 1 Supplier.
plans:
- name: Te Connectivity Plans Pricing
  plan_count: 1
  slug: te-connectivity-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 1
  name: Te Connectivity Rate Limits
  slug: te-connectivity-rate-limits
score:
  band: emerging
  composite: 13.9
  delta: -0.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 14.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/te-connectivity/refs/heads/main/screenshots/te-connectivity-2026-06-20T194955.png
security:
- kind: domain-security
  name: Te Connectivity Domain Security
  slug: te-connectivity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: te-connectivity
tags:
- Connectors
- Sensors
- Automotive
- Industrial
- Tier 1 Supplier
website: https://www.te.com/
---
