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
  - '{''url'': ''https://www.simplelegal.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.onit.com/products/elm/simplelegal/ — a different registrable domain (simplelegal.com -> onit.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Simplelegal Agentic Access
  operation_count: 17
  slug: simplelegal-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- baseURL: https://app.simplelegal.com/api
  baseurl_source: declared
  description: The Cost Codes API from SimpleLegal — 1 operation(s) for cost codes.
  name: SimpleLegal Cost Codes API
  slug: simplelegal-cost-codes-api
- baseURL: https://app.simplelegal.com/api
  baseurl_source: declared
  description: The Invoices API from SimpleLegal — 2 operation(s) for invoices.
  name: SimpleLegal Invoices API
  slug: simplelegal-invoices-api
- baseURL: https://app.simplelegal.com/api
  baseurl_source: declared
  description: The Matters API from SimpleLegal — 2 operation(s) for matters.
  name: SimpleLegal Matters API
  slug: simplelegal-matters-api
- baseURL: https://app.simplelegal.com/api
  baseurl_source: declared
  description: The Payments API from SimpleLegal — 1 operation(s) for payments.
  name: SimpleLegal Payments API
  slug: simplelegal-payments-api
- baseURL: https://app.simplelegal.com/api
  baseurl_source: declared
  description: The Users API from SimpleLegal — 1 operation(s) for users.
  name: SimpleLegal Users API
  slug: simplelegal-users-api
- baseURL: https://app.simplelegal.com/api
  baseurl_source: declared
  description: The Vendors API from SimpleLegal — 2 operation(s) for vendors.
  name: SimpleLegal Vendors API
  slug: simplelegal-vendors-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SimpleLegal Cost Codes API
  slug: open-simplelegal-cost-codes-api
- collection_type: open
  name: SimpleLegal Cost Codes Invoices API
  slug: open-simplelegal-invoices-api
- collection_type: open
  name: SimpleLegal Cost Codes Matters API
  slug: open-simplelegal-matters-api
- collection_type: open
  name: SimpleLegal Cost Codes Payments API
  slug: open-simplelegal-payments-api
- collection_type: open
  name: SimpleLegal Cost Codes Users API
  slug: open-simplelegal-users-api
- collection_type: open
  name: SimpleLegal Cost Codes Vendors API
  slug: open-simplelegal-vendors-api
- collection_type: open
  name: SimpleLegal API
  slug: open-simplelegal
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simplelegal-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/simplelegal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplelegal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simplelegal-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simplelegal
- group: company
  title: ''
  type: Website
  url: https://www.simplelegal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.simplelegal.com/
- group: company
  title: ''
  type: Blog
  url: https://www.simplelegal.com/blog/
- group: other
  title: ''
  type: Parent Company
  url: https://www.onit.com/products/elm/simplelegal/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SimpleLegal
- group: operate
  title: ''
  type: Support
  url: https://support.simplelegal.com/
- group: start
  title: ''
  type: CounselGO Vendor Portal
  url: https://www.simplelegal.com/counselgo
- group: commercial
  title: ''
  type: Legal Requests
  url: https://info.simplelegal.com/legal-requests-datasheet
- group: start
  title: ''
  type: Login
  url: https://app.simplelegal.com/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/simplelegal-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/simplelegal-well-known.yml
- group: auth
  title: ''
  type: Security
  url: security/simplelegal-vulnerability-disclosure.yml
created: '2025-03-01'
description: SimpleLegal is Onit's mid-market enterprise legal management (ELM) platform trusted by 550+ corporate legal departments. It provides matter management, eBilling, spend management, vendor management, legal requests, and legal operations analytics for in-house legal teams. The SimpleLegal API is organized around REST with predictable, resource-oriented URLs, enabling integration with ERP and finance systems to eliminate duplicate data entry and automate legal operations workflows.
examples:
- key_count: 3
  name: Simplelegal Create Matter Example
  slug: simplelegal-create-matter-example
- key_count: 3
  name: Simplelegal Create Vendor Example
  slug: simplelegal-create-vendor-example
- key_count: 3
  name: Simplelegal List Invoices Example
  slug: simplelegal-list-invoices-example
finops:
- name: Simplelegal Finops
  service_category: API
  slug: simplelegal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplelegal.png
json_schemas:
- name: SimpleLegal Invoice
  property_count: 13
  slug: simplelegal-invoice
- name: SimpleLegal Matter
  property_count: 15
  slug: simplelegal-matter
- name: SimpleLegal Vendor
  property_count: 10
  slug: simplelegal-vendor
json_structures:
- name: Simplelegal Invoice Structure
  property_count: 0
  slug: simplelegal-invoice-structure
- name: Simplelegal Matter Structure
  property_count: 0
  slug: simplelegal-matter-structure
jsonld:
- class_count: 39
  name: Simplelegal Context
  property_count: 4
  slug: simplelegal-context
layout: provider
modified: '2026-08-08'
name: SimpleLegal
nav: Providers
network: true
overview: 'SimpleLegal publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cost Codes API, Invoices API, Matters API, and 3 more. Tagged areas include E-Billing, Enterprise Legal Management, Legal Operations, Legal Spend Management, and Matter Management.


  The SimpleLegal catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SimpleLegal''s developer surface includes authentication, documentation, engineering blog, GitHub presence, support, and 12 more developer resources.'
plans:
- name: Simplelegal Plans Pricing
  plan_count: 3
  slug: simplelegal-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Simplelegal Rate Limits
  slug: simplelegal-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SimpleLegal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: simplelegal-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: SimpleLegal API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 5
  slug: simplelegal-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 28.8
    contract_quality: 59.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 23.7
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simplelegal/refs/heads/main/screenshots/simplelegal-2026-06-20T193933.png
security:
- kind: authentication
  name: Simplelegal Authentication
  slug: simplelegal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Simplelegal Domain Security
  slug: simplelegal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Simplelegal Vulnerability Disclosure
  slug: simplelegal-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: simplelegal
tags:
- E-Billing
- Enterprise Legal Management
- Legal Operations
- Legal Spend Management
- Matter Management
- Vendor Management
website: https://www.simplelegal.com/
---
