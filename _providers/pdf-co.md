---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 61
  human_in_the_loop: 0
  name: Pdf Co Agentic Access
  operation_count: 68
  slug: pdf-co-agentic-access
  summary_line: 68 operations · 61 acting
api_count: 1
apis:
- description: The Barcodes API from PDF.co — 2 operation(s) for barcodes.
  name: PDF.co Barcodes API
  slug: pdf-co-barcodes-api
- description: The Document, File & System API from PDF.co — 17 operation(s) for document, file & system.
  name: PDF.co Document, File & System API
  slug: pdf-co-document-file-system-api
- description: The Editing API from PDF.co — 4 operation(s) for editing.
  name: PDF.co Editing API
  slug: pdf-co-editing-api
- description: The Excel Conversion API from PDF.co — 6 operation(s) for excel conversion.
  name: PDF.co Excel Conversion API
  slug: pdf-co-excel-conversion-api
- description: The Extraction API from PDF.co — 5 operation(s) for extraction.
  name: PDF.co Extraction API
  slug: pdf-co-extraction-api
- description: The Find & Search API from PDF.co — 4 operation(s) for find & search.
  name: PDF.co Find & Search API
  slug: pdf-co-find-search-api
- description: The Forms API from PDF.co — 1 operation(s) for forms.
  name: PDF.co Forms API
  slug: pdf-co-forms-api
- description: The Pages API from PDF.co — 3 operation(s) for pages.
  name: PDF.co Pages API
  slug: pdf-co-pages-api
- description: The PDF Conversion API from PDF.co — 21 operation(s) for pdf conversion.
  name: PDF.co PDF Conversion API
  slug: pdf-co-pdf-conversion-api
- description: The PDF Merging & Splitting API from PDF.co — 4 operation(s) for pdf merging & splitting.
  name: PDF.co PDF Merging & Splitting API
  slug: pdf-co-pdf-merging-splitting-api
artifact_total: 46
collections:
- collection_type: postman
  name: PDF.co Barcodes API
  slug: postman-pdf-co-barcodes-api
- collection_type: postman
  name: PDF.co Barcodes Document, File & System API
  slug: postman-pdf-co-document-file-system-api
- collection_type: postman
  name: PDF.co Barcodes Editing API
  slug: postman-pdf-co-editing-api
- collection_type: postman
  name: PDF.co Barcodes Excel Conversion API
  slug: postman-pdf-co-excel-conversion-api
- collection_type: postman
  name: PDF.co Barcodes Extraction API
  slug: postman-pdf-co-extraction-api
- collection_type: postman
  name: PDF.co Barcodes Find & Search API
  slug: postman-pdf-co-find-search-api
- collection_type: postman
  name: PDF.co Barcodes Forms API
  slug: postman-pdf-co-forms-api
- collection_type: postman
  name: PDF.co Barcodes Pages API
  slug: postman-pdf-co-pages-api
- collection_type: postman
  name: PDF.co Barcodes PDF Conversion API
  slug: postman-pdf-co-pdf-conversion-api
- collection_type: postman
  name: PDF.co Barcodes PDF Merging & Splitting API
  slug: postman-pdf-co-pdf-merging-splitting-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PDF.co Barcodes API
  slug: open-pdf-co-barcodes-api
- collection_type: open
  name: PDF.co Barcodes Document, File & System API
  slug: open-pdf-co-document-file-system-api
- collection_type: open
  name: PDF.co Barcodes Editing API
  slug: open-pdf-co-editing-api
- collection_type: open
  name: PDF.co Barcodes Excel Conversion API
  slug: open-pdf-co-excel-conversion-api
- collection_type: open
  name: PDF.co Barcodes Extraction API
  slug: open-pdf-co-extraction-api
- collection_type: open
  name: PDF.co Barcodes Find & Search API
  slug: open-pdf-co-find-search-api
- collection_type: open
  name: PDF.co Barcodes Forms API
  slug: open-pdf-co-forms-api
- collection_type: open
  name: PDF.co Barcodes Pages API
  slug: open-pdf-co-pages-api
- collection_type: open
  name: PDF.co Barcodes PDF Conversion API
  slug: open-pdf-co-pdf-conversion-api
- collection_type: open
  name: PDF.co Barcodes PDF Merging & Splitting API
  slug: open-pdf-co-pdf-merging-splitting-api
- collection_type: open
  name: PDF.co API
  slug: open-pdf-co
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pdfco/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdf-co-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pdf-co-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdf-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pdf-co-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://pdf.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pdf.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pdf.co/api-reference
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.pdf.co/openapi.json
- group: start
  title: ''
  type: Signup
  url: https://app.pdf.co/signup
- group: start
  title: ''
  type: Login
  url: https://app.pdf.co/account/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://pdf.co/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.pdf.co/en
- group: docs
  title: ''
  type: Documentation
  url: https://pdf.co/integrations
- group: build
  title: ''
  type: GitHub
  url: https://github.com/pdfdotco
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pdfdotco/pdf-co-api-samples
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pdfdotco/pdfco-mcp
- group: build
  title: ''
  type: Plugin
  url: https://github.com/pdfdotco/n8n-nodes-pdfco
- group: company
  title: ''
  type: Blog
  url: https://pdf.co/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://pdf.co/tutorials
- group: auth
  title: ''
  type: Security
  url: https://docs.pdf.co/knowledgebase/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pdf.co/terms
- group: commercial
  title: ''
  type: Privacy
  url: https://pdf.co/privacy
- group: auth
  title: ''
  type: Authentication
  url: https://docs.pdf.co/api-reference/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://docs.pdf.co/glossary/webhook-and-callbacks
- group: company
  title: ''
  type: About
  url: https://pdf.co/about
- group: commercial
  title: ''
  type: Plans
  url: plans/pdf-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdf-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdf-co-finops.yml
created: '2026-05-25'
examples:
- key_count: 2
  name: Pdf Co Ai Invoice Parser Example
  slug: pdf-co-ai-invoice-parser-example
- key_count: 2
  name: Pdf Co Pdf To Json Example
  slug: pdf-co-pdf-to-json-example
finops:
- name: Pdf Co Finops
  service_category: Document Automation and OCR
  slug: pdf-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdf-co.png
json_schemas:
- name: PDF.co AI Invoice Parser Request
  property_count: 7
  slug: pdf-co-ai-invoice-parser
- name: PDF.co Document Parser Request
  property_count: 12
  slug: pdf-co-document-parser
- name: PDF.co Job Status
  property_count: 8
  slug: pdf-co-job-status
jsonld:
- class_count: 0
  name: Pdf Co Context
  property_count: 9
  slug: pdf-co-context
layout: provider
modified: '2026-05-25'
name: PDF.co
nav: Providers
network: true
overview: 'PDF.co publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Barcodes API, Document, File & System API, Editing API, and 7 more. Tagged areas include PDF, Document Automation, Artificial Intelligence, OCR, and Invoice Parsing.


  The PDF.co catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PDF.co''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, support, GitHub presence, and 22 more developer resources.'
plans:
- name: Pdf Co Plans Pricing
  plan_count: 7
  slug: pdf-co-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Pdf Co Rate Limits
  slug: pdf-co-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: PDF.co API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: pdf-co-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 9.8
    contract_quality: 65.5
    developer_ergonomics: 42.9
    discoverability: 44.4
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdf-co/refs/heads/main/screenshots/pdf-co-2026-06-20T191516.png
security:
- kind: authentication
  name: Pdf Co Authentication
  slug: pdf-co-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pdf Co Domain Security
  slug: pdf-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pdf Co Trust Center
  slug: pdf-co-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: pdf-co
tags:
- PDF
- Document Automation
- Artificial Intelligence
- OCR
- Invoice Parsing
- Document Parsing
- Conversion
- Forms
- Barcodes
- E-Signature
website: https://pdf.co
---
