---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.parseforme.com/v1
  baseurl_source: declared
  description: The webhooks API from ParseForMe — 4 operation(s) for webhooks.
  name: ParseForMe Webhooks API
  slug: parseforme-webhooks-api
- baseURL: https://api.parseforme.com/v1
  baseurl_source: declared
  description: The Document Types API from ParseForMe — 1 operation(s) for document types.
  name: ParseForMe Document Types API
  slug: parseforme-document-types-api
- baseURL: https://api.parseforme.com/v1
  baseurl_source: declared
  description: The Documents API from ParseForMe — 3 operation(s) for documents.
  name: ParseForMe Documents API
  slug: parseforme-documents-api
- baseURL: https://api.parseforme.com/v1
  baseurl_source: declared
  description: The Me API from ParseForMe — 1 operation(s) for me.
  name: ParseForMe Me API
  slug: parseforme-me-api
- baseURL: https://api.parseforme.com/v1
  baseurl_source: declared
  description: The Meta API from ParseForMe — 1 operation(s) for meta.
  name: ParseForMe Meta API
  slug: parseforme-meta-api
artifact_total: 16
asyncapis:
- description: ''
  name: Parseforme Webhooks
  slug: parseforme-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.parseforme.com/
- group: auth
  href: https://artifacts.apis.io/parseforme/security/parseforme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parseforme-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/parseforme/authentication/parseforme-authentication.yml
  title: ''
  type: Authentication
  url: authentication/parseforme-authentication.yml
- group: agent
  href: https://artifacts.apis.io/parseforme/well-known/parseforme-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/parseforme-well-known.yml
- group: agent
  href: https://artifacts.apis.io/parseforme/llms/parseforme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parseforme-llms.txt
- group: build
  href: https://artifacts.apis.io/parseforme/packages/parseforme-packages.yml
  title: ''
  type: Packages
  url: packages/parseforme-packages.yml
- group: other
  href: https://artifacts.apis.io/parseforme/overlays/parseforme-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/parseforme-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/parseforme/conformance/parseforme-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parseforme-conformance.yml
- group: design
  href: https://artifacts.apis.io/parseforme/errors/parseforme-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/parseforme-problem-types.yml
- group: design
  href: https://artifacts.apis.io/parseforme/lifecycle/parseforme-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/parseforme-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/parseforme/conventions/parseforme-conventions.yml
  title: ''
  type: Conventions
  url: conventions/parseforme-conventions.yml
- group: design
  href: https://artifacts.apis.io/parseforme/conventions/parseforme-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/parseforme-conventions.yml
- group: design
  href: https://artifacts.apis.io/parseforme/data-model/parseforme-data-model.yml
  title: ''
  type: DataModel
  url: data-model/parseforme-data-model.yml
- group: design
  href: https://artifacts.apis.io/parseforme/asyncapi/parseforme-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/parseforme-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/parseforme/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/parseforme/sandbox/parseforme-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/parseforme-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/parseforme/plans/parseforme-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/parseforme-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/parseforme/rate-limits/parseforme-rate-limits.yml
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
finops:
- has_sources: true
  method: derived
  name: Parseforme Finops
  primary_unit: tokens (1 token = 1 page)
  service_category: ''
  slug: parseforme-finops
  template: false
image: https://parseforme.com/opengraph-image.png
layout: provider
modified: '2026-09-03'
name: ParseForMe
nav: Providers
network: true
overview: 'ParseForMe publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks API, Document Types API, Documents API, and 2 more. Tagged areas include Document Parsing, OCR, Data Extraction, Document AI, and Intelligent Document Processing.


  The ParseForMe catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ParseForMe''s developer surface includes authentication, sandbox, pricing, signup flow, engineering blog, support, and 19 more developer resources.'
plans:
- name: Parseforme Plans Pricing
  plan_count: 4
  slug: parseforme-plans-pricing
- name: Parseforme Price Estimates
  plan_count: 0
  slug: parseforme-price-estimates
random_paper: 20
rate_limits:
- limit_count: 5
  name: Parseforme Rate Limits
  slug: parseforme-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: ParseForMe API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: parseforme-rules
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 57.4
    developer_ergonomics: 44.6
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 52.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 19.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/parseforme/parseforme-2026-10-11T112357.png
security:
- kind: authentication
  name: Parseforme Authentication
  slug: parseforme-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Parseforme Domain Security
  slug: parseforme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Parse a document and read back its fields
  slug: parseforme-parse-a-document
- name: Poll for parsed documents and export them
  slug: parseforme-poll-and-export
- name: Receive parse results by webhook
  slug: parseforme-receive-webhooks
slug: parseforme
tags:
- Document Parsing
- OCR
- Data Extraction
- Document AI
- Intelligent Document Processing
- Invoices
- Bank Statements
- Receipts
- Resume
- PDF
- Webhook
- REST
website: https://www.parseforme.com/
---
