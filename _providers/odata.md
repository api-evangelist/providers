---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Standard OData service endpoints including service document, metadata document, entity set CRUD operations, and batch processing as defined by the OData v4.01 specification.
  name: OData Service API
  slug: odata-service
- description: The $Batch API from OData — 1 operation(s) for $batch.
  name: OData $Batch API
  slug: odata-batch-api
- description: The $Metadata API from OData — 1 operation(s) for $metadata.
  name: OData $Metadata API
  slug: odata-metadata-api
- description: The OData Service API API from OData — 3 operation(s) for odata service api.
  name: OData OData Service API API
  slug: odata-odata-service-api-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OData Service $Batch API
  slug: open-odata-batch-api
- collection_type: open
  name: OData Service $Metadata API
  slug: open-odata-metadata-api
- collection_type: open
  name: OData Service OData Service API API
  slug: open-odata-odata-service-api-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/odata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.odata.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.odata.org/documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OData
- group: docs
  title: ''
  type: Reference
  url: https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/OData/MCP
- group: company
  title: ''
  type: Blog
  url: https://www.odata.org/blog/feed.xml
created: '2025-01-01'
description: OData (Open Data Protocol) is an OASIS standard that defines best practices for building and consuming RESTful APIs. It enables the creation of query-based data services over HTTP, providing a uniform way to describe data and data models, query and edit data, and perform batch operations.
finops:
- name: Odata Finops
  service_category: API
  slug: odata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/odata.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: OData
nav: Providers
network: true
overview: 'OData publishes 3 APIs on the [APIs.io](https://apis.io/) network: $Batch API, $Metadata API, and OData Service API API. Tagged areas include OASIS Standard, OData, Open Data Protocol, Query Language, and RESTful APIs.


  OData''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Odata Plans Pricing
  plan_count: 3
  slug: odata-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Odata Rate Limits
  slug: odata-rate-limits
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.5
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/odata/refs/heads/main/screenshots/odata-2026-06-20T190618.png
security:
- kind: domain-security
  name: Odata Domain Security
  slug: odata-domain-security
  summary_line: TLSv1.3 · HSTS
slug: odata
tags:
- OASIS Standard
- OData
- Open Data Protocol
- Query Language
- RESTful APIs
website: https://www.odata.org/
---
