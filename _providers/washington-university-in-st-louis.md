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
api_count: 2
apis:
- description: 'Institutional integration APIs published via MuleSoft Anypoint Exchange ("WashU API Portal"), covering Person, Financial, Supplier, Location, Academic, and Organization data domains. Access is gated: '
  name: WashU Enterprise Integration APIs (MuleSoft Anypoint)
  slug: enterprise-apis
- description: The Becker Medical Library / School of Medicine research data repository runs on the Elsevier Digital Commons Data (Mendeley Data) platform. It publishes an API docs page and a working OAI-PMH metadat
  name: Digital Commons Data@Becker (Research Repository)
  slug: digital-commons-data
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/washington-university-in-st-louis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wustl.edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wustl
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/washington-university-in-st-louis/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.wustl.edu/api-portal/
- group: commercial
  title: ''
  type: Plans
  url: plans/washington-university-in-st-louis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/washington-university-in-st-louis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/washington-university-in-st-louis-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Washington University in St. Louis (WashU) is a private research university in St. Louis, Missouri, ranked #171 in the QS World University Rankings 2025. Its public developer footprint is modest: WashU operates an enterprise API program ("Data at WashU") delivered through MuleSoft Anypoint Exchange, exposing institutional APIs (Person, Financial, Supplier, Location, Academic, Organization) that are gated and require access requests through ServiceNow for WashU integrators rather than open public consumption. The Becker Medical Library School of Medicine runs a Digital Commons Data (Elsevier/Mendeley Data) research repository that exposes an OAI-PMH endpoint and API docs. Most other surfaces (course catalog, registrar) are web applications rather than documented public APIs.'
finops:
- name: Washington University In St Louis Finops
  service_category: Education
  slug: washington-university-in-st-louis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/washington-university-in-st-louis.png
jsonld:
- class_count: 17
  name: Washington University In St Louis Context
  property_count: 3
  slug: washington-university-in-st-louis-context
layout: provider
modified: '2026-06-03'
name: Washington University in St. Louis
nav: Providers
network: true
overview: 'Washington University in St. Louis publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and United States.


  The Washington University in St. Louis catalog on APIs.io includes 1 JSON-LD context.


  Washington University in St. Louis'' developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Washington University In St Louis Plans Pricing
  plan_count: 2
  slug: washington-university-in-st-louis-plans-pricing
random_paper: 116
rate_limits:
- limit_count: 1
  name: Washington University In St Louis Rate Limits
  slug: washington-university-in-st-louis-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/washington-university-in-st-louis/refs/heads/main/screenshots/washington-university-in-st-louis-2026-06-20T201236.png
security:
- kind: domain-security
  name: Washington University In St Louis Domain Security
  slug: washington-university-in-st-louis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: washington-university-in-st-louis
tags:
- Education
- Higher Education
- University
- Research
- United States
- MuleSoft
- OAI-PMH
website: https://wustl.edu
---
