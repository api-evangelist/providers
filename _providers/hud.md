---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hud Agentic Access
  operation_count: 8
  slug: hud-agentic-access
  summary_line: 8 operations
api_count: 10
apis:
- description: Provides Fair Market Rent (FMR) data by state, county, and metropolitan area. Returns efficiency through four-bedroom rental rates used as the basis for Section 8 Housing Choice Voucher payment standa
  name: HUD User Fair Market Rents API
  slug: hud-user-fair-market-rents-api
- description: Returns HUD Income Limits at 30%, 50%, and 80% of Area Median Income (AMI) thresholds by geographic area. Used to determine eligibility for HUD housing assistance programs.
  name: HUD User Income Limits API
  slug: hud-user-income-limits-api
- description: Maps USPS ZIP codes to and from census tracts, counties, CBSAs, congressional districts, and county subdivisions. Supports geographic lookups and crosswalk queries for housing analysis.
  name: HUD User USPS ZIP Code Crosswalk API
  slug: hud-user-usps-zip-code-crosswalk-api
- description: Comprehensive Housing Affordability Strategy (CHAS) data provides custom tabulations of American Community Survey data on housing needs at national, state, county, and municipal levels. Used for Conso
  name: HUD User CHAS API
  slug: hud-user-chas-api
- description: Search for HUD-approved housing counseling agencies by name, city, state, or geographic coordinates. Returns agency contact information and services offered. No API key required.
  name: HUD Housing Counselor Search API
  slug: hud-housing-counselor-search-api
- description: Comprehensive Housing Affordability Strategy data
  name: HUD - US Department of Housing and Urban Development CHAS API
  slug: hud-chas-api
- description: Fair Market Rent data by geography
  name: HUD - US Department of Housing and Urban Development Fair Market Rents API
  slug: hud-fair-market-rents-api
- description: HUD-approved housing counseling agency search
  name: HUD - US Department of Housing and Urban Development Housing Counseling API
  slug: hud-housing-counseling-api
- description: Area Median Income limits by geography
  name: HUD - US Department of Housing and Urban Development Income Limits API
  slug: hud-income-limits-api
- description: ZIP code to geographic area crosswalk queries
  name: HUD - US Department of Housing and Urban Development ZIP Code Crosswalk API
  slug: hud-zip-code-crosswalk-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HUD User CHAS API
  slug: open-hud-chas-api
- collection_type: open
  name: HUD User CHAS Fair Market Rents API
  slug: open-hud-fair-market-rents-api
- collection_type: open
  name: HUD User CHAS Housing Counseling API
  slug: open-hud-housing-counseling-api
- collection_type: open
  name: HUD User CHAS Income Limits API
  slug: open-hud-income-limits-api
- collection_type: open
  name: HUD User CHAS ZIP Code Crosswalk API
  slug: open-hud-zip-code-crosswalk-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hud-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hud.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.huduser.gov/portal/dataset/api.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/HUD-Data-Lab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-department-of-housing-and-urban-development/
- group: company
  title: ''
  type: Blog
  url: https://www.hud.gov/press/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.huduser.gov/portal/dataset/api-terms-of-service.html
- group: operate
  title: ''
  type: StatusPage
  url: https://data.hud.gov/
- group: other
  title: ''
  type: X
  url: https://x.com/HUDgov
- group: commercial
  title: ''
  type: Plans
  url: plans/hud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hud-finops.yml
created: '2026-06-13'
description: The U.S. Department of Housing and Urban Development (HUD) provides public REST APIs for fair housing data, Fair Market Rents, Income Limits, USPS ZIP code crosswalk files, Comprehensive Housing Affordability Strategy (CHAS) data, and housing counseling agency search. All HUD User dataset APIs require a free bearer token obtained from the HUD User portal; the Housing Counselor search API is publicly accessible without authentication.
examples:
- key_count: 1
  name: Hud Fair Market Rent Example
  slug: hud-fair-market-rent-example
- key_count: 1
  name: Hud Income Limits Example
  slug: hud-income-limits-example
- key_count: 1
  name: Hud Usps Zip Crosswalk Example
  slug: hud-usps-zip-crosswalk-example
finops:
- name: Hud Finops
  service_category: ''
  slug: hud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hud.png
json_schemas:
- name: HUD Fair Market Rent
  property_count: 8
  slug: hud-fair-market-rent
- name: HUD Housing Counseling Agency
  property_count: 31
  slug: hud-housing-counseling-agency
- name: HUD Income Limits
  property_count: 9
  slug: hud-income-limits
jsonld:
- class_count: 0
  name: Hud Context
  property_count: 67
  slug: hud-context
layout: provider
modified: '2026-06-13'
name: HUD - US Department of Housing and Urban Development
nav: Providers
network: true
overview: 'HUD - US Department of Housing and Urban Development publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CHAS API, Fair Market Rents API, Housing Counseling API, and 2 more. Tagged areas include Housing, Government, Fair Market Rent, Mortgage, and Community Development.


  The HUD - US Department of Housing and Urban Development catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HUD - US Department of Housing and Urban Development''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Hud Plans Pricing
  plan_count: 2
  slug: hud-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Hud Rate Limits
  slug: hud-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: HUD - US Department of Housing and Urban Development API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hud-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 64.1
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hud/refs/heads/main/screenshots/hud-2026-06-20T182921.png
security:
- kind: authentication
  name: Hud Authentication
  slug: hud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hud Domain Security
  slug: hud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hud
tags:
- Housing
- Government
- Fair Market Rent
- Mortgage
- Community Development
- Public Housing
- Section 8
- Income Limits
website: https://www.hud.gov/
---
