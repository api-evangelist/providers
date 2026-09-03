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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Arlula Agentic Access
  operation_count: 16
  slug: arlula-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 4
apis:
- baseURL: https://api.arlula.com
  baseurl_source: declared
  description: Search and order historical satellite imagery
  name: Arlula Archive API
  slug: arlula-archive-api
- baseURL: https://api.arlula.com
  baseurl_source: declared
  description: API connection testing
  name: Arlula Connection API
  slug: arlula-connection-api
- baseURL: https://api.arlula.com
  baseurl_source: declared
  description: Manage orders, campaigns, datasets, and resources
  name: Arlula Orders API
  slug: arlula-orders-api
- baseURL: https://api.arlula.com
  baseurl_source: declared
  description: Schedule future satellite captures
  name: Arlula Tasking API
  slug: arlula-tasking-api
artifact_total: 90
collections:
- collection_type: postman
  name: Arlula Archive API
  slug: postman-arlula-archive-api
- collection_type: postman
  name: Arlula Archive Connection API
  slug: postman-arlula-connection-api
- collection_type: postman
  name: Arlula Archive Orders API
  slug: postman-arlula-orders-api
- collection_type: postman
  name: Arlula Archive Tasking API
  slug: postman-arlula-tasking-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arlula Archive API
  slug: open-arlula-archive-api
- collection_type: open
  name: Arlula Archive Connection API
  slug: open-arlula-connection-api
- collection_type: open
  name: Arlula Archive Orders API
  slug: open-arlula-orders-api
- collection_type: open
  name: Arlula Archive Tasking API
  slug: open-arlula-tasking-api
- collection_type: open
  name: API Collection
  slug: open-arlula
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/arlula/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arlula-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arlula-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arlula-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arlula
- group: company
  title: ''
  type: Website
  url: https://arlula.com/
- group: docs
  title: ''
  type: Documentation
  url: https://arlula.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://arlula.com/documentation/
- group: start
  title: ''
  type: Portal
  url: https://dashboard.arlula.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Arlula
- group: design
  title: ''
  type: SpectralRules
  url: rules/arlula-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/arlula-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://arlula.com/news
created: '2025-02-06'
description: Arlula is a satellite imagery marketplace and API platform providing programmatic access to archive and tasking satellite imagery from multiple providers. The Arlula API enables developers to search the global satellite archive, discover tasking opportunities, place imagery orders, and download delivered datasets including GeoTIFF imagery, preview images, and metadata files.
examples:
- key_count: 6
  name: Arlula Archive Order Request Example
  slug: arlula-archive-order-request-example
- key_count: 8
  name: Arlula Archive Scene Example
  slug: arlula-archive-scene-example
- key_count: 8
  name: Arlula Archive Search Request Example
  slug: arlula-archive-search-request-example
- key_count: 3
  name: Arlula Batch Archive Order Request Example
  slug: arlula-batch-archive-order-request-example
- key_count: 2
  name: Arlula Batch Tasking Order Request Example
  slug: arlula-batch-tasking-order-request-example
- key_count: 3
  name: Arlula Bundle Example
  slug: arlula-bundle-example
- key_count: 3
  name: Arlula Campaign Example
  slug: arlula-campaign-example
- key_count: 1
  name: Arlula Campaigns List Response Example
  slug: arlula-campaigns-list-response-example
- key_count: 2
  name: Arlula Cancel Response Example
  slug: arlula-cancel-response-example
- key_count: 4
  name: Arlula Dataset Example
  slug: arlula-dataset-example
- key_count: 1
  name: Arlula Datasets List Response Example
  slug: arlula-datasets-list-response-example
- key_count: 4
  name: Arlula Order Example
  slug: arlula-order-example
- key_count: 3
  name: Arlula Order Response Example
  slug: arlula-order-response-example
- key_count: 1
  name: Arlula Orders List Response Example
  slug: arlula-orders-list-response-example
- key_count: 3
  name: Arlula Resource Example
  slug: arlula-resource-example
- key_count: 6
  name: Arlula Tasking Opportunity Example
  slug: arlula-tasking-opportunity-example
- key_count: 8
  name: Arlula Tasking Order Request Example
  slug: arlula-tasking-order-request-example
- key_count: 10
  name: Arlula Tasking Search Request Example
  slug: arlula-tasking-search-request-example
- key_count: 2
  name: Arlula Test Response Example
  slug: arlula-test-response-example
features:
- description: Search a global satellite image archive from multiple providers using area-of-interest (polygon/bounding box) and temporal filters to find available historical scenes.
  name: Archive Search
- description: Commission future satellite captures by searching tasking opportunities and placing orders for specific areas of interest and time windows.
  name: Satellite Tasking
- description: Access imagery from multiple satellite providers through a single unified API, enabling price and resolution comparisons across providers.
  name: Multi-Provider Access
- description: Choose from available product bundles (e.g., analytic, visual) when ordering scenes to match data requirements and budget.
  name: Bundle Selection
- description: Download delivered imagery resources including GeoTIFF files, preview images, and metadata through the Orders API after capture and processing.
  name: Dataset Download
- description: Place multiple archive or tasking orders in a single batch API request to efficiently process large-scale imagery acquisitions.
  name: Batch Ordering
finops:
- name: Arlula Finops
  service_category: API
  slug: arlula-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arlula.png
json_schemas:
- name: ArchiveOrderRequest
  property_count: 6
  slug: arlula-archive-order-request
- name: ArchiveScene
  property_count: 8
  slug: arlula-archive-scene
- name: ArchiveSearchRequest
  property_count: 8
  slug: arlula-archive-search-request
- name: BatchArchiveOrderRequest
  property_count: 3
  slug: arlula-batch-archive-order-request
- name: BatchTaskingOrderRequest
  property_count: 2
  slug: arlula-batch-tasking-order-request
- name: Bundle
  property_count: 3
  slug: arlula-bundle
- name: Campaign
  property_count: 3
  slug: arlula-campaign
- name: CampaignsListResponse
  property_count: 1
  slug: arlula-campaigns-list-response
- name: CancelResponse
  property_count: 2
  slug: arlula-cancel-response
- name: Dataset
  property_count: 4
  slug: arlula-dataset
- name: DatasetsListResponse
  property_count: 1
  slug: arlula-datasets-list-response
- name: OrderResponse
  property_count: 3
  slug: arlula-order-response
- name: Order
  property_count: 4
  slug: arlula-order
- name: OrdersListResponse
  property_count: 1
  slug: arlula-orders-list-response
- name: Resource
  property_count: 3
  slug: arlula-resource
- name: TaskingOpportunity
  property_count: 6
  slug: arlula-tasking-opportunity
- name: TaskingOrderRequest
  property_count: 8
  slug: arlula-tasking-order-request
- name: TaskingSearchRequest
  property_count: 10
  slug: arlula-tasking-search-request
- name: TestResponse
  property_count: 2
  slug: arlula-test-response
json_structures:
- name: Arlula Archive Order Request Structure
  property_count: 0
  slug: arlula-archive-order-request-structure
- name: Arlula Archive Scene Structure
  property_count: 0
  slug: arlula-archive-scene-structure
- name: Arlula Archive Search Request Structure
  property_count: 0
  slug: arlula-archive-search-request-structure
- name: Arlula Batch Archive Order Request Structure
  property_count: 0
  slug: arlula-batch-archive-order-request-structure
- name: Arlula Batch Tasking Order Request Structure
  property_count: 0
  slug: arlula-batch-tasking-order-request-structure
- name: Arlula Bundle Structure
  property_count: 0
  slug: arlula-bundle-structure
- name: Arlula Campaign Structure
  property_count: 0
  slug: arlula-campaign-structure
- name: Arlula Campaigns List Response Structure
  property_count: 0
  slug: arlula-campaigns-list-response-structure
- name: Arlula Cancel Response Structure
  property_count: 0
  slug: arlula-cancel-response-structure
- name: Arlula Dataset Structure
  property_count: 0
  slug: arlula-dataset-structure
- name: Arlula Datasets List Response Structure
  property_count: 0
  slug: arlula-datasets-list-response-structure
- name: Arlula Order Response Structure
  property_count: 0
  slug: arlula-order-response-structure
- name: Arlula Order Structure
  property_count: 0
  slug: arlula-order-structure
- name: Arlula Orders List Response Structure
  property_count: 0
  slug: arlula-orders-list-response-structure
- name: Arlula Resource Structure
  property_count: 0
  slug: arlula-resource-structure
- name: Arlula Tasking Opportunity Structure
  property_count: 0
  slug: arlula-tasking-opportunity-structure
- name: Arlula Tasking Order Request Structure
  property_count: 0
  slug: arlula-tasking-order-request-structure
- name: Arlula Tasking Search Request Structure
  property_count: 0
  slug: arlula-tasking-search-request-structure
- name: Arlula Test Response Structure
  property_count: 0
  slug: arlula-test-response-structure
jsonld:
- class_count: 19
  name: Arlula Api Context
  property_count: 26
  slug: arlula-api-context
layout: provider
modified: '2026-05-19'
name: Arlula
nav: Providers
network: true
overview: 'Arlula publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Archive API, Connection API, Orders API, and 1 more. Tagged areas include Earth Observation, Geospatial, Imagery, Remote Sensing, and Satellites.


  The Arlula catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Arlula''s developer surface includes authentication, documentation, getting-started guide, developer portal, engineering blog, and 8 more developer resources.'
plans:
- name: Arlula Plans Pricing
  plan_count: 3
  slug: arlula-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Arlula Rate Limits
  slug: arlula-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Arlula API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: arlula-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: Arlula API Rules
  rule_count: 38
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 21
  slug: arlula-spectral-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 29.6
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arlula/refs/heads/main/screenshots/arlula-2026-06-20T172434.png
security:
- kind: authentication
  name: Arlula Authentication
  slug: arlula-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arlula Domain Security
  slug: arlula-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arlula
tags:
- Earth Observation
- Geospatial
- Imagery
- Remote Sensing
- Satellites
use_cases:
- description: Search and order archive or tasking imagery to monitor crop health, irrigation patterns, and field conditions over growing seasons.
  name: Agricultural Monitoring
- description: Acquire multi-temporal satellite imagery to detect deforestation, coastal erosion, urban expansion, or disaster impact areas.
  name: Environmental Change Detection
- description: Order high-resolution imagery for remote inspection of pipelines, power lines, roads, and construction site progress monitoring.
  name: Infrastructure Inspection
- description: Rapidly search and order post-event imagery to assess damage extent and support emergency response and recovery planning.
  name: Disaster Response
website: https://arlula.com/
---
