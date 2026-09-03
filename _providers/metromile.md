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
  scored_at: '2026-09-03'
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
random_paper: 8
rate_limits:
- limit_count: 0
  name: Metromile Rate Limits
  slug: metromile-rate-limits
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 15.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Insurtech
website: https://www.metromile.com/
---
