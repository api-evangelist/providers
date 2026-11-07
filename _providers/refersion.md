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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Refersion Agentic Access
  operation_count: 15
  slug: refersion-agentic-access
  summary_line: 15 operations · 10 acting
api_count: 2
apis:
- description: GraphQL API providing an explorer interface for querying affiliate data, managing program configurations, and integrating with e-commerce platforms.
  name: Refersion GraphQL API
  slug: refersion-graphql-api
- description: Webhook API for receiving real-time notifications about affiliate activity, including new conversions, conversion approvals/denials, payments, affiliate status changes, and bonus tier movements.
  name: Refersion Webhooks API
  slug: refersion-webhooks-api
- description: Inbound order-reporting surface used to send completed orders to Refersion so commissions are calculated. Server-side integrations POST the order JSON plus a merchant-generated cart_id to inbound-webh
  name: Refersion Order Tracking API
  slug: refersion-order-tracking-api
- baseURL: https://api.refersion.com
  baseurl_source: declared
  description: Create, retrieve, update, search, and manage affiliate accounts and their conversion triggers.
  name: Refersion Affiliates API
  slug: refersion-affiliates-api
- baseURL: https://api.refersion.com
  baseurl_source: declared
  description: Cancel conversions, get totals, issue manual credits, and change conversion statuses.
  name: Refersion Conversions API
  slug: refersion-conversions-api
- baseURL: https://api.refersion.com
  baseurl_source: declared
  description: Manage offer-level configurations including SKU-specific commission rates.
  name: Refersion Offers API
  slug: refersion-offers-api
- baseURL: https://api.refersion.com
  baseurl_source: declared
  description: Generate download links for saved reports.
  name: Refersion Reporting API
  slug: refersion-reporting-api
artifact_total: 30
asyncapis:
- description: ''
  name: Refersion Webhooks
  slug: refersion-webhooks
collections:
- collection_type: open
  name: Refersion REST Affiliates API
  slug: open-refersion-affiliates-api
- collection_type: open
  name: Refersion REST Affiliates Conversions API
  slug: open-refersion-conversions-api
- collection_type: open
  name: Refersion REST Affiliates Offers API
  slug: open-refersion-offers-api
- collection_type: open
  name: Refersion REST Affiliates Reporting API
  slug: open-refersion-reporting-api
common:
- group: agent
  href: https://artifacts.apis.io/refersion/agentic-access/refersion-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/refersion-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/refersion/security/refersion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/refersion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.refersion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.refersion.dev/reference/welcome-to-refersion
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/refersion
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/refersion
- group: company
  title: ''
  type: Blog
  url: https://www.refersion.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.refersion.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://statuspage.refersion.com
- group: other
  title: ''
  type: X
  url: https://x.com/refersion
- group: commercial
  href: https://artifacts.apis.io/refersion/plans/refersion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/refersion-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/refersion/rate-limits/refersion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/refersion-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/refersion/finops/refersion-finops.yml
  title: ''
  type: FinOps
  url: finops/refersion-finops.yml
- group: design
  href: https://artifacts.apis.io/refersion/vocabulary/refersion-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/refersion-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/refersion/packages/refersion-packages.yml
  title: ''
  type: Packages
  url: packages/refersion-packages.yml
- group: agent
  href: https://artifacts.apis.io/refersion/llms/refersion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/refersion-llms.txt
- group: auth
  href: https://artifacts.apis.io/refersion/authentication/refersion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/refersion-authentication.yml
- group: design
  href: https://artifacts.apis.io/refersion/conventions/refersion-conventions.yml
  title: ''
  type: Conventions
  url: conventions/refersion-conventions.yml
- group: design
  href: https://artifacts.apis.io/refersion/errors/refersion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/refersion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/refersion/data-model/refersion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/refersion-data-model.yml
- group: design
  href: https://artifacts.apis.io/refersion/lifecycle/refersion-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/refersion-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/refersion/conformance/refersion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/refersion-conformance.yml
- group: design
  href: https://artifacts.apis.io/refersion/components/refersion-components.yml
  title: ''
  type: Components
  url: components/refersion-components.yml
- group: design
  href: https://artifacts.apis.io/refersion/asyncapi/refersion-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/refersion-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/refersion/mcp/refersion-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/refersion-mcp.yml
- group: build
  href: https://artifacts.apis.io/refersion/mcp/refersion-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/refersion-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/refersion/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.refersion.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://www.refersion.dev/reference/welcome-to-refersion
- group: start
  title: ''
  type: GettingStarted
  url: https://www.refersion.dev/reference/order-tracking-overview
- group: operate
  title: ''
  type: Support
  url: https://support.refersion.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://auth.refersion.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://auth.refersion.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.refersion.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.refersion.com/privacy/
- group: design
  href: https://artifacts.apis.io/refersion/json-ld/refersion-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/refersion-context.jsonld
created: '2026-06-13'
description: Affiliate marketing platform for e-commerce brands providing a REST and GraphQL API for managing affiliates, tracking referrals, processing commissions, and integrating with Shopify, BigCommerce, WooCommerce, and other platforms.
examples:
- key_count: 2
  name: Cancel Conversion Request
  slug: cancel-conversion-request
- key_count: 18
  name: New Affiliate Request
  slug: new-affiliate-request
- key_count: 3
  name: New Affiliate Response
  slug: new-affiliate-response
- key_count: 2
  name: Sku Commission Request
  slug: sku-commission-request
finops:
- has_sources: true
  method: derived
  name: Refersion Finops
  primary_unit: subscription
  service_category: ''
  slug: refersion-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refersion.png
json_schemas:
- name: Affiliate
  property_count: 9
  slug: affiliate
- name: ConversionTrigger
  property_count: 4
  slug: conversion-trigger
- name: Conversion
  property_count: 13
  slug: conversion
jsonld:
- class_count: 7
  name: Refersion Context
  property_count: 68
  slug: refersion-context
layout: provider
modified: '2026-08-13'
name: Refersion
nav: Providers
network: true
overview: 'Refersion publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Affiliates API, Conversions API, Offers API, and 4 more. Tagged areas include Affiliate Marketing, Influencer Marketing, E-Commerce, Referral Tracking, and Commission Management.


  The Refersion catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Refersion''s developer surface includes documentation, engineering blog, pricing, authentication, API reference, getting-started guide, support, and 29 more developer resources.'
plans:
- name: Refersion Plans Pricing
  plan_count: 4
  slug: refersion-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Refersion Rate Limits
  slug: refersion-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Refersion — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: refersion-jsonschema-spectral-rules
score:
  band: strong
  composite: 63.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 82.8
    catalog_earned_first_party: 24.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 84.2
    contract_governance: 28.0
    contract_quality: 63.2
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 60.5
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/refersion/refersion-2026-06-20T192744.png
security:
- kind: authentication
  name: Refersion Authentication
  slug: refersion-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Refersion Domain Security
  slug: refersion-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: refersion-onboard-affiliate
  slug: refersion-onboard-affiliate
- name: refersion-reconcile-conversions
  slug: refersion-reconcile-conversions
- name: refersion-track-orders
  slug: refersion-track-orders
slug: refersion
tags:
- Affiliate Marketing
- Influencer Marketing
- E-Commerce
- Referral Tracking
- Commission Management
- Shopify
website: https://www.refersion.com/
---
