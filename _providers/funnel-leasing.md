---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 23.1
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Single-customer integration API for the Funnel leasing platform — create prospects in the CRM, schedule property tours/appointments, and process lease applications. Resources include Appointments, Com
  name: Funnel Customer API
  slug: funnel-customer-api
- description: Reusable, multi-customer integration API for partners and platform providers (not tied to a single customer account). Areas include Appointment Booking, Community Details, Prospects & Leads, Communica
  name: Funnel Partner API
  slug: funnel-partner-api
artifact_total: 5
asyncapis:
- description: ''
  name: Funnel Leasing Webhooks
  slug: funnel-leasing-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://funnelleasing.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.funnelleasing.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.funnelleasing.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.funnelleasing.com/apis/customer-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.funnelleasing.com/apis/customer-api/authentication
- group: auth
  title: ''
  type: Authentication
  url: authentication/funnel-leasing-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/funnel-leasing-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/funnel-leasing-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/funnel-leasing-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/funnel-leasing-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/funnel-leasing-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/funnel-leasing-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/funnel-leasing-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://funnelleasing.com/products/packages/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://funnelleasing.com/privacy-notice
- group: operate
  title: ''
  type: Support
  url: https://funnelleasing.com/contact/
- group: start
  title: ''
  type: Login
  url: https://nestiolistings.com/login/
created: '2026-07-17'
description: Funnel Leasing provides AI-infused CRM and property management software for multifamily (apartment) operators. The platform centralizes the leasing lifecycle from prospect to resident with a next-generation CRM, an AI Virtual Leasing Agent, voice AI insights, marketing automation, and a resident portal (Nestio ResApp), and integrates with property management systems including Yardi, RentManager, and Entrata. Funnel exposes a Customer API for single-account integrations (creating prospects, scheduling tours, and processing lease applications) and a Partner API for reusable, multi-customer integrations, plus an outbound webhooks surface. Formerly known as Nestio.
image: https://static.funnelleasing.com/archer/dist/assets/img/funnel-logos/favicon.png
layout: provider
modified: '2026-07-19'
name: Funnel Leasing
nav: Providers
network: true
overview: 'Funnel Leasing publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, PropTech, Property Management, and Multifamily.


  The Funnel Leasing catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Funnel Leasing''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, support, and 11 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 50.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 32.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Funnel Leasing Authentication
  slug: funnel-leasing-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Funnel Leasing Domain Security
  slug: funnel-leasing-domain-security
  summary_line: TLSv1.3 · DMARC
slug: funnel-leasing
tags:
- Company
- Real Estate
- PropTech
- Property Management
- Multifamily
- Leasing
- CRM
- Webhooks
website: https://funnelleasing.com/
---
