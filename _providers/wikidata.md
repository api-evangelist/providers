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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Wikidata Agentic Access
  operation_count: 11
  slug: wikidata-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 9
apis:
- description: The MediaWiki Action API provides batch entity retrieval, editing, and search for Wikidata via wbgetentities, wbsearchentities, wbeditentity, and other actions. Supports up to 50 entities per request.
  name: MediaWiki Action API
  slug: mediawiki-action-api
- description: The Wikidata Query Service provides a SPARQL 1.1 endpoint at query.wikidata.org for running complex graph queries over the full Wikidata knowledge base. Supports federated queries, GeoSPARQL, and time
  name: SPARQL Query Service
  slug: sparql-query-service
- description: The Wikidata Linked Data Interface provides individual entity data via content negotiation at http://www.wikidata.org/entity/{QID}. Supports JSON, JSON-LD, RDF/XML, Turtle, and N-Triples output format
  name: Linked Data Interface
  slug: linked-data-interface
- description: The Wikimedia Event Stream provides real-time Server-Sent Events (SSE) for Wikidata changes, revision creations, and page events. Available at stream.wikimedia.org. Ideal for monitoring Wikidata edits
  name: Recent Changes Event Stream
  slug: event-stream
- description: Description management
  name: Wikidata Descriptions API
  slug: wikidata-descriptions-api
- description: Wikidata item (Q-entity) operations
  name: Wikidata Items API
  slug: wikidata-items-api
- description: Label management
  name: Wikidata Labels API
  slug: wikidata-labels-api
- description: Wikidata property (P-entity) operations
  name: Wikidata Properties API
  slug: wikidata-properties-api
- description: Statement (claim) operations
  name: Wikidata Statements API
  slug: wikidata-statements-api
artifact_total: 75
collections:
- collection_type: postman
  name: Wikidata REST API & MediaWiki Descriptions API
  slug: postman-wikidata-descriptions-api
- collection_type: postman
  name: Wikidata REST API & MediaWiki Descriptions Items API
  slug: postman-wikidata-items-api
- collection_type: postman
  name: Wikidata REST API & MediaWiki Descriptions Labels API
  slug: postman-wikidata-labels-api
- collection_type: postman
  name: Wikidata REST API & MediaWiki Descriptions Properties API
  slug: postman-wikidata-properties-api
- collection_type: postman
  name: Wikidata REST API & MediaWiki Descriptions Statements API
  slug: postman-wikidata-statements-api
- collection_type: open
  name: Wikidata REST API & MediaWiki API
  slug: open-wikidata-mediawiki
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wikidata/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wikidata-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wikidata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wikidata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wikidata-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wikidata-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wikidata-wf
- group: company
  title: ''
  type: Website
  url: https://www.wikidata.org/
- group: start
  title: ''
  type: Portal
  url: https://www.wikidata.org/wiki/Wikidata:Data_access
- group: docs
  title: ''
  type: Documentation
  url: https://www.wikidata.org/wiki/Wikidata:Data_access
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wikimedia
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/wikimedia/mediawiki
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundation.wikimedia.org/wiki/Terms_of_Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foundation.wikimedia.org/wiki/Privacy_policy
- group: operate
  title: ''
  type: Support
  url: https://www.wikidata.org/wiki/Wikidata:Contact_the_development_team
- group: company
  title: ''
  type: Blog
  url: https://blog.wikimedia.org/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.wikimediastatus.net/
- group: operate
  title: ''
  type: RateLimits
  url: https://www.mediawiki.org/wiki/API:Etiquette
- group: auth
  title: ''
  type: Authentication
  url: https://www.mediawiki.org/wiki/OAuth/For_Developers
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/rules/wikidata-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/vocabulary/wikidata-vocabulary.yaml
created: '2025-01-01'
description: Wikidata is a free, collaborative, multilingual knowledge graph hosted by the Wikimedia Foundation. It provides structured linked data for Wikipedia and other Wikimedia projects, as well as a public platform for anyone to read and edit. Wikidata exposes several APIs including a Wikibase REST API for entity read/write operations, the MediaWiki Action API for batch entity retrieval and editing, a SPARQL endpoint for complex graph queries, Linked Data URIs for individual entity access in multiple RDF formats, a real-time Server-Sent Events stream for change monitoring, and full database dumps for bulk data processing.
examples:
- key_count: 2
  name: Wikidata Data  Value Example
  slug: wikidata-data--value-example
- key_count: 10
  name: Wikidata Entity Example
  slug: wikidata-entity-example
- key_count: 6
  name: Wikidata Item  Create Example
  slug: wikidata-item--create-example
- key_count: 7
  name: Wikidata Item Example
  slug: wikidata-item-example
- key_count: 4
  name: Wikidata Patch  Request Example
  slug: wikidata-patch--request-example
- key_count: 5
  name: Wikidata Property Example
  slug: wikidata-property-example
- key_count: 3
  name: Wikidata Sitelink Example
  slug: wikidata-sitelink-example
- key_count: 6
  name: Wikidata Statement  Create Example
  slug: wikidata-statement--create-example
- key_count: 6
  name: Wikidata Statement Example
  slug: wikidata-statement-example
features:
- description: All entities support labels, descriptions, and aliases in hundreds of languages via BCP 47 language codes.
  name: Multilingual Support
- description: Every claim is modeled as a statement with property, value, rank, qualifiers, and references for full provenance.
  name: Structured Statements
- description: All Wikidata content is released under CC0 1.0 Universal (Public Domain) — no attribution required.
  name: Open License
- description: Complex multi-hop queries over 100M+ entities via SPARQL 1.1 at query.wikidata.org with GeoSPARQL and time extensions.
  name: SPARQL Graph Queries
- description: Server-Sent Events at stream.wikimedia.org deliver real-time change notifications for Wikidata edits.
  name: Real-Time Event Streaming
- description: Entities available as JSON, JSON-LD, RDF/XML, Turtle, and N-Triples via content negotiation on Linked Data URIs.
  name: Multiple Serialization Formats
- description: Wikidata is an instance of Wikibase; federated SPARQL queries can cross Wikibase instances including Wikimedia Commons.
  name: Wikibase Federation
- description: Full JSON and RDF/TTL database dumps refreshed weekly at dumps.wikimedia.org for local bulk processing.
  name: Database Dumps
finops:
- name: Wikidata Finops
  service_category: Open Knowledge Graph
  slug: wikidata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wikidata.png
integrations:
- description: Wikidata powers structured data for all Wikipedia language editions via Lua modules and infobox templates.
  name: Wikipedia
- description: Media files on Wikimedia Commons are described using Wikidata items via structured data on Commons.
  name: Wikimedia Commons
- description: OSM features are linked to Wikidata via the wikidata=* tag, enabling geographic entity cross-referencing.
  name: OpenStreetMap
- description: Scholia is a Wikidata-based scholarly profile service that visualizes publications, authors, and institutions.
  name: Scholia
- description: Reasonator renders human-readable pages for Wikidata items, integrating maps, timelines, and media.
  name: Reasonator
- description: Mix'n'match links Wikidata items to external databases (VIAF, ORCID, GND, etc.) for authority control.
  name: Mix'n'match
- description: OpenRefine has a Wikidata reconciliation service and can batch-upload tabular data as Wikidata statements.
  name: OpenRefine
json_schemas:
- name: DataValue
  property_count: 2
  slug: wikidata-data--value
- name: Wikidata Entity
  property_count: 10
  slug: wikidata-entity
- name: ItemCreate
  property_count: 6
  slug: wikidata-item--create
- name: Item
  property_count: 7
  slug: wikidata-item
- name: PatchRequest
  property_count: 4
  slug: wikidata-patch--request
- name: Property
  property_count: 5
  slug: wikidata-property
- name: Sitelink
  property_count: 3
  slug: wikidata-sitelink
- name: StatementCreate
  property_count: 6
  slug: wikidata-statement--create
- name: Statement
  property_count: 6
  slug: wikidata-statement
json_structures:
- name: Wikidata Data  Value Structure
  property_count: 2
  slug: wikidata-data--value-structure
- name: Wikidata Entity Structure
  property_count: 10
  slug: wikidata-entity-structure
- name: Wikidata Item  Create Structure
  property_count: 6
  slug: wikidata-item--create-structure
- name: Wikidata Item Structure
  property_count: 7
  slug: wikidata-item-structure
- name: Wikidata Patch  Request Structure
  property_count: 4
  slug: wikidata-patch--request-structure
- name: Wikidata Property Structure
  property_count: 5
  slug: wikidata-property-structure
- name: Wikidata Sitelink Structure
  property_count: 3
  slug: wikidata-sitelink-structure
- name: Wikidata Statement  Create Structure
  property_count: 6
  slug: wikidata-statement--create-structure
- name: Wikidata Statement Structure
  property_count: 6
  slug: wikidata-statement-structure
jsonld:
- class_count: 10
  name: Wikidata Context
  property_count: 27
  slug: wikidata-context
layout: provider
modified: '2026-05-19'
name: Wikidata
nav: Providers
network: true
overview: 'Wikidata publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Descriptions API, Items API, Labels API, and 2 more. Tagged areas include Knowledge Graph, Linked Data, Open Data, Semantic Web, and SPARQL.


  The Wikidata catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wikidata''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 16 more developer resources.'
plans:
- name: Wikidata Plans Pricing
  plan_count: 2
  slug: wikidata-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 4
  name: Wikidata Rate Limits
  slug: wikidata-rate-limits
rules:
- name: Wikidata API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wikidata-jsonschema-spectral-rules
- name: Wikidata API Rules
  rule_count: 37
  severity_counts:
    error: 12
    hint: 0
    info: 5
    warn: 20
  slug: wikidata-spectral-rules
scopes:
- name: Wikidata Scopes
  scope_count: 2
  slug: wikidata-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 62.3
  delta: -5.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 78.3
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/screenshots/wikidata-2026-06-20T201453.png
security:
- kind: authentication
  name: Wikidata Authentication
  slug: wikidata-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Wikidata Domain Security
  slug: wikidata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wikidata Vulnerability Disclosure
  slug: wikidata-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wikidata
tags:
- Knowledge Graph
- Linked Data
- Open Data
- Semantic Web
- SPARQL
- Wikipedia
use_cases:
- description: Enrich private datasets with structured Wikidata facts — entities, dates, relationships — via item and SPARQL queries.
  name: Knowledge Graph Augmentation
- description: Retrieve canonical statements with references to verify biographical, geographic, or scientific claims in text.
  name: Fact-Checking and Verification
- description: Power Wikipedia infoboxes and sister-project templates with live Wikidata entity data via the MediaWiki Action API.
  name: Wikipedia Infobox Data
- description: Resolve named entities from natural language to Wikidata Q-IDs using wbsearchentities and SPARQL label lookups.
  name: NLP Entity Linking
- description: Build ontology-aware search systems using Wikidata's P31 (instance of) and P279 (subclass of) property hierarchies.
  name: Semantic Search
- description: Track real-time edits to Wikidata entities relevant to a domain using the SSE event stream.
  name: Change Monitoring
- description: Publish organizational data as Linked Open Data by aligning custom schemas to Wikidata properties and Q-IDs.
  name: Linked Open Data Publishing
website: https://www.wikidata.org/
---
