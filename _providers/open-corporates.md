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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API providing access to the world's largest open database of companies. Search and retrieve company registration data, officer information, corporate filings, and jurisdiction data across more th
  name: OpenCorporates API
  slug: open-corporates-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-corporates-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opencorporates.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.opencorporates.com/documentation/API-Reference
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opencorporates
- group: company
  title: ''
  type: Blog
  url: https://blog.opencorporates.com
- group: commercial
  title: ''
  type: Pricing
  url: https://opencorporates.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opencorporates.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/opencorporates
- group: commercial
  title: ''
  type: Plans
  url: plans/open-corporates-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-corporates-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-corporates-finops.yml
created: 2026-06-13
description: OpenCorporates is the world's largest open database of companies, providing a REST API for searching and retrieving company registration data, officer information, and corporate filings globally across more than 140 jurisdictions. The API enables access to company details, director and officer records, statutory filings, and corporate groupings, making it a primary resource for compliance, due diligence, investigative journalism, and corporate transparency.
finops:
- name: Open Corporates Finops
  service_category: ''
  slug: open-corporates-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-corporates.png
layout: provider
modified: 2026-06-13
name: OpenCorporates
nav: Providers
network: true
overview: 'OpenCorporates publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Companies, Corporate Data, Business Intelligence, Compliance, and Due Diligence.


  OpenCorporates'' developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Open Corporates Plans Pricing
  plan_count: 6
  slug: open-corporates-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 9
  name: Open Corporates Rate Limits
  slug: open-corporates-rate-limits
score:
  band: thin
  composite: 29.1
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-corporates/refs/heads/main/screenshots/open-corporates-2026-06-20T190736.png
security:
- kind: domain-security
  name: Open Corporates Domain Security
  slug: open-corporates-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-corporates
tags:
- Companies
- Corporate Data
- Business Intelligence
- Compliance
- Due Diligence
- Officers
- Filings
- Corporate Transparency
- Open Data
website: https://opencorporates.com
---
