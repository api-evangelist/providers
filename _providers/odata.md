---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Odata Agentic Access
  operation_count: 8
  slug: odata-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: Standard OData service endpoints including service document, metadata document, entity set CRUD operations, and batch processing as defined by the OData v4.01 specification.
  name: OData Service API
  slug: odata-service
- baseURL: https://services.odata.org/V4/TripPinService
  baseurl_source: spec
  description: The $Batch API from OData — 1 operation(s) for $batch.
  name: OData $Batch API
  slug: odata-batch-api
- baseURL: https://services.odata.org/V4/TripPinService
  baseurl_source: spec
  description: The $Metadata API from OData — 1 operation(s) for $metadata.
  name: OData $Metadata API
  slug: odata-metadata-api
- baseURL: https://services.odata.org/V4/TripPinService
  baseurl_source: spec
  description: The OData Service API API from OData — 3 operation(s) for odata service api.
  name: OData Service API
  slug: odata-odata-service-api-api
artifact_total: 20
collections:
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
- group: agent
  href: https://artifacts.apis.io/odata/agentic-access/odata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/odata-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/odata/rules/odata-rules.yml
  title: ''
  type: Spectral
  url: rules/odata-rules.yml
- group: design
  href: https://artifacts.apis.io/odata/json-ld/odata-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/odata-context.jsonld
- group: design
  href: https://artifacts.apis.io/odata/vocabulary/odata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/odata-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/odata/data-model/odata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/odata-data-model.yml
- group: design
  href: https://artifacts.apis.io/odata/errors/odata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/odata-problem-types.yml
- group: design
  href: https://artifacts.apis.io/odata/conformance/odata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/odata-conformance.yml
- group: other
  href: https://artifacts.apis.io/odata/hosts/odata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/odata-hosts.yml
- group: commercial
  href: https://artifacts.apis.io/odata/plans/odata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/odata-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/odata/rate-limits/odata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/odata-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/odata/finops/odata-finops.yml
  title: ''
  type: FinOps
  url: finops/odata-finops.yml
- group: auth
  href: https://artifacts.apis.io/odata/security/odata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/odata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.odata.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.odata.org/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.odata.org/getting-started/
- group: build
  title: ''
  type: Postman
  url: https://www.odata.org/getting-started/learning-odata-on-postman/
- group: build
  title: ''
  type: SDKs
  url: https://www.odata.org/libraries/
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
- has_sources: false
  method: generated
  name: Odata Finops
  primary_unit: request
  service_category: API
  slug: odata-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/odata.png
json_schemas:
- name: BatchRequest
  property_count: 1
  slug: odata-batch-request
- name: BatchResponse
  property_count: 1
  slug: odata-batch-response
- name: EntityCollection
  property_count: 5
  slug: odata-entity-collection
- name: Entity
  property_count: 5
  slug: odata-entity
- name: ServiceDocument
  property_count: 2
  slug: odata-service-document
jsonld:
- class_count: 7
  name: Odata Context
  property_count: 7
  slug: odata-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-09-16'
name: OData
nav: Providers
network: true
overview: 'OData publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including $Batch API, $Metadata API, Service API, and 1 more. Tagged areas include OASIS Standard, OData, Open Data Protocol, Query Language, and RESTful APIs.


  The OData catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OData''s developer surface includes getting-started guide, documentation, engineering blog, and 19 more developer resources.'
plans:
- name: Odata Plans Pricing
  plan_count: 3
  slug: odata-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Odata Rate Limits
  slug: odata-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: OData API Rules
  rule_count: 53
  severity_counts:
    error: 50
    hint: 0
    info: 2
    warn: 1
  slug: odata-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.5
  facets:
    access_clarity: 7.9
    contract_governance: 35.6
    contract_quality: 56.9
    developer_ergonomics: 52.4
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 25.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/odata/odata-2026-06-20T190618.png
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
