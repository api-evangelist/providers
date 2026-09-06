---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Sitecore Agentic Access
  operation_count: 107
  slug: sitecore-agentic-access
  summary_line: 107 operations · 64 acting
api_count: 6
apis:
- description: The Sitecore XM Cloud GraphQL Delivery API provides access to approved and published content from Sitecore XM Cloud via a GraphQL endpoint optimized for production delivery. Developers use this API to
  name: Sitecore XM Cloud GraphQL Delivery API
  slug: xm-cloud-graphql-delivery-api
- description: The Sitecore XM Cloud Authoring and Management GraphQL API provides a single GraphQL endpoint and schema for managing Sitecore content programmatically. It supports creating, updating, and querying co
  name: Sitecore XM Cloud Authoring and Management GraphQL API
  slug: xm-cloud-authoring-management-graphql-api
- baseURL: https://api-engage-us.sitecorecloud.io
  baseurl_source: declared
  description: The Sitecore CDP Stream API enables applications to send real-time behavioral and transactional events about users to the Sitecore Customer Data Platform. It is designed for high-throughput event inge
  name: Sitecore CDP Stream API
  slug: cdp-stream-api
- description: The Sitecore CDP Batch API supports uploading large volumes of guest data and offline order records into Sitecore Customer Data Platform. It is intended for bulk data migration, historical data ingest
  name: Sitecore CDP Batch API
  slug: cdp-batch-api
- description: The Sitecore Content Hub Admin API is a GraphQL API that provides access to administrative functions within a Content Hub tenant, accessible at the path /api/graphql/admin/v1 relative to the Content H
  name: Sitecore Content Hub Admin API
  slug: content-hub-admin-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for retrieving and querying audit log entries that track changes to entities and configuration within the Content Hub instance.
  name: sitecore Audit API
  slug: sitecore-audit-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for obtaining access tokens used to authenticate API requests to Sitecore Discover.
  name: sitecore Authentication API
  slug: sitecore-authentication-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing buyer organizations and their associated users, user groups, addresses, credit cards, spending accounts, cost centers, and approval rules.
  name: sitecore Buyers API
  slug: sitecore-buyers-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating, retrieving, updating, and deleting site collections within an XM Cloud tenant. Collections group related sites that share resources and organizational context.
  name: sitecore Collections API
  slug: sitecore-collections-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating, retrieving, updating, and testing connections to external systems used in personalization flows and decision models. Connections define authentication credentials and URL confi
  name: sitecore Connections API
  slug: sitecore-connections-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing decision models that power programmatic targeting and offer selection logic within Sitecore Personalize. Decision models contain variant configurations and deployment settings.
  name: sitecore Decision Models API
  slug: sitecore-decision-models-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating and managing download orders that package assets for delivery, supporting both single and batch asset downloads.
  name: sitecore Download Orders API
  slug: sitecore-download-orders-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for performing CRUD operations on Content Hub entities including assets, taxonomy nodes, content items, and all other entity types managed within the platform.
  name: sitecore Entities API
  slug: sitecore-entities-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for sending behavioral and interaction events from storefronts to Sitecore Discover. Events include clicks, purchases, and page views that improve recommendation relevance over time.
  name: sitecore Events API
  slug: sitecore-events-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating, retrieving, and updating flow definitions that represent experiments, experiences, and personalization flows in Sitecore Personalize. Flows can be web-based, full-stack, or tri
  name: sitecore Flow Definitions API
  slug: sitecore-flow-definitions-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing custom key-value data extensions attached to guest profiles. Data extensions allow organizations to store additional structured information beyond the standard guest fields.
  name: sitecore Guest Data Extensions API
  slug: sitecore-guest-data-extensions-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating, retrieving, updating, and deleting guest profiles in Sitecore CDP. Guests represent the core customer entity storing personal, behavioral, and transactional data.
  name: sitecore Guests API
  slug: sitecore-guests-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for pushing real-time product catalog updates to Sitecore Discover without requiring a full feed re-index. Supports adding, updating, and removing products incrementally.
  name: sitecore Incremental Feed API
  slug: sitecore-incremental-feed-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing background job targets including retrieval, creation, update, and deletion of job configurations.
  name: sitecore Jobs API
  slug: sitecore-jobs-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing language availability at the tenant and site levels, including listing supported languages and adding or removing language options.
  name: sitecore Languages API
  slug: sitecore-languages-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing individual line items within guest orders, including product references, quantities, and pricing information.
  name: sitecore Order Items API
  slug: sitecore-order-items-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating, retrieving, updating, and deleting order records associated with guests. Orders capture purchase transactions including line items, payments, and fulfillment data.
  name: sitecore Orders API
  slug: sitecore-orders-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing site pages including full CRUD operations, versioning, variant management, layout editing, field value updates, and publishing state verification.
  name: sitecore Pages API
  slug: sitecore-pages-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating, retrieving, updating, and deleting products within the OrderCloud catalog. Products support extended properties, variants, specs, and inventory tracking.
  name: sitecore Products API
  slug: sitecore-products-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating and managing discount promotions and coupon codes that can be applied to orders at checkout.
  name: sitecore Promotions API
  slug: sitecore-promotions-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for creating, monitoring, and managing publishing jobs that push content from XM Cloud authoring to the Experience Edge delivery layer.
  name: sitecore Publishing Jobs API
  slug: sitecore-publishing-jobs-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for fetching entities that match specific criteria using structured query expressions against entity properties and relations.
  name: sitecore Querying API
  slug: sitecore-querying-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for performing product and content search queries, retrieving ranked results, applying faceted filters, and fetching personalized product recommendations based on behavioral data.
  name: sitecore Search and Recommendations API
  slug: sitecore-search-and-recommendations-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for executing search queries against the Content Hub entity index, retrieving facet values, and managing search filters.
  name: sitecore Search API
  slug: sitecore-search-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing entity selections across selection pools, allowing grouping of entities for bulk operations or editorial workflows.
  name: sitecore Selections API
  slug: sitecore-selections-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing sites within site collections, including creation, duplication, renaming, deletion, sorting, and retrieving site hierarchies and rendering hosts.
  name: sitecore Sites API
  slug: sitecore-sites-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for managing web and decision templates used to define the visual and logic components of personalization experiences within flows.
  name: sitecore Templates API
  slug: sitecore-templates-api
- baseURL: https://edge.sitecorecloud.io/api/graphql
  baseurl_source: declared
  description: Endpoints for uploading digital assets into Content Hub, including creating upload requests, uploading binary content, and completing asset ingest.
  name: sitecore Upload API
  slug: sitecore-upload-api
artifact_total: 87
asyncapis:
- description: The Sitecore CDP Stream API enables applications to send real-time behavioral and transactional events about users to the Sitecore Customer Data Platform. It is designed for high-throughput event inge
  name: Sitecore CDP Stream API
  slug: sitecore-cdp-stream-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sitecore CDP REST Audit API
  slug: open-sitecore-audit-api
- collection_type: open
  name: Sitecore CDP REST Audit Authentication API
  slug: open-sitecore-authentication-api
- collection_type: open
  name: Sitecore CDP REST Audit Buyers API
  slug: open-sitecore-buyers-api
- collection_type: open
  name: Sitecore CDP REST API
  slug: open-sitecore-cdp-rest-api
- collection_type: open
  name: Sitecore CDP REST Audit Collections API
  slug: open-sitecore-collections-api
- collection_type: open
  name: Sitecore CDP REST Audit Connections API
  slug: open-sitecore-connections-api
- collection_type: open
  name: Sitecore Content Hub REST API
  slug: open-sitecore-content-hub-rest-api
- collection_type: open
  name: Sitecore CDP REST Audit Decision Models API
  slug: open-sitecore-decision-models-api
- collection_type: open
  name: Sitecore Discover API
  slug: open-sitecore-discover-api
- collection_type: open
  name: Sitecore CDP REST Audit Download Orders API
  slug: open-sitecore-download-orders-api
- collection_type: open
  name: Sitecore CDP REST Audit Entities API
  slug: open-sitecore-entities-api
- collection_type: open
  name: Sitecore CDP REST Audit Events API
  slug: open-sitecore-events-api
- collection_type: open
  name: Sitecore CDP REST Audit Flow Definitions API
  slug: open-sitecore-flow-definitions-api
- collection_type: open
  name: Sitecore CDP REST Audit Guest Data Extensions API
  slug: open-sitecore-guest-data-extensions-api
- collection_type: open
  name: Sitecore CDP REST Audit Guests API
  slug: open-sitecore-guests-api
- collection_type: open
  name: Sitecore CDP REST Audit Incremental Feed API
  slug: open-sitecore-incremental-feed-api
- collection_type: open
  name: Sitecore CDP REST Audit Jobs API
  slug: open-sitecore-jobs-api
- collection_type: open
  name: Sitecore CDP REST Audit Languages API
  slug: open-sitecore-languages-api
- collection_type: open
  name: Sitecore CDP REST Audit Order Items API
  slug: open-sitecore-order-items-api
- collection_type: open
  name: Sitecore OrderCloud API
  slug: open-sitecore-ordercloud-api
- collection_type: open
  name: Sitecore CDP REST Audit Orders API
  slug: open-sitecore-orders-api
- collection_type: open
  name: Sitecore CDP REST Audit Pages API
  slug: open-sitecore-pages-api
- collection_type: open
  name: Sitecore Personalize REST API
  slug: open-sitecore-personalize-rest-api
- collection_type: open
  name: Sitecore CDP REST Audit Products API
  slug: open-sitecore-products-api
- collection_type: open
  name: Sitecore CDP REST Audit Promotions API
  slug: open-sitecore-promotions-api
- collection_type: open
  name: Sitecore CDP REST Audit Publishing Jobs API
  slug: open-sitecore-publishing-jobs-api
- collection_type: open
  name: Sitecore CDP REST Audit Querying API
  slug: open-sitecore-querying-api
- collection_type: open
  name: Sitecore CDP REST Audit Search and Recommendations API
  slug: open-sitecore-search-and-recommendations-api
- collection_type: open
  name: Sitecore CDP REST Audit Search API
  slug: open-sitecore-search-api
- collection_type: open
  name: Sitecore CDP REST Audit Selections API
  slug: open-sitecore-selections-api
- collection_type: open
  name: Sitecore CDP REST Audit Sites API
  slug: open-sitecore-sites-api
- collection_type: open
  name: Sitecore CDP REST Audit Templates API
  slug: open-sitecore-templates-api
- collection_type: open
  name: Sitecore CDP REST Audit Upload API
  slug: open-sitecore-upload-api
- collection_type: open
  name: Sitecore XM Cloud REST API
  slug: open-sitecore-xm-cloud-rest-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sitecore-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sitecore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sitecore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sitecore-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sitecore
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sitecore
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sitecore-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sitecore-cdp-guest-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sitecore-ordercloud-order-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/sitecore-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sitecore-vocabulary.yml
description: Sitecore is a global digital experience platform that combines content management, marketing automation, e-commerce, customer insight, and personalization to help brands deliver personalized customer experiences. Through its developer documentation at doc.sitecore.com and api-docs.sitecore.com, Sitecore provides REST, GraphQL, and event-streaming APIs spanning XM Cloud, Customer Data Platform, Personalize, OrderCloud, Content Hub, and Discover.
examples:
- key_count: 5
  name: Sitecore Cdp List Guests Example
  slug: sitecore-cdp-list-guests-example
- key_count: 5
  name: Sitecore Ordercloud List Products Example
  slug: sitecore-ordercloud-list-products-example
- key_count: 5
  name: Sitecore Xm Cloud List Collections Example
  slug: sitecore-xm-cloud-list-collections-example
finops:
- name: Sitecore Finops
  service_category: Digital Experience Platform
  slug: sitecore-finops
graphqls:
- description: The Sitecore XM Cloud GraphQL Delivery API provides access to approved and published content from Sitecore XM Cloud via a GraphQL endpoint optimized for production delivery. Developers use this API to
  name: sitecore GraphQL API
  slug: sitecore-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sitecore.png
json_schemas:
- name: Sitecore CDP Guest
  property_count: 13
  slug: sitecore-cdp-guest
- name: Sitecore OrderCloud Order
  property_count: 22
  slug: sitecore-ordercloud-order
json_structures:
- name: Sitecore Cdp Structure
  property_count: 0
  slug: sitecore-cdp-structure
- name: Sitecore Xm Cloud Structure
  property_count: 0
  slug: sitecore-xm-cloud-structure
jsonld:
- class_count: 0
  name: Sitecore Context
  property_count: 14
  slug: sitecore-context
layout: provider
modified: '2026-05-19'
name: Sitecore
nav: Providers
network: true
overview: 'Sitecore publishes 29 APIs on the [APIs.io](https://apis.io/) network, including CDP Stream API, Audit API, Authentication API, and 26 more.


  The Sitecore catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Sitecore''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Sitecore Plans Pricing
  plan_count: 1
  slug: sitecore-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Sitecore Rate Limits
  slug: sitecore-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Sitecore API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: sitecore-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Sitecore API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: sitecore-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Sitecore API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 6
  slug: sitecore-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.5
    catalog_earned_first_party: 0.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 75.1
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sitecore/refs/heads/main/screenshots/sitecore-2026-06-20T194003.png
security:
- kind: authentication
  name: Sitecore Authentication
  slug: sitecore-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Sitecore Domain Security
  slug: sitecore-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sitecore
---
