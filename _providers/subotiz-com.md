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
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 4
  name: Subotiz Com Agentic Access
  operation_count: 108
  slug: subotiz-com-agentic-access
  summary_line: 108 operations · 44 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: 结账会话
  name: subotiz-com Checkout Session API
  slug: subotiz-com-checkout-session-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: 顾客
  name: subotiz-com Customer API
  slug: subotiz-com-customer-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: 顾客门户
  name: subotiz-com Customer Portal API
  slug: subotiz-com-customer-portal-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: The 争议 API from subotiz-com — 2 operation(s) for 争议.
  name: subotiz-com 争议 API
  slug: subotiz-com-default-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: The Discount API from subotiz-com — 3 operation(s) for discount.
  name: subotiz-com Discount API
  slug: subotiz-com-discount-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: The Invoice API from subotiz-com — 2 operation(s) for invoice.
  name: subotiz-com Invoice API
  slug: subotiz-com-invoice-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: 支付流水
  name: subotiz-com Payment API
  slug: subotiz-com-payment-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: 商品定价方案
  name: subotiz-com Price API
  slug: subotiz-com-price-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: The Product API from subotiz-com — 6 operation(s) for product.
  name: subotiz-com Product API
  slug: subotiz-com-product-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: The Refund API from subotiz-com — 2 operation(s) for refund.
  name: subotiz-com Refund API
  slug: subotiz-com-refund-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: 订阅
  name: subotiz-com Subscription API
  slug: subotiz-com-subscription-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: 交易单
  name: subotiz-com Trade API
  slug: subotiz-com-trade-api
- baseURL: https://api.subotiz.com
  baseurl_source: declared
  description: The Webhook API from subotiz-com — 3 operation(s) for webhook.
  name: subotiz-com Webhook API
  slug: subotiz-com-webhook-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/subotiz-com/agentic-access/subotiz-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/subotiz-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/subotiz-com/plans/subotiz-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/subotiz-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/subotiz-com/rules/subotiz-com-rules.yml
  title: ''
  type: Spectral
  url: rules/subotiz-com-rules.yml
- group: design
  href: https://artifacts.apis.io/subotiz-com/json-ld/subotiz-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/subotiz-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/subotiz-com/vocabulary/subotiz-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/subotiz-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/subotiz-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/subotiz-com/data-model/subotiz-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/subotiz-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/subotiz-com/conventions/subotiz-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/subotiz-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/subotiz-com/authentication/subotiz-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/subotiz-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/subotiz-com/errors/subotiz-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/subotiz-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/subotiz-com/conformance/subotiz-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/subotiz-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/subotiz-com/llms/subotiz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/subotiz-com-llms.txt
- group: other
  href: https://artifacts.apis.io/subotiz-com/a2a/subotiz-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/subotiz-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/subotiz-com/mcp/subotiz-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/subotiz-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/subotiz-com/mcp/subotiz-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/subotiz-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/subotiz-com/well-known/subotiz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/subotiz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/subotiz-com/hosts/subotiz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/subotiz-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/subotiz-com/vendors/subotiz-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/subotiz-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/subotiz-com/security/subotiz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/subotiz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://subotiz.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://admin.subotiz.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.subotiz.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.subotiz.com/en/quick-start/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.subotiz.com/en/quick-start/overview
- group: operate
  title: ''
  type: Support
  url: https://help.subotiz.com
- group: company
  title: ''
  type: Blog
  url: https://www.subotiz.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.subotiz.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://admin.subotiz.com/signup
- group: start
  title: ''
  type: Login
  url: https://admin.subotiz.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.subotiz.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.subotiz.com/privacy-policy
created: '2026-10-30'
description: Subotiz provides an AI‑native billing platform that enables merchants to operate as a Merchant of Record, offering services such as custom checkout, global payments, subscription management, revenue intelligence, and AI‑driven financial insights. The platform includes developer tools, APIs, and documentation for integrating AI‑enhanced payment flows, supporting SaaS startups and AI developers. Subotiz’s suite also offers white‑label partnerships, pricing plans, and a help center for developers.
image: https://cdn.prod.website-files.com/67da8815fb02800d19851e2c%2F6a0afae5b4c1cbdc180b5f26_subotiz_compressed_poster.0000000.jpg
json_schemas:
- name: CreateCheckoutSessionRequest
  property_count: 26
  slug: subotiz-com-create-checkout-session-request
- name: CreatePriceRequest
  property_count: 23
  slug: subotiz-com-create-price-request
- name: CreateTradeRequest
  property_count: 14
  slug: subotiz-com-create-trade-request
- name: Product
  property_count: 13
  slug: subotiz-com-product
- name: ProductVersion
  property_count: 14
  slug: subotiz-com-product-version
- name: UpdateSubscriptionRequest
  property_count: 6
  slug: subotiz-com-update-subscription-request
jsonld:
- class_count: 120
  name: Subotiz Com Context
  property_count: 218
  slug: subotiz-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.subotiz.com.
  name: subotiz-com MCP Server
  slug: subotiz-com-mcp-yml
modified: '2026-10-30'
name: subotiz-com
nav: Providers
network: true
overview: 'subotiz-com publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checkout Session API, Customer API, Customer Portal API, and 10 more. Tagged areas include Payments, Artificial Intelligence, Billing, Software-as-a-Service, and Fintech.


  The subotiz-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  subotiz-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Subotiz Com Plans Pricing
  plan_count: 1
  slug: subotiz-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Subotiz Com Rate Limits
  slug: subotiz-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: subotiz-com API Rules
  rule_count: 54
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 8
  slug: subotiz-com-rules
scopes:
- name: Subotiz Com Scopes
  scope_count: 0
  slug: subotiz-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 35
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 58.8
    developer_ergonomics: 41.0
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/subotiz-com/subotiz-com-2026-11-03T143951.png
security:
- kind: authentication
  name: Subotiz Com Authentication
  slug: subotiz-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Subotiz Com Domain Security
  slug: subotiz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: create-customer
  slug: subotiz-com-create-customer
slug: subotiz-com
tags:
- Payments
- Artificial Intelligence
- Billing
- Software-as-a-Service
- Fintech
- Company
website: https://subotiz.com/
---
