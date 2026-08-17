---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: RESTful shipping API for printing labels and manifesting shipping data for GLS Netherlands. Covers login validation, label creation (parcel ShipType "P" and freight ShipType "F"), label deletion, sing
  name: GLS Netherlands Label API
  slug: gls-netherlands-label-api
- description: Read API for parcel status and proof of delivery in the GLS Netherlands network. Three documented operations — POST /api/parcel/v1/details, POST /api/parcel/v1/search and POST /api/pod/v1 — return par
  name: GLS Netherlands Track and Trace API
  slug: gls-netherlands-track-and-trace-api
- description: Group-wide shipping integration web service (version 3.4.19) exposed by the GLS ShipIT backend, documented publicly as Doxygen reference pages. Resource groups cover shipment processing (POST /backend
  name: GLS ShipIT REST API
  slug: gls-shipit-rest-api
artifact_total: 7
collections:
- collection_type: open
  name: GLS.API (Version 1.0)
  slug: open-gls-netherlands-label-api-test
- collection_type: open
  name: GLS Netherlands LabelApi - Production
  slug: open-gls-netherlands-label-api
- collection_type: open
  name: GLS T&T Api - Test
  slug: open-gls-track-and-trace-api-test
- collection_type: open
  name: GLS T&T Api - Production
  slug: open-gls-track-and-trace-api
common:
- group: company
  title: ''
  type: Website
  url: https://gls-group.com/
- group: start
  title: ''
  type: PortalHome
  url: https://dev-portal.gls-group.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev-portal.gls-group.net/get-started
- group: operate
  title: ''
  type: FAQ
  url: https://dev-portal.gls-group.net/faq
- group: start
  title: ''
  type: SignUp
  url: https://dev-portal.gls-group.net/accounts/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev-portal.gls-group.net/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dev-portal.gls-group.net/privacy-policy
- group: auth
  title: ''
  type: SecurityDisclosure
  url: https://gls-group.com/.well-known/security.txt
- group: start
  title: ''
  type: PortalHome
  url: https://api-portal.gls.nl/
- group: docs
  title: ''
  type: APIReference
  url: https://shipit.gls-group.eu/webservices/3_4_19/doxygen/WS-REST-API/index.html
created: '2026-07-30'
description: 'GLS Group (General Logistics Systems B.V.) is a European ground-based parcel and freight carrier headquartered in Amsterdam-Duivendrecht, Netherlands, and owned by International Distributions Services plc. It operates a road network of more than 120 hubs and roughly 1,600 depots across some 50 countries in Europe, the United States and Canada, moving B2B and B2C parcels up to about 32 kg plus a freight/LTL and express line, with an out-of-home ParcelShop and locker network. In the supply chain it is a last-mile and middle-mile parcel integrator: the party a shipper, e-commerce platform or shipping-API aggregator hands a consignment to for pickup, linehaul, customs clearance and delivery. Its API posture is federated and contract-bound rather than unified. The GLS Group developer portal (dev-portal.gls-group.net, run by GLS IT Services GmbH on Apigee) allows self-serve account and app registration with API keys or OAuth 2.0, but its API catalog is only visible after sign-in
  and "restricted" APIs additionally require approval by a local GLS representative. National units run their own portals — GLS Netherlands publishes an Azure API Management portal at api-portal.gls.nl whose OpenAPI 3.0.1 definitions for the Label API and the Track & Trace API are anonymously readable, but calling them still requires MyGLS credentials issued to a contracted shipper. The group-wide GLS ShipIT REST/SOAP web services are fully documented in public Doxygen reference pages, yet the base URL itself is handed out only with credentials by a customer''s primary GLS contact. No industry data standard — GS1/EPCIS, UPU, DCSA, IATA ONE Record, UN/EDIFACT or ANSI X12 — is referenced anywhere in the artifacts GLS publishes; every identifier and event vocabulary is GLS-proprietary.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-30'
name: GLS Group
nav: Providers
network: true
overview: 'GLS Group publishes 2 APIs on the [APIs.io](https://apis.io/) network: GLS Netherlands Label API and GLS Netherlands Track and Trace API. Tagged areas include Logistics, Supply Chain, Netherlands, Parcel, and Shipping.


  GLS Group''s developer surface includes getting-started guide, FAQ, signup flow, API reference, and 6 more developer resources.'
random_paper: 34
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.1
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gls-group/refs/heads/main/screenshots/gls-group-2026-08-07T165749.png
slug: gls-group
tags:
- Logistics
- Supply Chain
- Netherlands
- Parcel
- Shipping
- Track and Trace
- Freight
- Last Mile
- Europe
- Customs
website: https://gls-group.com/
---
