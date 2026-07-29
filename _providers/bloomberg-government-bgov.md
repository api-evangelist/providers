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
- description: Access BGOV legislative, regulatory, and government contracting data programmatically. Retrieve bill tracking, regulatory actions, federal contract awards, and lobbying disclosures for integration int
  name: Bloomberg Government Data API
  slug: bgov-data-api
- description: Access federal contract award data, procurement intelligence, and vendor spending data. Track USASpending.gov data enriched with Bloomberg analytics for competitive intelligence and business developme
  name: BGOV Government Contracting Intelligence
  slug: bgov-contracting-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-government-bgov-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomberg-government
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://about.bgov.com/
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
  url: https://about.bgov.com/contact/
created: '2024-01-01'
description: Bloomberg Government (BGOV) is a comprehensive intelligence platform for professionals working at the intersection of government and business. BGOV provides legislative tracking, regulatory intelligence, government contracting data, federal budget analysis, and policy research tools. It offers APIs and data feeds for integrating government and regulatory data into enterprise workflows.
features:
- description: Real-time tracking of bills, hearings, and committee activity across Congress.
  name: Legislative Tracking
- description: Monitor federal agency rulemaking, proposed rules, and final regulations.
  name: Regulatory Intelligence
- description: Federal contract awards, task orders, and spending analysis.
  name: Government Contracting Data
- description: Appropriations tracking, budget requests, and spending trends.
  name: Federal Budget Analysis
- description: Lobbying registrations, disclosures, and advocacy activity tracking.
  name: Lobbying Disclosure Data
finops:
- name: Bloomberg Government Bgov Finops
  service_category: API
  slug: bloomberg-government-bgov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-government-bgov.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Government (BGOV)
nav: Providers
network: true
overview: 'Bloomberg Government (BGOV) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Legislative, Regulatory, Government Contracting, and Federal Budget.


  Bloomberg Government (BGOV)''s developer surface includes developer portal, documentation, support, and 4 more developer resources.'
plans:
- name: Bloomberg Government Bgov Plans Pricing
  plan_count: 3
  slug: bloomberg-government-bgov-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Bloomberg Government Bgov Rate Limits
  slug: bloomberg-government-bgov-rate-limits
score:
  band: emerging
  composite: 27.2
  delta: -2.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-government-bgov/refs/heads/main/screenshots/bloomberg-government-bgov-2026-06-20T173440.png
security:
- kind: domain-security
  name: Bloomberg Government Bgov Domain Security
  slug: bloomberg-government-bgov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-government-bgov
tags:
- Government
- Legislative
- Regulatory
- Government Contracting
- Federal Budget
- Policy Research
- Bloomberg
use_cases:
- description: Track legislation and regulatory developments affecting business interests.
  name: Government Relations
- description: Identify contracting opportunities and analyze competitor awards.
  name: Federal Contracting
- description: Deep research on policy developments and their business implications.
  name: Policy Research
- description: Monitor regulatory changes for compliance and risk management.
  name: Compliance Monitoring
website: https://www.bloomberg.com/professional/
---
