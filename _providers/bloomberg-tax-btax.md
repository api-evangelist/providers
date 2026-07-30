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
- description: Access Bloomberg Tax data including tax rates, regulations, guidance, and compliance data for integration into enterprise tax technology systems and workflows. Covers federal, state, and international
  name: Bloomberg Tax Data API
  slug: btax-data-api
- description: Specialized transfer pricing research and data platform providing comparables databases, country-by-country reporting data, and transfer pricing documentation tools for multinational tax compliance.
  name: Bloomberg Tax Transfer Pricing
  slug: btax-transfer-pricing
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-tax-btax-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomberg-tax
- group: start
  title: ''
  type: Portal
  url: https://pro.bloombergtax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pro.bloombergtax.com/
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
description: Bloomberg Tax (BTAX) is a comprehensive tax research, planning, and compliance platform providing tax professionals with authoritative primary sources, expert analysis, and practical tools. Bloomberg Tax covers federal, state, and international tax law and provides data APIs for integrating tax rates, regulations, and guidance into enterprise tax technology workflows.
features:
- description: Access to IRC, regulations, rulings, and court decisions.
  name: Primary Tax Sources
- description: Bloomberg Tax practitioner analysis and practice portfolios.
  name: Expert Analysis
- description: Federal, state, local, and international tax rates data.
  name: Tax Rates Database
- description: Real-time tax news and regulatory update alerts.
  name: News and Updates
- description: Comparables databases and documentation tools for transfer pricing.
  name: Transfer Pricing Tools
- description: Integration with tax workpaper and compliance software.
  name: Workpapers Integration
finops:
- name: Bloomberg Tax Btax Finops
  service_category: API
  slug: bloomberg-tax-btax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-tax-btax.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Tax (BTAX)
nav: Providers
network: true
overview: 'Bloomberg Tax (BTAX) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Tax, Tax Research, Tax Compliance, Tax Planning, and Federal Tax.


  Bloomberg Tax (BTAX)''s developer surface includes developer portal, documentation, support, and 4 more developer resources.'
plans:
- name: Bloomberg Tax Btax Plans Pricing
  plan_count: 3
  slug: bloomberg-tax-btax-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Bloomberg Tax Btax Rate Limits
  slug: bloomberg-tax-btax-rate-limits
score:
  band: emerging
  composite: 27.4
  delta: -2.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-tax-btax/refs/heads/main/screenshots/bloomberg-tax-btax-2026-06-20T173507.png
security:
- kind: domain-security
  name: Bloomberg Tax Btax Domain Security
  slug: bloomberg-tax-btax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-tax-btax
tags:
- Tax
- Tax Research
- Tax Compliance
- Tax Planning
- Federal Tax
- International Tax
- Bloomberg Tax
use_cases:
- description: Research federal and state tax law using authoritative primary sources.
  name: Tax Research
- description: Analyze tax planning strategies with expert guidance and analysis.
  name: Tax Planning
- description: Navigate international tax obligations and transfer pricing rules.
  name: International Tax Compliance
- description: Integrate Bloomberg Tax data into tax software and ERP systems.
  name: Tax Technology Integration
website: https://pro.bloombergtax.com/
---
