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
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: Downloadable budget and economic data accompanying CBO's Budget and Economic Outlook reports. Includes 10-year projections of revenues, outlays, deficits, debt, employment, GDP, interest rates, and hi
  name: CBO Budget and Economic Data
  slug: budget-and-economic-data
- description: CBO publishes cost estimates for legislation under consideration by Congress, covering both direct spending and revenue impact and including PAYGO scoring. Cost estimates are released as PDFs along wi
  name: CBO Cost Estimates
  slug: cost-estimates
- description: CBO publishes RSS feeds for its publications, including reports, cost estimates, blog posts, working papers, and presentations. RSS is the primary machine-readable surface for new CBO releases.
  name: CBO Publications RSS Feeds
  slug: publications-rss
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/congressional-budget-office-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/us-cbo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/congressional-budget-office
- group: company
  title: ''
  type: Website
  url: https://www.cbo.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cbo.gov/data/budget-economic-data
- group: docs
  title: ''
  type: Reference
  url: https://www.cbo.gov/about/products
- group: other
  title: ''
  type: Feeds
  url: https://www.cbo.gov/about/get-cbo-information#rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cbo.gov/about/policies/privacy-and-security-policy
created: '2024-12-03'
description: The Congressional Budget Office (CBO) is the U.S. legislative branch agency that provides nonpartisan analyses of budgetary and economic issues to Congress. CBO publishes the Budget and Economic Outlook, projections of spending, revenues, deficits, and debt, cost estimates of legislation, and analytical reports. CBO data is distributed primarily as Excel and PDF files on cbo.gov; CBO does not currently publish a programmatic JSON API, but RSS feeds and downloadable structured workbooks make it possible to ingest CBO data into automated pipelines.
finops:
- name: Congressional Budget Office Finops
  service_category: API
  slug: congressional-budget-office-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/congressional-budget-office.png
layout: provider
modified: '2026-04-28'
name: Congressional Budget Office
nav: Providers
network: true
overview: 'Congressional Budget Office publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Budget, CBO, Economic Projections, Federal-Government, and Legislative Branch.


  Congressional Budget Office''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Congressional Budget Office Plans Pricing
  plan_count: 3
  slug: congressional-budget-office-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Congressional Budget Office Rate Limits
  slug: congressional-budget-office-rate-limits
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/congressional-budget-office/refs/heads/main/screenshots/congressional-budget-office-2026-07-25T210253.png
security:
- kind: domain-security
  name: Congressional Budget Office Domain Security
  slug: congressional-budget-office-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: congressional-budget-office
tags:
- Budget
- CBO
- Economic Projections
- Federal-Government
- Legislative Branch
- Open Data
- RSS
website: https://www.cbo.gov/
---
