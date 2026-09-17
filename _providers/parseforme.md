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
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://api.parseforme.com/v1
  baseurl_source: declared
  description: The v1 API from ParseForMe — 6 operation(s) for v1.
  name: ParseForMe V1 API
  slug: parseforme-v1-api
- baseURL: https://api.parseforme.com/v1
  baseurl_source: declared
  description: The webhooks API from ParseForMe — 4 operation(s) for webhooks.
  name: ParseForMe Webhooks API
  slug: parseforme-webhooks-api
artifact_total: 7
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
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/security/parseforme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parseforme-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/authentication/parseforme-authentication.yml
  title: ''
  type: Authentication
  url: authentication/parseforme-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/well-known/parseforme-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/parseforme-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/llms/parseforme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parseforme-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/packages/parseforme-packages.yml
  title: ''
  type: Packages
  url: packages/parseforme-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/overlays/parseforme-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/parseforme-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/conformance/parseforme-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parseforme-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/errors/parseforme-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/parseforme-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/lifecycle/parseforme-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/parseforme-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/conventions/parseforme-conventions.yml
  title: ''
  type: Conventions
  url: conventions/parseforme-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/conventions/parseforme-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/parseforme-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/data-model/parseforme-data-model.yml
  title: ''
  type: DataModel
  url: data-model/parseforme-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/asyncapi/parseforme-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/parseforme-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/sandbox/parseforme-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/parseforme-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/plans/parseforme-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/parseforme-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/parseforme/refs/heads/main/rate-limits/parseforme-rate-limits.yml
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
overview: 'ParseForMe publishes 2 APIs on the [APIs.io](https://apis.io/) network: V1 API and Webhooks API. Tagged areas include Document Parsing, OCR, Data Extraction, Document AI, and IDP.


  The ParseForMe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ParseForMe''s developer surface includes authentication, sandbox, pricing, signup flow, engineering blog, support, and 19 more developer resources.'
plans:
- name: Parseforme Plans Pricing
  plan_count: 3
  slug: parseforme-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Parseforme Rate Limits
  slug: parseforme-rate-limits
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 59.1
    developer_ergonomics: 44.6
    discoverability: 75.9
    operational_transparency: 39.5
  previous_composite: 47.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Resume
- PDF
- Webhook
- REST
website: https://www.parseforme.com/
---
