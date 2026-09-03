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
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schaeffler-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/schaefflergroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/schaeffler
- group: company
  title: ''
  type: Website
  url: https://www.schaeffler.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/schaeffler-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/schaeffler-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/schaeffler-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.schaeffler.com/en/_global/rss/rss-feed-press.jsp
created: '2026-05-06'
description: Schaeffler Group is a German global Tier 1 automotive and industrial supplier headquartered in Herzogenaurach. Schaeffler designs and manufactures precision bearings, powertrain components, chassis applications, and e-mobility systems for the automotive and industrial sectors.
finops:
- name: Schaeffler Finops
  service_category: Industrial / Automotive
  slug: schaeffler-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/schaeffler.png
layout: provider
modified: '2026-05-06'
name: Schaeffler
nav: Providers
network: true
overview: 'Schaeffler is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Industrial, Tier 1 Supplier, Bearings, and Powertrain.


  Schaeffler''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Schaeffler Plans Pricing
  plan_count: 1
  slug: schaeffler-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Schaeffler Rate Limits
  slug: schaeffler-rate-limits
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/schaeffler/refs/heads/main/screenshots/schaeffler-2026-06-20T193512.png
security:
- kind: domain-security
  name: Schaeffler Domain Security
  slug: schaeffler-domain-security
  summary_line: TLSv1.3
slug: schaeffler
tags:
- Automotive
- Industrial
- Tier 1 Supplier
- Bearings
- Powertrain
- E-Mobility
website: https://www.schaeffler.com/
---
