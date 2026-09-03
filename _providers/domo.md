---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Domo API allows users to integrate and interact with data from various sources within the Domo platform. With Domo API, users can access real-time data, automate data processes, and create custom data
  name: Domo API
  slug: domo-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/domo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/domoinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/domo-inc
- group: company
  title: ''
  type: Website
  url: https://www.domo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.domo.com
created: '2025-03-01'
description: Domo is a cloud-based software company that specializes in providing business intelligence tools for organizations. Their platform allows businesses to gather, analyze, and visualize data from various sources in order to make more informed decisions. Domo helps companies streamline their data management processes and gain valuable insights into their operations, sales, marketing, and overall performance.
finops:
- name: Domo Finops
  service_category: API
  slug: domo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domo.png
layout: provider
modified: '2026-04-28'
name: Domo
nav: Providers
network: true
overview: Domo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analysis, Business Intelligence, Data, Pipelines, and Visualizations.
plans:
- name: Domo Plans Pricing
  plan_count: 3
  slug: domo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Domo Rate Limits
  slug: domo-rate-limits
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/domo/refs/heads/main/screenshots/domo-2026-06-20T180144.png
security:
- kind: domain-security
  name: Domo Domain Security
  slug: domo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: domo
tags:
- Analysis
- Business Intelligence
- Data
- Pipelines
- Visualizations
website: https://www.domo.com
---
