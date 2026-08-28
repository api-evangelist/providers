---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: 'The eAdaptor Inbound Service is a RESTful XML interface for pushing data into a CargoWise (CW1) instance and querying records. A single inbound endpoint accepts a Universal XML or Native XML payload; '
  name: CargoWise eAdaptor Inbound API
  slug: cargowise-eadaptor-inbound-api
- description: The eAdaptor Outbound Service is the webhook equivalent - CargoWise emits messages to a listening SOAP service when configured Workflow Template milestones or triggers fire. Actions are set to XUS (fu
  name: CargoWise eAdaptor Outbound API
  slug: cargowise-eadaptor-outbound-api
- description: The Universal Shipment (XUS) message is CargoWise's canonical XML model for a full logistics record - forwarding shipment, customs declaration, warehouse order, transport leg, and the associated organ
  name: CargoWise Universal Shipment API
  slug: cargowise-universal-shipment-api
- description: The Universal Event (XUE) message carries a minimal record identifier plus the event or milestone responsible for a notification - the basis for tracking and status integrations. XUE messages are emit
  name: CargoWise Universal Event API
  slug: cargowise-universal-event-api
- description: WiseTech's newer integration path (referred to as eAdaptor Next and xHub) adds REST access authenticated with OAuth 2.0 authorization-code flow, where a registered application receives a client ID and
  name: CargoWise REST Integration API
  slug: cargowise-rest-integration-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cargowise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cargowise-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wisetech-global
- group: company
  title: ''
  type: Website
  url: https://www.cargowise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://wisetechacademy.com/explore/product-learning/
- group: company
  title: ''
  type: Partners
  url: https://www.cargowise.com/partners/become-a-partner/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cargowise.com/lp/cargowise-value-pack/
- group: other
  title: ''
  type: Company
  url: https://www.wisetechglobal.com/
created: '2026-07-05'
description: CargoWise is WiseTech Global's logistics execution platform - a single-database ERP for international freight forwarding, customs, warehousing, transport, and landside logistics. Its integration surface is delivered primarily through eAdaptor, which pairs a RESTful XML inbound service (push, query, add, and update records) with a SOAP-based outbound service (a webhook equivalent that emits messages on milestones). Payloads use CargoWise's Universal XML schemas - Universal Shipment (XUS), Universal Event (XUE), and Universal Transaction - or the legacy Native XML format. Newer REST integration (eAdaptor Next / xHub) adds OAuth 2.0 authorization-code access. The integration API is real but heavily gated - the eAdaptor Developers Guide and endpoint details are released only after a customer purchases the eAdaptor modules, and partner access runs through WiseTech accreditation and certification. Endpoints below are modeled from public developer references; the authoritative specification
  is not publicly published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cargowise.png
layout: provider
modified: '2026-07-05'
name: CargoWise
nav: Providers
network: true
overview: 'CargoWise publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Freight Forwarding, Supply Chain, Customs, and Shipping.


  CargoWise''s developer surface includes documentation, pricing, and 6 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.2
  delta: 0.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cargowise/refs/heads/main/screenshots/cargowise-2026-07-25T204615.png
security:
- kind: domain-security
  name: Cargowise Domain Security
  slug: cargowise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cargowise Vulnerability Disclosure
  slug: cargowise-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cargowise
tags:
- Logistics
- Freight Forwarding
- Supply Chain
- Customs
- Shipping
- eAdaptor
- Universal XML
- EDI
- WiseTech Global
website: https://www.cargowise.com/
---
