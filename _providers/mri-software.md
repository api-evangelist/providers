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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: An open and connected ecosystem of secure REST APIs built by MRI and its partners that enables controlled data exchange between MRI's core property management and accounting platform and third-party o
  name: MRI Information Exchange (MIX) API
  slug: mri-information-exchange-api
- description: 'A REST API for integrating with MRI OnLocation''s people presence management platform. Enables programmatic access to visitor, contractor, and employee sign-in data, assets, certifications, locations, '
  name: MRI OnLocation REST API
  slug: mri-onlocation-api
- description: REST APIs providing programmatic access to MRI's core property management platform, covering residential and commercial property portfolios, units, leases, resident ledgers, maintenance work orders, a
  name: MRI Property Management X API
  slug: mri-property-management-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mri-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mrisoftware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mrisoftware.com/mrifunctionalspecs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/MRI-Software
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mri-software-llc
- group: company
  title: ''
  type: Blog
  url: https://www.mrisoftware.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mrisoftware.com/products/onlocation/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mrisoftware.com/
- group: other
  title: ''
  type: X
  url: https://x.com/mrisoftware
- group: commercial
  title: ''
  type: Plans
  url: plans/mri-software-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mri-software-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mri-software-finops.yml
created: '2026-06-13'
description: MRI Software is a real estate technology platform serving over 45,000 clients across 170+ countries. It provides REST APIs and an open integration ecosystem for property management, investment management, lease accounting, facilities management, visitor and contractor management, and commercial real estate analytics. The MRI Information Exchange (MIX) hosts over 1,000 vetted APIs for data exchange between MRI's core platform and third-party or custom applications.
finops:
- name: Mri Software Finops
  service_category: ''
  slug: mri-software-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mri-software.png
layout: provider
modified: '2026-06-13'
name: MRI Software
nav: Providers
network: true
overview: 'MRI Software publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Property Management, Investment Management, Lease Accounting, and Facilities Management.


  MRI Software''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Mri Software Plans Pricing
  plan_count: 5
  slug: mri-software-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 3
  name: Mri Software Rate Limits
  slug: mri-software-rate-limits
score:
  band: emerging
  composite: 29.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 29.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mri-software/refs/heads/main/screenshots/mri-software-2026-06-20T185841.png
security:
- kind: domain-security
  name: Mri Software Domain Security
  slug: mri-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mri-software
tags:
- Real Estate
- Property Management
- Investment Management
- Lease Accounting
- Facilities Management
- Commercial Real Estate
- Visitor Management
- PropTech
website: https://www.mrisoftware.com/
---
