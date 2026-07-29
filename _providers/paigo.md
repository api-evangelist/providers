---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Paigo Agentic Access
  operation_count: 48
  slug: paigo-agentic-access
  summary_line: 48 operations · 25 acting
api_count: 8
apis:
- description: Manage customers in Paigo.
  name: Paigo Customers API
  slug: paigo-customers-api
- description: Manage dimensions in Paigo.
  name: Paigo Dimensions API
  slug: paigo-dimensions-api
- description: Manage invoices in Paigo.
  name: Paigo Invoices API
  slug: paigo-invoices-api
- description: Manage measurements in Paigo. <br><br> See <a href="https://docs.paigo.tech/measure-usage-and-collect-data/measure-and-collect-usage-data-at-production-scale">Measure and Collect Usage Data at Product
  name: Paigo Measurements API
  slug: paigo-measurements-api
- description: Manage offerings in Paigo.
  name: Paigo Offerings API
  slug: paigo-offerings-api
- description: The Settings API from Paigo — 2 operation(s) for settings.
  name: Paigo Settings API
  slug: paigo-settings-api
- description: Measure and collect usage data.
  name: Paigo Usage API
  slug: paigo-usage-api
- description: The Webhooks API from Paigo — 7 operation(s) for webhooks.
  name: Paigo Webhooks API
  slug: paigo-webhooks-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paigo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paigo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paigo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paigo-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.paigo.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paigo.tech/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/paigo-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paigo-tech
- group: company
  title: ''
  type: Blog
  url: https://blog.paigo.tech/
- group: commercial
  title: ''
  type: Pricing
  url: https://paigo.tech/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/PaigoTech
- group: commercial
  title: ''
  type: Plans
  url: plans/paigo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paigo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paigo-finops.yml
created: '2026-06-13'
description: Paigo is a usage-based billing infrastructure platform with a REST API for metering API calls, tracking consumption, managing pricing tiers, and automating invoice generation for developer products. It supports pay-as-you-go, subscription tier, seat-based, custom unit, and top-up pricing models with zero transaction fees.
examples:
- key_count: 4
  name: Paigo Auth Token Example
  slug: paigo-auth-token-example
- key_count: 5
  name: Paigo Customer Create Example
  slug: paigo-customer-create-example
- key_count: 4
  name: Paigo Invoice Create Example
  slug: paigo-invoice-create-example
- key_count: 4
  name: Paigo Offering Create Example
  slug: paigo-offering-create-example
- key_count: 5
  name: Paigo Usage Create Example
  slug: paigo-usage-create-example
finops:
- name: Paigo Finops
  service_category: ''
  slug: paigo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paigo.png
json_schemas:
- name: AggregatedUsageResponse
  property_count: 3
  slug: paigo-aggregated-usage
- name: CreateCustomerDto
  property_count: 13
  slug: paigo-create-customer
- name: CreateDimensionDto
  property_count: 15
  slug: paigo-create-dimension
- name: CreateInvoicesDto
  property_count: 6
  slug: paigo-create-invoices
- name: CreateOfferingDTO
  property_count: 14
  slug: paigo-create-offering
- name: CreateUsageDto
  property_count: 5
  slug: paigo-create-usage
- name: CreateWebhookDto
  property_count: 5
  slug: paigo-create-webhook
- name: ReadCustomerResponseData
  property_count: 22
  slug: paigo-read-customer
- name: ReadInvoicesDto
  property_count: 15
  slug: paigo-read-invoices
- name: UpdateCustomerEnrollmentDto
  property_count: 5
  slug: paigo-update-customer-enrollment
jsonld:
- class_count: 12
  name: Paigo Context
  property_count: 30
  slug: paigo-context
layout: provider
modified: '2026-06-13'
name: Paigo
nav: Providers
network: true
overview: 'Paigo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Dimensions API, Invoices API, and 5 more. Tagged areas include Billing, Usage-Based Billing, Metering, Invoicing, and Pricing.


  The Paigo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Paigo''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Paigo Plans Pricing
  plan_count: 1
  slug: paigo-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 0
  name: Paigo Rate Limits
  slug: paigo-rate-limits
rules:
- name: Paigo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: paigo-jsonschema-spectral-rules
scopes:
- name: Paigo Scopes
  scope_count: 0
  slug: paigo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.5
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paigo/refs/heads/main/screenshots/paigo-2026-06-20T191330.png
security:
- kind: authentication
  name: Paigo Authentication
  slug: paigo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Paigo Domain Security
  slug: paigo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paigo
tags:
- Billing
- Usage-Based Billing
- Metering
- Invoicing
- Pricing
- SaaS
- Subscriptions
- Developer Tools
- FinOps
website: https://www.paigo.tech/
---
