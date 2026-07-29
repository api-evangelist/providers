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
api_count: 1
apis:
- description: REST API for PDF generation (HTML, URL, visual-editor templates) and image generation. Bearer-token auth via API key. Regional endpoints improve latency.
  name: APITemplate.io REST API
  slug: rest
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apitemplate-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apitemplate-io
- group: company
  title: ''
  type: Website
  url: https://apitemplate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://apitemplate.io/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://apitemplate.io/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/apitemplateio
- group: commercial
  title: ''
  type: Plans
  url: plans/apitemplate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apitemplate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apitemplate-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://apitemplate.io/feed/
created: '2026-05-08'
description: APITemplate.io is a templating service that auto-generates PDFs and images programmatically from HTML/CSS templates with Jinja2-style data binding. Drag-and-drop visual editor; sync and async generation with webhooks; regional endpoints in US, EU, Singapore and Australia. SDKs for Python, JavaScript, PHP, C# and Java.
finops:
- name: Apitemplate Finops
  service_category: Document Generation
  slug: apitemplate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apitemplate.png
layout: provider
modified: '2026-05-08'
name: APITemplate.io
nav: Providers
network: true
overview: 'APITemplate.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Document Generation, PDF, Images, Templates, and API.


  APITemplate.io''s developer surface includes documentation, pricing, GitHub presence, engineering blog, and 6 more developer resources.'
plans:
- name: Apitemplate Plans Pricing
  plan_count: 8
  slug: apitemplate-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 3
  name: Apitemplate Rate Limits
  slug: apitemplate-rate-limits
score:
  band: emerging
  composite: 23.8
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apitemplate/refs/heads/main/screenshots/apitemplate-2026-06-20T172257.png
security:
- kind: domain-security
  name: Apitemplate Domain Security
  slug: apitemplate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apitemplate
tags:
- Document Generation
- PDF
- Images
- Templates
- API
- Jinja2
website: https://apitemplate.io/
---
