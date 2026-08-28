---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: The documented MyCarrier Public API — order creation and management, rate quoting and dispatch, routing-guide rules, shipping locations and shipment detail retrieval. 17 operations over HTTP Basic aut
  name: MyCarrier Public API
  slug: mycarrier-public-api
- description: The MyCarrier Order Public API — create or modify an order, delete an order by reference ID, and retrieve an order by reference ID. Served from its own host with HTTP Basic authentication (email / api
  name: MyCarrier Order API
  slug: mycarrier-order-api
- description: The MyCarrier FreightAudit (Invoice Hub) API — freight bill audit, invoice filtering and retrieval, disputes, notes, tags, bulk import/export, payments and remittance, invoice analytics and shipment l
  name: MyCarrier FreightAudit API
  slug: mycarrier-freightaudit-api
- description: The MyCarrier webhook registration surface (ITM.Services.Webhook.Api) — register, update and delete webhook subscriptions, webhook types and additional outbound HTTP headers. Bearer JWT. The published
  name: MyCarrier Webhook Registration API
  slug: mycarrier-webhook-api
artifact_total: 11
asyncapis:
- description: ''
  name: Mycarrier Events Webhooks
  slug: mycarrier-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://go.mycarrier.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mycarrier.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mycarrier.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mycarrier.io/reference/getrates-1
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mycarrier.io/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/mycarrier-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://help-center.mycarriertms.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help-center.mycarriertms.com/en/
- group: company
  title: ''
  type: Blog
  url: https://go.mycarrier.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://go.mycarrier.io/plans-and-pricing
- group: start
  title: ''
  type: SignUp
  url: https://go.mycarrier.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://login.mycarriertms.com/a/b38da2f/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://go.mycarrier.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://go.mycarrier.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mycarriertms.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.mycarrier.io/
- group: auth
  title: ''
  type: Compliance
  url: security/mycarrier-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mycarrier-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/mycarrier-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mycarrier-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mycarrier-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mycarrier-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mycarrier-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mycarrier-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mycarrier-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mycarrier-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mycarrier-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/mycarrier-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mycarrier-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mycarrier-domain-security.yml
created: '2026-08-26'
description: MyCarrier is a transportation management system (TMS) for less-than-truckload (LTL) and full-truckload freight, founded in 2018 by Michael Bookout and Chris Scheid. The platform lets shippers quote, book, dispatch, track, audit and pay freight from a single connected workspace using direct carrier rates rather than broker markups, and connects to more than a dozen national LTL carriers. MyCarrier publishes a public REST API on developer.mycarrier.io covering order creation and management, rate quoting and dispatch, routing-guide rules, shipping locations, shipment detail retrieval, and a FreightAudit / invoice surface for freight bill audit, disputes, notes and payments. It also publishes a webhook catalog for shipment and invoice lifecycle events.
image: https://apporderprocessprodsa.blob.core.windows.net/$web/images/tms-logo.svg
layout: provider
modified: '2026-08-26'
name: MyCarrier
nav: Providers
network: true
overview: 'MyCarrier publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Public API, Order API, FreightAudit API, and 1 more. Tagged areas include Company, Logistics, Transportation, Freight, and Shipping.


  The MyCarrier catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MyCarrier''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Mycarrier Plans Pricing
  plan_count: 4
  slug: mycarrier-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Mycarrier Rate Limits
  slug: mycarrier-rate-limits
score:
  band: strong
  composite: 56.2
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 56.7
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Mycarrier Authentication
  slug: mycarrier-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Mycarrier Domain Security
  slug: mycarrier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mycarrier Vulnerability Disclosure
  slug: mycarrier-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Mycarrier Trust Center
  slug: mycarrier-trust-center
  summary_line: trust center published
slug: mycarrier
tags:
- Company
- Logistics
- Transportation
- Freight
- Shipping
- LTL
- Supply Chain
- Transportation Management
- Freight Audit
- Invoicing
website: https://go.mycarrier.io/
---
