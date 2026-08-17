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
- description: The ForeignAssistance.gov Data API (OAS 3.0) is the U.S. government's flagship source for foreign assistance budgetary and financial data. It exposes spending, obligations, and disbursements across al
  name: ForeignAssistance.gov Data API
  slug: foreignassistancegov-data-api
- description: The USAID Development Data Library (DDL) provides programmatic access to USAID's open datasets via the Socrata Open Data API (SODA). Developers can filter, query, and aggregate datasets covering devel
  name: USAID Development Data Library API
  slug: usaid-development-data-library-api
- description: The USAID Development Experience Clearinghouse (DEC) API provides programmatic access to the largest online repository of USAID-funded international development documentation, including technical repo
  name: USAID Development Experience Clearinghouse API
  slug: usaid-development-experience-clearinghouse-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usaid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usaid.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.usaid.gov/developer
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/USAID
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usaid
- group: company
  title: ''
  type: Blog
  url: https://www.usaid.gov/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usaid.gov/data
- group: operate
  title: ''
  type: StatusPage
  url: https://www.usaid.gov
- group: other
  title: ''
  type: X
  url: https://x.com/USAID
- group: commercial
  title: ''
  type: Plans
  url: plans/usaid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usaid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usaid-finops.yml
created: '2026-06-13'
description: The U.S. Agency for International Development (USAID) provides programmatic access to foreign assistance data, development finance records, project tracking, aid flow analysis, and global development datasets through a suite of REST APIs. Key offerings include the ForeignAssistance.gov Data API (OAS 3.0) for budgetary and financial foreign aid data across U.S. government agencies, the Development Data Library (DDL) powered by the Socrata Open Data API (SODA) for querying and filtering open datasets, and the Development Experience Clearinghouse (DEC) API for programmatic access to USAID-funded international development documentation. These APIs support researchers, policymakers, journalists, and developers building tools around international aid transparency and global development outcomes.
finops:
- name: Usaid Finops
  service_category: ''
  slug: usaid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usaid.png
layout: provider
modified: '2026-06-13'
name: USAID
nav: Providers
network: true
overview: 'USAID publishes 1 API on the [APIs.io](https://apis.io/) network: ForeignAssistance.gov Data API. Tagged areas include Foreign Assistance, International Development, Aid Data, Development Finance, and Global Datasets.


  USAID''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Usaid Plans Pricing
  plan_count: 2
  slug: usaid-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 4
  name: Usaid Rate Limits
  slug: usaid-rate-limits
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 29.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usaid/refs/heads/main/screenshots/usaid-2026-06-20T200640.png
security:
- kind: domain-security
  name: Usaid Domain Security
  slug: usaid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: usaid
tags:
- Foreign Assistance
- International Development
- Aid Data
- Development Finance
- Global Datasets
- Government
website: https://www.usaid.gov
---
