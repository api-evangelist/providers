---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: REST, GraphQL, and JDBC APIs for the Luma Scientific Intelligence Platform, enabling data access, workflow automation, instrument integration, and scientific data management for pharma and biotech R&D
  name: Dotmatics Luma API
  slug: dotmatics-luma-api
- description: Open REST API for the Dotmatics Electronic Lab Notebook (ELN), enabling data routing to data warehouses, LIMS, BI tools, and external systems via the Integration Framework using Apache NiFi.
  name: Dotmatics ELN API
  slug: dotmatics-eln-api
- description: RESTful API layer for Dotmatics Studies, which organizes acquired screening data from HTS, HCS, and DMPK studies, enabling protocol definition, assay execution, and integration with external systems a
  name: Dotmatics Studies API
  slug: dotmatics-studies-api
- description: REST API for compound, sample, and entity registration management in Dotmatics, supporting single and batch registration, stereochemistry handling, uniqueness rules, and crosscheck workflows for chemi
  name: Dotmatics Registration API
  slug: dotmatics-registration-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dotmatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dotmatics.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.dotmatics.com/whats-new
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dotmatics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dotmatics/
- group: company
  title: ''
  type: Blog
  url: https://www.dotmatics.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dotmatics.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dotmatics.com
- group: other
  title: ''
  type: X
  url: https://x.com/dotmatics
- group: commercial
  title: ''
  type: Plans
  url: plans/dotmatics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dotmatics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dotmatics-finops.yml
created: '2026-06-13'
description: Dotmatics is a scientific informatics platform for R&D organizations in pharma and biotech, offering REST, GraphQL, and JDBC APIs for managing experimental data, compound and sample registrations, study definitions, screening workflows, ELN data, and instrument integration through its Luma scientific intelligence platform.
finops:
- name: Dotmatics Finops
  service_category: ''
  slug: dotmatics-finops
graphqls:
- description: Dotmatics provides a GraphQL API as part of its Luma Scientific Intelligence Platform, alongside REST and JDBC interfaces. The GraphQL layer enables flexible, query-driven access to scientific data ma
  name: Dotmatics GraphQL API
  slug: dotmatics-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dotmatics.png
layout: provider
modified: '2026-06-13'
name: Dotmatics
nav: Providers
network: true
overview: 'Dotmatics publishes 1 API on the [APIs.io](https://apis.io/) network: Luma API. Tagged areas include Scientific Informatics, Pharma, Biotech, Drug Discovery, and ELN.


  Dotmatics'' developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Dotmatics Plans Pricing
  plan_count: 4
  slug: dotmatics-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Dotmatics Rate Limits
  slug: dotmatics-rate-limits
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 38.9
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 29.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dotmatics/refs/heads/main/screenshots/dotmatics-2026-06-20T180201.png
security:
- kind: domain-security
  name: Dotmatics Domain Security
  slug: dotmatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dotmatics
tags:
- Scientific Informatics
- Pharma
- Biotech
- Drug Discovery
- ELN
- LIMS
- Compound Registration
- Experimental Data
- R&D
website: https://www.dotmatics.com
---
