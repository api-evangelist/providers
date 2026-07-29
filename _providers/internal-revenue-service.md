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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The IRS Modernized e-File (MeF) system is the web-based electronic filing platform supporting individual, business, and tax-exempt return submission via XML-based schemas. Software developers and tran
  name: IRS Modernized e-File (MeF)
  slug: modernized-e-file
- description: 'IRS e-Services is a suite of web-based products for tax professionals, reporting agents, and authorized e-file providers offering Transcript Delivery, TIN Matching, e-file application management, and '
  name: IRS e-Services
  slug: e-services
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/internal-revenue-service-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IRS-Public
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/irs
- group: company
  title: ''
  type: Website
  url: https://www.irs.gov/
- group: other
  title: ''
  type: Developer
  url: https://www.irs.gov/e-file-providers/software-developers
- group: operate
  title: ''
  type: Support
  url: https://www.irs.gov/help
created: '2024-12-25'
description: The Internal Revenue Service (IRS) is the United States federal tax collection agency and a bureau of the Department of the Treasury. The IRS publishes developer resources for tax software providers and transmitters including the Modernized e-File (MeF) system for electronic tax return submission, the e-Services suite for authorized e-file providers, and Publication 4164 (the MeF Guide for Software Developers and Transmitters) which documents the XML schemas and transmission protocols required for integration.
finops:
- name: Internal Revenue Service Finops
  service_category: API
  slug: internal-revenue-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/internal-revenue-service.png
layout: provider
modified: '2026-04-28'
name: Internal Revenue Service
nav: Providers
network: true
overview: 'Internal Revenue Service publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Finance, IRS, Tax, and Tax Filing.


  Internal Revenue Service''s developer surface includes support and 5 more developer resources.'
plans:
- name: Internal Revenue Service Plans Pricing
  plan_count: 3
  slug: internal-revenue-service-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Internal Revenue Service Rate Limits
  slug: internal-revenue-service-rate-limits
score:
  band: emerging
  composite: 19.5
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/internal-revenue-service/refs/heads/main/screenshots/internal-revenue-service-2026-06-20T183453.png
security:
- kind: domain-security
  name: Internal Revenue Service Domain Security
  slug: internal-revenue-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: internal-revenue-service
tags:
- Federal Government
- Finance
- IRS
- Tax
- Tax Filing
website: https://www.irs.gov/
---
