---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Amberflo Agentic Access
  operation_count: 17
  slug: amberflo-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 10
apis:
- description: The Amberflo Cost Tracking API provides AI and cloud cost management capabilities including cloud provider integrations, business unit management, cost allocation rules, budget management, and cost qu
  name: Amberflo Cost Tracking API
  slug: cost-tracking-api
- description: The Amberflo AI Gateway provides a unified API for routing requests to 1,500+ LLM models with intelligent model routing, cost optimization, built-in fallbacks, and MCP server traffic monitoring. It tr
  name: Amberflo AI Gateway API
  slug: ai-gateway-api
- baseURL: https://app.amberflo.io
  baseurl_source: declared
  description: Manage customer accounts and lifecycle
  name: Amberflo Customers API
  slug: amberflo-customers-api
- baseURL: https://app.amberflo.io
  baseurl_source: declared
  description: Ingest meter events for usage tracking
  name: Amberflo Event Ingestion API
  slug: amberflo-event-ingestion-api
- baseURL: https://app.amberflo.io
  baseurl_source: declared
  description: Manage meter event filtering rules
  name: Amberflo Filtering Rules API
  slug: amberflo-filtering-rules-api
- baseURL: https://app.amberflo.io
  baseurl_source: declared
  description: Retrieve customer invoices
  name: Amberflo Invoices API
  slug: amberflo-invoices-api
- baseURL: https://app.amberflo.io
  baseurl_source: declared
  description: Create, read, update, and delete meter definitions
  name: Amberflo Meter Definitions API
  slug: amberflo-meter-definitions-api
- baseURL: https://app.amberflo.io
  baseurl_source: declared
  description: Manage customer prepaid credit orders
  name: Amberflo Prepaid Orders API
  slug: amberflo-prepaid-orders-api
- baseURL: https://app.amberflo.io
  baseurl_source: declared
  description: Manage pricing plans and customer plan assignments
  name: Amberflo Pricing Plans API
  slug: amberflo-pricing-plans-api
- baseURL: https://app.amberflo.io
  baseurl_source: declared
  description: Query aggregated usage data and raw events
  name: Amberflo Usage Queries API
  slug: amberflo-usage-queries-api
arazzos:
- description: Create a customer account then assign a pricing plan to them.
  name: Amberflo Create Customer and Assign Plan
  slug: amberflo-create-customer-and-assign-plan-workflow
- description: Create a meter definition and immediately ingest a usage event against it.
  name: Amberflo Create Meter and Ingest Event
  slug: amberflo-create-meter-and-ingest-event-workflow
- description: List meter definitions then query aggregated usage for a selected meter.
  name: Amberflo Discover Meter and Query Usage
  slug: amberflo-discover-meter-and-query-usage-workflow
- description: Look up a customer by ID then list their invoices.
  name: Amberflo Get Customer Invoices
  slug: amberflo-get-customer-invoices-workflow
- description: Ingest a meter event for a customer then query aggregated usage for that meter.
  name: Amberflo Ingest and Query Usage
  slug: amberflo-ingest-and-query-usage-workflow
- description: Create a meter, onboard a customer, assign a plan, then ingest first usage.
  name: Amberflo Launch Usage Based Product
  slug: amberflo-launch-usage-based-product-workflow
- description: Ingest a usage event for a customer then fund a prepaid credit top-up.
  name: Amberflo Meter Usage and Top Up Prepaid
  slug: amberflo-meter-usage-and-topup-prepaid-workflow
- description: Create a meter, attach a dimension filtering rule, then ingest an event.
  name: Amberflo Meter with Filtering Rule
  slug: amberflo-meter-with-filtering-rule-workflow
- description: Look up a customer, check for invoices, and delete them only when none exist.
  name: Amberflo Offboard Customer If No Invoices
  slug: amberflo-offboard-customer-if-no-invoices-workflow
- description: Create a customer, ingest a usage event for them, then query their aggregated usage.
  name: Amberflo Onboard Customer and Meter Usage
  slug: amberflo-onboard-customer-and-meter-usage-workflow
- description: Create a customer, assign a pricing plan, then fund a prepaid credit order.
  name: Amberflo Provision Customer Billing
  slug: amberflo-provision-customer-billing-workflow
- description: Find a customer by ID and update it if it exists, otherwise create it.
  name: Amberflo Upsert Customer
  slug: amberflo-upsert-customer-workflow
artifact_total: 118
collections:
- collection_type: postman
  name: Amberflo Billing Customers API
  slug: postman-amberflo-customers-api
- collection_type: postman
  name: Amberflo Billing Customers Event Ingestion API
  slug: postman-amberflo-event-ingestion-api
- collection_type: postman
  name: Amberflo Billing Customers Filtering Rules API
  slug: postman-amberflo-filtering-rules-api
- collection_type: postman
  name: Amberflo Billing Customers Invoices API
  slug: postman-amberflo-invoices-api
- collection_type: postman
  name: Amberflo Billing Customers Meter Definitions API
  slug: postman-amberflo-meter-definitions-api
- collection_type: postman
  name: Amberflo Billing Customers Prepaid Orders API
  slug: postman-amberflo-prepaid-orders-api
- collection_type: postman
  name: Amberflo Billing Customers Pricing Plans API
  slug: postman-amberflo-pricing-plans-api
- collection_type: postman
  name: Amberflo Billing Customers Usage Queries API
  slug: postman-amberflo-usage-queries-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amberflo Billing Customers API
  slug: open-amberflo-customers-api
- collection_type: open
  name: Amberflo Billing Customers Event Ingestion API
  slug: open-amberflo-event-ingestion-api
- collection_type: open
  name: Amberflo Billing Customers Filtering Rules API
  slug: open-amberflo-filtering-rules-api
- collection_type: open
  name: Amberflo Billing Customers Invoices API
  slug: open-amberflo-invoices-api
- collection_type: open
  name: Amberflo Billing Customers Meter Definitions API
  slug: open-amberflo-meter-definitions-api
- collection_type: open
  name: Amberflo Billing Customers Prepaid Orders API
  slug: open-amberflo-prepaid-orders-api
- collection_type: open
  name: Amberflo Billing Customers Pricing Plans API
  slug: open-amberflo-pricing-plans-api
- collection_type: open
  name: Amberflo Billing Customers Usage Queries API
  slug: open-amberflo-usage-queries-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amberflo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amberflo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amberflo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amberflo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amberflo-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-create-customer-and-assign-plan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-create-meter-and-ingest-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-discover-meter-and-query-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-get-customer-invoices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-ingest-and-query-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-launch-usage-based-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-meter-usage-and-topup-prepaid-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-meter-with-filtering-rule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-offboard-customer-if-no-invoices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-onboard-customer-and-meter-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-provision-customer-billing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amberflo-upsert-customer-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amberflo
- group: company
  title: ''
  type: Website
  url: https://www.amberflo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amberflo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.amberflo.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amberflo.io/docs/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amberflo.io/reference/
- group: start
  title: ''
  type: Signup
  url: https://ui.amberflo.io/cGxnLXNpZ251cA==
- group: start
  title: ''
  type: Login
  url: https://ui.amberflo.io/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amberflo.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.amberflo.io/resources/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amberflo.io/legal/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amberflo.io/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.amberflo.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.amberflo.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amberflo
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/amberflo-metering-python/
- group: build
  title: TypeScript SDK
  type: SDKs
  url: https://github.com/amberflo/metering-typescript
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/amberflo/metering-go
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/rules/amberflo-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/vocabulary/amberflo-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.amberflo.io/llms.txt
created: '2026-03-27'
description: Amberflo is a cloud metering, usage-based billing, and AI cost management platform. It provides real-time event ingestion, customer billing automation, AI gateway capabilities, and FinOps visibility for API-driven and AI-powered businesses. The platform supports usage-based, token-based, seat-based, and outcome-based pricing models with automated invoicing and embeddable billing dashboards.
examples:
- key_count: 6
  name: Billing Address Example
  slug: billing-address-example
- key_count: 13
  name: Billing Customer Example
  slug: billing-customer-example
- key_count: 8
  name: Billing Customer Request Example
  slug: billing-customer-request-example
- key_count: 7
  name: Billing Invoice Example
  slug: billing-invoice-example
- key_count: 6
  name: Billing Prepaid Order Example
  slug: billing-prepaid-order-example
- key_count: 4
  name: Billing Prepaid Order Request Example
  slug: billing-prepaid-order-request-example
- key_count: 3
  name: Billing Pricing Plan Assignment Example
  slug: billing-pricing-plan-assignment-example
- key_count: 5
  name: Metering Filtering Rule Example
  slug: metering-filtering-rule-example
- key_count: 6
  name: Metering Meter Definition Example
  slug: metering-meter-definition-example
- key_count: 4
  name: Metering Meter Definition Request Example
  slug: metering-meter-definition-request-example
- key_count: 7
  name: Metering Meter Event Example
  slug: metering-meter-event-example
- key_count: 8
  name: Metering Usage Query Request Example
  slug: metering-usage-query-request-example
- key_count: 1
  name: Metering Usage Query Response Example
  slug: metering-usage-query-response-example
- key_count: 2
  name: Metering Usage Record Example
  slug: metering-usage-record-example
features:
- description: Ingest millions to billions of high-cardinality usage events in real time with idempotency, deduplication, and automatic aggregation.
  name: Real-Time Event Ingestion
- description: Unified LLM access and control across 1,500+ models with per-unit costs, rollups, budgets, Cost Guards, and margin analysis per customer.
  name: AI Cost Management
- description: Single API for multiple LLM providers with intelligent cost optimization, automatic retries, fallbacks, and MCP server traffic monitoring.
  name: AI Gateway and Model Routing
- description: Flexible billing models including usage-based, token-based, seat-based, fixed fee, and outcome-based pricing with multi-currency support and automated invoicing.
  name: Usage-Based Billing
- description: Customer-facing billing portals and dashboards via a React.js UI Kit with custom domain support and SSO integration.
  name: Embeddable Billing Dashboards
- description: Revenue recognition automation, RevRec ledger tracking, tax management, and integrations with Stripe and NetSuite.
  name: Revenue Operations
- description: Spending limits, threshold alerts, Cost Guards, and automated notifications for cloud and AI cost governance.
  name: Budget Management
- description: Chargeback rates, quotes, and invoices for internal cost allocation and showback reporting across business units.
  name: Chargeback and Showback
finops:
- name: Amberflo Finops
  service_category: FinOps / Metering and Billing
  slug: amberflo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amberflo.png
integrations:
- description: Native integration with Stripe for payment processing and revenue operations workflows.
  name: Stripe
- description: Integration with NetSuite for revenue recognition and financial reporting.
  name: NetSuite
- description: Official Kong plugin for metering API requests handled by Kong instances and monetizing APIs.
  name: Kong
- description: Integration with AWS SaaS Builder Toolkit for SaaS billing and metering best practices on AWS.
  name: AWS SaaS Builder Toolkit
- description: Logging callback for LiteLLM to meter LLM usage and monitor AI costs.
  name: LiteLLM
- description: Examples and utilities for metering AWS Lambda function invocations.
  name: AWS Lambda
json_schemas:
- name: Address
  property_count: 6
  slug: billing-address
- name: CustomerRequest
  property_count: 8
  slug: billing-customer-request
- name: Customer
  property_count: 13
  slug: billing-customer
- name: Invoice
  property_count: 7
  slug: billing-invoice
- name: PrepaidOrderRequest
  property_count: 4
  slug: billing-prepaid-order-request
- name: PrepaidOrder
  property_count: 6
  slug: billing-prepaid-order
- name: PricingPlanAssignment
  property_count: 3
  slug: billing-pricing-plan-assignment
- name: FilteringRule
  property_count: 5
  slug: metering-filtering-rule
- name: MeterDefinitionRequest
  property_count: 4
  slug: metering-meter-definition-request
- name: MeterDefinition
  property_count: 6
  slug: metering-meter-definition
- name: MeterEvent
  property_count: 7
  slug: metering-meter-event
- name: UsageQueryRequest
  property_count: 8
  slug: metering-usage-query-request
- name: UsageQueryResponse
  property_count: 1
  slug: metering-usage-query-response
- name: UsageRecord
  property_count: 2
  slug: metering-usage-record
json_structures:
- name: Billing Address Structure
  property_count: 6
  slug: billing-address-structure
- name: Billing Customer Request Structure
  property_count: 8
  slug: billing-customer-request-structure
- name: Billing Customer Structure
  property_count: 13
  slug: billing-customer-structure
- name: Billing Invoice Structure
  property_count: 7
  slug: billing-invoice-structure
- name: Billing Prepaid Order Request Structure
  property_count: 4
  slug: billing-prepaid-order-request-structure
- name: Billing Prepaid Order Structure
  property_count: 6
  slug: billing-prepaid-order-structure
- name: Billing Pricing Plan Assignment Structure
  property_count: 3
  slug: billing-pricing-plan-assignment-structure
- name: Metering Filtering Rule Structure
  property_count: 5
  slug: metering-filtering-rule-structure
- name: Metering Meter Definition Request Structure
  property_count: 4
  slug: metering-meter-definition-request-structure
- name: Metering Meter Definition Structure
  property_count: 6
  slug: metering-meter-definition-structure
- name: Metering Meter Event Structure
  property_count: 7
  slug: metering-meter-event-structure
- name: Metering Usage Query Request Structure
  property_count: 8
  slug: metering-usage-query-request-structure
- name: Metering Usage Query Response Structure
  property_count: 1
  slug: metering-usage-query-response-structure
- name: Metering Usage Record Structure
  property_count: 2
  slug: metering-usage-record-structure
jsonld:
- class_count: 1
  name: Amberflo Billing Address Context
  property_count: 6
  slug: amberflo-billing-address-context
- class_count: 5
  name: Amberflo Billing Customer Context
  property_count: 10
  slug: amberflo-billing-customer-context
- class_count: 1
  name: Amberflo Billing Invoice Context
  property_count: 7
  slug: amberflo-billing-invoice-context
- class_count: 3
  name: Amberflo Billing Prepaid Context
  property_count: 5
  slug: amberflo-billing-prepaid-context
- class_count: 1
  name: Amberflo Billing Pricing Context
  property_count: 3
  slug: amberflo-billing-pricing-context
- class_count: 1
  name: Amberflo Metering Filtering Context
  property_count: 5
  slug: amberflo-metering-filtering-context
- class_count: 3
  name: Amberflo Metering Meter Context
  property_count: 10
  slug: amberflo-metering-meter-context
- class_count: 3
  name: Amberflo Metering Usage Context
  property_count: 11
  slug: amberflo-metering-usage-context
layout: provider
modified: '2026-05-19'
name: Amberflo
nav: Providers
network: true
overview: 'Amberflo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Event Ingestion API, Filtering Rules API, and 5 more. Tagged areas include Usage-Based Billing, Metering, FinOps, AI Cost Management, and Billing.


  The Amberflo catalog on APIs.io includes 8 JSON-LD contexts and 2 Spectral governance rulesets.


  Amberflo''s developer surface includes authentication, documentation, getting-started guide, API reference, signup flow, pricing, engineering blog, and 31 more developer resources.'
plans:
- name: Amberflo Plans Pricing
  plan_count: 4
  slug: amberflo-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Amberflo Rate Limits
  slug: amberflo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amberflo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amberflo-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Amberflo API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: amberflo-spectral-rules
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 28.8
    contract_quality: 25.2
    developer_ergonomics: 58.3
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/screenshots/amberflo-2026-06-20T171855.png
security:
- kind: authentication
  name: Amberflo Authentication
  slug: amberflo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amberflo Domain Security
  slug: amberflo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Amberflo Trust Center
  slug: amberflo-trust-center
  summary_line: SOC 2
slug: amberflo
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
use_cases:
- description: Meter API usage and automatically bill customers based on calls, tokens, or custom events with flexible pricing models.
  name: API Monetization
- description: Track and govern LLM spending across teams and customers with budgets, alerts, and per-customer cost attribution.
  name: AI Cost Governance
- description: Automate end-to-end billing for SaaS products with usage-based pricing plans, invoicing, and customer portals.
  name: SaaS Billing Automation
- description: Allocate and showback cloud costs to business units and customers using automated cost allocation rules and chargeback workflows.
  name: Cloud FinOps
- description: Provide customers with real-time visibility into their usage and costs via embedded dashboards and billing portals.
  name: Customer Cost Transparency
- description: Query and analyze usage data in real time with batch and sparse query modes, raw event queries, and revenue calculation analytics.
  name: Usage Analytics and Reporting
website: https://www.amberflo.io/
---
