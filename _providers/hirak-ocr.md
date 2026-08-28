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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Image to text -text recognition- from image more than 100 language, accurate, unlimited requests
  name: Hirak OCR
  slug: hirak-ocr
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hirak-ocr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hirak-ocr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ocr.hirak.site/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Image to text -text recognition- from image more than 100 language, accurate, unlimited requests
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hirak-ocr.png
layout: provider
modified: '2026-05-28'
name: Hirak OCR
nav: Providers
network: true
overview: Hirak OCR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Text Analysis and Public APIs.
random_paper: 14
score:
  band: minimal
  composite: 7.6
  delta: 1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hirak-ocr/refs/heads/main/screenshots/hirak-ocr-2026-06-20T182754.png
security:
- kind: domain-security
  name: Hirak Ocr Domain Security
  slug: hirak-ocr-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Hirak Ocr Vulnerability Disclosure
  slug: hirak-ocr-vulnerability-disclosure
  summary_line: disclosure policy published
slug: hirak-ocr
tags:
- Text Analysis
- Public APIs
website: https://ocr.hirak.site/
---
