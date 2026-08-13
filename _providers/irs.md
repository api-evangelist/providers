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
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: Allows payers to submit Taxpayer Identification Number (TIN) and name combinations to be matched against IRS records before filing information returns. Supports interactive matching of up to 25 combin
  name: IRS TIN Matching API
  slug: tin-matching
- description: Application-to-Application (A2A) API allowing authorized participants such as lenders, banks, credit unions, and financial institutions to request IRS tax transcripts for income verification purposes.
  name: IRS Income Verification Express Service (IVES) API
  slug: ives
- description: Application-to-Application (A2A) API for electronic filing of 1099 series information returns directly with the IRS. Supports high-volume automated submission by software developers and large-scale fi
  name: IRS Information Return Intake System (IRIS) API
  slug: iris
- description: Application-to-Application (A2A) system enabling authorized software developers and transmitters to electronically submit tax returns directly to the IRS. Supports individual and business tax forms in
  name: IRS Modernized e-File (MeF) API
  slug: mef
- description: e-Services API allowing authorized tax professionals and institutions to retrieve tax transcripts programmatically. Part of the IRS e-Services suite alongside TIN Matching and the Secure Object Reposi
  name: IRS Transcript Delivery System (TDS) API
  slug: tds
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/irs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.irs.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.irs.gov/tax-professionals/get-an-api-client-id
- group: start
  title: ''
  type: GettingStarted
  url: https://www.irs.gov/tax-professionals/get-an-api-client-id
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.irs.gov/e-file-providers/information-and-technical-guidance-for-software-developers-and-transmitters
- group: operate
  title: ''
  type: StatusPage
  url: https://www.irs.gov/e-file-providers/modernized-e-file-mef-status
- group: commercial
  title: ''
  type: Plans
  url: plans/irs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/irs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/irs-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/irs
- group: other
  title: ''
  type: X
  url: https://x.com/irsnews
- group: company
  title: ''
  type: Blog
  url: https://www.irs.gov/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.irs.gov/privacy-disclosure/irs-website-privacy-policy-statement
created: '2026-06-13'
description: The US Internal Revenue Service (IRS) provides REST APIs and Application-to-Application (A2A) interfaces for tax information access, identity verification, income verification, information return filing, and taxpayer account data. Authorized applications can integrate with IRS e-Services for TIN matching, the Transcript Delivery System (TDS), the Income Verification Express Service (IVES), the Information Return Intake System (IRIS) for 1099 series filings, and the Modernized e-File (MeF) system for electronic tax return submission. Access requires enrollment in IRS e-Services and obtaining an API client ID.
finops:
- name: Irs Finops
  service_category: ''
  slug: irs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/irs.png
layout: provider
modified: '2026-06-13'
name: IRS
nav: Providers
network: true
overview: 'IRS publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include IRS, Tax, Federal Government, TIN Matching, and Income Verification.


  IRS''s developer surface includes documentation, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Irs Plans Pricing
  plan_count: 2
  slug: irs-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 2
  name: Irs Rate Limits
  slug: irs-rate-limits
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/irs/refs/heads/main/screenshots/irs-2026-06-20T183613.png
security:
- kind: domain-security
  name: Irs Domain Security
  slug: irs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: irs
tags:
- IRS
- Tax
- Federal Government
- TIN Matching
- Income Verification
- Information Returns
- e-File
- Identity Verification
- Taxpayer
website: https://www.irs.gov/
---
