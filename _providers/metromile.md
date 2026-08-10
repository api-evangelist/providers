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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'REST API platform for property and casualty insurance carriers enabling touchless claims automation, digital first-notice-of-loss reporting, telematics-based accident reconstruction, fraud detection, '
  name: Metromile Enterprise API
  slug: metromile-enterprise-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metromile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.metromile.com/
- group: docs
  title: ''
  type: Documentation
  url: https://enterprise.metromile.com/platform/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/metromile
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metromile
- group: company
  title: ''
  type: Blog
  url: https://www.metromile.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.metromile.com/auto-insurance/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metromile.com/
- group: other
  title: ''
  type: X
  url: https://x.com/metromile
- group: commercial
  title: ''
  type: Plans
  url: plans/metromile-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metromile-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/metromile-finops.yml
created: 2026-06-13
description: Metromile is a pay-per-mile auto insurance platform powered by telematics and data science. Customers attach the Pulse OBD device to their vehicle to track mileage; premiums consist of a base monthly rate plus a per-mile charge, rewarding low-mileage drivers with significant savings. Beyond consumer insurance, Metromile Enterprise offers a cloud-based REST API platform for property and casualty insurers covering touchless claims automation, accident reconstruction (Replay), fraud detection (Detect), digital FNOL reporting (Report), and back-office workflow automation (Streamline). Metromile was acquired by Lemonade in July 2022.
finops:
- name: Metromile Finops
  service_category: ''
  slug: metromile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metromile.png
layout: provider
modified: 2026-06-13
name: Metromile
nav: Providers
network: true
overview: 'Metromile publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Telematics, Pay-Per-Mile, Auto Insurance, and Claims Automation.


  Metromile''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Metromile Plans Pricing
  plan_count: 2
  slug: metromile-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 0
  name: Metromile Rate Limits
  slug: metromile-rate-limits
score:
  band: emerging
  composite: 18.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Metromile Domain Security
  slug: metromile-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: metromile
tags:
- Insurance
- Telematics
- Pay-Per-Mile
- Auto Insurance
- Claims Automation
- Vehicle Diagnostics
- Mileage Tracking
- InsurTech
website: https://www.metromile.com/
---
