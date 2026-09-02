---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
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
api_count: 2
apis:
- description: REST API for connecting small businesses with lenders. Supports loan application submission, eligibility checking, lender matching, and loan product management. The Embedded Financing API allows servi
  name: Lendio Loan Marketplace API
  slug: lendio-loan-marketplace-api
- description: 'API integration for high-volume lenders that allows bulk submission of loan performance data. Supports up to 10,000 records per submission through custom code requests. Provides transaction analytics '
  name: Lendio Loan Performance Tracking API
  slug: lendio-loan-performance-tracking-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lendio.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.lendio.com/embedded-financing
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/LendioDevs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lendio
- group: company
  title: ''
  type: Blog
  url: https://www.lendio.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lendio.com/embedded-financing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.lendio.com/security
- group: other
  title: ''
  type: X
  url: https://x.com/lendio
- group: commercial
  title: ''
  type: Plans
  url: plans/lendio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lendio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lendio-finops.yml
created: '2026-06-13'
description: Lendio is a small business lending marketplace that connects businesses with funding through a network of 75+ lenders. The platform offers a REST API for submitting loan applications, checking eligibility, connecting businesses with lenders, and managing loan products. Lendio provides Embedded Financing for service providers to integrate loan marketplace functionality, Intelligent Lending software for banks and lenders, and a Loan Performance Tracking API for high-volume lenders submitting bulk data records.
finops:
- name: Lendio Finops
  service_category: ''
  slug: lendio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lendio.png
layout: provider
modified: '2026-06-13'
name: Lendio
nav: Providers
network: true
overview: 'Lendio publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Lending, Small Business, Loans, Fintech, and Marketplace.


  Lendio''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Lendio Plans Pricing
  plan_count: 3
  slug: lendio-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Lendio Rate Limits
  slug: lendio-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 26.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lendio/refs/heads/main/screenshots/lendio-2026-06-20T184449.png
security:
- kind: domain-security
  name: Lendio Domain Security
  slug: lendio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lendio
tags:
- Lending
- Small Business
- Loans
- Fintech
- Marketplace
- Embedded Finance
website: https://www.lendio.com
---
