---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Turvo Agentic Access
  operation_count: 24
  slug: turvo-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 1
apis:
- description: Customers, shippers, and business partners.
  name: Turvo Accounts API
  slug: turvo-accounts-api
- description: OAuth 2.0 token exchange for the Public API.
  name: Turvo Authentication API
  slug: turvo-authentication-api
- description: Transportation providers hauling freight.
  name: Turvo Carriers API
  slug: turvo-carriers-api
- description: Facility and address master used as shipment stops.
  name: Turvo Locations API
  slug: turvo-locations-api
- description: Customer demand records planned into shipments.
  name: Turvo Orders API
  slug: turvo-orders-api
- description: Freight loads - the core shipment object in Turvo.
  name: Turvo Shipments API
  slug: turvo-shipments-api
- description: Real-time location updates and status milestones on a shipment.
  name: Turvo Tracking API
  slug: turvo-tracking-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Turvo Public Accounts API
  slug: open-turvo-accounts-api
- collection_type: open
  name: Turvo Public Accounts Authentication API
  slug: open-turvo-authentication-api
- collection_type: open
  name: Turvo Public Accounts Carriers API
  slug: open-turvo-carriers-api
- collection_type: open
  name: Turvo Public Accounts Locations API
  slug: open-turvo-locations-api
- collection_type: open
  name: Turvo Public Accounts Orders API
  slug: open-turvo-orders-api
- collection_type: open
  name: Turvo Public Accounts Shipments API
  slug: open-turvo-shipments-api
- collection_type: open
  name: Turvo Public Accounts Tracking API
  slug: open-turvo-tracking-api
- collection_type: open
  name: Turvo Public API
  slug: open-turvo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/turvo-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/turvo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turvo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turvo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turvo
- group: company
  title: ''
  type: Website
  url: https://turvo.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.turvo.com/hc/en-us/sections/12970447299987-API-Documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/turvo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/turvo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/turvo-finops.yml
created: '2026-07-05'
description: Turvo is a collaborative cloud transportation management system (TMS) that unifies shippers, freight brokers, and carriers on a single real-time platform. Its self-service Public API is a JSON REST interface (base https://publicapi.turvo.com) secured with OAuth 2.0 plus a per-tenant API key, covering shipments, orders, locations, accounts (customers), and carriers, with event-driven webhooks for status changes and location updates. API credentials and the interactive reference are provisioned per tenant from the API profile inside the Turvo application, so the surface is self-serve for Turvo customers rather than openly public.
finops:
- name: Turvo Finops
  service_category: Logistics and Supply Chain Software
  slug: turvo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turvo.png
layout: provider
modified: '2026-07-05'
name: Turvo
nav: Providers
network: true
overview: 'Turvo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Carriers API, and 4 more. Tagged areas include Logistics, Transportation Management System, TMS, Supply Chain, and Freight.


  Turvo''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Turvo Plans Pricing
  plan_count: 1
  slug: turvo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Turvo Rate Limits
  slug: turvo-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 59.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Turvo Authentication
  slug: turvo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Turvo Domain Security
  slug: turvo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: turvo
tags:
- Logistics
- Transportation Management System
- TMS
- Supply Chain
- Freight
- Shipments
- Carriers
website: https://turvo.com
---
