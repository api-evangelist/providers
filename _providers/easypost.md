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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Easypost Agentic Access
  operation_count: 15
  slug: easypost-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 11
apis:
- description: 'Core REST API. Resources: Shipments (immutable; ship + buy rate), Rates, Addresses, Parcels, CustomsInfo, Forms, Labels (PNG/PDF/ZPL/EPL2), Pickups, ScanForms, Refunds, Batches, EndShippers, CarrierAc'
  name: EasyPost Shipping API
  slug: shipping
- description: 'Standalone Tracking API: create Trackers from a tracking code + carrier, receive webhooks on status changes, query historical scan events. Standard Tracking and Advanced Tracking tiers are available w'
  name: EasyPost Tracking API
  slug: tracking
- description: Asynchronous Event delivery surface. EasyPost POSTs Event objects to subscriber URLs whenever asynchronous objects (batches, trackers, scan forms, refunds, reports, payments, claims, insurance, shipme
  name: EasyPost Webhooks API
  slug: webhooks
- description: 'Insurance API: insure shipments at 1% of declared value with a $1 minimum. Claims API: file and manage damage/loss/theft claims via REST.'
  name: EasyPost Insurance & Claims API
  slug: insurance-claims
- description: Generate Shipment, Tracker, Refund, Payment Log, and other reports asynchronously; download CSVs from the URL returned in the report object.
  name: EasyPost Reports API
  slug: reports
- description: The Addresses API from EasyPost — 2 operation(s) for addresses.
  name: EasyPost Addresses API
  slug: easypost-addresses-api
- description: The Parcels API from EasyPost — 1 operation(s) for parcels.
  name: EasyPost Parcels API
  slug: easypost-parcels-api
- description: The Refunds API from EasyPost — 1 operation(s) for refunds.
  name: EasyPost Refunds API
  slug: easypost-refunds-api
- description: The Reports API from EasyPost — 1 operation(s) for reports.
  name: EasyPost Reports API
  slug: easypost-reports-api
- description: The Shipments API from EasyPost — 5 operation(s) for shipments.
  name: EasyPost Shipments API
  slug: easypost-shipments-api
- description: The Trackers API from EasyPost — 2 operation(s) for trackers.
  name: EasyPost Trackers API
  slug: easypost-trackers-api
artifact_total: 28
asyncapis:
- description: AsyncAPI specification for EasyPost's webhook surface. EasyPost dispatches Event objects to subscriber URLs whenever asynchronous objects (batches, trackers, scan forms, refunds, reports, payments, cl
  name: EasyPost Webhooks API
  slug: easypost-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EasyPost Shipping Addresses API
  slug: open-easypost-addresses-api
- collection_type: open
  name: EasyPost Shipping Addresses Parcels API
  slug: open-easypost-parcels-api
- collection_type: open
  name: EasyPost Shipping Addresses Refunds API
  slug: open-easypost-refunds-api
- collection_type: open
  name: EasyPost Shipping Addresses Reports API
  slug: open-easypost-reports-api
- collection_type: open
  name: EasyPost Shipping Addresses Shipments API
  slug: open-easypost-shipments-api
- collection_type: open
  name: EasyPost Shipping Addresses Trackers API
  slug: open-easypost-trackers-api
- collection_type: open
  name: EasyPost Shipping API
  slug: open-easypost
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/easypost-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/easypost-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/easypost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/easypost-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/easypost
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/easypost
- group: company
  title: ''
  type: Website
  url: https://www.easypost.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.easypost.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/easypost-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/easypost-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/easypost-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.easypost.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.easypost.com/feed/
created: '2026-05-08'
description: EasyPost is a multi-carrier shipping API platform for the United States and international markets. It exposes a REST API spanning shipments, rating, labels, tracking, addresses, parcels, insurance, claims, pickups, scan forms, refunds, batches, end-shippers, reports, customs info, carrier accounts, and webhooks. EasyPost integrates 100+ carriers including USPS, UPS, FedEx, DHL, Canada Post, and Royal Mail.
finops:
- name: Easypost Finops
  service_category: Shipping API
  slug: easypost-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/easypost.png
layout: provider
modified: '2026-05-30'
name: EasyPost
nav: Providers
network: true
overview: 'EasyPost publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Addresses API, Parcels API, and 4 more. Tagged areas include Shipping, Logistics, Multi-Carrier, Tracking, and Labels.


  The EasyPost catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  EasyPost''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Easypost Plans Pricing
  plan_count: 5
  slug: easypost-plans-pricing
random_paper: 143
rate_limits:
- limit_count: 2
  name: Easypost Rate Limits
  slug: easypost-rate-limits
rules:
- name: EasyPost API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: easypost-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 64.1
    developer_ergonomics: 21.7
    discoverability: 81.5
    governance: 47.9
    operational_transparency: 10.5
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/easypost/refs/heads/main/screenshots/easypost-2026-07-25T212719.png
security:
- kind: authentication
  name: Easypost Authentication
  slug: easypost-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Easypost Domain Security
  slug: easypost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Easypost Trust Center
  slug: easypost-trust-center
  summary_line: SOC 2
slug: easypost
tags:
- Shipping
- Logistics
- Multi-Carrier
- Tracking
- Labels
- Insurance
website: https://www.easypost.com/
---
