---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-10-17'
api_count: 10
apis:
- description: API documentation is not publicly machine‑readable; the developer portal provides help articles but no OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts.
  name: Precoro API
  slug: precoro-api-2
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Invoices API from Precoro — 1 operation(s) for invoices.
  name: Precoro Invoices API
  slug: precoro-invoices-api
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Items API from Precoro — 1 operation(s) for items.
  name: Precoro Items API
  slug: precoro-items-api
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Legalentities API from Precoro — 1 operation(s) for legalentities.
  name: Precoro Legalentities API
  slug: precoro-legalentities-api
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Locations API from Precoro — 1 operation(s) for locations.
  name: Precoro Locations API
  slug: precoro-locations-api
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Purchaseorders API from Precoro — 1 operation(s) for purchaseorders.
  name: Precoro Purchaseorders API
  slug: precoro-purchaseorders-api
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Purchaserequisitions API from Precoro — 2 operation(s) for purchaserequisitions.
  name: Precoro Purchaserequisitions API
  slug: precoro-purchaserequisitions-api
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Receipts API from Precoro — 2 operation(s) for receipts.
  name: Precoro Receipts API
  slug: precoro-receipts-api
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Suppliers API from Precoro — 2 operation(s) for suppliers.
  name: Precoro Suppliers API
  slug: precoro-suppliers-api
- baseURL: https://api.precoro.com
  baseurl_source: declared
  description: The Taxes API from Precoro — 1 operation(s) for taxes.
  name: Precoro Taxes API
  slug: precoro-taxes-api
artifact_total: 22
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/rate-limits/precoro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/precoro-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/plans/precoro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/precoro-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/rules/precoro-rules.yml
  title: ''
  type: Spectral
  url: rules/precoro-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/json-ld/precoro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/precoro-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/vocabulary/precoro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/precoro-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/data-model/precoro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/precoro-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://precoro.com/trust-and-security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/conformance/precoro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/precoro-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/llms/precoro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/precoro-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/well-known/precoro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/precoro-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/hosts/precoro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/precoro-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/vendors/precoro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/precoro-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://precoro.com/terms
- group: auth
  title: ''
  type: Security
  url: https://precoro.com/security
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.precoro.com/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://precoro.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://precoro.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://precoro.com/press
- group: start
  title: ''
  type: Login
  url: https://app.precoro.com/login
- group: company
  title: ''
  type: Blog
  url: https://precoro.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.precoro.com/getting-started-with-bill-integration
- group: docs
  title: ''
  type: Documentation
  url: https://help.precoro.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/security/precoro-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/precoro-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/precoro/refs/heads/main/security/precoro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/precoro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.precoro.com
coverage:
  checked: '2026-10-13'
  detail: The help site provides articles but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://help.precoro.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Precoro is an agentic procurement and accounts payable platform that centralizes purchasing, approvals, budgets, suppliers, invoices, and payments. AI agents automate routine intake-to-pay work while teams stay in control of policies and exceptions. It serves mid-sized and multi-entity companies, offering AI‑driven automation, spend management, and ERP integration.
image: https://precoro.com/build/images/og_img.DQ01zr4h.png
json_schemas:
- name: PatchReceiptsIdnRequest
  property_count: 2
  slug: precoro-patch-receipts-idn-request
- name: PatchSuppliersIdRequest
  property_count: 1
  slug: precoro-patch-suppliers-id-request
- name: PostInvoicesRequest
  property_count: 5
  slug: precoro-post-invoices-request
- name: PostPurchaseordersRequest
  property_count: 5
  slug: precoro-post-purchaseorders-request
- name: PostPurchaserequisitionsRequest
  property_count: 5
  slug: precoro-post-purchaserequisitions-request
- name: PutSuppliersIdRequest
  property_count: 2
  slug: precoro-put-suppliers-id-request
jsonld:
- class_count: 10
  name: Precoro Context
  property_count: 9
  slug: precoro-context
layout: provider
modified: '2026-10-13'
name: Precoro
nav: Providers
network: true
overview: 'Precoro is listed with 10 APIs on the [APIs.io](https://apis.io/) network, including Invoices API, Items API, Legalentities API, and 7 more. Tagged areas include Procurement, Spend Management, Vendor Management, Purchase-To-Pay, and AP Automation.


  The Precoro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Precoro''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 21 more developer resources.'
plans:
- name: Precoro Plans Pricing
  plan_count: 4
  slug: precoro-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Precoro Rate Limits
  slug: precoro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Precoro API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: precoro-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 22.8
    developer_ergonomics: 23.8
    discoverability: 71.4
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: domain-security
  name: Precoro Domain Security
  slug: precoro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Precoro Trust Center
  slug: precoro-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: precoro
tags:
- Procurement
- Spend Management
- Vendor Management
- Purchase-To-Pay
- AP Automation
- Contract Management
- AI Procurement
website: https://www.precoro.com
---
