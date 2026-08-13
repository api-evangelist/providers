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
- description: 'Following the Fiserv merger, legacy First Data API products are now hosted on the Fiserv developer portal. These include Commerce Hub, Payeezy, and Bolt for merchant payment acceptance, tokenization, '
  name: Fiserv Developer (First Data Legacy)
  slug: fiserv-developer
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-data-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firstdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-data-corporation
- group: company
  title: ''
  type: Website
  url: https://www.fiserv.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fiserv.com
created: '2025-03-01'
description: First Data was a global payment technology solutions company providing merchant transaction processing, financial institution services, and prepaid services before merging with Fiserv in 2019. Legacy First Data API products including Payeezy, Bolt, and Commerce Hub are now part of the Fiserv developer portal.
finops:
- name: First Data Finops
  service_category: Payments
  slug: first-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/first-data.png
layout: provider
modified: '2026-04-28'
name: First Data (Fiserv)
nav: Providers
network: true
overview: First Data (Fiserv) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Merchant Services, Financial Services, Transaction Processing, and Fortune 500.
plans:
- name: First Data Plans Pricing
  plan_count: 2
  slug: first-data-plans-pricing
press:
- date: '2026-05-25'
  title: Powering the AI Era
  url: https://www.goldmansachs.com/what-we-do/investment-banking/insights/articles/powering-the-ai-era/report.pdf
- date: '2026-05-25'
  title: Fiserv Embarks on 2-Year AI Transformation with IBM ...
  url: https://www.linkedin.com/posts/josephbutler1_fiserv-projectelevate-ai-activity-7429911576381661184-OHJq
- date: '2026-05-25'
  title: Press Releases
  url: https://www.googlecloudpresscorner.com/ai-infrastructure?l=100
- date: '2026-05-25'
  title: Applied Digital Advances AI Factory Buildout with Second ...
  url: https://ir.applieddigital.com/news-events/press-releases/detail/135/applied-digital-advances-ai-factory-buildout-with-second
- date: '2026-05-25'
  title: First Data Center Project Gains Permitting Council's FAST ...
  url: https://www.permitting.gov/newsroom/press-releases/first-data-center-project-gains-permitting-councils-fast-41-coverage
random_paper: 47
rate_limits:
- limit_count: 1
  name: First Data Rate Limits
  slug: first-data-rate-limits
score:
  band: minimal
  composite: 11.3
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-data/refs/heads/main/screenshots/first-data-2026-06-20T181236.png
security:
- kind: domain-security
  name: First Data Domain Security
  slug: first-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: first-data
tags:
- Payments
- Merchant Services
- Financial Services
- Transaction Processing
- Fortune 500
website: https://www.fiserv.com
---
