---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.8
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.agnic.ai
  baseurl_source: declared
  description: 'Agnic API Reference API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Agnic API Reference API
  slug: api-reference-api
- baseURL: https://api.agnic.ai
  baseurl_source: declared
  description: 'Agnic core API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Agnic core API
  slug: core-api
- baseURL: https://api.agnic.ai
  baseurl_source: declared
  description: 'Agnic X402 API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Agnic X402 API
  slug: x402-api
artifact_total: 25
common:
- group: operate
  href: https://artifacts.apis.io/agnic-ai/rate-limits/agnic-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agnic-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agnic-ai/plans/agnic-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agnic-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agnic-ai/rules/agnic-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agnic-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agnic-ai/json-ld/agnic-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agnic-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/agnic-ai/vocabulary/agnic-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agnic-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agnic-ai/data-model/agnic-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agnic-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/agnic-ai/cli/agnic-ai-cli.yml
  title: ''
  type: CLI
  url: cli/agnic-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/agnic-ai/authentication/agnic-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agnic-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/agnic-ai/conformance/agnic-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agnic-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agnic-ai/llms/agnic-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agnic-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/agnic-ai/well-known/agnic-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agnic-ai-app-security.txt
- group: agent
  href: https://artifacts.apis.io/agnic-ai/well-known/agnic-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agnic-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agnic-ai/hosts/agnic-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agnic-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agnic-ai/vendors/agnic-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agnic-ai-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agnicpay
- group: auth
  href: https://artifacts.apis.io/agnic-ai/security/agnic-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agnic-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agnic.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.agnic.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agnic.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agnic.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agnic.ai/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.agnic.ai/blog
- group: company
  title: ''
  type: About
  url: https://www.agnic.ai/about
- group: operate
  title: ''
  type: Contact
  url: https://www.agnic.ai/contact
coverage:
  detail: Documentation pages are served as markdown but the API spec is not publicly available.
  evidence:
  - status: 200
    url: https://docs.agnic.ai/docs/api-reference.mdx
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Agnic provides a wallet platform enabling AI agents to perform purchases across any store without merchant integration. The service offers granular spending controls, real‑time receipts, and cryptographic proof of transactions. Developers can integrate via a single API to complete checkout, manage limits, and access detailed logs, empowering agentic commerce with secure, auditable payments.
image: https://agnic.ai/agnic-tc.jpg
json_schemas:
- name: GetApiAgentEmailResponse
  property_count: 7
  slug: agnic-ai-get-api-agent-email-response
- name: GetApiAgentIdentityResponse
  property_count: 8
  slug: agnic-ai-get-api-agent-identity-response
- name: GetApiAutofillOrdersIdResponse
  property_count: 14
  slug: agnic-ai-get-api-autofill-orders-id-response
- name: GetDiscoveryResourcesResponse
  property_count: 3
  slug: agnic-ai-get-discovery-resources-response
- name: GetPaidEndpointResponse
  property_count: 2
  slug: agnic-ai-get-paid-endpoint-response
- name: PostApiAgentEmailResponse
  property_count: 7
  slug: agnic-ai-post-api-agent-email-response
- name: PostApiAutofillShopifyQuoteRequest
  property_count: 9
  slug: agnic-ai-post-api-autofill-shopify-quote-request
- name: PostApiAutofillShopifyQuoteResponse
  property_count: 15
  slug: agnic-ai-post-api-autofill-shopify-quote-response
- name: PostApiSignPaymentResponse
  property_count: 2
  slug: agnic-ai-post-api-sign-payment-response
- name: PostDispatchRequest
  property_count: 5
  slug: agnic-ai-post-dispatch-request
- name: PostEndpointRequest
  property_count: 1
  slug: agnic-ai-post-endpoint-request
- name: PostEndpointResponse
  property_count: 2
  slug: agnic-ai-post-endpoint-response
- name: PostSettleRequest
  property_count: 2
  slug: agnic-ai-post-settle-request
- name: PostSettleResponse
  property_count: 5
  slug: agnic-ai-post-settle-response
- name: PostVerifyRequest
  property_count: 2
  slug: agnic-ai-post-verify-request
- name: PostVerifyResponse
  property_count: 3
  slug: agnic-ai-post-verify-response
jsonld:
- class_count: 39
  name: Agnic Ai Context
  property_count: 98
  slug: agnic-ai-context
layout: provider
modified: '2026-11-01'
name: Agnic
nav: Providers
network: true
overview: 'Agnic is listed with 3 APIs on the [APIs.io](https://apis.io/) network: API Reference API, core API, and X402 API. Tagged areas include Agent Wallet, Payment Infrastructure, AI Commerce, Verifiable Credentials, and API Monetization.


  The Agnic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agnic''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, and 18 more developer resources.'
plans:
- name: Agnic Ai Plans Pricing
  plan_count: 1
  slug: agnic-ai-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Agnic Ai Rate Limits
  slug: agnic-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Agnic API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: agnic-ai-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 26.1
    developer_ergonomics: 39.3
    discoverability: 71.4
    operational_transparency: 44.7
  previous_composite: 39.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agnic Ai Authentication
  slug: agnic-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agnic Ai Domain Security
  slug: agnic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agnic-ai
tags:
- Agent Wallet
- Payment Infrastructure
- AI Commerce
- Verifiable Credentials
- API Monetization
- Service Discovery
website: https://agnic.ai/
---
