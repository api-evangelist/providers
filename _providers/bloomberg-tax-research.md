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
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: Programmatic access to Bloomberg Tax research content including tax portfolios, practitioner analysis, primary sources, and tax news for integration into legal research and tax technology platforms.
  name: Bloomberg Tax Research API
  slug: btax-research-api
- description: State and local tax (SALT) research platform covering income, sales, property, and other state and local tax types with state-by-state analysis and guidance.
  name: Bloomberg Tax SALT Research
  slug: salt-research
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-tax-research-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://pro.bloombergtax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pro.bloombergtax.com/tax-research/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://pro.bloombergtax.com/contact/
created: '2024-01-01'
description: Bloomberg Tax Research provides tax professionals with comprehensive access to primary sources, expert practitioner analysis, portfolios, and tax news for conducting in-depth tax research. The platform covers federal income tax, state and local tax (SALT), international tax, estate planning, benefits, payroll, and transfer pricing research.
features:
- description: Practitioner-authored portfolio analysis on tax topics.
  name: Tax Portfolios
- description: Access to Internal Revenue Code, Treasury regulations, and rulings.
  name: Primary Sources
- description: State and local tax research across all 50 states.
  name: State Tax Research
- description: Global tax research covering international income tax and treaties.
  name: International Tax Research
- description: Breaking tax news and regulatory updates.
  name: Tax News
- description: Payroll tax and employee benefits research and compliance.
  name: Payroll and Benefits
finops:
- name: Bloomberg Tax Research Finops
  service_category: API
  slug: bloomberg-tax-research-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-tax-research.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Tax Research
nav: Providers
network: true
overview: 'Bloomberg Tax Research publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Tax Research, Federal Tax, State Tax, International Tax, and Tax Analysis.


  Bloomberg Tax Research''s developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Tax Research Plans Pricing
  plan_count: 3
  slug: bloomberg-tax-research-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Bloomberg Tax Research Rate Limits
  slug: bloomberg-tax-research-rate-limits
score:
  band: emerging
  composite: 27.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-tax-research/refs/heads/main/screenshots/bloomberg-tax-research-2026-06-20T173508.png
security:
- kind: domain-security
  name: Bloomberg Tax Research Domain Security
  slug: bloomberg-tax-research-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-tax-research
tags:
- Tax Research
- Federal Tax
- State Tax
- International Tax
- Tax Analysis
- Bloomberg Tax
use_cases:
- description: Research complex federal income tax issues with authoritative sources.
  name: Federal Tax Research
- description: Research state tax obligations and filing requirements.
  name: State Tax Compliance
- description: Analyze international tax structures and treaty positions.
  name: International Tax Planning
- description: Research estate, gift, and generation-skipping transfer tax issues.
  name: Estate Planning
website: https://pro.bloombergtax.com/
---
