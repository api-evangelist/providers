---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sejda Agentic Access
  operation_count: 1
  slug: sejda-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 4
apis:
- description: Sejda's full PDF task catalog - merge, split, compress, convert (Office/HTML to PDF, PDF to images), edit, watermark, OCR, and fill forms - delivered as online (browser) and desktop applications. Thes
  name: Sejda PDF Tools (Web and Desktop)
  slug: sejda-pdf-tools
- description: Open-source (AGPLv3) Java library for PDF manipulation - merge, split, rotate, encrypt, watermark, and more - built on SAMBox (a maintained PDFBox fork). This is an embeddable code library, not a host
  name: Sejda SDK
  slug: sejda-sdk
- description: Command-line shell over the Sejda SDK for running PDF tasks (merge, split, etc.) from a terminal or scripts. Requires a Java runtime. A commercial sejda-console-pro build exists. This is a local CLI t
  name: Sejda Console
  slug: sejda-console
- description: The HTML to PDF API from Sejda — 1 operation(s) for html to pdf.
  name: Sejda HTML to PDF API
  slug: sejda-html-to-pdf-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sejda HTML to PDF API
  slug: open-sejda-html-to-pdf-api
- collection_type: open
  name: Sejda HTML to PDF API
  slug: open-sejda
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sejda-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sejda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sejda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sejda-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sejda-pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sejda
- group: company
  title: ''
  type: Website
  url: https://www.sejda.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.sejda.com/developers
- group: commercial
  title: ''
  type: Plans
  url: plans/sejda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sejda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sejda-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sejda.com/blog/rss
created: '2026-06-25'
description: Sejda provides online and desktop tools for editing and manipulating PDF documents - merge, split, compress, convert, edit, watermark, OCR, and fill forms. Its only documented hosted REST API is the HTML-to-PDF conversion API at api.sejda.com; the broader merge/split/OCR task set is delivered through the web and desktop apps and through the open-source Sejda SDK and sejda-console (Java, AGPLv3), not a hosted task API.
finops:
- name: Sejda Finops
  service_category: Document Management
  slug: sejda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sejda.png
layout: provider
modified: '2026-06-25'
name: Sejda
nav: Providers
network: true
overview: 'Sejda publishes 1 API on the [APIs.io](https://apis.io/) network: HTML to PDF API. Tagged areas include PDF, Document Conversion, HTML to PDF, PDF Editing, and OCR.


  Sejda''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Sejda Plans Pricing
  plan_count: 9
  slug: sejda-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 3
  name: Sejda Rate Limits
  slug: sejda-rate-limits
score:
  band: thin
  composite: 39.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Sejda Authentication
  slug: sejda-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sejda Domain Security
  slug: sejda-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sejda Vulnerability Disclosure
  slug: sejda-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sejda
tags:
- PDF
- Document Conversion
- HTML to PDF
- PDF Editing
- OCR
website: https://www.sejda.com
---
