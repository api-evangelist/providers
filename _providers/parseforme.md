---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Document parsing REST API that converts documents into structured, confidence-scored fields, with exports and HMAC-signed webhooks. Bearer-token (pfm_live_ workspace key) auth.
  name: ParseForMe API
  slug: parseforme-api
artifact_total: 6
asyncapis:
- description: ''
  name: Parseforme Webhooks
  slug: parseforme-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parseforme-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parseforme-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parseforme-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parseforme-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/parseforme-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/parseforme-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/parseforme-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parseforme-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parseforme-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parseforme-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/parseforme-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parseforme-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/parseforme-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/parseforme-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/parseforme-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parseforme-rate-limits.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://parseforme.com/robots.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://parseforme.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://parseforme.com/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parseforme.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parseforme.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://parseforme.com/blog
- group: operate
  title: ''
  type: Support
  url: https://parseforme.com/contact
created: '2026-09-03'
description: A document-parsing / intelligent-document-processing service that converts PDFs, scans and photos (invoices, bank statements, receipts, resumes, purchase orders, shipping docs, utility bills, payslips) into typed, confidence-scored fields, exportable to JSON/CSV/XLSX/Google Sheets or driven via REST.
image: https://parseforme.com/opengraph-image.png
layout: provider
modified: '2026-09-03'
name: ParseForMe
nav: Providers
network: true
overview: 'ParseForMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Document Parsing, OCR, Data Extraction, Document AI, and IDP.


  The ParseForMe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ParseForMe''s developer surface includes authentication, sandbox, pricing, signup flow, engineering blog, support, and 18 more developer resources.'
plans:
- name: Parseforme Plans Pricing
  plan_count: 3
  slug: parseforme-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Parseforme Rate Limits
  slug: parseforme-rate-limits
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 39.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
security:
- kind: authentication
  name: Parseforme Authentication
  slug: parseforme-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Parseforme Domain Security
  slug: parseforme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parseforme
tags:
- Document Parsing
- OCR
- Data Extraction
- Document AI
- IDP
- Invoices
- Bank Statements
- Receipts
- Resumes
- PDF
- Webhooks
- REST
---
