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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Mathpix Agentic Access
  operation_count: 8
  slug: mathpix-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 7
apis:
- description: Recognize handwritten math, text, and chemistry from raw stroke coordinates (x/y arrays) via v3/strokes. Pairs with the App Tokens API and strokes_session_id for client-side digital-ink capture in bro
  name: Mathpix Strokes API
  slug: mathpix-strokes-api
- description: Mint short-lived client-side app_token credentials (30 seconds to 12 hours; 5 minutes by default) so browsers, mobile clients, and digital-ink surfaces can call Mathpix without exposing the long-lived
  name: Mathpix App Tokens API
  slug: mathpix-app-tokens-api
- description: Process multiple images in one request.
  name: Mathpix Batches API
  slug: mathpix-batches-api
- description: Convert Mathpix Markdown into export formats.
  name: Mathpix Conversions API
  slug: mathpix-conversions-api
- description: Process a single image for STEM OCR.
  name: Mathpix Images API
  slug: mathpix-images-api
- description: Inspect OCR consumption.
  name: Mathpix Usage API
  slug: mathpix-usage-api
- description: Submit, monitor, and retrieve document OCR jobs.
  name: Mathpix Documents API
  slug: mathpix-documents-api
artifact_total: 41
collections:
- collection_type: postman
  name: Mathpix App Tokens API
  slug: postman-mathpix-app-tokens-api
- collection_type: postman
  name: Mathpix App Tokens Batches API
  slug: postman-mathpix-batches-api
- collection_type: postman
  name: Mathpix App Tokens Conversions API
  slug: postman-mathpix-conversions-api
- collection_type: postman
  name: Mathpix App Tokens Images API
  slug: postman-mathpix-images-api
- collection_type: postman
  name: Mathpix App Tokens Strokes API
  slug: postman-mathpix-strokes-api
- collection_type: postman
  name: Mathpix App Tokens Usage API
  slug: postman-mathpix-usage-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mathpix App Tokens API
  slug: open-mathpix-app-tokens-api
- collection_type: open
  name: Mathpix Batch API
  slug: open-mathpix-batch-api
- collection_type: open
  name: Mathpix App Tokens Batches API
  slug: open-mathpix-batches-api
- collection_type: open
  name: Mathpix App Tokens Conversions API
  slug: open-mathpix-conversions-api
- collection_type: open
  name: Mathpix Convert API
  slug: open-mathpix-convert-api
- collection_type: open
  name: Mathpix Document OCR Documents API
  slug: open-mathpix-documents-api
- collection_type: open
  name: Mathpix Image OCR API
  slug: open-mathpix-image-ocr-api
- collection_type: open
  name: Mathpix App Tokens Images API
  slug: open-mathpix-images-api
- collection_type: open
  name: Mathpix OCR Usage API
  slug: open-mathpix-ocr-usage-api
- collection_type: open
  name: Mathpix App Tokens Strokes API
  slug: open-mathpix-strokes-api
- collection_type: open
  name: Mathpix App Tokens Usage API
  slug: open-mathpix-usage-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mathpix/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mathpix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mathpix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mathpix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mathpix
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MathpixApp
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Mathpix
- group: start
  title: ''
  type: Portal
  url: https://docs.mathpix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mathpix.com/reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mathpix.com/guides/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://mathpix.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://accounts.mathpix.com/signup
- group: start
  title: ''
  type: Login
  url: https://accounts.mathpix.com/login
- group: start
  title: ''
  type: Console
  url: https://console.mathpix.com
- group: company
  title: ''
  type: Blog
  url: https://mathpix.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@mathpix.com
- group: operate
  title: ''
  type: ContactSales
  url: https://mathpix.com/contact-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mathpix.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mathpix.com/privacy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Mathpix/mpxpy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Mathpix/ios-client
- group: build
  title: ''
  type: CLI
  url: https://github.com/Mathpix/mpx-cli
- group: build
  title: ''
  type: Samples
  url: https://github.com/Mathpix/api-examples
- group: build
  title: ''
  type: Tools
  url: https://github.com/Mathpix/mathpix-markdown-it
- group: build
  title: ''
  type: Tools
  url: https://github.com/Mathpix/vscode-mathpix-markdown
- group: build
  title: ''
  type: Tools
  url: https://github.com/Mathpix/PDF_Accessibility
- group: other
  title: ''
  type: Application
  url: https://snip.mathpix.com
- group: other
  title: ''
  type: Application
  url: https://snip.mathpix.com/download
- group: other
  title: ''
  type: Application
  url: https://chromewebstore.google.com/detail/mathpix-snipping-tool/
- group: commercial
  title: ''
  type: Plans
  url: plans/mathpix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mathpix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mathpix-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mathpix-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/mathpix-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mathpix-context.jsonld
created: '2026-05-25'
examples:
- key_count: 7
  name: Mathpix Batch Example
  slug: mathpix-batch-example
- key_count: 7
  name: Mathpix Convert Markdown Example
  slug: mathpix-convert-markdown-example
- key_count: 8
  name: Mathpix Process Document Example
  slug: mathpix-process-document-example
- key_count: 6
  name: Mathpix Process Image Example
  slug: mathpix-process-image-example
- key_count: 6
  name: Mathpix Strokes Example
  slug: mathpix-strokes-example
finops:
- name: Mathpix Finops
  service_category: AI and Machine Learning
  slug: mathpix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mathpix.png
json_schemas:
- name: Mathpix Document OCR Job
  property_count: 0
  slug: mathpix-document-result
- name: Mathpix Image OCR Result
  property_count: 17
  slug: mathpix-image-result
jsonld:
- class_count: 0
  name: Mathpix Context
  property_count: 8
  slug: mathpix-context
layout: provider
modified: '2026-05-25'
name: Mathpix
nav: Providers
network: true
overview: 'Mathpix publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Strokes API, App Tokens API, Batches API, and 4 more. Tagged areas include OCR, STEM, Math, Chemistry, and Document Conversion.


  The Mathpix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mathpix''s developer surface includes authentication, GitHub presence, developer portal, documentation, pricing, signup flow, developer console, and 28 more developer resources.'
plans:
- name: Mathpix Plans Pricing
  plan_count: 4
  slug: mathpix-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 7
  name: Mathpix Rate Limits
  slug: mathpix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Mathpix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mathpix-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Mathpix API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: mathpix-rules
score:
  band: strong
  composite: 55.6
  delta: -8.5
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 25.0
    contract_quality: 64.1
    developer_ergonomics: 64.3
    discoverability: 55.6
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 64.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mathpix/refs/heads/main/screenshots/mathpix-2026-06-20T185033.png
security:
- kind: authentication
  name: Mathpix Authentication
  slug: mathpix-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mathpix Domain Security
  slug: mathpix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mathpix
tags:
- OCR
- STEM
- Math
- Chemistry
- Document Conversion
- PDF
- LaTeX
- Handwriting
- AI
- Machine Learning
website: https://docs.mathpix.com
---
