---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://nonnatech.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nonnatech.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nonnatech.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://nonnatech.com/about/contact-information/
- group: operate
  title: ''
  type: FAQ
  url: https://nonnatech.com/faqs/
- group: company
  title: ''
  type: Blog
  url: https://nonnatech.com/about/awards-and-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://nonnatech.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nonnatech
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nonnatech
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nonnatech-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nonnatech-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nonnatech-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nonnatech-llms.txt
coverage:
  checked: '2026-08-15'
  detail: Nonnatech ships an end-user clinician dashboard at app.nonnatech.com and markets EHR integration as a delivered service, but the word "API" appears nowhere on its 22-page WordPress site and every contract-discovery path (/openapi.json, /swagger.json, /graphql, /mcp, /api-docs, /llms.txt and all seven /.well-known/ documents) returns 404 on both the marketing host and the dashboard host.
  evidence:
  - status: 404
    url: https://app.nonnatech.com/openapi.json
  - status: 404
    url: https://app.nonnatech.com/graphql
  - status: 404
    url: https://nonnatech.com/developers
  - status: 404
    url: https://nonnatech.com/.well-known/api-catalog
  - status: 200
    url: https://nonnatech.com/page-sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Nonnatech is a New York-based remote patient monitoring (RPM) and virtual health company that provides HIPAA-secured technology and clinical services for healthcare providers. Its platform integrates biometric sensors and passive home devices to deliver real-time analytics, chronic condition management, and population health programs across hospitals, health systems, physician practices, payers, ACOs, home care, long-term care, and senior living communities. Nonnatech offers turnkey device ordering, EHR data integration, and optional clinical monitoring, with no upfront costs to providers and roughly 30-day implementation. Nonnatech is a 500 Global portfolio company. It does not publish a public developer program, API documentation, or developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nonnatech.png
layout: provider
modified: '2026-08-15'
name: Nonnatech
nav: Providers
network: true
overview: 'Nonnatech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Remote Patient Monitoring, Digital Health, and Telehealth.


  Nonnatech''s developer surface includes support, FAQ, engineering blog, and 10 more developer resources.'
plans:
- name: Nonnatech Plans Pricing
  plan_count: 0
  slug: nonnatech-plans-pricing
random_paper: 64
score:
  band: emerging
  composite: 13.1
  delta: 1.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nonnatech/refs/heads/main/screenshots/nonnatech-2026-08-07T185449.png
security:
- kind: domain-security
  name: Nonnatech Domain Security
  slug: nonnatech-domain-security
  summary_line: TLSv1.3
slug: nonnatech
tags:
- Company
- Healthcare
- Remote Patient Monitoring
- Digital Health
- Telehealth
- HIPAA
- Population Health
- Chronic Care
website: https://nonnatech.com
---
