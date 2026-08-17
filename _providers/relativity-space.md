---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Terran R is a reusable medium-to-heavy lift launch vehicle offering up to 23,500 kg to LEO (downrange landing) and 5,500 kg to GTO, with a planned first launch from Launch Complex 16 at Cape Canaveral
  name: Relativity Space Terran R Launch
  slug: terran-r-launch
- description: Stargate is Relativity Space's proprietary fourth-generation metal 3D printing platform used to manufacture Terran R structures at its Long Beach headquarters. This is an internal manufacturing techno
  name: Relativity Space Stargate Manufacturing
  slug: stargate-manufacturing
- description: Payload integration for dedicated constellation deployments, single large satellites, and multi-customer rideshare missions, supported through a standard Payload Attach Fitting (PAF) interface and doc
  name: Relativity Space Payload and Rideshare
  slug: payload-rideshare
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Relativity Space API
  slug: open-relativity-space
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relativity-space-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/relativity-space
- group: company
  title: ''
  type: Website
  url: https://www.relativityspace.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.relativityspace.com/terran-r
- group: commercial
  title: ''
  type: Plans
  url: plans/relativity-space-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/relativity-space-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/relativity-space-finops.yml
created: '2026-06-20'
description: Relativity Space is an aerospace manufacturer building Terran R, a reusable medium-to-heavy lift orbital launch vehicle produced with the company's proprietary Stargate metal 3D printing platform in Long Beach, CA. The company sells launch services - dedicated and rideshare payload missions to LEO and GTO - to government, commercial, and telecommunications customers. Relativity Space does not publish a public developer API; its developer-facing artifact is the Terran payload user's guide (mission integration documentation), not a programmatic interface.
finops:
- name: Relativity Space Finops
  service_category: Aerospace and Launch Services
  slug: relativity-space-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relativity-space.png
layout: provider
modified: '2026-06-20'
name: Relativity Space
nav: Providers
network: true
overview: 'Relativity Space publishes 3 APIs on the [APIs.io](https://apis.io/) network: Terran R Launch, Stargate Manufacturing, and Payload and Rideshare. Tagged areas include Aerospace, Launch Services, Space, Rocket, and 3D Printing.


  Relativity Space''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Relativity Space Plans Pricing
  plan_count: 1
  slug: relativity-space-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 0
  name: Relativity Space Rate Limits
  slug: relativity-space-rate-limits
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 30.6
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relativity-space/refs/heads/main/screenshots/relativity-space-2026-06-20T192820.png
security:
- kind: domain-security
  name: Relativity Space Domain Security
  slug: relativity-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: relativity-space
tags:
- Aerospace
- Launch Services
- Space
- Rocket
- 3D Printing
- Additive Manufacturing
website: https://www.relativityspace.com
---
