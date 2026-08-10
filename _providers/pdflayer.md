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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST API for converting HTML content and web page URLs to PDF documents with support for custom page sizes, margins, headers, footers, watermarks, page numbering, and 256-bit HTTPS encryption.
  name: pdflayer API
  slug: pdflayer-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdflayer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pdflayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://pdflayer.com/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/apilayer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apilayer/pdflayer-API
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apilayer/
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://pdflayer.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://pdflayer.com/api-status
- group: other
  title: ''
  type: X
  url: https://twitter.com/apilayer/
- group: operate
  title: ''
  type: Contact
  url: https://pdflayer.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://pdflayer.com/faq
- group: commercial
  title: ''
  type: Plans
  url: plans/pdflayer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdflayer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdflayer-finops.yml
created: '2026-06-13'
description: pdflayer is a PDF generation REST API by APILayer for converting HTML to PDF and capturing web pages as PDFs. It supports rendering from standard HTTP URLs or raw HTML code, with extensive customization options including custom page sizes, margins, headers, footers, watermarks, and 256-bit encryption. The lightweight RESTful API supports both GET and POST methods and is powered by high-throughput infrastructure capable of processing thousands of requests simultaneously.
finops:
- name: Pdflayer Finops
  service_category: ''
  slug: pdflayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdflayer.png
layout: provider
modified: '2026-06-13'
name: pdflayer
nav: Providers
network: true
overview: 'pdflayer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PDF, HTML to PDF, Document Generation, Web Capture, and APILayer.


  pdflayer''s developer surface includes documentation, engineering blog, pricing, FAQ, and 11 more developer resources.'
plans:
- name: Pdflayer Plans Pricing
  plan_count: 4
  slug: pdflayer-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 4
  name: Pdflayer Rate Limits
  slug: pdflayer-rate-limits
score:
  band: thin
  composite: 33.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 33.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdflayer/refs/heads/main/screenshots/pdflayer-2026-06-20T191518.png
security:
- kind: domain-security
  name: Pdflayer Domain Security
  slug: pdflayer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pdflayer
tags:
- PDF
- HTML to PDF
- Document Generation
- Web Capture
- APILayer
- PDF Conversion
website: https://pdflayer.com
---
