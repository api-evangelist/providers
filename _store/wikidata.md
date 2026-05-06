---
aid: wikidata
name: Wikidata
description: Wikidata is a free, collaborative, multilingual knowledge graph hosted by the Wikimedia Foundation. It provides structured linked data for Wikipedia and other Wikimedia projects, as well as a public platform for anyone to read and edit. Wikidata exposes several APIs including a Wikibase REST API for entity read/write operations, the MediaWiki Action API for batch entity retrieval and editing, a SPARQL endpoint for complex graph queries, Linked Data URIs for individual entity access in multiple RDF formats, a real-time Server-Sent Events stream for change monitoring, and full database dumps for bulk data processing.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Knowledge Graph
  - Linked Data
  - Open Data
  - Semantic Web
  - SPARQL
  - Wikipedia
created: '2025-01-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wikidata:wikibase-rest-api
    name: Wikibase REST API
    description: The Wikibase REST API provides OpenAPI-based read and write operations for Wikidata entities (items and properties), including labels, descriptions, aliases, statements, sitelinks, and patches. Authentication via OAuth2 or MediaWiki session is required for write operations.
    humanURL: https://www.wikidata.org/wiki/Wikidata:REST_API
    baseURL: https://www.wikidata.org/w/rest.php/wikibase/v0
    tags:
      - Knowledge Graph
      - Entities
      - Items
      - Properties
      - Statements
      - Linked Data
    properties:
      - type: Documentation
        url: https://www.wikidata.org/wiki/Wikidata:REST_API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/openapi/wikidata-mediawiki-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/json-schema/wikidata-entity-schema.json
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/json-ld/wikidata-context.jsonld
  - aid: wikidata:mediawiki-action-api
    name: MediaWiki Action API
    description: The MediaWiki Action API provides batch entity retrieval, editing, and search for Wikidata via wbgetentities, wbsearchentities, wbeditentity, and other actions. Supports up to 50 entities per request. Accessible at wikidata.org/w/api.php.
    humanURL: https://www.mediawiki.org/wiki/Wikibase/API
    baseURL: https://www.wikidata.org/w/api.php
    tags:
      - MediaWiki
      - Batch Operations
      - Entity Retrieval
      - Search
    properties:
      - type: Documentation
        url: https://www.mediawiki.org/wiki/Wikibase/API
      - type: SDK
        url: https://pypi.org/project/pywikibot/
        title: Pywikibot (Python)
      - type: SDK
        url: https://www.npmjs.com/package/wikibase-sdk
        title: wikibase-sdk (JavaScript)
      - type: SDK
        url: https://www.wikidata.org/wiki/Wikidata:Tools/Wikidata_Toolkit
        title: Wikidata Toolkit (Java)
  - aid: wikidata:sparql-query-service
    name: SPARQL Query Service
    description: The Wikidata Query Service provides a SPARQL 1.1 endpoint at query.wikidata.org for running complex graph queries over the full Wikidata knowledge base. Supports federated queries, GeoSPARQL, and time-aware queries. Data is CC0 licensed.
    humanURL: https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service
    baseURL: https://query.wikidata.org/sparql
    tags:
      - SPARQL
      - Graph Query
      - Linked Data
      - Open Data
    properties:
      - type: Documentation
        url: https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual
      - type: APIReference
        url: https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples
  - aid: wikidata:linked-data-interface
    name: Linked Data Interface
    description: The Wikidata Linked Data Interface provides individual entity data via content negotiation at http://www.wikidata.org/entity/{QID}. Supports JSON, JSON-LD, RDF/XML, Turtle, and N-Triples output formats. No authentication required.
    humanURL: https://www.wikidata.org/wiki/Wikidata:Data_access#Linked_Data_Interface
    baseURL: https://www.wikidata.org/entity
    tags:
      - Linked Data
      - RDF
      - JSON-LD
      - Content Negotiation
    properties:
      - type: Documentation
        url: https://www.wikidata.org/wiki/Wikidata:Data_access#Linked_Data_Interface
  - aid: wikidata:event-stream
    name: Recent Changes Event Stream
    description: The Wikimedia Event Stream provides real-time Server-Sent Events (SSE) for Wikidata changes, revision creations, and page events. Available at stream.wikimedia.org. Ideal for monitoring Wikidata edits in near-real-time.
    humanURL: https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams
    baseURL: https://stream.wikimedia.org/v2/stream
    tags:
      - Event Streaming
      - Real-time
      - Server-Sent Events
      - Change Detection
    properties:
      - type: Documentation
        url: https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams
common:
  - type: Website
    url: https://www.wikidata.org/
  - type: Portal
    url: https://www.wikidata.org/wiki/Wikidata:Data_access
  - type: Documentation
    url: https://www.wikidata.org/wiki/Wikidata:Data_access
  - type: GitHubOrganization
    url: https://github.com/wikimedia
  - type: GitHubRepository
    url: https://github.com/wikimedia/mediawiki
  - type: TermsOfService
    url: https://foundation.wikimedia.org/wiki/Terms_of_Use
  - type: PrivacyPolicy
    url: https://foundation.wikimedia.org/wiki/Privacy_policy
  - type: Support
    url: https://www.wikidata.org/wiki/Wikidata:Contact_the_development_team
  - type: Blog
    url: https://blog.wikimedia.org/
  - type: StatusPage
    url: https://www.wikimediastatus.net/
  - type: RateLimits
    url: https://www.mediawiki.org/wiki/API:Etiquette
  - type: Authentication
    url: https://www.mediawiki.org/wiki/OAuth/For_Developers
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/rules/wikidata-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/vocabulary/wikidata-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/wikidata/refs/heads/main/capabilities/knowledge-graph-access.yaml
  - type: Features
    data:
      - name: Multilingual Support
        description: All entities support labels, descriptions, and aliases in hundreds of languages via BCP 47 language codes.
      - name: Structured Statements
        description: Every claim is modeled as a statement with property, value, rank, qualifiers, and references for full provenance.
      - name: Open License
        description: All Wikidata content is released under CC0 1.0 Universal (Public Domain) — no attribution required.
      - name: SPARQL Graph Queries
        description: Complex multi-hop queries over 100M+ entities via SPARQL 1.1 at query.wikidata.org with GeoSPARQL and time extensions.
      - name: Real-Time Event Streaming
        description: Server-Sent Events at stream.wikimedia.org deliver real-time change notifications for Wikidata edits.
      - name: Multiple Serialization Formats
        description: Entities available as JSON, JSON-LD, RDF/XML, Turtle, and N-Triples via content negotiation on Linked Data URIs.
      - name: Wikibase Federation
        description: Wikidata is an instance of Wikibase; federated SPARQL queries can cross Wikibase instances including Wikimedia Commons.
      - name: Database Dumps
        description: Full JSON and RDF/TTL database dumps refreshed weekly at dumps.wikimedia.org for local bulk processing.
  - type: UseCases
    data:
      - name: Knowledge Graph Augmentation
        description: Enrich private datasets with structured Wikidata facts — entities, dates, relationships — via item and SPARQL queries.
      - name: Fact-Checking and Verification
        description: Retrieve canonical statements with references to verify biographical, geographic, or scientific claims in text.
      - name: Wikipedia Infobox Data
        description: Power Wikipedia infoboxes and sister-project templates with live Wikidata entity data via the MediaWiki Action API.
      - name: NLP Entity Linking
        description: Resolve named entities from natural language to Wikidata Q-IDs using wbsearchentities and SPARQL label lookups.
      - name: Semantic Search
        description: Build ontology-aware search systems using Wikidata's P31 (instance of) and P279 (subclass of) property hierarchies.
      - name: Change Monitoring
        description: Track real-time edits to Wikidata entities relevant to a domain using the SSE event stream.
      - name: Linked Open Data Publishing
        description: Publish organizational data as Linked Open Data by aligning custom schemas to Wikidata properties and Q-IDs.
  - type: Integrations
    data:
      - name: Wikipedia
        description: Wikidata powers structured data for all Wikipedia language editions via Lua modules and infobox templates.
      - name: Wikimedia Commons
        description: Media files on Wikimedia Commons are described using Wikidata items via structured data on Commons.
      - name: OpenStreetMap
        description: OSM features are linked to Wikidata via the wikidata=* tag, enabling geographic entity cross-referencing.
      - name: Scholia
        description: Scholia is a Wikidata-based scholarly profile service that visualizes publications, authors, and institutions.
      - name: Reasonator
        description: Reasonator renders human-readable pages for Wikidata items, integrating maps, timelines, and media.
      - name: Mix'n'match
        description: Mix'n'match links Wikidata items to external databases (VIAF, ORCID, GND, etc.) for authority control.
      - name: OpenRefine
        description: OpenRefine has a Wikidata reconciliation service and can batch-upload tabular data as Wikidata statements.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
