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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
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
overview: 'Klippa publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Document AI, IDP, OCR, and Verification.


  Klippa''s developer surface includes pricing, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Klippa Plans Pricing
  plan_count: 5
  slug: klippa-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Klippa Rate Limits
  slug: klippa-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Artificial Intelligence
- Document AI
- IDP
- OCR
- Verification
- GDPR
- EU
website: https://www.klippa.com/
---
