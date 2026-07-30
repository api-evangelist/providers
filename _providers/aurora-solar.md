---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Aurora Solar Agentic Access
  operation_count: 37
  slug: aurora-solar-agentic-access
  summary_line: 37 operations · 15 acting
api_count: 8
apis:
- description: Customer agreements and signed downloads.
  name: Aurora Solar Agreements API
  slug: aurora-solar-agreements-api
- description: Energy consumption profiles and utility bills.
  name: Aurora Solar Consumption Profiles API
  slug: aurora-solar-consumption-profiles-api
- description: Design requests and PV designs with simulation output.
  name: Aurora Solar Designs API
  slug: aurora-solar-designs-api
- description: Financings and financier integrations.
  name: Aurora Solar Financings API
  slug: aurora-solar-financings-api
- description: Customer/site records that anchor designs and proposals.
  name: Aurora Solar Projects API
  slug: aurora-solar-projects-api
- description: Customer-facing proposals, templates, and PDFs.
  name: Aurora Solar Proposals API
  slug: aurora-solar-proposals-api
- description: Tenant, users, roles, teams, and SSO.
  name: Aurora Solar Users & Tenants API
  slug: aurora-solar-users-tenants-api
- description: Event notification subscriptions.
  name: Aurora Solar Webhooks API
  slug: aurora-solar-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: Aurora Solar API
  slug: open-aurora-solar
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aurora-solar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aurora-solar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aurora-solar-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aurorasolar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aurorasolar
- group: company
  title: ''
  type: Website
  url: https://aurorasolar.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aurorasolar.com
- group: commercial
  title: ''
  type: Plans
  url: plans/aurora-solar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aurora-solar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aurora-solar-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://aurorasolar.com/blog/
created: '2026-07-04'
description: Aurora Solar is a cloud platform for solar sales and design. It provides remote shading analysis, LIDAR and satellite-based roof modeling, PV system design, performance simulation, financing, and proposal generation so installers can design and sell solar projects without a site visit. The Aurora API (v2024.05) is a tenant-scoped REST API secured with API-key bearer tokens that lets integrations manage projects, request and retrieve designs, generate proposals, pull consumption profiles, manage users and webhooks, and push financings and agreements.
finops:
- name: Aurora Solar Finops
  service_category: Software as a Service
  slug: aurora-solar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aurora-solar.png
layout: provider
modified: '2026-07-04'
name: Aurora Solar
nav: Providers
network: true
overview: 'Aurora Solar publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agreements API, Consumption Profiles API, Designs API, and 5 more. Tagged areas include Solar, Solar Design, PV, Proposals, and CleanTech.


  Aurora Solar''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Aurora Solar Plans Pricing
  plan_count: 5
  slug: aurora-solar-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Aurora Solar Rate Limits
  slug: aurora-solar-rate-limits
score:
  band: thin
  composite: 36.0
  delta: -5.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/aurora-solar/refs/heads/main/screenshots/aurora-solar-2026-07-25T201754.png
security:
- kind: authentication
  name: Aurora Solar Authentication
  slug: aurora-solar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aurora Solar Domain Security
  slug: aurora-solar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aurora-solar
tags:
- Solar
- Solar Design
- PV
- Proposals
- CleanTech
- Energy
- Sales Software
website: https://aurorasolar.com
---
