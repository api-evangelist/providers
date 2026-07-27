---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lincoln National Agentic Access
  operation_count: 3
  slug: lincoln-national-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: The Enrollment API from Lincoln National — 1 operation(s) for enrollment.
  name: Lincoln National Enrollment API
  slug: lincoln-national-enrollment-api
- description: The Eoi API from Lincoln National — 1 operation(s) for eoi.
  name: Lincoln National Eoi API
  slug: lincoln-national-eoi-api
- description: The Plan Design API from Lincoln National — 1 operation(s) for plan design.
  name: Lincoln National Plan Design API
  slug: lincoln-national-plan-design-api
artifact_total: 9
collections:
- collection_type: open
  name: Lincoln Financial LincSmart APIs
  slug: open-lincoln-national
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lincoln-national-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lincoln-national-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lincolnfinancial
- group: company
  title: ''
  type: Website
  url: https://www.lincolnfinancial.com
- group: other
  title: ''
  type: LincSmartPlatform
  url: https://www.lincolnfinancial.com/public/static/digitalbrochure/gp/lincsmart/index.html
- group: start
  title: ''
  type: Portal
  url: https://www.mylincolnportal.com
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/lincoln-national/refs/heads/main/openapi/lincoln-national-openapi.yml
created: '2026-03-21'
description: Lincoln National Corporation, operating as Lincoln Financial Group, is a diversified financial services company offering annuities, retirement plan services, life insurance, and group protection products. The company provides solutions for employers, brokers, and retirement professionals through its LincSmart platform of API integrations.
finops:
- name: Lincoln National Finops
  service_category: Insurance / Retirement / API
  slug: lincoln-national-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lincoln-national.png
layout: provider
modified: '2026-05-19'
name: Lincoln National
nav: Providers
network: true
overview: 'Lincoln National publishes 3 APIs on the [APIs.io](https://apis.io/) network: Enrollment API, Eoi API, and Plan Design API. Tagged areas include Annuities, Benefits, Enrollment, HR, and Insurance.


  Lincoln National''s developer surface includes developer portal and 6 more developer resources.'
plans:
- name: Lincoln National Plans Pricing
  plan_count: 1
  slug: lincoln-national-plans-pricing
press:
- date: '2026-05-25'
  title: Lincoln Financial appoints Neel Adhya as chief AI and data ...
  url: https://www.investing.com/news/company-news/lincoln-financial-appoints-neel-adhya-as-chief-ai-and-data-officer-93CH-4392038
- date: '2026-05-25'
  title: Core earnings rise as Lincoln Financial (NYSE - LNC
  url: https://www.stocktitan.net/sec-filings/LNC/8-k-lincoln-national-corp-reports-material-event-87aa44acf693.html
- date: '2026-05-25'
  title: Lincoln Financial Group expands partnership to support ...
  url: https://www.lincolnfinancial.com/public/aboutus/newsroom/pressreleases/EvolutionIQ
- date: '2026-05-25'
  title: Lincoln Financial Appoints Nilanjan (Neel) Adhya as EVP ...
  url: https://www.businesswire.com/news/home/20251204014069/en/Lincoln-Financial-Appoints-Nilanjan-Neel-Adhya-as-EVP-Chief-AI-Data-and-Analytics-Officer
- date: '2026-05-25'
  title: Delaware Market Conduct Examination Report The Lincoln ...
  url: https://insurance.delaware.gov/wp-content/uploads/sites/15/2025/09/LincolnNationalLifeInsuranceCo2024web.pdf
random_paper: 18
rate_limits:
- limit_count: 1
  name: Lincoln National Rate Limits
  slug: lincoln-national-rate-limits
score:
  band: thin
  composite: 30.6
  delta: 2.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.0
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.9
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lincoln-national/refs/heads/main/screenshots/lincoln-national-2026-06-20T184534.png
security:
- kind: domain-security
  name: Lincoln National Domain Security
  slug: lincoln-national-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lincoln-national
tags:
- Annuities
- Benefits
- Enrollment
- HR
- Insurance
- Retirement
- Fortune 500
website: https://www.lincolnfinancial.com
---
