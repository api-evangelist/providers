---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: Flagship REST API for end-to-end document AI — OCR, classification, extraction, conversion (JSON/XML/PDF/CSV/XLSX/UBL), verification, fraud detection, anonymization. API-key auth.
  name: Klippa DocHorizon (Doxis AI.dp) API
  slug: dochorizon
- description: REST API specifically for parsing receipts, invoices and bank statements. Returns structured JSON with line items, taxes, totals.
  name: Klippa Financial Document API (Receipts / Invoices)
  slug: financial
- description: REST API and SDKs for ID document verification, passport verification, face match and liveness detection.
  name: Klippa Identity Verification (KIV) API
  slug: identity
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/klippa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klippa-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/klippa-ai
- group: company
  title: ''
  type: Website
  url: https://www.klippa.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.klippa.com/en/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/klippa-app
- group: commercial
  title: ''
  type: Plans
  url: plans/klippa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/klippa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/klippa-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.klippa.com/en/blog/
created: '2026-05-08'
description: Klippa is a document AI platform whose flagship product, DocHorizon (rebranded as Doxis AI.dp following the SER acquisition), provides OCR, document classification, conversion, verification, fraud detection and anonymization for 50+ document types. Klippa also publishes dedicated APIs for receipts, invoices, IDs/passports and expense management. EU-hosted, GDPR / ISO 27001 certified.
finops:
- name: Klippa Finops
  service_category: Document AI
  slug: klippa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klippa.png
layout: provider
modified: '2026-05-08'
name: Klippa
nav: Providers
network: true
overview: 'Klippa publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Document AI, IDP, OCR, and Verification.


  Klippa''s developer surface includes pricing, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Klippa Plans Pricing
  plan_count: 5
  slug: klippa-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 2
  name: Klippa Rate Limits
  slug: klippa-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klippa/refs/heads/main/screenshots/klippa-2026-06-20T184105.png
security:
- kind: domain-security
  name: Klippa Domain Security
  slug: klippa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Klippa Vulnerability Disclosure
  slug: klippa-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: klippa
tags:
- AI
- Document AI
- IDP
- OCR
- Verification
- GDPR
- EU
website: https://www.klippa.com/
---
