---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: Securely verifies client identity and issues access tokens via OAuth 2.0 client credentials grant for authenticating requests to all G-P APIs.
  name: G-P Authentication API
  slug: g-p-authentication-api
- description: Provides capabilities for accessing and managing employee and employment data within the G-P Employer of Record (EOR) product, including international hires, employment contracts, benefits, and compli
  name: G-P EOR API
  slug: g-p-eor-api
- description: API set for accessing and managing detailed Contractor information, enabling companies to onboard, manage, and pay international contractors compliantly through the G-P platform.
  name: G-P Contractor API
  slug: g-p-contractor-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/g-p-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.globalization-partners.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.g-p.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.g-p.com/guides/quick-start
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/globalization-partners
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/g-p/
- group: company
  title: ''
  type: Blog
  url: https://www.globalization-partners.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.globalization-partners.com/g-p-api/
- group: other
  title: ''
  type: X
  url: https://x.com/GlobalEOR
- group: commercial
  title: ''
  type: Plans
  url: plans/g-p-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/g-p-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/g-p-finops.yml
created: '2026-06-13'
description: G-P (Globalization Partners) is the recognized leader in global employment, providing a comprehensive platform to hire, manage, and pay employees and contractors in 180+ countries without setting up local entities. Their REST APIs enable companies to automate HR workflows, manage employment contracts, benefits, payroll, and compliance across international teams through EOR (Employer of Record) and Contractor products.
finops:
- name: G P Finops
  service_category: ''
  slug: g-p-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/g-p.png
layout: provider
modified: '2026-06-13'
name: G-P
nav: Providers
network: true
overview: 'G-P publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, EOR API, and Contractor API. Tagged areas include Global Employment, Employer of Record, EOR, Payroll, and HR.


  G-P''s developer surface includes documentation, getting-started guide, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: G P Plans Pricing
  plan_count: 3
  slug: g-p-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 0
  name: G P Rate Limits
  slug: g-p-rate-limits
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/g-p/refs/heads/main/screenshots/g-p-2026-06-20T181628.png
security:
- kind: domain-security
  name: G P Domain Security
  slug: g-p-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: g-p
tags:
- Global Employment
- Employer of Record
- EOR
- Payroll
- HR
- Compliance
- Contractors
- International Hiring
website: https://www.globalization-partners.com/
---
