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
api_count: 1
apis:
- description: RESTful HTTPS-based API for cannabis tax compliance. Enables calculation of state, county, and local cannabis excise taxes, storage of tax data, and support for monthly cannabis tax return filing acro
  name: TaxNexus API
  slug: taxnexus-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taxnexus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taxnexus.io/
- group: docs
  title: ''
  type: Documentation
  url: https://taxnexus.io/index.php/taxnexus-api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/taxnexus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taxnexus-ai
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@taxnexus
- group: commercial
  title: ''
  type: Pricing
  url: https://taxnexus.io/
- group: other
  title: ''
  type: X
  url: https://x.com/taxnexus
- group: commercial
  title: ''
  type: Plans
  url: plans/taxnexus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taxnexus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/taxnexus-finops.yml
created: 2026-06-13
description: TaxNexus is a cannabis tax compliance REST API and financial technology service that automates calculation of state, county, and local cannabis excise taxes across supported jurisdictions including California and Oregon. Cannabis POS and ERP software developers can integrate with the TaxNexus API to calculate excise taxes, track and store tax data, and file monthly cannabis tax returns. The platform serves cannabis businesses, software makers, and accountants seeking to automate real-world cannabis tax compliance problems for recreational and medical cannabis taxpayers.
finops:
- name: Taxnexus Finops
  service_category: ''
  slug: taxnexus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taxnexus.png
layout: provider
modified: 2026-06-13
name: TaxNexus
nav: Providers
network: true
overview: 'TaxNexus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tax, Cannabis, Sales Tax, Tax Compliance, and Excise Tax.


  TaxNexus'' developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Taxnexus Plans Pricing
  plan_count: 3
  slug: taxnexus-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 2
  name: Taxnexus Rate Limits
  slug: taxnexus-rate-limits
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Taxnexus Domain Security
  slug: taxnexus-domain-security
  summary_line: TLSv1.2
slug: taxnexus
tags:
- Tax
- Cannabis
- Sales Tax
- Tax Compliance
- Excise Tax
- FinTech
- Cannabis Industry
website: https://taxnexus.io/
---
