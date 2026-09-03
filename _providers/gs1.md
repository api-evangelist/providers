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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'GS1 AISBL''s own live, unauthenticated GS1-Conformant Resolver, implementing the GS1-Conformant Resolver Standard 1.2.0. It takes a GS1 Digital Link URI built from a GS1 identification key and returns '
  name: GS1 Digital Link Resolver (id.gs1.org)
  slug: gs1-digital-link-resolver
- baseURL: https://id.gs1.org
  baseurl_source: declared
  description: Endpoints to capture EPCIS events in bulk or individually.
  name: GS1 Capture API
  slug: gs1-capture-api
- baseURL: https://id.gs1.org
  baseurl_source: declared
  description: Endpoints to obtain information about the endpoint, such as EPCIS and CBV versions or custom vocabularies.
  name: GS1 Discovery API
  slug: gs1-discovery-api
- baseURL: https://id.gs1.org
  baseurl_source: declared
  description: Endpoints that allow you to retrieve EPCIS events as Web resources.
  name: GS1 Events API
  slug: gs1-events-api
- baseURL: https://id.gs1.org
  baseurl_source: declared
  description: 'Endpoints to create large named or anonymous queries using the EPCIS Query Language. Named queries have a custom name and are stored until deleted by the user. Anonymous queries are not persisted and '
  name: GS1 Queries API
  slug: gs1-queries-api
- baseURL: https://id.gs1.org
  baseurl_source: declared
  description: EPCIS 2.0 supports query subscriptions using Webhooks or Websockets.
  name: GS1 Subscriptions API
  slug: gs1-subscriptions-api
- baseURL: https://id.gs1.org
  baseurl_source: declared
  description: 'Endpoints to browse or retrieve information about EPCIS resources: - events - types of events - electronic product codes - business steps - business locations - read points - dispositions'
  name: GS1 Top Level API
  slug: gs1-top-level-api
artifact_total: 13
collections:
- collection_type: open
  name: EPCIS 2.0 REST Bindings
  slug: open-gs1-epcis-2-0-1
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/gs1/GS1_DigitalLink_Resolver_CE/blob/master/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gs1-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/gs1/EPCIS/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/gs1/EPCIS/blob/master/CODE_OF_CONDUCT.md
- group: company
  title: ''
  type: Website
  url: https://www.gs1.org/
- group: docs
  title: ''
  type: Documentation
  url: https://ref.gs1.org/
- group: docs
  title: ''
  type: SpecificationsRepository
  url: https://ref.gs1.org/standards/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gs1
- group: design
  title: ''
  type: Vocabulary
  url: https://ref.gs1.org/voc/
- group: other
  title: ''
  type: Governance
  url: https://www.gs1.org/standards/development-work-groups
- group: other
  title: ''
  type: Standard
  url: https://ref.gs1.org/standards/genspecs/
- group: other
  title: ''
  type: Standard
  url: https://ref.gs1.org/standards/digital-link/uri-syntax/
- group: other
  title: ''
  type: Standard
  url: https://ref.gs1.org/standards/cbv/
- group: other
  title: ''
  type: Standard
  url: https://ref.gs1.org/standards/eancom/
- group: other
  title: ''
  type: Standard
  url: https://ref.gs1.org/standards/edi-business-terms/
- group: other
  title: ''
  type: Standard
  url: https://ref.gs1.org/standards/logistics-interoperability/
- group: other
  title: ''
  type: Standard
  url: https://ref.gs1.org/standards/tds/
- group: other
  title: ''
  type: Standard
  url: https://ref.gs1.org/standards/gdm/
- group: build
  title: ''
  type: Tools
  url: https://ref.gs1.org/tools/gs1-barcode-syntax-resource/
- group: start
  title: ''
  type: Registry
  url: https://www.gs1.org/services/verified-by-gs1
- group: start
  title: ''
  type: Industry
  url: https://www.gs1.org/industries/transport-and-logistics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gs1
created: '2026-07-30'
description: 'GS1 (GS1 AISBL) is the not-for-profit, neutral standards body headquartered at Avenue Louise 523, 1050 Brussels, Belgium, that maintains the identification keys and data standards the rest of the supply chain hangs its transactions on — GTIN, GLN, SSCC, GINC and GSIN, the barcode and EPC/RFID capture standards, EPCIS and the Core Business Vocabulary for supply chain visibility events, GS1 Digital Link, and EANCOM, GS1''s own subset of UN/EDIFACT. GS1 does not run a commercial logistics service; it sits underneath every party in the chain, defining the identifiers a shipper, forwarder, carrier, terminal, customs authority and last-mile network all quote at each other. Its API posture is unusually open for a standards body: the full standards library is downloadable free as PDF from ref.gs1.org with no login, EPCIS 2.0.1 ships a normative OpenAPI 3.0.3 REST binding plus JSON Schema, XSD, WSDL, SHACL and JSON-LD ontologies, and GS1 AISBL itself operates a live, unauthenticated
  GS1-Conformant Resolver at id.gs1.org. What is gated is the other half — issuing GS1 identifiers and querying the Verified by GS1 registry are federated to national GS1 Member Organisations and sold under paid membership or a commercial API subscription, not offered self-serve by the Global Office.'
image: https://ref.gs1.org/favicon-196x196.png
json_schemas:
- name: Gs1 Epcis Json
  property_count: 1
  slug: gs1-epcis-json
- name: EPCIS Query Schema
  property_count: 0
  slug: gs1-epcis-query
- name: Gs1 Resolver Description File
  property_count: 10
  slug: gs1-resolver-description-file
- name: JSON schema for linksets as defined in RFC 9264
  property_count: 1
  slug: gs1-resolver-linkset
jsonld:
- class_count: 3
  name: Gs1 Resolver Linkset Context
  property_count: 7
  slug: gs1-resolver-linkset-context
layout: provider
modified: '2026-07-30'
name: GS1
nav: Providers
network: true
overview: 'GS1 publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Capture API, Discovery API, Events API, and 3 more. Tagged areas include Logistics, Supply Chain, Belgium, Standards, and Track and Trace.


  The GS1 catalog on APIs.io includes 1 JSON-LD context.


  GS1''s developer surface includes documentation, tooling, and 20 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 52.6
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 2.6
  previous_composite: 21.7
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gs1/refs/heads/main/screenshots/gs1-2026-08-07T165851.png
slug: gs1
tags:
- Logistics
- Supply Chain
- Belgium
- Standards
- Track and Trace
- Traceability
- Identifiers
- Barcodes
- Freight Forwarding
- Retail
website: https://www.gs1.org/
---
