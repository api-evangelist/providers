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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Centralized HKUST API platform run by the IT Services Office on Azure API Management. Departments publish application APIs to the portal, where users can discover APIs, read documentation, try them in
  name: HKUST API Portal & Gateway
  slug: developer-portal
- description: DataSpace@HKUST is the institutional research data repository for the HKUST research community, hosted on Dataverse (version 6.1, confirmed live). It exposes the standard Dataverse Native REST API for
  name: DataSpace@HKUST Research Data Repository API
  slug: dataspace
- description: Secure central data repository established by HKUST ITSO for collecting and sharing smart-campus data. Built on the Elastic Stack to ingest data from varied sources and formats and search, analyze, an
  name: HKUST Open Data Platform
  slug: open-data-platform
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hkust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ust.hk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hkust.developer.azure-api.net/
- group: company
  title: ''
  type: LinkedIn
  url: https://hk.linkedin.com/school/hkust/
- group: commercial
  title: ''
  type: Plans
  url: plans/hkust-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hkust-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hkust-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Hong Kong University of Science and Technology (HKUST) is a public research university in Clear Water Bay, Hong Kong SAR, ranked #82 in the QS World University Rankings 2025. HKUST operates a real developer footprint: an Azure API Management developer portal and API Gateway run by its Information Technology Services Office (ITSO) for departments to publish and consume internal application APIs, an Open Data Platform built on the Elastic Stack for smart-campus data, and DataSpace@HKUST, a Dataverse 6.1 research data repository with a public Native API. Most API access is gated behind institutional affiliation, sign-up, and a data access request process rather than being open self-service.'
finops:
- name: Hkust Finops
  service_category: Education
  slug: hkust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hkust.png
jsonld:
- class_count: 10
  name: Hkust Context
  property_count: 1
  slug: hkust-context
layout: provider
modified: '2026-06-03'
name: Hong Kong University of Science and Technology
nav: Providers
network: true
overview: 'Hong Kong University of Science and Technology publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Hong Kong University of Science and Technology catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Hkust Plans Pricing
  plan_count: 2
  slug: hkust-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Hkust Rate Limits
  slug: hkust-rate-limits
score:
  band: emerging
  composite: 20.0
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hkust/refs/heads/main/screenshots/hkust-2026-06-20T182813.png
security:
- kind: domain-security
  name: Hkust Domain Security
  slug: hkust-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hkust
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Hong Kong
- China
website: https://www.ust.hk/
---
