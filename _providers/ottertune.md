---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ottertune-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ottertune.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ottertune
created: '2026-07-17'
description: OtterTune was a database optimization ("on autopilot") start-up spun out of Carnegie Mellon University's database research group, operating from roughly 2020 to 2024. It applied machine learning to automatically tune the configuration knobs of PostgreSQL and MySQL databases (including managed instances such as Amazon RDS and Aurora) to improve performance and reduce cost. The company shut down in 2024 and its homepage now states the company is defunct. Its public GitHub organization remains available with infrastructure and agent tooling (ot-agent, Helm chart, CloudFormation/Terraform templates). This API Evangelist profile was added as a portfolio-company lead of Accel and captures the residual public footprint of a now-inactive company rather than a live API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ottertune.png
layout: provider
modified: '2026-07-20'
name: OtterTune
nav: Providers
network: true
overview: OtterTune is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Big Data, Database, Database Optimization, and Machine-Learning.
random_paper: 15
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ottertune/refs/heads/main/screenshots/ottertune-2026-08-07T191032.png
security:
- kind: domain-security
  name: Ottertune Domain Security
  slug: ottertune-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ottertune
tags:
- Company
- Big Data
- Database
- Database Optimization
- Machine-Learning
- PostgreSQL
- MySQL
- Defunct
website: https://ottertune.com/
---
