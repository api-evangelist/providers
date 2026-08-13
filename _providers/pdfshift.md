---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Pdfshift Agentic Access
  operation_count: 15
  slug: pdfshift-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 8
apis:
- description: The account API from PDFShift — 1 operation(s) for account.
  name: PDFShift account API
  slug: pdfshift-account-api
- description: The Convert API from PDFShift — 4 operation(s) for convert.
  name: PDFShift Convert API
  slug: pdfshift-convert-api
- description: The credits API from PDFShift — 1 operation(s) for credits.
  name: PDFShift credits API
  slug: pdfshift-credits-api
- description: The details API from PDFShift — 1 operation(s) for details.
  name: PDFShift details API
  slug: pdfshift-details-api
- description: The Invoices API from PDFShift — 1 operation(s) for invoices.
  name: PDFShift Invoices API
  slug: pdfshift-invoices-api
- description: The Logs API from PDFShift — 2 operation(s) for logs.
  name: PDFShift Logs API
  slug: pdfshift-logs-api
- description: The templates API from PDFShift — 4 operation(s) for templates.
  name: PDFShift templates API
  slug: pdfshift-templates-api
- description: The usage API from PDFShift — 1 operation(s) for usage.
  name: PDFShift usage API
  slug: pdfshift-usage-api
artifact_total: 39
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdfshift-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pdfshift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdfshift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pdfshift-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pdfshift.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pdfshift.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pdfshift
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pdfshift-io
- group: company
  title: ''
  type: Blog
  url: https://pdfshift.io/guides/
- group: commercial
  title: ''
  type: Pricing
  url: https://pdfshift.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pdfshift.io/
- group: other
  title: ''
  type: X
  url: https://x.com/pdfshift
- group: commercial
  title: ''
  type: Plans
  url: plans/pdfshift-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdfshift-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdfshift-finops.yml
created: '2026-06-13'
description: PDFShift is an HTML to PDF conversion REST API that generates pixel-perfect PDFs from HTML and CSS using Chromium rendering. It supports custom headers, footers, watermarks, password protection, JavaScript execution, screenshot capture, webhook notifications, and direct export to Amazon S3 and Google Cloud Storage.
finops:
- name: Pdfshift Finops
  service_category: ''
  slug: pdfshift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdfshift.png
json_schemas:
- name: Account
  property_count: 2
  slug: account
- name: BasicAuthForm
  property_count: 2
  slug: basicauthform
- name: ConvertForm
  property_count: 23
  slug: convertform
- name: CookieForm
  property_count: 4
  slug: cookieform
- name: Credits
  property_count: 2
  slug: credits
- name: CustomHeaderFooter
  property_count: 3
  slug: customheaderfooter
- name: Error
  property_count: 3
  slug: error
- name: Errors
  property_count: 3
  slug: errors
- name: ImageConvertForm
  property_count: 7
  slug: imageconvertform
- name: Invoices
  property_count: 2
  slug: invoices
- name: Log
  property_count: 2
  slug: log
- name: LogObject
  property_count: 11
  slug: logobject
- name: Logs
  property_count: 2
  slug: logs
- name: MarginForm
  property_count: 4
  slug: marginform
- name: ProtectionForm
  property_count: 6
  slug: protectionform
- name: Template
  property_count: 2
  slug: template
- name: TemplateCreateForm
  property_count: 3
  slug: templatecreateform
- name: Templates
  property_count: 2
  slug: templates
- name: TemplateUpdateForm
  property_count: 2
  slug: templateupdateform
- name: WatermarkForm
  property_count: 12
  slug: watermarkform
- name: WebhookForm
  property_count: 4
  slug: webhookform
jsonld:
- class_count: 0
  name: Pdfshift Api Context
  property_count: 0
  slug: pdfshift-api
- class_count: 26
  name: Pdfshift Context
  property_count: 2
  slug: pdfshift-context
layout: provider
modified: '2026-06-13'
name: PDFShift
nav: Providers
network: true
overview: 'PDFShift publishes 8 APIs on the [APIs.io](https://apis.io/) network, including account API, Convert API, credits API, and 5 more. Tagged areas include PDF, HTML to PDF, Document Conversion, Screenshot, and Chromium.


  The PDFShift catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  PDFShift''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Pdfshift Plans Pricing
  plan_count: 5
  slug: pdfshift-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Pdfshift Rate Limits
  slug: pdfshift-rate-limits
rules:
- name: PDFShift API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pdfshift-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdfshift/refs/heads/main/screenshots/pdfshift-2026-06-20T191519.png
security:
- kind: authentication
  name: Pdfshift Authentication
  slug: pdfshift-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pdfshift Domain Security
  slug: pdfshift-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pdfshift Vulnerability Disclosure
  slug: pdfshift-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pdfshift
tags:
- PDF
- HTML to PDF
- Document Conversion
- Screenshot
- Chromium
- REST API
website: https://pdfshift.io/
---
