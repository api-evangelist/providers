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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 8
apis:
- description: 'Access to Current Employment Statistics (CES), Current Population Survey (CPS), Occupational Employment Statistics Survey (OES), Quarterly Census Employment and Wage (CEW), and Consumer Price Indexes '
  name: DOL Employment Statistics API
  slug: dol-employment-statistics-api
- description: Access OSHA inspection and enforcement data including inspection details, violations, citations, penalties, and accident injury reports. Covers all OSHA compliance actions with summary information abo
  name: DOL OSHA Enforcement API
  slug: dol-osha-enforcement-api
- description: Access Wage and Hour Division (WHD) compliance action data covering all concluded compliance actions since FY 2005, including back wages, violations, and employer information. Also includes Farm Labor
  name: DOL Wage and Hour Compliance API
  slug: dol-wage-and-hour-compliance-api
- description: Access Labor Condition Application (LCA) data collected by the Employment and Training Administration's Office of Foreign Labor Certification (OFLC) covering H-1B, H-1B1, E-3, H-2A, H-2B, and D-1 visa
  name: DOL H-1B Foreign Labor Certification API
  slug: dol-h-1b-foreign-labor-certification-api
- description: Access Mine Safety and Health Administration (MSHA) data including mine-by-mine information, accidents and injuries, inspections, violations, assessments, employment and production reports. Covers Ful
  name: DOL Mine Safety and Health API
  slug: dol-mine-safety-and-health-api
- description: Access Public Workforce System data including Initial Unemployment Insurance (UI) Claims, Workforce Investment Act data, job openings, and workforce development program information from the Employment
  name: DOL Public Workforce System API
  slug: dol-public-workforce-system-api
- description: Access VETS-4212 and VETS-100 datasets containing veteran employment data reported by federal contractors and subcontractors, including hiring benchmarks and veteran representation across contractor o
  name: DOL Veterans Employment API
  slug: dol-veterans-employment-api
- description: Access the International Labor Affairs Bureau (ILAB) Sweat and Toil data covering child labor and forced labor worldwide, including goods produced with child or forced labor by country and good, sourc
  name: DOL Sweat and Toil API
  slug: dol-sweat-and-toil-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dol.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dol.gov/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/USDepartmentofLabor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-department-of-labor
- group: company
  title: ''
  type: Blog
  url: https://blog.dol.gov/
- group: commercial
  title: ''
  type: Pricing
  url: https://dataportal.dol.gov/
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.dol.gov/others/api-metrics-per-key/
- group: other
  title: ''
  type: X
  url: https://x.com/USDOL
- group: commercial
  title: ''
  type: Plans
  url: plans/dol-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dol-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dol-finops.yml
- group: start
  title: ''
  type: OpenDataPortal
  url: https://dataportal.dol.gov/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.dol.gov/release-notes/
- group: other
  title: ''
  type: EnforceData
  url: https://enforcedata.dol.gov/
created: '2026-06-13'
description: The U.S. Department of Labor provides REST APIs exposing over 200 datasets covering employment statistics, H-1B and foreign labor visa data, OSHA inspections and enforcement, wage and hour violations, job openings, union reports, workforce development data, mine safety, and Bureau of Labor Statistics economic indicators including CPI, CES, OES, and CPS. APIs are free to use with registration via the Open Data Portal.
finops:
- name: Dol Finops
  service_category: ''
  slug: dol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dol.png
jsonld:
- class_count: 14
  name: Dol Context
  property_count: 30
  slug: dol-context
layout: provider
modified: '2026-06-13'
name: Department of Labor
nav: Providers
network: true
overview: 'Department of Labor publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Employment, Labor, Workforce, and OSHA.


  The Department of Labor catalog on APIs.io includes 1 JSON-LD context.


  Department of Labor''s developer surface includes documentation, engineering blog, pricing, changelog, and 11 more developer resources.'
plans:
- name: Dol Plans Pricing
  plan_count: 2
  slug: dol-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 0
  name: Dol Rate Limits
  slug: dol-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dol/refs/heads/main/screenshots/dol-2026-06-20T180132.png
security:
- kind: domain-security
  name: Dol Domain Security
  slug: dol-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dol
tags:
- Government
- Employment
- Labor
- Workforce
- OSHA
- Safety
- Wages
- H-1B
- Statistics
- Open Data
website: https://www.dol.gov/
---
