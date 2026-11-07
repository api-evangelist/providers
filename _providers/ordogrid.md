---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Ordogrid Agentic Access
  operation_count: 79
  slug: ordogrid-agentic-access
  summary_line: 79 operations · 39 acting
api_count: 1
apis:
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: Company-scoped customer records used as document recipients.
  name: OrdoGrid Clients API
  slug: ordogrid-clients-api
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: Legal credit notes linked to an existing or externally issued invoice.
  name: OrdoGrid Credit Notes API
  slug: ordogrid-credit-notes-api
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: Loyalty programs, members, balances, ledger, rewards and cards.
  name: OrdoGrid Fidelity API
  slug: ordogrid-fidelity-api
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: Invoice creation, recovery, lifecycle and PDF documents.
  name: OrdoGrid Invoices API
  slug: ordogrid-invoices-api
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: API identity, capabilities, scope catalogue and public specification.
  name: OrdoGrid Meta API
  slug: ordogrid-meta-api
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: Confirmed financial movements, reversals, refunds and settlement history.
  name: OrdoGrid Payments API
  slug: ordogrid-payments-api
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: UBL transmission, exchanged archives, inbox and participant directory.
  name: OrdoGrid Peppol API
  slug: ordogrid-peppol-api
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: Quote creation, recovery, lifecycle and PDF documents.
  name: OrdoGrid Quotes API
  slug: ordogrid-quotes-api
- baseURL: https://ordogrid.com/api/v1
  baseurl_source: declared
  description: Paid-on-the-spot receipt documents and their payment details.
  name: OrdoGrid Receipts API
  slug: ordogrid-receipts-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/ordogrid/agentic-access/ordogrid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ordogrid-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ordogrid/plans/ordogrid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ordogrid-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ordogrid/rules/ordogrid-rules.yml
  title: ''
  type: Spectral
  url: rules/ordogrid-rules.yml
- group: design
  href: https://artifacts.apis.io/ordogrid/json-ld/ordogrid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ordogrid-context.jsonld
- group: design
  href: https://artifacts.apis.io/ordogrid/vocabulary/ordogrid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ordogrid-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ordogrid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ordogrid/data-model/ordogrid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ordogrid-data-model.yml
- group: design
  href: https://artifacts.apis.io/ordogrid/conventions/ordogrid-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ordogrid-conventions.yml
- group: design
  href: https://artifacts.apis.io/ordogrid/conventions/ordogrid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ordogrid-conventions.yml
- group: design
  href: https://artifacts.apis.io/ordogrid/errors/ordogrid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ordogrid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ordogrid/conformance/ordogrid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ordogrid-conformance.yml
- group: other
  href: https://artifacts.apis.io/ordogrid/hosts/ordogrid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ordogrid-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://ordogrid.com/login
- group: auth
  href: https://artifacts.apis.io/ordogrid/authentication/ordogrid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ordogrid-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ordogrid/security/ordogrid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ordogrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ordogrid.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://ordogrid.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://ordogrid.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ordogrid.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ordogrid.com/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://ordogrid.com/en/help
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://ordogrid.com/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: OrdoGrid provides a cloud‑based invoicing and business document platform tailored for Belgian companies. It supports Peppol e‑invoicing, allowing unlimited incoming invoices and a limited number of outgoing invoices on its free forever plan. The service also includes project management tools, quote generation, and compliance features for Belgian e‑reporting regulations. Designed as a SaaS solution, OrdoGrid aims to simplify financial workflows for small and medium enterprises in Belgium.
image: https://ordogrid.com/social-image/en
json_schemas:
- name: CreditNoteCreate
  property_count: 19
  slug: ordogrid-credit-note-create
- name: CreditNoteUpdate
  property_count: 17
  slug: ordogrid-credit-note-update
- name: Document
  property_count: 35
  slug: ordogrid-document
- name: InvoiceCreate
  property_count: 18
  slug: ordogrid-invoice-create
- name: QuoteCreate
  property_count: 17
  slug: ordogrid-quote-create
- name: ReceiptCreate
  property_count: 19
  slug: ordogrid-receipt-create
jsonld:
- class_count: 89
  name: Ordogrid Context
  property_count: 222
  slug: ordogrid-context
layout: provider
modified: '2026-11-02'
name: OrdoGrid
nav: Providers
network: true
overview: 'OrdoGrid publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clients API, Credit Notes API, Fidelity API, and 6 more. Tagged areas include Invoicing, PEPPOL, Belgium, Software-as-a-Service, and business-documents.


  The OrdoGrid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OrdoGrid''s developer surface includes authentication, documentation, pricing, support, and 17 more developer resources.'
plans:
- name: Ordogrid Plans Pricing
  plan_count: 3
  slug: ordogrid-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Ordogrid Rate Limits
  slug: ordogrid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: OrdoGrid API Rules
  rule_count: 63
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 12
  slug: ordogrid-rules
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 63.4
    developer_ergonomics: 25.5
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ordogrid Authentication
  slug: ordogrid-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ordogrid Domain Security
  slug: ordogrid-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: ordogrid-client-management
  slug: ordogrid-client-management
slug: ordogrid
tags:
- Invoicing
- PEPPOL
- Belgium
- Software-as-a-Service
- business-documents
website: https://ordogrid.com/en
---
