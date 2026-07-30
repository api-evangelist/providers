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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pdf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.wikipedia.org/wiki/PDF
- group: docs
  title: ''
  type: Specification
  url: https://www.iso.org/standard/75839.html
created: '2025'
description: PDF (Portable Document Format) is a file format developed by Adobe in 1993 used to present documents in a manner independent of application software, hardware, and operating systems. This index tracks providers and standards related to PDF as a concept; it does not represent a single API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdf.png
layout: provider
modified: '2026-04-28'
name: PDF
nav: Providers
network: true
overview: PDF is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include PDF, Document, and File Format.
random_paper: 68
score:
  band: minimal
  composite: 4.1
  delta: -1.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdf/refs/heads/main/screenshots/pdf-2026-06-20T191515.png
security:
- kind: domain-security
  name: Pdf Domain Security
  slug: pdf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pdf Vulnerability Disclosure
  slug: pdf-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pdf
tags:
- PDF
- Document
- File Format
website: https://en.wikipedia.org/wiki/PDF
---
