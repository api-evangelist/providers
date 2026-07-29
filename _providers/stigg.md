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
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 7
  name: Stigg Agentic Access
  operation_count: 13
  slug: stigg-agentic-access
  summary_line: 13 operations · 8 acting · 7 human-in-the-loop
api_count: 9
apis:
- description: Official Node.js / TypeScript SDK for integrating Stigg entitlements, feature flags, and usage-based billing into backend services.
  name: Stigg Node.js SDK
  slug: stigg-node-sdk
- description: Official Python SDK for integrating Stigg entitlements and usage-based billing into Python backend services.
  name: Stigg Python SDK
  slug: stigg-python-sdk
- description: Official Go SDK for integrating Stigg entitlements and usage-based billing into Go backend services.
  name: Stigg Go SDK
  slug: stigg-go-sdk
- description: Official React frontend SDK for rendering pricing tables, entitlement gates, and usage meters in React applications.
  name: Stigg React SDK
  slug: stigg-react-sdk
- description: Coupon retrieval.
  name: Stigg Coupons API
  slug: stigg-coupons-api
- description: Customer provisioning and management.
  name: Stigg Customers API
  slug: stigg-customers-api
- description: Feature access and entitlement checks.
  name: Stigg Entitlements API
  slug: stigg-entitlements-api
- description: Subscription lifecycle management.
  name: Stigg Subscriptions API
  slug: stigg-subscriptions-api
- description: Usage reporting and metering.
  name: Stigg Usage API
  slug: stigg-usage-api
artifact_total: 49
collections:
- collection_type: open
  name: Stigg API
  slug: open-stigg
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stigg-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stigg-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stigg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stigg-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/stiggio/skills
- group: company
  title: ''
  type: Website
  url: https://www.stigg.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stigg.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stigg.io/getting-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/stiggio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getstigg
- group: company
  title: ''
  type: Blog
  url: https://www.stigg.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stigg.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stigg.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/getstigg
- group: start
  title: ''
  type: Signup
  url: https://app.stigg.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.stigg.io/llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/stigg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stigg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stigg-finops.yml
created: '2026-03-27'
description: Stigg is a product-led growth monetization platform providing REST and GraphQL APIs for managing pricing plans, entitlements, usage-based billing, feature flags, and subscription lifecycle. It serves as a monetization control layer for SaaS and AI products, enabling engineering teams to implement flexible pricing, granular access control, and real-time usage metering without rebuilding billing infrastructure from scratch. Stigg is SOC 2 Type II and ISO 27001 certified and delivers 99.99% uptime SLA with multi-region deployment.
examples:
- key_count: 2
  name: Stigg Check Entitlement Example
  slug: stigg-check-entitlement-example
- key_count: 6
  name: Stigg Executegraphql Example
  slug: stigg-executegraphql-example
- key_count: 2
  name: Stigg Provision Customer Example
  slug: stigg-provision-customer-example
- key_count: 2
  name: Stigg Rest Provision Customer Example
  slug: stigg-rest-provision-customer-example
- key_count: 2
  name: Stigg Rest Provision Subscription Example
  slug: stigg-rest-provision-subscription-example
- key_count: 2
  name: Stigg Rest Report Usage Example
  slug: stigg-rest-report-usage-example
finops:
- name: Stigg Finops
  service_category: Pricing & Entitlements Platform
  slug: stigg-finops
graphqls:
- description: The Stigg GraphQL API provides full access to customer provisioning, subscription management, entitlement checking, usage reporting, and pricing plan management. Authentication uses the X-API-KEY head
  name: Stigg GraphQL API
  slug: stigg-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stigg.png
json_schemas:
- name: Coupon
  property_count: 10
  slug: stigg-coupon
- name: Stigg Customer
  property_count: 6
  slug: stigg-customer
- name: Stigg Entitlement
  property_count: 5
  slug: stigg-entitlement
- name: GraphQLError
  property_count: 4
  slug: stigg-graphqlerror
- name: GraphQLRequest
  property_count: 3
  slug: stigg-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: stigg-graphqlresponse
- name: Plan
  property_count: 3
  slug: stigg-plan
- name: Subscription
  property_count: 5
  slug: stigg-subscription
- name: UsageMeasurement
  property_count: 8
  slug: stigg-usage-measurement
json_structures:
- name: Stigg Entitlement Structure
  property_count: 0
  slug: stigg-entitlement-structure
- name: Stigg Structure
  property_count: 0
  slug: stigg-structure
jsonld:
- class_count: 35
  name: Stigg Context
  property_count: 0
  slug: stigg-context
layout: provider
modified: '2026-06-13'
name: Stigg
nav: Providers
network: true
overview: 'Stigg publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Coupons API, Customers API, Entitlements API, and 2 more. Tagged areas include FinOps, Pricing, Billing, Entitlements, and Usage-Based Billing.


  The Stigg catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stigg''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Stigg Plans Pricing
  plan_count: 3
  slug: stigg-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Stigg Rate Limits
  slug: stigg-rate-limits
rules:
- name: Stigg API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 2
  slug: stigg-jsonschema-spectral-rules
- name: Stigg API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: stigg-rules
score:
  band: developing
  composite: 55.6
  delta: -4.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 68.9
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stigg/refs/heads/main/screenshots/stigg-2026-06-20T194550.png
security:
- kind: authentication
  name: Stigg Authentication
  slug: stigg-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stigg Domain Security
  slug: stigg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stigg Trust Center
  slug: stigg-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 11
skills:
- name: stigg-api
  slug: stigg-api
- name: stigg-credits
  slug: stigg-credits
- name: stigg-entitlements
  slug: stigg-entitlements
- name: stigg-mcp
  slug: stigg-mcp
- name: stigg-pricing-expert
  slug: stigg-pricing-expert
- name: stigg-pricing-modeling
  slug: stigg-pricing-modeling
- name: stigg-recipes
  slug: stigg-recipes
- name: stigg-subscriptions
  slug: stigg-subscriptions
- name: stigg-webhooks
  slug: stigg-webhooks
- name: stigg-widgets
  slug: stigg-widgets
- name: stigg
  slug: stigg
slug: stigg
tags:
- FinOps
- Pricing
- Billing
- Entitlements
- Usage-Based Billing
- Feature Flags
- Product-Led Growth
- Subscriptions
- SaaS
- GraphQL
- REST
website: https://www.stigg.io/
---
