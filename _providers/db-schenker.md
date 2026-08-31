---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: Responsible for all Web API functions related to Service Points
  name: DB Schenker Delivery Point API
  slug: db-schenker-deliverypoint-api
- description: Responsible for all Web API functions related to Service Points
  name: DB Schenker Delivery Point2 API
  slug: db-schenker-deliverypoint2-api
- description: Responsible for all Web API functions related to Service Points
  name: DB Schenker Delivery Point3 API
  slug: db-schenker-deliverypoint3-api
- description: Responsible for all Web API functions related to Service Points
  name: DB Schenker Delivery Point4 API
  slug: db-schenker-deliverypoint4-api
- description: 'Responsible for all Web API functions related to EDI (For example: Register, Register Return)'
  name: DB Schenker Edi API
  slug: db-schenker-edi-api
- description: Responsible for all Web API functions related to HITTA
  name: DB Schenker Extended Delivery Point API
  slug: db-schenker-extendeddeliverypoint-api
- description: Responsible for (QR) print codes.
  name: DB Schenker Print Code API
  slug: db-schenker-printcode-api
- description: Responsible for all Web API functions related to handling sorting codes in MANET.
  name: DB Schenker Sorting Code API
  slug: db-schenker-sortingcode-api
- description: Responsible for all Web API functions related to Advanced Track and Trace.
  name: DB Schenker Track And Trace Advanced2 API
  slug: db-schenker-trackandtraceadvanced2-api
- description: Responsible for all Web API functions related to Boxes Track and Trace.
  name: DB Schenker Track And Trace Boxes API
  slug: db-schenker-trackandtraceboxes-api
artifact_total: 14
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/db-schenker-capability-edges.yml
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
overview: 'DB Schenker publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Delivery Point API, Delivery Point2 API, Delivery Point3 API, and 7 more. Tagged areas include Logistics, Supply Chain, Germany, Freight Forwarding, and Parcel.


  DB Schenker''s developer surface includes API reference, documentation, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.2
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 26.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
