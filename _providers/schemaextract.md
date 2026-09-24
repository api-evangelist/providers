---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://schemaextract.shop
  baseurl_source: declared
  description: REST API for document-to-JSON extraction. Sync extraction via POST /v1/extract and async jobs via POST /v1/extract/jobs, plus a /health liveness endpoint. Bearer API key auth with a demo/anonymous alt
  name: SchemaExtract API
  slug: schemaextract-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/security/schemaextract-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/schemaextract-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/authentication/schemaextract-authentication.yml
  title: ''
  type: Authentication
  url: authentication/schemaextract-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://schemaextract.shop/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://schemaextract.shop/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://schemaextract.shop/pricing
- group: start
  title: ''
  type: Login
  url: https://schemaextract.shop/login
- group: operate
  title: ''
  type: Support
  url: https://schemaextract.shop/faq
- group: operate
  title: ''
  type: StatusPage
  url: https://schemaextract.shop/status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/lifecycle/schemaextract-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/schemaextract-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/errors/schemaextract-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/schemaextract-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/rate-limits/schemaextract-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/schemaextract-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/plans/schemaextract-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/schemaextract-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/sandbox/schemaextract-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/schemaextract-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/conventions/schemaextract-conventions.yml
  title: ''
  type: Conventions
  url: conventions/schemaextract-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/data-model/schemaextract-data-model.yml
  title: ''
  type: DataModel
  url: data-model/schemaextract-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/conformance/schemaextract-conformance.yml
  title: ''
  type: Conformance
  url: conformance/schemaextract-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/schemaextract/refs/heads/main/overlays/schemaextract-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/schemaextract-openapi-overlay.yaml
created: '2026-09-19'
description: A document-to-JSON extraction service. Upload a PDF or image, pick a preset or paste a JSON schema, and get typed fields back — vendor, totals, line items, packages, containers. Supports invoice, packing list, bank statement, and bill of lading presets plus custom schemas.
layout: provider
modified: '2026-09-20'
name: SchemaExtract
nav: Providers
network: true
overview: 'SchemaExtract publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Document AI, IDP, Data Extraction, PDF/OCR-to-JSON, and Invoice & AP automation.


  SchemaExtract''s developer surface includes authentication, pricing, support, sandbox, and 14 more developer resources.'
plans:
- name: Schemaextract Plans Pricing
  plan_count: 3
  slug: schemaextract-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Schemaextract Rate Limits
  slug: schemaextract-rate-limits
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 4.5
    contract_quality: 45.6
    developer_ergonomics: 51.8
    discoverability: 66.7
    operational_transparency: 47.4
  previous_composite: 45.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Schemaextract Authentication
  slug: schemaextract-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Schemaextract Domain Security
  slug: schemaextract-domain-security
  summary_line: TLSv1.3 · HSTS
slug: schemaextract
tags:
- Document AI
- IDP
- Data Extraction
- PDF/OCR-to-JSON
- Invoice & AP automation
- Logistics/freight
- Fintech
- Developer API
website: https://schemaextract.shop/
---
