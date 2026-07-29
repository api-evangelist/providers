---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Near real-time access to a dealership's sales and deal data - deal jackets, desking, F&I products, and sold-vehicle records - through the Automotive Partner Cloud. Concrete paths and schemas are publi
  name: Tekion Sales and Deals API
  slug: tekion-sales-deals-api
- description: Access to new and used vehicle inventory - stock, VIN-level detail, pricing, and availability - exposed to approved partners via APC standard open APIs and webhooks. Exact endpoints live behind the pa
  name: Tekion Inventory API
  slug: tekion-inventory-api
- description: Fixed-operations and service data - repair orders, service appointments, labor operations, and status updates - available to approved partners through APC APIs and webhooks for near real-time sync. En
  name: Tekion Service API
  slug: tekion-service-api
- description: Parts inventory, catalog lookup, pricing, and ordering data (including electronic parts catalog / EPC integration) exposed to approved partners via APC. Concrete endpoints are published in the gated p
  name: Tekion Parts API
  slug: tekion-parts-api
- description: Customer and CRM records - contact, ownership, and relationship data tied to sales and service activity - made available to approved partners through APC, subject to the dealer's data-sharing authoriz
  name: Tekion Customers API
  slug: tekion-customers-api
- description: Server-to-endpoint webhooks that keep partner systems in sync as dealership data changes across sales, service, inventory, and parts. Webhooks POST event payloads to a partner-registered HTTP endpoint
  name: Tekion Webhooks
  slug: tekion-webhooks-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/tekion-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tekion-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tekion
- group: company
  title: ''
  type: Website
  url: https://tekion.com
- group: docs
  title: ''
  type: Documentation
  url: https://tekion.com/products/apc
- group: start
  title: ''
  type: Portal
  url: https://apc.tekioncloud.com
- group: start
  title: ''
  type: SignUp
  url: https://apc.tekioncloud.com/user/register
- group: commercial
  title: ''
  type: Plans
  url: plans/tekion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tekion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tekion-finops.yml
created: '2026-07-10'
description: 'Tekion is a cloud-native, AI-native automotive retail platform whose flagship Automotive Retail Cloud (ARC) is a modern dealer management system (DMS) spanning sales, service, parts, inventory, F&I, accounting, and CRM for franchise dealerships and OEMs. Tekion exposes its data and workflows to technology partners through the Automotive Partner Cloud (APC) - an open, OpenAPI-standard partner API program with REST APIs and webhooks that give approved partners near real-time access to a dealership''s sales, service, inventory, and parts data. APC is partner-gated: developers register at the APC portal, submit a use case, and are reviewed (typically within ~48 hours) before the API documentation dashboard, credentials, and endpoints are unlocked. Access is tiered (Standard, Enterprise/Elevated, Premium/Strategic) with different API scopes, rate limits, and read/write capabilities. Because the technical reference is behind partner authentication, the APIs below are honestly modeled
  by data domain rather than transcribed from a public spec.'
finops:
- name: Tekion Finops
  service_category: Automotive Software and Integration
  slug: tekion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tekion.png
layout: provider
modified: '2026-07-10'
name: Tekion
nav: Providers
network: true
overview: 'Tekion publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Dealership, DMS, Automotive Retail Cloud, and Partner API.


  Tekion''s developer surface includes documentation, developer portal, signup flow, and 7 more developer resources.'
plans:
- name: Tekion Plans Pricing
  plan_count: 3
  slug: tekion-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Tekion Rate Limits
  slug: tekion-rate-limits
score:
  band: emerging
  composite: 27.1
  delta: -2.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Tekion Domain Security
  slug: tekion-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Tekion Trust Center
  slug: tekion-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tekion
tags:
- Automotive
- Dealership
- DMS
- Automotive Retail Cloud
- Partner API
- Sales
- Service
- Inventory
- Parts
- Webhooks
- Gated
website: https://tekion.com
---
