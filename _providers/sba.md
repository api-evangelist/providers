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
- description: A microservice API providing search access to SBA.gov content including lenders, articles, documents, and personnel. The lenders endpoint constructs queries to the AWS CloudSearch domain for lenders.
  name: SBA.gov Content API
  slug: sba-gov-content-api
- description: API for SBA lenders and partners to originate, service, and manage SBA 7(a) loans. Supports loan origination, status checking, compliance validation, servicing, 1502 reporting, and partner information
  name: Capital Access Financial System (CAFS) Loan Origination API
  slug: cafs-loan-origination-api
- description: API enabling SBA-approved lenders to submit, track, and manage PPP (Paycheck Protection Program) loan forgiveness requests. Supports submission, re-submission, status lookup, document upload, loan val
  name: PPP Loan Forgiveness API
  slug: ppp-loan-forgiveness-api
- description: Public API providing access to SBIR (Small Business Innovation Research) and STTR (Small Business Technology Transfer) award and solicitation data. Returns award details including firm name, agency, p
  name: SBIR/STTR Awards and Solicitations API
  slug: sbir-sttr-api
- description: CKAN-based open data API providing access to SBA datasets including small business size standards by NAICS code, 7(a) and 504 loan data reports (FOIA), and other SBA program data available in JSON and
  name: SBA Open Data API
  slug: sba-open-data-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sba-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sba.gov
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sba.gov/about/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/USSBA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-small-business-administration
- group: company
  title: ''
  type: Blog
  url: https://www.sba.gov/blog
- group: commercial
  title: ''
  type: Pricing
  url: plans/sba-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sba-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sba-finops.yml
- group: other
  title: ''
  type: X
  url: https://x.com/SBAgov
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sba.gov/about-sba/open-government/about-sbagov-website
created: '2026-06-13'
description: The U.S. Small Business Administration provides REST APIs for accessing SBA loan data including 7(a) and 504 loan programs, SBIR/STTR award data, business licensing and size standards, disaster loan application processing, government contracting opportunities, and small business certification programs including HUBZone, 8(a), WOSB, and SDVOSB.
finops:
- name: Sba Finops
  service_category: ''
  slug: sba-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sba.png
jsonld:
- class_count: 11
  name: Sba Context
  property_count: 37
  slug: sba-context
layout: provider
modified: '2026-06-13'
name: Small Business Administration (SBA)
nav: Providers
network: true
overview: 'Small Business Administration (SBA) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Small Business, Loans, Certifications, and Contracting.


  The Small Business Administration (SBA) catalog on APIs.io includes 1 JSON-LD context.


  Small Business Administration (SBA)''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Sba Plans Pricing
  plan_count: 3
  slug: sba-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Sba Rate Limits
  slug: sba-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 49.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sba/refs/heads/main/screenshots/sba-2026-06-20T193446.png
security:
- kind: domain-security
  name: Sba Domain Security
  slug: sba-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sba
tags:
- Government
- Small Business
- Loans
- Certifications
- Contracting
- Disaster Assistance
- SBIR
- STTR
website: https://www.sba.gov
---
