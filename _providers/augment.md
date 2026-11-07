---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Augment Agentic Access
  operation_count: 23
  slug: augment-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 1
apis:
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: API key based authorization. Please refer to the [authorization documentation](docs/authorization.md) for details.
  name: Augment API Key API
  slug: augment-api-key-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: API endpoints for managing carriers, carrier contacts, and carrier-manager relationships.
  name: Augment Carrier Management API
  slug: augment-carrier-management-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: Public API endpoints for correlating carrier issues (detention, lumper, TONU, etc.) with the matching incidents in your TMS. Access is gated by brokerage; talk to Augment before using these endpoints.
  name: Augment Carrier Support API
  slug: augment-carrier-support-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: API endpoints for creating, updating, and retrieving loads.
  name: Augment Load Management API
  slug: augment-load-management-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: Public API endpoints for approved brokerages to create, update, list, and delete webhook endpoints. Self-service endpoints send version 2 webhook payloads only. Access is gated by brokerage; talk to A
  name: Augment Webhook Endpoints API
  slug: augment-webhook-endpoints-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: Public API endpoints for approved brokerages to list supported webhook event types, subscribe endpoints to event types, and send test deliveries. Subscriptions created through these public APIs delive
  name: Augment Webhook Event Subscriptions API
  slug: augment-webhook-event-subscriptions-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: Public API endpoint for submitting CSV files for asynchronous ingestion into Augment.
  name: Augment CSV Imports API
  slug: augment-csv-imports-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: Public API endpoints for creating and updating facilities.
  name: Augment Facility Management API
  slug: augment-facility-management-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: API endpoints for creating and retrieving purchase orders together with their line items.
  name: Augment Purchase Order Management API
  slug: augment-purchase-order-management-api
- baseURL: https://api.prod.goaugment.com
  baseurl_source: declared
  description: 'Rate quoting. This is the one endpoint in this reference implemented by the rate provider and called by Augment: Augment submits a shipment, the provider prices it and returns the applicable rates. Au'
  name: Augment Quote Management API
  slug: augment-quote-management-api
artifact_total: 28
asyncapis:
- description: ''
  name: Augment Webhooks
  slug: augment-webhooks
collections:
- collection_type: open
  name: Augment API Key API
  slug: open-augment-api-key-api
- collection_type: open
  name: Augment API Key Carrier Management API
  slug: open-augment-carrier-management-api
- collection_type: open
  name: Augment API Key Carrier Support API
  slug: open-augment-carrier-support-api
- collection_type: open
  name: Augment API Key Load Management API
  slug: open-augment-load-management-api
- collection_type: open
  name: Augment API Key Webhook Endpoints API
  slug: open-augment-webhook-endpoints-api
- collection_type: open
  name: Augment API Key Webhook Event Subscriptions API
  slug: open-augment-webhook-event-subscriptions-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goaugment.com/pricing
- group: commercial
  href: https://artifacts.apis.io/augment/plans/augment-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/augment-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/augment/capabilities/augment-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/augment-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://goaugment.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.goaugment.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.goaugment.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.goaugment.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.goaugment.com/guide/start-developing/authorization/
- group: company
  title: ''
  type: Blog
  url: https://www.goaugment.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.goaugment.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.goaugment.com/get-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goaugment.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goaugment.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goaugment
- group: auth
  href: https://artifacts.apis.io/augment/authentication/augment-authentication.yml
  title: ''
  type: Authentication
  url: authentication/augment-authentication.yml
- group: docs
  href: https://artifacts.apis.io/augment/openapi/_original/augment-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/augment-openapi-original.json
- group: other
  href: https://artifacts.apis.io/augment/overlays/augment-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/augment-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/augment/mcp/augment-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/augment-mcp.yml
- group: agent
  href: https://artifacts.apis.io/augment/llms/augment-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/augment-llms.txt
- group: agent
  href: https://artifacts.apis.io/augment/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/augment/agentic-access/augment-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/augment-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/augment/conventions/augment-conventions.yml
  title: ''
  type: Conventions
  url: conventions/augment-conventions.yml
- group: design
  href: https://artifacts.apis.io/augment/errors/augment-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/augment-problem-types.yml
- group: design
  href: https://artifacts.apis.io/augment/lifecycle/augment-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/augment-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.goaugment.com/guide/start-developing/migration-guide
- group: operate
  href: https://artifacts.apis.io/augment/rate-limits/augment-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/augment-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/augment/asyncapi/augment-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/augment-webhooks.yml
- group: design
  href: https://artifacts.apis.io/augment/data-model/augment-data-model.yml
  title: ''
  type: DataModel
  url: data-model/augment-data-model.yml
- group: design
  href: https://artifacts.apis.io/augment/conformance/augment-conformance.yml
  title: ''
  type: Conformance
  url: conformance/augment-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.goaugment.com/
- group: auth
  href: https://artifacts.apis.io/augment/security/augment-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/augment-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/augment/security/augment-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augment-domain-security.yml
created: '2026-07-17'
description: Augment (Augie) is an AI productivity platform for the freight and logistics industry, automating complex supply-chain workflows for brokerages, carriers, and distributors — quoting, booking, load building, capacity sourcing, track & trace, carrier support, and order-to-cash — while integrating with existing TMS, ERP, email, and messaging systems. Its public REST API (api.prod.goaugment.com) lets partner systems manage loads and route stops, upsert and archive carriers, post tracking events, report carrier issues, and configure webhook endpoints and event subscriptions across nine event types. Authentication is HTTP Basic with an API key; the company is SOC 2 Type II certified. Augment is backed by 8VC, Lightspeed Venture Partners, and Redpoint Ventures.
finops:
- has_sources: true
  method: derived
  name: Augment Finops
  primary_unit: ''
  service_category: ''
  slug: augment-finops
  template: true
image: https://framerusercontent.com/assets/hYTkXfUxYj558HcJLnhl8l2ogig.png
layout: provider
modified: '2026-07-18'
name: Augment
nav: Providers
network: true
overview: 'Augment publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Key API, Carrier Management API, Carrier Support API, and 7 more. Tagged areas include Company, Logistics, Freight, Supply Chain, and Transportation.


  The Augment catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Augment''s developer surface includes pricing, documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Augment Plans Pricing
  plan_count: 0
  slug: augment-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Augment Rate Limits
  slug: augment-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Augment API Rules
  rule_count: 59
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 9
  slug: augment-rules
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 63.7
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 58.8
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/augment/augment-2026-07-25T201709.png
security:
- kind: authentication
  name: Augment Authentication
  slug: augment-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Augment Domain Security
  slug: augment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Augment Trust Center
  slug: augment-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: Configure webhook endpoints and subscriptions
  slug: augment-configure-webhooks
- name: Create a load and post tracking updates
  slug: augment-create-load-and-track
- name: Onboard and manage carriers
  slug: augment-onboard-carrier
slug: augment
tags:
- Company
- Logistics
- Freight
- Supply Chain
- Transportation
- Webhook
- Artificial Intelligence
- Automation
website: https://goaugment.com
---
