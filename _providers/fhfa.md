---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
api_count: 5
apis:
- description: The FHFA House Price Index (HPI) is a comprehensive, publicly available dataset measuring changes in single-family home values across all 50 states and over 400 American cities, with data extending ba
  name: FHFA House Price Index (HPI) API
  slug: fhfa-house-price-index-api
- description: The National Mortgage Database (NMDB) is a nationally representative, longitudinal database of residential mortgages providing aggregate statistics on outstanding residential mortgages and mortgage or
  name: FHFA National Mortgage Database (NMDB) API
  slug: fhfa-national-mortgage-database-api
- description: The FHFA Enterprise Public Use Database (PUDB) provides loan-level data on single-family and multifamily mortgages acquired by Fannie Mae and Freddie Mac, as well as data on Federal Home Loan Bank mem
  name: FHFA Enterprise Public Use Database (PUDB) API
  slug: fhfa-public-use-database-api
- description: FHFA publishes annual conforming loan limit (CLL) values establishing the maximum mortgage amounts that Fannie Mae and Freddie Mac may purchase. Data is available at the county level for all U.S. stat
  name: FHFA Conforming Loan Limits API
  slug: fhfa-conforming-loan-limits-api
- description: The FHFA Uniform Appraisal Dataset (UAD) Aggregate Statistics provide data on residential appraisals submitted to Fannie Mae and Freddie Mac, covering appraisal values, property characteristics, and g
  name: FHFA Uniform Appraisal Dataset (UAD) Aggregate Statistics API
  slug: fhfa-uad-aggregate-statistics-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fhfa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fhfa.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.fhfa.gov/data/developer-information
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fhfa.gov/about/fhfa-policies/api-terms-of-service
- group: other
  title: ''
  type: Datasets
  url: https://www.fhfa.gov/data/datasets
- group: company
  title: ''
  type: Blog
  url: https://www.fhfa.gov/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fhfa
- group: other
  title: ''
  type: X
  url: https://x.com/FHFA
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/fhfa
- group: commercial
  title: ''
  type: Plans
  url: plans/fhfa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fhfa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fhfa-finops.yml
created: '2026-06-13'
description: The Federal Housing Finance Agency (FHFA) is an independent federal regulator established in 2008 that supervises Fannie Mae, Freddie Mac, and the Federal Home Loan Bank System. FHFA provides publicly accessible data APIs and datasets covering house price indexes (FHFA HPI), mortgage market surveys, conforming loan limits, National Mortgage Database (NMDB) aggregate statistics, Public Use Databases (PUDB) for Fannie Mae and Freddie Mac, Uniform Appraisal Dataset (UAD) statistics, and GSE performance and duty-to-serve data. Data is available in CSV, JSON, XML, and Excel formats with open public access under FHFA's API Terms of Service.
finops:
- name: Fhfa Finops
  service_category: API
  slug: fhfa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fhfa.png
jsonld:
- class_count: 22
  name: Fhfa Context
  property_count: 18
  slug: fhfa-context
layout: provider
modified: '2026-06-13'
name: Federal Housing Finance Agency (FHFA)
nav: Providers
network: true
overview: 'Federal Housing Finance Agency (FHFA) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Housing Finance, House Price Index, Mortgage, Government, and GSE.


  The Federal Housing Finance Agency (FHFA) catalog on APIs.io includes 1 JSON-LD context.


  Federal Housing Finance Agency (FHFA)''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Fhfa Plans Pricing
  plan_count: 1
  slug: fhfa-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Fhfa Rate Limits
  slug: fhfa-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fhfa/refs/heads/main/screenshots/fhfa-2026-06-20T181144.png
security:
- kind: domain-security
  name: Fhfa Domain Security
  slug: fhfa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fhfa
tags:
- Housing Finance
- House Price Index
- Mortgage
- Government
- GSE
- Fannie Mae
- Freddie Mac
- Federal
website: https://www.fhfa.gov
---
