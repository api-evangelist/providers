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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ncua Agentic Access
  operation_count: 2
  slug: ncua-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 6
apis:
- description: Quarterly publicly available financial performance data for all federally insured credit unions based on their quarterly Call Report (Form 5300) filings. Data is available as bulk ZIP downloads in com
  name: NCUA 5300 Call Report Data
  slug: call-report-data-api
- description: An interactive web application allowing users to query and filter financial information collected during the 5300 Call Report cycle. Supports filtering by charter number, region, credit union type, ci
  name: NCUA Custom Data Query Tool
  slug: custom-query-api
- description: A bulk data web service providing the same financial data as the quarterly Call Report ZIP files but in a dynamic, real-time fashion as submissions are validated. Designed for large industry data aggr
  name: NCUA CUOnline Data Web Service
  slug: cuonline-data-web-service
- description: A web-based system and searchable registry of Credit Union Service Organizations (CUSOs) that provide information about their services, financials, and relationships with credit unions. Accessible thr
  name: NCUA CUSO Registry
  slug: cuso-registry-api
- description: The FindCUByRadius.aspx API from National Credit Union Administration (NCUA) — 1 operation(s) for findcubyradius.aspx.
  name: National Credit Union Administration (NCUA) FindCUByRadius.aspx API
  slug: ncua-findcubyradius-aspx-api
- description: The SingleResult.aspx API from National Credit Union Administration (NCUA) — 1 operation(s) for singleresult.aspx.
  name: National Credit Union Administration (NCUA) SingleResult.aspx API
  slug: ncua-singleresult-aspx-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ncua-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ncua-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ncua-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ncua.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://ncua.gov/data
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ContinuityControl/ncua
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-credit-union-administration
- group: company
  title: ''
  type: Blog
  url: https://ncua.gov/news/latest-news
- group: commercial
  title: ''
  type: Pricing
  url: plans/ncua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ncua-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ncua-finops.yml
- group: other
  title: ''
  type: X
  url: https://x.com/TheNCUA
- group: commercial
  title: ''
  type: Plans
  url: plans/ncua-plans-pricing.yml
created: '2026-06-13'
description: The National Credit Union Administration (NCUA) is the independent federal agency that regulates, charters, and supervises federal credit unions. NCUA provides public REST APIs and data services for accessing credit union call report data, financial performance metrics, membership statistics, credit union locator information, and NCUA examination and enforcement findings.
finops:
- name: Ncua Finops
  service_category: ''
  slug: ncua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ncua.png
json_schemas:
- name: NCUA Credit Union Office
  property_count: 16
  slug: ncua-credit-union-office
jsonld:
- class_count: 4
  name: Ncua Context
  property_count: 30
  slug: ncua-context
layout: provider
modified: '2026-06-13'
name: National Credit Union Administration (NCUA)
nav: Providers
network: true
overview: 'National Credit Union Administration (NCUA) publishes 2 APIs on the [APIs.io](https://apis.io/) network: FindCUByRadius.aspx API and SingleResult.aspx API. Tagged areas include Federal Government, Credit Unions, Financial Data, Call Reports, and Banking.


  The National Credit Union Administration (NCUA) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  National Credit Union Administration (NCUA)''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Ncua Plans Pricing
  plan_count: 2
  slug: ncua-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 0
  name: Ncua Rate Limits
  slug: ncua-rate-limits
rules:
- name: National Credit Union Administration (NCUA) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ncua-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.8
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ncua/refs/heads/main/screenshots/ncua-2026-06-20T190114.png
security:
- kind: domain-security
  name: Ncua Domain Security
  slug: ncua-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ncua Vulnerability Disclosure
  slug: ncua-vulnerability-disclosure
  summary_line: Bugcrowd
slug: ncua
tags:
- Federal Government
- Credit Unions
- Financial Data
- Call Reports
- Banking
- Regulatory Data
website: https://ncua.gov/
---
