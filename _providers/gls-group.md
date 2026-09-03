---
agent_readiness:
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: Group-wide shipping integration web service (version 3.4.19) exposed by the GLS ShipIT backend, documented publicly as Doxygen reference pages. Resource groups cover shipment processing (POST /backend
  name: GLS ShipIT REST API
  slug: gls-shipit-rest-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The Authentication API from GLS Group — 1 operation(s) for authentication.
  name: GLS Group Authentication API
  slug: gls-group-authentication-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The Delivery API from GLS Group — 4 operation(s) for delivery.
  name: GLS Group Delivery API
  slug: gls-group-delivery-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The DeliveryOptions API from GLS Group — 1 operation(s) for deliveryoptions.
  name: GLS Group Delivery Options API
  slug: gls-group-deliveryoptions-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The Home API from GLS Group — 1 operation(s) for home.
  name: GLS Group Home API
  slug: gls-group-home-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The Monitor API from GLS Group — 1 operation(s) for monitor.
  name: GLS Group Monitor API
  slug: gls-group-monitor-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The Parcel API from GLS Group — 2 operation(s) for parcel.
  name: GLS Group Parcel API
  slug: gls-group-parcel-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The ParcelShop API from GLS Group — 1 operation(s) for parcelshop.
  name: GLS Group Parcel Shop API
  slug: gls-group-parcelshop-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The Pickup API from GLS Group — 2 operation(s) for pickup.
  name: GLS Group Pickup API
  slug: gls-group-pickup-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The Pod API from GLS Group — 1 operation(s) for pod.
  name: GLS Group Pod API
  slug: gls-group-pod-api
- baseURL: https://api.gls.nl/v1
  baseurl_source: declared
  description: The ShopReturn API from GLS Group — 1 operation(s) for shopreturn.
  name: GLS Group Shop Return API
  slug: gls-group-shopreturn-api
artifact_total: 15
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gls-group-capability-edges.yml
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
layout: provider
modified: '2026-07-30'
name: GLS Group
nav: Providers
network: true
overview: 'GLS Group publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Delivery API, Delivery Options API, and 7 more. Tagged areas include Logistics, Supply Chain, Netherlands, Parcel, and Shipping.


  GLS Group''s developer surface includes getting-started guide, FAQ, signup flow, API reference, and 7 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 82.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 46.7
    developer_ergonomics: 23.8
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
