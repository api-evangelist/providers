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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The ARC Data Report Tool provides state- and county-level data for the entire Appalachian Region across six topic areas comparing Appalachian data with national averages. Data covers economic, demogra
  name: ARC Data Report Tool
  slug: arc-data-reports
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appalachian-regional-commission-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.arc.gov/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appalachian-regional-commission
- group: docs
  title: ''
  type: Documentation
  url: https://www.arc.gov/research-and-data/
- group: start
  title: ''
  type: Portal
  url: https://data.arc.gov/data
created: '2024-11-21'
description: The Appalachian Regional Commission (ARC) is a federal-state partnership that invests in Appalachia's economic future by funding projects that promote economic development, infrastructure improvement, workforce training, and community development across 423 counties in 13 states. ARC provides research data, county-level economic reports, and maps via its Data Report Tool at data.arc.gov.
features:
- description: State and county-level data reports for all 423 Appalachian counties across six topic areas.
  name: County-Level Data Reports
- description: Appalachian Region data compared against national averages for benchmarking.
  name: Regional Comparison Data
- description: Regular research publications addressing socioeconomic issues in the Appalachian Region.
  name: Research Reports
- description: Geographic mapping data and visualizations covering the Appalachian Region.
  name: Maps
- description: Data on ARC's investment portfolios, grants, and program evaluations.
  name: Grant Program Data
finops:
- name: Appalachian Regional Commission Finops
  service_category: API
  slug: appalachian-regional-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appalachian-regional-commission.png
layout: provider
modified: '2026-04-19'
name: Appalachian Regional Commission
nav: Providers
network: true
overview: 'Appalachian Regional Commission publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Appalachia, Economic Development, Federal-Government, Government, and Infrastructure.


  Appalachian Regional Commission''s developer surface includes engineering blog, documentation, developer portal, and 2 more developer resources.'
plans:
- name: Appalachian Regional Commission Plans Pricing
  plan_count: 3
  slug: appalachian-regional-commission-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Appalachian Regional Commission Rate Limits
  slug: appalachian-regional-commission-rate-limits
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/screenshots/appalachian-regional-commission-2026-06-20T172312.png
security:
- kind: domain-security
  name: Appalachian Regional Commission Domain Security
  slug: appalachian-regional-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appalachian-regional-commission
tags:
- Appalachia
- Economic Development
- Federal-Government
- Government
- Infrastructure
- Regional Development
- Workforce Development
use_cases:
- description: Access county-level economic, demographic, and quality-of-life data for Appalachian research.
  name: Economic Research
- description: Evaluate ARC investment portfolios and grant outcomes across the Appalachian Region.
  name: Grant Program Analysis
- description: Use regional data to inform economic development and infrastructure policy decisions.
  name: Policy Development
- description: Access local data to support community-level economic development planning.
  name: Community Development Planning
website: https://data.arc.gov/data
---
