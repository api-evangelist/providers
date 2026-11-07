---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Outpost Ai Agentic Access
  operation_count: 8
  slug: outpost-ai-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.outpostanywhere.com
  baseurl_source: declared
  description: Server-to-server access tokens.
  name: Outpost OAuth API
  slug: outpost-ai-oauth-api
- baseURL: https://api.outpostanywhere.com
  baseurl_source: declared
  description: Payment lifecycle operations — provisioning a SetupIntent at signup, confirming the payment after card collection, and refunding in full or in part.
  name: Outpost Payments API
  slug: outpost-ai-payments-api
- baseURL: https://api.outpostanywhere.com
  baseurl_source: declared
  description: Events Outpost posts to the merchant during renewal cycles.
  name: Outpost Webhooks API
  slug: outpost-ai-webhooks-api
artifact_total: 16
asyncapis:
- description: ''
  name: Outpost Ai Webhooks
  slug: outpost-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/outpost-ai/agentic-access/outpost-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/outpost-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/outpost-ai/rules/outpost-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/outpost-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/outpost-ai/json-ld/outpost-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/outpost-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/outpost-ai/vocabulary/outpost-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/outpost-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/outpost-ai/asyncapi/outpost-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/outpost-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/outpost-ai/data-model/outpost-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/outpost-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/outpost-ai/conventions/outpost-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/outpost-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/outpost-ai/conventions/outpost-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/outpost-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/outpost-ai/authentication/outpost-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/outpost-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/outpost-ai/errors/outpost-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/outpost-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/outpost-ai/conformance/outpost-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/outpost-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/outpost-ai/hosts/outpost-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outpost-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/outpost-ai/vendors/outpost-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/outpost-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.outpost.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://outpost.ai/docs/account-setup
- group: docs
  title: ''
  type: APIReference
  url: https://outpost.ai/docs/api-reference/
- group: auth
  href: https://artifacts.apis.io/outpost-ai/security/outpost-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outpost-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://outpost.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://outpost.ai/docs/
- group: company
  title: ''
  type: Blog
  url: https://outpost.ai/blog/
- group: company
  title: ''
  type: Careers
  url: https://outpost.ai/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://outpost.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://outpost.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.outpost.ai/
created: '2026-10-29'
description: Outpost provides a modular platform for global commerce, handling payments, tax, customs, and invoicing across borders. Their solution enables merchants to sell internationally with a unified API, offering Merchant of Record, Tax of Record, and Importer of Record services. Backed by local businesses and investors, Outpost simplifies cross‑border transactions, compliance, and settlement reporting, allowing companies to focus on growth while Outpost manages the complex financial and regulatory layers.
json_schemas:
- name: PaymentIntentRequest
  property_count: 5
  slug: outpost-ai-payment-intent-request
- name: PaymentIntentResponse
  property_count: 4
  slug: outpost-ai-payment-intent-response
- name: RefundRequest
  property_count: 3
  slug: outpost-ai-refund-request
- name: RefundResponse
  property_count: 8
  slug: outpost-ai-refund-response
- name: SetupIntentRequest
  property_count: 2
  slug: outpost-ai-setup-intent-request
- name: SetupIntentResponse
  property_count: 4
  slug: outpost-ai-setup-intent-response
jsonld:
- class_count: 12
  name: Outpost Ai Context
  property_count: 42
  slug: outpost-ai-context
layout: provider
modified: '2026-10-29'
name: Outpost
nav: Providers
network: true
overview: 'Outpost publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: OAuth API, Payments API, and Webhooks API. Tagged areas include Company, Payments, Tax, Commerce, and Software-as-a-Service.


  The Outpost catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Outpost''s developer surface includes authentication, getting-started guide, API reference, documentation, engineering blog, and 19 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Outpost API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: outpost-ai-rules
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 14.5
    contract_governance: 22.0
    contract_quality: 72.4
    developer_ergonomics: 27.4
    discoverability: 62.5
    operational_transparency: 15.8
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/outpost-ai/outpost-ai-2026-11-03T140812.png
security:
- kind: authentication
  name: Outpost Ai Authentication
  slug: outpost-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Outpost Ai Domain Security
  slug: outpost-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: outpost-ai-payments-process
  slug: outpost-ai-payments-process
slug: outpost-ai
tags:
- Company
- Payments
- Tax
- Commerce
- Software-as-a-Service
website: https://outpost.ai/
---
