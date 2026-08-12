---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cargoson Agentic Access
  operation_count: 5
  slug: cargoson-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 5
apis:
- description: Cargoson can deliver real-time event notifications (shipment status updates, booking confirmations, shipment changes) to a customer-configured endpoint URL, set up under Settings > Integrations > Webh
  name: Cargoson Webhooks
  slug: webhooks
- description: List carrier services available on the account.
  name: Cargoson Carriers API
  slug: cargoson-carriers-api
- description: Retrieve live freight rate quotes across activated carriers.
  name: Cargoson Price Requests API
  slug: cargoson-price-requests-api
- description: Create shipment queries and direct bookings, retrieve labels.
  name: Cargoson Shipments API
  slug: cargoson-shipments-api
- description: Retrieve booking, transport, and tracking details.
  name: Cargoson Transports & Tracking API
  slug: cargoson-transports-tracking-api
artifact_total: 13
collections:
- collection_type: open
  name: Cargoson API
  slug: open-cargoson
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cargoson-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cargoson-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cargoson-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cargoson-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cargoson
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cargoson
- group: company
  title: ''
  type: Website
  url: https://www.cargoson.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cargoson.com/en/integrations
- group: commercial
  title: ''
  type: Plans
  url: plans/cargoson-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cargoson-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cargoson-finops.yml
created: '2026-06-21'
description: Cargoson is an Estonian B2B cloud transport management software (TMS) platform for manufacturers and wholesalers. Its unified REST API lets shippers request freight rates, book shipments, generate labels, and track deliveries across 2,000+ carriers using one set of endpoints, authentication, and data formats. Cargoson is carrier-neutral; customers contract directly with their own carriers and upload their own freight rates.
finops:
- name: Cargoson Finops
  service_category: Logistics and Transport Management
  slug: cargoson-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cargoson.png
layout: provider
modified: '2026-06-21'
name: Cargoson
nav: Providers
network: true
overview: 'Cargoson publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Carriers API, Price Requests API, Shipments API, and 1 more. Tagged areas include Transport Management, TMS, Freight, Shipping, and Logistics.


  Cargoson''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Cargoson Plans Pricing
  plan_count: 4
  slug: cargoson-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 2
  name: Cargoson Rate Limits
  slug: cargoson-rate-limits
score:
  band: thin
  composite: 36.0
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cargoson/refs/heads/main/screenshots/cargoson-2026-07-25T204610.png
security:
- kind: authentication
  name: Cargoson Authentication
  slug: cargoson-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cargoson Domain Security
  slug: cargoson-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cargoson Vulnerability Disclosure
  slug: cargoson-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cargoson
tags:
- Transport Management
- TMS
- Freight
- Shipping
- Logistics
- Carriers
website: https://www.cargoson.com/
---
