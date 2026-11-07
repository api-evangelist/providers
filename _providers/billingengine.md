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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Billingengine Agentic Access
  operation_count: 12
  slug: billingengine-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- baseURL: https://www.billingengine.com/api/v1
  baseurl_source: declared
  description: Customers of the account.
  name: BillingEngine Customers API
  slug: billingengine-customers-api
- baseURL: https://www.billingengine.com/api/v1
  baseurl_source: declared
  description: Invoices, created as drafts, and their PDF and XML e-invoice downloads.
  name: BillingEngine Invoices API
  slug: billingengine-invoices-api
- baseURL: https://www.billingengine.com/api/v1
  baseurl_source: declared
  description: Payments received for sent invoices.
  name: BillingEngine Payments API
  slug: billingengine-payments-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/billingengine/agentic-access/billingengine-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/billingengine-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/billingengine/plans/billingengine-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/billingengine-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/billingengine/rules/billingengine-rules.yml
  title: ''
  type: Spectral
  url: rules/billingengine-rules.yml
- group: design
  href: https://artifacts.apis.io/billingengine/json-ld/billingengine-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/billingengine-context.jsonld
- group: design
  href: https://artifacts.apis.io/billingengine/vocabulary/billingengine-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/billingengine-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/billingengine/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/billingengine/data-model/billingengine-data-model.yml
  title: ''
  type: DataModel
  url: data-model/billingengine-data-model.yml
- group: design
  href: https://artifacts.apis.io/billingengine/errors/billingengine-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/billingengine-problem-types.yml
- group: design
  href: https://artifacts.apis.io/billingengine/conformance/billingengine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billingengine-conformance.yml
- group: agent
  href: https://artifacts.apis.io/billingengine/llms/billingengine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billingengine-llms.txt
- group: agent
  href: https://artifacts.apis.io/billingengine/mcp/billingengine-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/billingengine-mcp.yml
- group: other
  href: https://artifacts.apis.io/billingengine/hosts/billingengine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billingengine-hosts.yml
- group: other
  href: https://artifacts.apis.io/billingengine/vendors/billingengine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billingengine-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.billingengine.com/de/terms_of_service
- group: operate
  title: ''
  type: Support
  url: https://www.billingengine.com/de/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.billingengine.com/de/privacy_notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.billingengine.com/de/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.billingengine.com/de/news
- group: other
  title: ''
  type: Leadership
  url: https://www.billingengine.com/de/team
- group: company
  title: ''
  type: Blog
  url: https://www.billingengine.com/de/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/billingengine
- group: auth
  href: https://artifacts.apis.io/billingengine/authentication/billingengine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/billingengine-authentication.yml
- group: auth
  href: https://artifacts.apis.io/billingengine/security/billingengine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billingengine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billingengine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.billingengine.com/en/api
created: '2026-10-19'
description: BillingEngine provides online invoicing software tailored for freelancers and small businesses in Germany. Its REST API enables listing, creating, and updating customers and draft invoices, recording payments, and downloading invoices as PDF or XML e‑invoices (ZUGFeRD / XRechnung, EN 16931). The platform also offers an MCP server for AI assistants, requiring an API key from a paid plan.
json_schemas:
- name: Customer
  property_count: 11
  slug: billingengine-customer
- name: InvoiceDetail
  property_count: 24
  slug: billingengine-invoice-detail
- name: InvoiceInput
  property_count: 9
  slug: billingengine-invoice-input
- name: Invoice
  property_count: 16
  slug: billingengine-invoice
- name: PaymentInput
  property_count: 4
  slug: billingengine-payment-input
- name: Payment
  property_count: 9
  slug: billingengine-payment
jsonld:
- class_count: 12
  name: Billingengine Context
  property_count: 53
  slug: billingengine-context
layout: provider
mcp_servers:
- description: ''
  name: BillingEngine MCP Server
  slug: billingengine-mcp-yml
modified: '2026-10-19'
name: BillingEngine
nav: Providers
network: true
overview: 'BillingEngine publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Customers API, Invoices API, and Payments API. Tagged areas include Invoicing, Fintech, Germany, and Small Business.


  The BillingEngine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BillingEngine''s developer surface includes support, pricing, engineering blog, authentication, documentation, and 20 more developer resources.'
plans:
- name: Billingengine Plans Pricing
  plan_count: 3
  slug: billingengine-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: BillingEngine API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: billingengine-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 65.6
    developer_ergonomics: 22.0
    discoverability: 61.7
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/billingengine/billingengine-2026-11-03T121725.png
security:
- kind: authentication
  name: Billingengine Authentication
  slug: billingengine-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Billingengine Domain Security
  slug: billingengine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: billingengine-create-invoice
  slug: billingengine-create-invoice
- name: billingengine-record-and-list-payments
  slug: billingengine-record-and-list-payments
slug: billingengine
tags:
- Invoicing
- Fintech
- Germany
- Small Business
website: https://www.billingengine.com/
---
