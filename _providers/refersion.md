---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Refersion Agentic Access
  operation_count: 15
  slug: refersion-agentic-access
  summary_line: 15 operations · 15 acting
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
- description: Create, retrieve, update, search, and manage affiliate accounts and their conversion triggers.
  name: Refersion Affiliates API
  slug: refersion-affiliates-api
- description: Cancel conversions, get totals, issue manual credits, and change conversion statuses.
  name: Refersion Conversions API
  slug: refersion-conversions-api
- description: Manage offer-level configurations including SKU-specific commission rates.
  name: Refersion Offers API
  slug: refersion-offers-api
- description: Generate download links for saved reports.
  name: Refersion Reporting API
  slug: refersion-reporting-api
artifact_total: 30
asyncapis:
- description: ''
  name: Refersion Webhooks
  slug: refersion-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/refersion-agentic-access.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/refersion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/refersion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/refersion-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/refersion-vocabulary.yml
- group: build
  title: ''
  type: Packages
  url: packages/refersion-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/refersion-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/refersion-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/refersion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/refersion-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/refersion-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/refersion-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/refersion-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/refersion-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/refersion-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/refersion-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/refersion-tool-crosswalk.yml
- group: agent
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
- name: Refersion Finops
  service_category: ''
  slug: refersion-finops
graphqls:
- description: Refersion provides a GraphQL API that supplements its REST API, enabling flexible, ad-hoc queries and data manipulation for affiliate marketing programs. The GraphQL API allows clients to request exac
  name: Refersion GraphQL API
  slug: refersion-graphql
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
mcp_servers:
- description: Refersion publishes NO Model Context Protocol server — remote or local. This document is a DERIVED candidate tool surface, computed one-to-one from the 15 operations in Refersion's own published OpenA
  name: Refersion MCP Server (candidate)
  slug: refersion-mcp-server-candidate
modified: '2026-08-13'
name: Refersion
nav: Providers
network: true
overview: 'Refersion publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Affiliates API, Conversions API, Offers API, and 1 more. Tagged areas include Affiliate Marketing, Influencer Marketing, E-Commerce, Referral Tracking, and Commission Management.


  The Refersion catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Refersion''s developer surface includes documentation, engineering blog, pricing, authentication, API reference, getting-started guide, support, and 29 more developer resources.'
plans:
- name: Refersion Plans Pricing
  plan_count: 4
  slug: refersion-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Refersion Rate Limits
  slug: refersion-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Refersion API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: refersion-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 29
    catalog_gap: 31.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 29.5
    contract_quality: 72.9
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 29.5
    operational_transparency: 60.5
  previous_composite: 62.0
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/refersion/refs/heads/main/screenshots/refersion-2026-06-20T192744.png
security:
- kind: authentication
  name: Refersion Authentication
  slug: refersion-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Refersion Domain Security
  slug: refersion-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
