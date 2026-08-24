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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: Version 1 of the Schenker AB (Sweden) Partner services API — the Nordic parcel network surface inherited from Privpak. Nine operations covering service point lookup (DeliveryPoint and ExtendedDelivery
  name: DB Schenker Partner Services API V1
  slug: db-schenker-partner-services-api-v1
- description: 'Version 2 of the Schenker AB (Sweden) Partner services API. Four operations: DeliveryPoint/v2 GetServicePoint (by four-digit service point number), GetAllServicePoints and GetNearestServicePoint, plus'
  name: DB Schenker Partner Services API V2
  slug: db-schenker-partner-services-api-v2
- description: 'Version 3 of the Schenker AB (Sweden) Partner services API, adding the parcel-box surface used in e-commerce checkout. Six operations across DeliveryPoint/v3: GetServicePoint, GetAllServicePoints, Get'
  name: DB Schenker Partner Services API V3
  slug: db-schenker-partner-services-api-v3
- description: Version 4 of the Schenker AB (Sweden) Partner services API, the current CollectionPoint surface (published specification version 4.2.0, document dated 2025-04-23). Six operations across DeliveryPoint/
  name: DB Schenker Partner Services API V4
  slug: db-schenker-partner-services-api-v4
artifact_total: 8
collections:
- collection_type: open
  name: Partner services API V1.
  slug: open-db-schenker-partner-services-v1-swagger
- collection_type: open
  name: Partner services API V2.
  slug: open-db-schenker-partner-services-v2-swagger
- collection_type: open
  name: Partner services API V3.
  slug: open-db-schenker-partner-services-v3-swagger
- collection_type: open
  name: Partner services API V4.
  slug: open-db-schenker-partner-services-v4-swagger
common:
- group: company
  title: ''
  type: Website
  url: https://www.dbschenker.com/
- group: docs
  title: ''
  type: APIReference
  url: https://parcelservices-se.dbschenker.com/Apipartner/swagger/ui/index
- group: docs
  title: ''
  type: Documentation
  url: https://parcelservices-se.dbschenker.com/Apipartner/Help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dbschenker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/db-schenker
- group: docs
  title: ''
  type: SupportDocumentation
  url: https://help.eschenker.dbschenker.com/helpsystem/content/
- group: other
  title: ''
  type: SuccessorOrganization
  url: https://www.dsv.com/en
created: '2026-07-30'
description: DB Schenker (Schenker AG, headquartered in Essen, Germany) is one of the world's largest freight forwarders and contract logistics providers, moving air, ocean, land and rail freight and running warehousing for shippers across roughly 1,850 locations. As a forwarder it sits in the intermediation layer of the supply chain — between the shipper who owns the cargo and the carriers, terminals and customs authorities who move and clear it — buying capacity it does not own and reselling visibility it did not have to publish. Its API posture is honestly a customer-contract posture, not a public developer posture. Deutsche Bahn sold DB Schenker to DSV A/S, completing 30 April 2025, and as of this profile www.dbschenker.com 301-redirects to dsv.com while the global developer portal at api-portal.dbschenker.com answers HTTP 410 Gone. The one DB Schenker-branded machine-readable API surface still live is the Nordic parcel "Partner services API" at parcelservices-se.dbschenker.com/Apipartner,
  which publishes four Swagger 2.0 documents openly but returns 401 on every operation without HTTP Basic credentials issued against a signed Swedish transport agreement. Its EDI endpoints are proprietary JSON, not EDIFACT or X12, and no DCSA, IATA ONE Record, GS1 EPCIS or WCO Data Model conformant contract was found on any reachable host.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-30'
name: DB Schenker
nav: Providers
network: true
overview: 'DB Schenker publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Partner Services API V1, Partner Services API V2, Partner Services API V3, and 1 more. Tagged areas include Logistics, Supply Chain, Germany, Freight Forwarding, and Parcel.


  DB Schenker''s developer surface includes API reference, documentation, and 5 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 23.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/db-schenker/refs/heads/main/screenshots/db-schenker-2026-08-07T164220.png
slug: db-schenker
tags:
- Logistics
- Supply Chain
- Germany
- Freight Forwarding
- Parcel
- Track and Trace
- Customs
- Air Cargo
- Ocean Freight
- Contract Logistics
- EDI
website: https://www.dbschenker.com/
---
