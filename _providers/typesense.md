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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 52
  human_in_the_loop: 5
  name: Typesense Agentic Access
  operation_count: 95
  slug: typesense-agentic-access
  summary_line: 95 operations · 52 acting · 5 human-in-the-loop
api_count: 25
apis:
- description: The core Typesense REST API for managing collections, indexing documents, and performing full-text, faceted, filtered, sorted, geo-based, and multi-search queries. Supports synonym sets, curation sets
  name: Typesense Search API
  slug: typesense-search-api
- description: The Typesense Vector Search API extends the core search capabilities with vector and hybrid search. It supports indexing embedding fields, querying by vector proximity, and combining semantic vector s
  name: Typesense Vector Search API
  slug: typesense-vector-search-api
- description: The Typesense Conversational Search API enables AI-powered question answering over your search index. It supports conversation models (OpenAI, Cloudflare Workers AI), NL search models, and stateful mu
  name: Typesense Conversational Search API
  slug: typesense-conversational-search-api
- description: Log and retrieve user interaction events such as clicks, conversions, and visits for tracking search behavior and personalization.
  name: Typesense Analytics Events API
  slug: typesense-analytics-events-api
- description: Operational endpoints for managing the analytics subsystem.
  name: Typesense Analytics Operations API
  slug: typesense-analytics-operations-api
- description: Create and manage analytics rules that control how search queries and user events are aggregated for query suggestions and relevance tuning.
  name: Typesense Analytics Rules API
  slug: typesense-analytics-rules-api
- description: Create and manage API keys with fine-grained access control on a per-collection, per-action, or per-record level.
  name: Typesense API Keys API
  slug: typesense-api-keys-api
- description: Create, retrieve, update, and terminate Typesense Cloud clusters. Manage cluster lifecycle and generate Typesense Server API keys.
  name: Typesense Cluster Management API
  slug: typesense-cluster-management-api
- description: Create and manage aliases that point to collections, enabling zero-downtime reindexing.
  name: Typesense Collection Aliases API
  slug: typesense-collection-aliases-api
- description: Create, retrieve, update, and delete collections. A collection is a group of related documents with a defined schema.
  name: Typesense Collections API
  slug: typesense-collections-api
- description: Server configuration management including slow request logging.
  name: Typesense Configuration API
  slug: typesense-configuration-api
- description: Schedule, retrieve, list, and cancel configuration changes to running clusters such as memory upgrades, version changes, and HA toggles.
  name: Typesense Configuration Changes API
  slug: typesense-configuration-changes-api
- description: Create and manage conversation models that define which LLM provider and configuration to use for generating conversational answers from search results.
  name: Typesense Conversation Models API
  slug: typesense-conversation-models-api
- description: Manage top-level curation sets for pinning, hiding, and boosting search results across collections.
  name: Typesense Curation Sets API
  slug: typesense-curation-sets-api
- description: Index, retrieve, update, delete, import, and export documents within a collection.
  name: Typesense Documents API
  slug: typesense-documents-api
- description: Health checks, debug information, metrics, and API statistics.
  name: Typesense Monitoring API
  slug: typesense-monitoring-api
- description: Send multiple search requests across one or more collections in a single HTTP request.
  name: Typesense Multi-Search API
  slug: typesense-multi-search-api
- description: Manage natural language search models used for query understanding and semantic matching.
  name: Typesense NL Search Models API
  slug: typesense-nl-search-models-api
- description: Cluster operations including snapshots, cache management, compaction, and voting.
  name: Typesense Operations API
  slug: typesense-operations-api
- description: Store and reference named sets of search parameters for reuse across queries.
  name: Typesense Presets API
  slug: typesense-presets-api
- description: Manage Typesense Server configuration parameters for cloud clusters.
  name: Typesense Server Configuration Parameters API
  slug: typesense-server-configuration-parameters-api
- description: Manage stemming dictionaries for custom word stemming rules.
  name: Typesense Stemming API
  slug: typesense-stemming-api
- description: Manage stopword sets that define keywords to be removed from search queries.
  name: Typesense Stopwords API
  slug: typesense-stopwords-api
- description: Manage top-level synonym sets that can be shared across multiple collections.
  name: Typesense Synonym Sets API
  slug: typesense-synonym-sets-api
- description: Create and manage collections with vector fields for semantic search and nearest-neighbor queries.
  name: Typesense Vector Collections API
  slug: typesense-vector-collections-api
artifact_total: 128
collections:
- collection_type: open
  name: Typesense Analytics API
  slug: open-typesense-analytics-api
- collection_type: open
  name: Typesense Cloud Management API
  slug: open-typesense-cloud-management-api
- collection_type: open
  name: Typesense Conversational Search API
  slug: open-typesense-conversational-search-api
- collection_type: open
  name: Typesense Search API
  slug: open-typesense-search-api
- collection_type: open
  name: Typesense Vector Search API
  slug: open-typesense-vector-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/typesense-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/typesense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/typesense-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/typesense
- group: company
  title: ''
  type: Website
  url: https://typesense.org
- group: docs
  title: ''
  type: Documentation
  url: https://typesense.org/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/typesense
- group: company
  title: ''
  type: Blog
  url: https://typesense.org/blog/
- group: operate
  title: ''
  type: Slack Community
  url: https://join.slack.com/t/typesense-community/shared_invite/zt-2fetvh0pw-ft5y2YQlq4FS3fVDFTfWJA
- group: other
  title: ''
  type: Docker Hub
  url: https://hub.docker.com/r/typesense/typesense
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/typesense
- group: commercial
  title: ''
  type: Pricing
  url: https://typesense.org/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://typesense.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://typesense.org/privacy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/typesense-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/typesense-collection-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/typesense-search-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/typesense-analytics-event-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/typesense-collection-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/typesense-search-result-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/typesense-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/typesense-rules.yml
created: '2026-05-03'
description: Typesense is a fast, typo-tolerant, open-source search engine designed for developer productivity. It provides instant search experiences with support for full-text search, faceting, filtering, sorting, geo-based search, vector search, and conversational AI search. Typesense is available as an open-source self-hosted solution or as a managed cloud service via Typesense Cloud.
examples:
- key_count: 2
  name: Typesense Create Collection Example
  slug: typesense-create-collection-example
- key_count: 2
  name: Typesense Index Document Example
  slug: typesense-index-document-example
- key_count: 2
  name: Typesense Multi Search Example
  slug: typesense-multi-search-example
- key_count: 2
  name: Typesense Search Example
  slug: typesense-search-example
features:
- 'Open Source: GPL v3 self-hosted, free at any scale'
- Cloud Small from ~$0.045/hr (0.5 GB RAM, single node)
- Cloud Medium from ~$0.18/hr (2 GB RAM, single node)
- 'Cloud HA Multi-node: ~3x base for 3-node cluster'
- 'Enterprise custom: dedicated support, self-hosted Enterprise license'
- Typo-tolerant full-text search
- Geosearch and faceted search
- Vector search and hybrid search
- Federated multi-collection search
- REST API with scoped API keys
- Configurable per-key rate limits
- InstantSearch.js compatibility
- Auto-suggestions and autocomplete
- Synonyms, stop words, stemming
- Curation rules for promoted results
- Open-source SDKs for many languages
finops:
- name: Typesense Finops
  service_category: Search
  slug: typesense-finops
graphqls:
- description: This GraphQL schema provides a conceptual type system for the [Typesense](https://typesense.org) open-source search engine REST API. Typesense is a fast, typo-tolerant search engine built for develope
  name: Typesense GraphQL Schema
  slug: typesense-graphql
image: https://typesense.org/favicon-32x32.png
json_schemas:
- name: Typesense Analytics Event
  property_count: 3
  slug: typesense-analytics-event
- name: AnalyticsEvent
  property_count: 4
  slug: typesense-analyticsevent
- name: AnalyticsEventCreateResponse
  property_count: 1
  slug: typesense-analyticseventcreateresponse
- name: AnalyticsEventCreateSchema
  property_count: 3
  slug: typesense-analyticseventcreateschema
- name: AnalyticsRule
  property_count: 4
  slug: typesense-analyticsrule
- name: AnalyticsRuleCreateSchema
  property_count: 3
  slug: typesense-analyticsrulecreateschema
- name: AnalyticsStatus
  property_count: 2
  slug: typesense-analyticsstatus
- name: ApiKey
  property_count: 7
  slug: typesense-apikey
- name: ApiKeySchema
  property_count: 5
  slug: typesense-apikeyschema
- name: ApiKeysResponse
  property_count: 1
  slug: typesense-apikeysresponse
- name: Cluster
  property_count: 15
  slug: typesense-cluster
- name: ClusterApiKeys
  property_count: 2
  slug: typesense-clusterapikeys
- name: ClusterCreateSchema
  property_count: 11
  slug: typesense-clustercreateschema
- name: ClusterUpdateSchema
  property_count: 2
  slug: typesense-clusterupdateschema
- name: Typesense Collection
  property_count: 11
  slug: typesense-collection
- name: CollectionAlias
  property_count: 2
  slug: typesense-collectionalias
- name: CollectionAliasesResponse
  property_count: 1
  slug: typesense-collectionaliasesresponse
- name: CollectionAliasSchema
  property_count: 1
  slug: typesense-collectionaliasschema
- name: CollectionResponse
  property_count: 8
  slug: typesense-collectionresponse
- name: CollectionSchema
  property_count: 9
  slug: typesense-collectionschema
- name: CollectionUpdateSchema
  property_count: 3
  slug: typesense-collectionupdateschema
- name: ConfigurationChange
  property_count: 8
  slug: typesense-configurationchange
- name: ConfigurationChangeCreateSchema
  property_count: 8
  slug: typesense-configurationchangecreateschema
- name: ConversationalSearchResult
  property_count: 5
  slug: typesense-conversationalsearchresult
- name: ConversationModel
  property_count: 6
  slug: typesense-conversationmodel
- name: ConversationModelCreateSchema
  property_count: 7
  slug: typesense-conversationmodelcreateschema
- name: ConversationModelUpdateSchema
  property_count: 4
  slug: typesense-conversationmodelupdateschema
- name: CurationItem
  property_count: 4
  slug: typesense-curationitem
- name: CurationItemSchema
  property_count: 3
  slug: typesense-curationitemschema
- name: CurationSet
  property_count: 1
  slug: typesense-curationset
- name: CurationSetSchema
  property_count: 1
  slug: typesense-curationsetschema
- name: DirtyValues
  property_count: 0
  slug: typesense-dirtyvalues
- name: EmbedConfig
  property_count: 2
  slug: typesense-embedconfig
- name: FacetCounts
  property_count: 3
  slug: typesense-facetcounts
- name: Field
  property_count: 17
  slug: typesense-field
- name: HealthStatus
  property_count: 1
  slug: typesense-healthstatus
- name: IndexAction
  property_count: 0
  slug: typesense-indexaction
- name: MultiSearchParameters
  property_count: 9
  slug: typesense-multisearchparameters
- name: MultiSearchResult
  property_count: 2
  slug: typesense-multisearchresult
- name: NLSearchModel
  property_count: 3
  slug: typesense-nlsearchmodel
- name: NLSearchModelCreateSchema
  property_count: 3
  slug: typesense-nlsearchmodelcreateschema
- name: NLSearchModelUpdateSchema
  property_count: 3
  slug: typesense-nlsearchmodelupdateschema
- name: Preset
  property_count: 2
  slug: typesense-preset
- name: PresetUpsertSchema
  property_count: 1
  slug: typesense-presetupsertschema
- name: SchemaChangeStatus
  property_count: 3
  slug: typesense-schemachangestatus
- name: Typesense Search Result
  property_count: 11
  slug: typesense-search-result
- name: SearchGroupedHit
  property_count: 3
  slug: typesense-searchgroupedhit
- name: SearchHighlight
  property_count: 7
  slug: typesense-searchhighlight
- name: SearchResult
  property_count: 11
  slug: typesense-searchresult
- name: SearchResultHit
  property_count: 8
  slug: typesense-searchresulthit
- name: ServerConfigurationParameters
  property_count: 3
  slug: typesense-serverconfigurationparameters
- name: StemmingDictionary
  property_count: 2
  slug: typesense-stemmingdictionary
- name: StopwordsSet
  property_count: 3
  slug: typesense-stopwordsset
- name: StopwordsSetUpsertSchema
  property_count: 2
  slug: typesense-stopwordssetupsertschema
- name: SuccessStatus
  property_count: 1
  slug: typesense-successstatus
- name: SynonymItem
  property_count: 3
  slug: typesense-synonymitem
- name: SynonymItemSchema
  property_count: 2
  slug: typesense-synonymitemschema
- name: SynonymSet
  property_count: 1
  slug: typesense-synonymset
- name: SynonymSetSchema
  property_count: 1
  slug: typesense-synonymsetschema
- name: VectorCollectionResponse
  property_count: 4
  slug: typesense-vectorcollectionresponse
- name: VectorCollectionSchema
  property_count: 4
  slug: typesense-vectorcollectionschema
- name: VectorField
  property_count: 8
  slug: typesense-vectorfield
- name: VectorMultiSearchParameters
  property_count: 8
  slug: typesense-vectormultisearchparameters
- name: VectorSearchHit
  property_count: 5
  slug: typesense-vectorsearchhit
- name: VectorSearchResult
  property_count: 6
  slug: typesense-vectorsearchresult
- name: VoiceQueryModelConfig
  property_count: 1
  slug: typesense-voicequerymodelconfig
json_structures:
- name: Typesense Collection Structure
  property_count: 7
  slug: typesense-collection-structure
- name: Typesense Search Result Structure
  property_count: 9
  slug: typesense-search-result-structure
- name: Typesense Structure
  property_count: 0
  slug: typesense-structure
jsonld:
- class_count: 0
  name: Typesense Context
  property_count: 12
  slug: typesense-context
layout: provider
modified: '2026-05-19'
name: Typesense
nav: Providers
network: true
overview: 'Typesense publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Search API, Vector Search API, Conversational Search API, and 22 more. Tagged areas include Full-Text Search, Open Source, Search Engine, Typo Tolerance, and Vector Search.


  The Typesense catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Typesense''s developer surface includes authentication, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Typesense Plans Pricing
  plan_count: 5
  slug: typesense-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Typesense Rate Limits
  slug: typesense-rate-limits
rules:
- name: Typesense API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: typesense-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.1
  delta: -3.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 69.3
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/typesense/refs/heads/main/screenshots/typesense-2026-06-20T195907.png
security:
- kind: authentication
  name: Typesense Authentication
  slug: typesense-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Typesense Domain Security
  slug: typesense-domain-security
  summary_line: TLSv1.3 · DMARC
slug: typesense
tags:
- Full-Text Search
- Open Source
- Search Engine
- Typo Tolerance
- Vector Search
website: https://typesense.org
---
