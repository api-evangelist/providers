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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 49
  human_in_the_loop: 1
  name: Wikipedia Agentic Access
  operation_count: 125
  slug: wikipedia-agentic-access
  summary_line: 125 operations · 49 acting · 1 human-in-the-loop
api_count: 33
apis:
- description: On-demand API
  name: Wikipedia / MediaWiki articles API
  slug: wikipedia-articles-api
- description: Login, logout, token retrieval (action=login, clientlogin, logout, query&meta=tokens)
  name: Wikipedia / MediaWiki Authentication API
  slug: wikipedia-authentication-api
- description: Realtime Batch API
  name: Wikipedia / MediaWiki batches API
  slug: wikipedia-batches-api
- description: generation of citation data
  name: Wikipedia / MediaWiki Citation API
  slug: wikipedia-citation-api
- description: Metadata
  name: Wikipedia / MediaWiki codes API
  slug: wikipedia-codes-api
- description: Create/modify page content (action=edit)
  name: Wikipedia / MediaWiki Edit API
  slug: wikipedia-edit-api
- description: Media file metadata
  name: Wikipedia / MediaWiki Files API
  slug: wikipedia-files-api
- description: Page revision history and edit statistics
  name: Wikipedia / MediaWiki History API
  slug: wikipedia-history-api
- description: Metadata
  name: Wikipedia / MediaWiki languages API
  slug: wikipedia-languages-api
- description: Page relationships - language and media links
  name: Wikipedia / MediaWiki Links API
  slug: wikipedia-links-api
- description: formula rendering
  name: Wikipedia / MediaWiki Math API
  slug: wikipedia-math-api
- description: Metadata operations (action=opensearch, action=feedrecentchanges)
  name: Wikipedia / MediaWiki Meta API
  slug: wikipedia-meta-api
- description: The Mobile API from Wikipedia / MediaWiki — 3 operation(s) for mobile.
  name: Wikipedia / MediaWiki Mobile API
  slug: wikipedia-mobile-api
- description: Metadata
  name: Wikipedia / MediaWiki namespaces API
  slug: wikipedia-namespaces-api
- description: The offline API from Wikipedia / MediaWiki — 2 operation(s) for offline.
  name: Wikipedia / MediaWiki offline API
  slug: wikipedia-offline-api
- description: page content in different formats
  name: Wikipedia / MediaWiki Page content API
  slug: wikipedia-page-content-api
- description: Page metadata, HTML, source, create, update
  name: Wikipedia / MediaWiki Pages API
  slug: wikipedia-pages-api
- description: Wikitext parsing (action=parse)
  name: Wikipedia / MediaWiki Parse API
  slug: wikipedia-parse-api
- description: Mark edits as patrolled (action=patrol)
  name: Wikipedia / MediaWiki Patrol API
  slug: wikipedia-patrol-api
- description: Metadata
  name: Wikipedia / MediaWiki projects API
  slug: wikipedia-projects-api
- description: Read-only data retrieval (action=query) — pages, revisions, links, search
  name: Wikipedia / MediaWiki Query API
  slug: wikipedia-query-api
- description: Private lists of selected pages
  name: Wikipedia / MediaWiki Reading lists API
  slug: wikipedia-reading-lists-api
- description: contribution recommendations
  name: Wikipedia / MediaWiki Recommendation API
  slug: wikipedia-recommendation-api
- description: Individual revision retrieval and comparison
  name: Wikipedia / MediaWiki Revisions API
  slug: wikipedia-revisions-api
- description: Title and full-text search
  name: Wikipedia / MediaWiki Search API
  slug: wikipedia-search-api
- description: Snapshot API
  name: Wikipedia / MediaWiki snapshots API
  slug: wikipedia-snapshots-api
- description: SPARQL 1.1 query endpoint
  name: Wikipedia / MediaWiki SPARQL API
  slug: wikipedia-sparql-api
- description: (Beta) Structured Contents On-demand API
  name: Wikipedia / MediaWiki structured-contents API
  slug: wikipedia-structured-contents-api
- description: (BETA) Structured Contents Snapshot API
  name: Wikipedia / MediaWiki structured-snapshots API
  slug: wikipedia-structured-snapshots-api
- description: The Talk pages API from Wikipedia / MediaWiki — 2 operation(s) for talk pages.
  name: Wikipedia / MediaWiki Talk pages API
  slug: wikipedia-talk-pages-api
- description: Wikitext <-> HTML transformation
  name: Wikipedia / MediaWiki Transforms API
  slug: wikipedia-transforms-api
- description: File upload (action=upload)
  name: Wikipedia / MediaWiki Upload API
  slug: wikipedia-upload-api
- description: The wikidata API from Wikipedia / MediaWiki — 3 operation(s) for wikidata.
  name: Wikipedia / MediaWiki wikidata API
  slug: wikipedia-wikidata-api
artifact_total: 289
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wikipedia-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wikipedia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wikipedia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wikipedia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wikipedia.org
- group: start
  title: ''
  type: APIPortal
  url: https://api.wikimedia.org/wiki/Main_Page
- group: other
  title: ''
  type: APICatalog
  url: https://api.wikimedia.org/wiki/API_catalog
- group: docs
  title: ''
  type: Documentation
  url: https://www.mediawiki.org/wiki/API:Main_page
- group: other
  title: ''
  type: Foundation
  url: https://wikimediafoundation.org/
- group: other
  title: ''
  type: Governance
  url: https://meta.wikimedia.org/wiki/Wikimedia_Foundation
- group: commercial
  title: CC BY-SA 4.0 (article content)
  type: License
  url: https://creativecommons.org/licenses/by-sa/4.0/
- group: commercial
  title: CC0 1.0 (Wikidata)
  type: License
  url: https://creativecommons.org/publicdomain/zero/1.0/
- group: other
  title: API Usage Guidelines
  type: Policy
  url: https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_API_Usage_Guidelines
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wikimedia
- group: build
  title: Wikimedia Enterprise GitHub Org
  type: GitHubOrganization
  url: https://github.com/wikimedia-enterprise
- group: build
  title: Wikimedia Deutschland (Wikidata) GitHub Org
  type: GitHubOrganization
  url: https://github.com/wmde
- group: build
  title: Wikimedia Gerrit (canonical source)
  type: SourceCode
  url: https://gerrit.wikimedia.org/
- group: operate
  title: ''
  type: Status
  url: https://www.wikimediastatus.net/
- group: other
  title: Wikimedia Database Dumps
  type: BulkDownload
  url: https://dumps.wikimedia.org/
- group: other
  title: EventStreams (SSE)
  type: Stream
  url: https://stream.wikimedia.org/v2/stream
- group: build
  title: MCP Server (Wikipedia, Python, Rudra-ravi)
  type: Tools
  url: https://github.com/Rudra-ravi/wikipedia-mcp
- group: build
  title: MCP Server (Wikipedia, TypeScript, timjuenemann)
  type: Tools
  url: https://github.com/timjuenemann/wikipedia-mcp
- group: build
  title: MCP Server (Wikipedia, .NET, ajayindfw)
  type: Tools
  url: https://github.com/ajayindfw/WikipediaMcpServer
- group: build
  title: MCP Server (Wikipedia, Vercel HTTP, Ravishka17)
  type: Tools
  url: https://github.com/Ravishka17/Wikipedia-MCP
- group: build
  title: MCP Server (Wikipedia caching+batch, 1999AZZAR)
  type: Tools
  url: https://github.com/1999AZZAR/wikipedia-mcp-server
- group: build
  title: MCP Server (MediaWiki multi-wiki, shiquda)
  type: Tools
  url: https://github.com/shiquda/mediawiki-mcp-server
- group: build
  title: MCP Server (MediaWiki search+edit, olgasafonova)
  type: Tools
  url: https://github.com/olgasafonova/mediawiki-mcp-server
- group: build
  title: MCP Server (MediaWiki authoring, mbruton)
  type: Tools
  url: https://github.com/mbruton/mediawiki-mcp
- group: build
  title: MCP Server (Wikidata, Wikimedia Deutschland)
  type: Tools
  url: https://github.com/wmde/WikidataMCP
- group: build
  title: MCP Server (Wikidata SPARQL, cyanheads)
  type: Tools
  url: https://github.com/cyanheads/wikidata-mcp-server
- group: commercial
  title: ''
  type: Plans
  url: plans/wikipedia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wikipedia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wikipedia-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/wikipedia-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wikipedia-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/wikipedia-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://wikimediafoundation.org/news/feed/
created: '2026-05-28'
description: 'Wikipedia is the free, multilingual online encyclopedia operated by the non-profit Wikimedia Foundation. The platform exposes its content and structured data through several public APIs: the original MediaWiki Action API (action=query|edit|parse|upload), the MediaWiki Core REST API (page CRUD, search, transforms), the Wikimedia REST API (page summaries, mobile HTML, math, citation, reading lists, recommendations), the Wikidata Query Service SPARQL endpoint (structured knowledge graph queries), and the Wikimedia Enterprise APIs (commercial Snapshot, On-demand, Realtime). All free APIs are governed by the Wikimedia API usage guidelines: contactable User-Agent, serial requests, maxlag for bots.'
examples:
- key_count: 4
  name: Mediawiki Action Api Action Api Error Example
  slug: mediawiki-action-api-action-api-error-example
- key_count: 22
  name: Mediawiki Action Api Action Api Write Request Example
  slug: mediawiki-action-api-action-api-write-request-example
- key_count: 8
  name: Mediawiki Action Api Action Result Example
  slug: mediawiki-action-api-action-result-example
- key_count: 3
  name: Mediawiki Core Rest Compare Response Example
  slug: mediawiki-core-rest-compare-response-example
- key_count: 5
  name: Mediawiki Core Rest Create Page Request Example
  slug: mediawiki-core-rest-create-page-request-example
- key_count: 2
  name: Mediawiki Core Rest Edit Counts Example
  slug: mediawiki-core-rest-edit-counts-example
- key_count: 5
  name: Mediawiki Core Rest File Example
  slug: mediawiki-core-rest-file-example
- key_count: 4
  name: Mediawiki Core Rest History Response Example
  slug: mediawiki-core-rest-history-response-example
- key_count: 4
  name: Mediawiki Core Rest Language Link Example
  slug: mediawiki-core-rest-language-link-example
- key_count: 9
  name: Mediawiki Core Rest Page Example
  slug: mediawiki-core-rest-page-example
- key_count: 10
  name: Mediawiki Core Rest Revision Example
  slug: mediawiki-core-rest-revision-example
- key_count: 1
  name: Mediawiki Core Rest Search Response Example
  slug: mediawiki-core-rest-search-response-example
- key_count: 7
  name: Mediawiki Core Rest Search Result Example
  slug: mediawiki-core-rest-search-result-example
- key_count: 5
  name: Mediawiki Core Rest Update Page Request Example
  slug: mediawiki-core-rest-update-page-request-example
- key_count: 2
  name: Rest V1 Cx Dict Example
  slug: rest-v1-cx-dict-example
- key_count: 1
  name: Rest V1 Cx Mt Example
  slug: rest-v1-cx-mt-example
- key_count: 5
  name: Rest V1 List Entry Read Example
  slug: rest-v1-list-entry-read-example
- key_count: 2
  name: Rest V1 List Entry Write Example
  slug: rest-v1-list-entry-write-example
- key_count: 5
  name: Rest V1 List Read Example
  slug: rest-v1-list-read-example
- key_count: 2
  name: Rest V1 List Write Example
  slug: rest-v1-list-write-example
- key_count: 2
  name: Rest V1 Listing Example
  slug: rest-v1-listing-example
- key_count: 6
  name: Rest V1 Media Item Example
  slug: rest-v1-media-item-example
- key_count: 3
  name: Rest V1 Media List Example
  slug: rest-v1-media-list-example
- key_count: 3
  name: Rest V1 Originalimage Example
  slug: rest-v1-originalimage-example
- key_count: 4
  name: Rest V1 Problem Example
  slug: rest-v1-problem-example
- key_count: 2
  name: Rest V1 Recommendation Result Example
  slug: rest-v1-recommendation-result-example
- key_count: 3
  name: Rest V1 Result Example
  slug: rest-v1-result-example
- key_count: 2
  name: Rest V1 Revision Example
  slug: rest-v1-revision-example
- key_count: 2
  name: Rest V1 Revision Identifier Example
  slug: rest-v1-revision-identifier-example
- key_count: 12
  name: Rest V1 Revision Info Example
  slug: rest-v1-revision-info-example
- key_count: 1
  name: Rest V1 Revisions Example
  slug: rest-v1-revisions-example
- key_count: 13
  name: Rest V1 Summary Example
  slug: rest-v1-summary-example
- key_count: 3
  name: Rest V1 Thumbnail Example
  slug: rest-v1-thumbnail-example
- key_count: 3
  name: Rest V1 Titles Set Example
  slug: rest-v1-titles-set-example
- key_count: 3
  name: Wikidata Sparql Sparql Results Example
  slug: wikidata-sparql-sparql-results-example
- key_count: 2
  name: Wikimedia Enterprise Article Body Example
  slug: wikimedia-enterprise-article-body-example
- key_count: 20
  name: Wikimedia Enterprise Article Example
  slug: wikimedia-enterprise-article-example
- key_count: 1
  name: Wikimedia Enterprise Article Namespace Example
  slug: wikimedia-enterprise-article-namespace-example
- key_count: 7
  name: Wikimedia Enterprise Batch Example
  slug: wikimedia-enterprise-batch-example
- key_count: 2
  name: Wikimedia Enterprise Category Example
  slug: wikimedia-enterprise-category-example
- key_count: 3
  name: Wikimedia Enterprise Citation Example
  slug: wikimedia-enterprise-citation-example
- key_count: 3
  name: Wikimedia Enterprise Code Example
  slug: wikimedia-enterprise-code-example
- key_count: 7
  name: Wikimedia Enterprise Editor Example
  slug: wikimedia-enterprise-editor-example
- key_count: 2
  name: Wikimedia Enterprise Entity Example
  slug: wikimedia-enterprise-entity-example
- key_count: 3
  name: Wikimedia Enterprise Event Example
  slug: wikimedia-enterprise-event-example
- key_count: 2
  name: Wikimedia Enterprise Filter Example
  slug: wikimedia-enterprise-filter-example
- key_count: 10
  name: Wikimedia Enterprise Image Example
  slug: wikimedia-enterprise-image-example
- key_count: 4
  name: Wikimedia Enterprise Language Example
  slug: wikimedia-enterprise-language-example
- key_count: 3
  name: Wikimedia Enterprise License Example
  slug: wikimedia-enterprise-license-example
- key_count: 3
  name: Wikimedia Enterprise Link Example
  slug: wikimedia-enterprise-link-example
- key_count: 4
  name: Wikimedia Enterprise Maintenance Tags Example
  slug: wikimedia-enterprise-maintenance-tags-example
- key_count: 3
  name: Wikimedia Enterprise Namespace Example
  slug: wikimedia-enterprise-namespace-example
- key_count: 8
  name: Wikimedia Enterprise Part Example
  slug: wikimedia-enterprise-part-example
- key_count: 5
  name: Wikimedia Enterprise Project Example
  slug: wikimedia-enterprise-project-example
- key_count: 3
  name: Wikimedia Enterprise Protection Example
  slug: wikimedia-enterprise-protection-example
- key_count: 2
  name: Wikimedia Enterprise Redirect Example
  slug: wikimedia-enterprise-redirect-example
- key_count: 7
  name: Wikimedia Enterprise Reference Example
  slug: wikimedia-enterprise-reference-example
- key_count: 1
  name: Wikimedia Enterprise Referenceneed Example
  slug: wikimedia-enterprise-referenceneed-example
- key_count: 1
  name: Wikimedia Enterprise Referencerisk Example
  slug: wikimedia-enterprise-referencerisk-example
- key_count: 2
  name: Wikimedia Enterprise Revertrisk Example
  slug: wikimedia-enterprise-revertrisk-example
- key_count: 3
  name: Wikimedia Enterprise Scores Example
  slug: wikimedia-enterprise-scores-example
- key_count: 2
  name: Wikimedia Enterprise Size Example
  slug: wikimedia-enterprise-size-example
- key_count: 8
  name: Wikimedia Enterprise Snapshot Example
  slug: wikimedia-enterprise-snapshot-example
- key_count: 18
  name: Wikimedia Enterprise Structured Content Example
  slug: wikimedia-enterprise-structured-content-example
- key_count: 4
  name: Wikimedia Enterprise Table Example
  slug: wikimedia-enterprise-table-example
- key_count: 2
  name: Wikimedia Enterprise Template Example
  slug: wikimedia-enterprise-template-example
- key_count: 3
  name: Wikimedia Enterprise Thumbnail Example
  slug: wikimedia-enterprise-thumbnail-example
- key_count: 9
  name: Wikimedia Enterprise Version Example
  slug: wikimedia-enterprise-version-example
- key_count: 3
  name: Wikimedia Enterprise Visibility Example
  slug: wikimedia-enterprise-visibility-example
- key_count: 13
  name: Wikimedia Enterprise Wikidata Article Example
  slug: wikimedia-enterprise-wikidata-article-example
- key_count: 7
  name: Wikimedia Enterprise Wikidata Entity Example
  slug: wikimedia-enterprise-wikidata-entity-example
- key_count: 3
  name: Wikimedia Enterprise Wikidata Entity Property Example
  slug: wikimedia-enterprise-wikidata-entity-property-example
- key_count: 2
  name: Wikimedia Enterprise Wikidata Entity Qualifier Example
  slug: wikimedia-enterprise-wikidata-entity-qualifier-example
- key_count: 2
  name: Wikimedia Enterprise Wikidata Entity Reference Part Example
  slug: wikimedia-enterprise-wikidata-entity-reference-part-example
- key_count: 2
  name: Wikimedia Enterprise Wikidata Entity Statement Reference Example
  slug: wikimedia-enterprise-wikidata-entity-statement-reference-example
- key_count: 4
  name: Wikimedia Enterprise Wikidata Entity Value Example
  slug: wikimedia-enterprise-wikidata-entity-value-example
- key_count: 2
  name: Wikimedia Enterprise Wikidata Labels Example
  slug: wikimedia-enterprise-wikidata-labels-example
- key_count: 3
  name: Wikimedia Enterprise Wikidata Sitelinks Example
  slug: wikimedia-enterprise-wikidata-sitelinks-example
- key_count: 6
  name: Wikimedia Enterprise Wikidata Statement Example
  slug: wikimedia-enterprise-wikidata-statement-example
finops:
- name: Wikipedia Finops
  service_category: Open Knowledge Data Feeds
  slug: wikipedia-finops
image: https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/120px-Wikipedia-logo-v2.svg.png
json_schemas:
- name: ActionApiError
  property_count: 4
  slug: mediawiki-action-api-action-api-error
- name: ActionApiWriteRequest
  property_count: 22
  slug: mediawiki-action-api-action-api-write-request
- name: ActionResult
  property_count: 8
  slug: mediawiki-action-api-action-result
- name: CompareResponse
  property_count: 3
  slug: mediawiki-core-rest-compare-response
- name: CreatePageRequest
  property_count: 5
  slug: mediawiki-core-rest-create-page-request
- name: EditCounts
  property_count: 2
  slug: mediawiki-core-rest-edit-counts
- name: File
  property_count: 5
  slug: mediawiki-core-rest-file
- name: HistoryResponse
  property_count: 4
  slug: mediawiki-core-rest-history-response
- name: LanguageLink
  property_count: 4
  slug: mediawiki-core-rest-language-link
- name: Page
  property_count: 9
  slug: mediawiki-core-rest-page
- name: Revision
  property_count: 10
  slug: mediawiki-core-rest-revision
- name: SearchResponse
  property_count: 1
  slug: mediawiki-core-rest-search-response
- name: SearchResult
  property_count: 7
  slug: mediawiki-core-rest-search-result
- name: UpdatePageRequest
  property_count: 5
  slug: mediawiki-core-rest-update-page-request
- name: cx_dict
  property_count: 2
  slug: rest-v1-cx-dict
- name: cx_mt
  property_count: 1
  slug: rest-v1-cx-mt
- name: list_entry_read
  property_count: 5
  slug: rest-v1-list-entry-read
- name: list_entry_write
  property_count: 2
  slug: rest-v1-list-entry-write
- name: list_read
  property_count: 5
  slug: rest-v1-list-read
- name: list_write
  property_count: 2
  slug: rest-v1-list-write
- name: listing
  property_count: 2
  slug: rest-v1-listing
- name: media_item
  property_count: 6
  slug: rest-v1-media-item
- name: media_list
  property_count: 3
  slug: rest-v1-media-list
- name: morelike_result
  property_count: 0
  slug: rest-v1-morelike-result
- name: originalimage
  property_count: 3
  slug: rest-v1-originalimage
- name: problem
  property_count: 4
  slug: rest-v1-problem
- name: recommendation_result
  property_count: 2
  slug: rest-v1-recommendation-result
- name: result
  property_count: 3
  slug: rest-v1-result
- name: revisionIdentifier
  property_count: 2
  slug: rest-v1-revision-identifier
- name: revisionInfo
  property_count: 12
  slug: rest-v1-revision-info
- name: revision
  property_count: 2
  slug: rest-v1-revision
- name: revisions
  property_count: 1
  slug: rest-v1-revisions
- name: summary
  property_count: 13
  slug: rest-v1-summary
- name: thumbnail
  property_count: 3
  slug: rest-v1-thumbnail
- name: titles_set
  property_count: 3
  slug: rest-v1-titles-set
- name: SparqlResults
  property_count: 3
  slug: wikidata-sparql-sparql-results
- name: article_body
  property_count: 2
  slug: wikimedia-enterprise-article-body
- name: article_namespace
  property_count: 1
  slug: wikimedia-enterprise-article-namespace
- name: article
  property_count: 20
  slug: wikimedia-enterprise-article
- name: batch
  property_count: 7
  slug: wikimedia-enterprise-batch
- name: category
  property_count: 2
  slug: wikimedia-enterprise-category
- name: citation
  property_count: 3
  slug: wikimedia-enterprise-citation
- name: code
  property_count: 3
  slug: wikimedia-enterprise-code
- name: editor
  property_count: 7
  slug: wikimedia-enterprise-editor
- name: entity
  property_count: 2
  slug: wikimedia-enterprise-entity
- name: event
  property_count: 3
  slug: wikimedia-enterprise-event
- name: filter
  property_count: 2
  slug: wikimedia-enterprise-filter
- name: image
  property_count: 10
  slug: wikimedia-enterprise-image
- name: language
  property_count: 4
  slug: wikimedia-enterprise-language
- name: license
  property_count: 3
  slug: wikimedia-enterprise-license
- name: link
  property_count: 3
  slug: wikimedia-enterprise-link
- name: maintenance_tags
  property_count: 4
  slug: wikimedia-enterprise-maintenance-tags
- name: namespace
  property_count: 3
  slug: wikimedia-enterprise-namespace
- name: part
  property_count: 8
  slug: wikimedia-enterprise-part
- name: project
  property_count: 5
  slug: wikimedia-enterprise-project
- name: protection
  property_count: 3
  slug: wikimedia-enterprise-protection
- name: redirect
  property_count: 2
  slug: wikimedia-enterprise-redirect
- name: reference
  property_count: 7
  slug: wikimedia-enterprise-reference
- name: referenceneed
  property_count: 1
  slug: wikimedia-enterprise-referenceneed
- name: referencerisk
  property_count: 1
  slug: wikimedia-enterprise-referencerisk
- name: revertrisk
  property_count: 2
  slug: wikimedia-enterprise-revertrisk
- name: scores
  property_count: 3
  slug: wikimedia-enterprise-scores
- name: size
  property_count: 2
  slug: wikimedia-enterprise-size
- name: snapshot
  property_count: 8
  slug: wikimedia-enterprise-snapshot
- name: structured-content
  property_count: 18
  slug: wikimedia-enterprise-structured-content
- name: table
  property_count: 4
  slug: wikimedia-enterprise-table
- name: template
  property_count: 2
  slug: wikimedia-enterprise-template
- name: thumbnail
  property_count: 3
  slug: wikimedia-enterprise-thumbnail
- name: version
  property_count: 9
  slug: wikimedia-enterprise-version
- name: visibility
  property_count: 3
  slug: wikimedia-enterprise-visibility
- name: wikidata_article
  property_count: 13
  slug: wikimedia-enterprise-wikidata-article
- name: wikidata_entity_property
  property_count: 3
  slug: wikimedia-enterprise-wikidata-entity-property
- name: wikidata_entity_qualifier
  property_count: 2
  slug: wikimedia-enterprise-wikidata-entity-qualifier
- name: wikidata_entity_reference_part
  property_count: 2
  slug: wikimedia-enterprise-wikidata-entity-reference-part
- name: wikidata_entity
  property_count: 7
  slug: wikimedia-enterprise-wikidata-entity
- name: wikidata_entity_statement_reference
  property_count: 2
  slug: wikimedia-enterprise-wikidata-entity-statement-reference
- name: wikidata_entity_value
  property_count: 4
  slug: wikimedia-enterprise-wikidata-entity-value
- name: wikidata_labels
  property_count: 0
  slug: wikimedia-enterprise-wikidata-labels
- name: wikidata_sitelinks
  property_count: 3
  slug: wikimedia-enterprise-wikidata-sitelinks
- name: wikidata_statement
  property_count: 6
  slug: wikimedia-enterprise-wikidata-statement
- name: wikidata_statements
  property_count: 0
  slug: wikimedia-enterprise-wikidata-statements
json_structures:
- name: Mediawiki Action Api Action Api Error Structure
  property_count: 4
  slug: mediawiki-action-api-action-api-error-structure
- name: Mediawiki Action Api Action Api Write Request Structure
  property_count: 22
  slug: mediawiki-action-api-action-api-write-request-structure
- name: Mediawiki Action Api Action Result Structure
  property_count: 8
  slug: mediawiki-action-api-action-result-structure
- name: Mediawiki Core Rest Compare Response Structure
  property_count: 3
  slug: mediawiki-core-rest-compare-response-structure
- name: Mediawiki Core Rest Create Page Request Structure
  property_count: 5
  slug: mediawiki-core-rest-create-page-request-structure
- name: Mediawiki Core Rest Edit Counts Structure
  property_count: 2
  slug: mediawiki-core-rest-edit-counts-structure
- name: Mediawiki Core Rest File Structure
  property_count: 5
  slug: mediawiki-core-rest-file-structure
- name: Mediawiki Core Rest History Response Structure
  property_count: 4
  slug: mediawiki-core-rest-history-response-structure
- name: Mediawiki Core Rest Language Link Structure
  property_count: 3
  slug: mediawiki-core-rest-language-link-structure
- name: Mediawiki Core Rest Page Structure
  property_count: 9
  slug: mediawiki-core-rest-page-structure
- name: Mediawiki Core Rest Revision Structure
  property_count: 10
  slug: mediawiki-core-rest-revision-structure
- name: Mediawiki Core Rest Search Response Structure
  property_count: 1
  slug: mediawiki-core-rest-search-response-structure
- name: Mediawiki Core Rest Search Result Structure
  property_count: 7
  slug: mediawiki-core-rest-search-result-structure
- name: Mediawiki Core Rest Update Page Request Structure
  property_count: 5
  slug: mediawiki-core-rest-update-page-request-structure
- name: Rest V1 Cx Dict Structure
  property_count: 2
  slug: rest-v1-cx-dict-structure
- name: Rest V1 Cx Mt Structure
  property_count: 1
  slug: rest-v1-cx-mt-structure
- name: Rest V1 List Entry Read Structure
  property_count: 5
  slug: rest-v1-list-entry-read-structure
- name: Rest V1 List Entry Write Structure
  property_count: 2
  slug: rest-v1-list-entry-write-structure
- name: Rest V1 List Read Structure
  property_count: 5
  slug: rest-v1-list-read-structure
- name: Rest V1 List Write Structure
  property_count: 2
  slug: rest-v1-list-write-structure
- name: Rest V1 Listing Structure
  property_count: 2
  slug: rest-v1-listing-structure
- name: Rest V1 Media Item Structure
  property_count: 6
  slug: rest-v1-media-item-structure
- name: Rest V1 Media List Structure
  property_count: 3
  slug: rest-v1-media-list-structure
- name: Rest V1 Morelike Result Structure
  property_count: 0
  slug: rest-v1-morelike-result-structure
- name: Rest V1 Originalimage Structure
  property_count: 3
  slug: rest-v1-originalimage-structure
- name: Rest V1 Problem Structure
  property_count: 4
  slug: rest-v1-problem-structure
- name: Rest V1 Recommendation Result Structure
  property_count: 2
  slug: rest-v1-recommendation-result-structure
- name: Rest V1 Result Structure
  property_count: 3
  slug: rest-v1-result-structure
- name: Rest V1 Revision Identifier Structure
  property_count: 2
  slug: rest-v1-revision-identifier-structure
- name: Rest V1 Revision Info Structure
  property_count: 12
  slug: rest-v1-revision-info-structure
- name: Rest V1 Revision Structure
  property_count: 2
  slug: rest-v1-revision-structure
- name: Rest V1 Revisions Structure
  property_count: 1
  slug: rest-v1-revisions-structure
- name: Rest V1 Summary Structure
  property_count: 13
  slug: rest-v1-summary-structure
- name: Rest V1 Thumbnail Structure
  property_count: 3
  slug: rest-v1-thumbnail-structure
- name: Rest V1 Titles Set Structure
  property_count: 3
  slug: rest-v1-titles-set-structure
- name: Wikidata Sparql Sparql Results Structure
  property_count: 3
  slug: wikidata-sparql-sparql-results-structure
- name: Wikimedia Enterprise Article Body Structure
  property_count: 2
  slug: wikimedia-enterprise-article-body-structure
- name: Wikimedia Enterprise Article Namespace Structure
  property_count: 1
  slug: wikimedia-enterprise-article-namespace-structure
- name: Wikimedia Enterprise Article Structure
  property_count: 20
  slug: wikimedia-enterprise-article-structure
- name: Wikimedia Enterprise Batch Structure
  property_count: 7
  slug: wikimedia-enterprise-batch-structure
- name: Wikimedia Enterprise Category Structure
  property_count: 2
  slug: wikimedia-enterprise-category-structure
- name: Wikimedia Enterprise Citation Structure
  property_count: 3
  slug: wikimedia-enterprise-citation-structure
- name: Wikimedia Enterprise Code Structure
  property_count: 3
  slug: wikimedia-enterprise-code-structure
- name: Wikimedia Enterprise Editor Structure
  property_count: 7
  slug: wikimedia-enterprise-editor-structure
- name: Wikimedia Enterprise Entity Structure
  property_count: 2
  slug: wikimedia-enterprise-entity-structure
- name: Wikimedia Enterprise Event Structure
  property_count: 3
  slug: wikimedia-enterprise-event-structure
- name: Wikimedia Enterprise Filter Structure
  property_count: 2
  slug: wikimedia-enterprise-filter-structure
- name: Wikimedia Enterprise Image Structure
  property_count: 10
  slug: wikimedia-enterprise-image-structure
- name: Wikimedia Enterprise Language Structure
  property_count: 4
  slug: wikimedia-enterprise-language-structure
- name: Wikimedia Enterprise License Structure
  property_count: 3
  slug: wikimedia-enterprise-license-structure
- name: Wikimedia Enterprise Link Structure
  property_count: 3
  slug: wikimedia-enterprise-link-structure
- name: Wikimedia Enterprise Maintenance Tags Structure
  property_count: 4
  slug: wikimedia-enterprise-maintenance-tags-structure
- name: Wikimedia Enterprise Namespace Structure
  property_count: 3
  slug: wikimedia-enterprise-namespace-structure
- name: Wikimedia Enterprise Part Structure
  property_count: 8
  slug: wikimedia-enterprise-part-structure
- name: Wikimedia Enterprise Project Structure
  property_count: 5
  slug: wikimedia-enterprise-project-structure
- name: Wikimedia Enterprise Protection Structure
  property_count: 3
  slug: wikimedia-enterprise-protection-structure
- name: Wikimedia Enterprise Redirect Structure
  property_count: 2
  slug: wikimedia-enterprise-redirect-structure
- name: Wikimedia Enterprise Reference Structure
  property_count: 7
  slug: wikimedia-enterprise-reference-structure
- name: Wikimedia Enterprise Referenceneed Structure
  property_count: 1
  slug: wikimedia-enterprise-referenceneed-structure
- name: Wikimedia Enterprise Referencerisk Structure
  property_count: 1
  slug: wikimedia-enterprise-referencerisk-structure
- name: Wikimedia Enterprise Revertrisk Structure
  property_count: 2
  slug: wikimedia-enterprise-revertrisk-structure
- name: Wikimedia Enterprise Scores Structure
  property_count: 3
  slug: wikimedia-enterprise-scores-structure
- name: Wikimedia Enterprise Size Structure
  property_count: 2
  slug: wikimedia-enterprise-size-structure
- name: Wikimedia Enterprise Snapshot Structure
  property_count: 8
  slug: wikimedia-enterprise-snapshot-structure
- name: Wikimedia Enterprise Structured Content Structure
  property_count: 18
  slug: wikimedia-enterprise-structured-content-structure
- name: Wikimedia Enterprise Table Structure
  property_count: 4
  slug: wikimedia-enterprise-table-structure
- name: Wikimedia Enterprise Template Structure
  property_count: 2
  slug: wikimedia-enterprise-template-structure
- name: Wikimedia Enterprise Thumbnail Structure
  property_count: 3
  slug: wikimedia-enterprise-thumbnail-structure
- name: Wikimedia Enterprise Version Structure
  property_count: 9
  slug: wikimedia-enterprise-version-structure
- name: Wikimedia Enterprise Visibility Structure
  property_count: 3
  slug: wikimedia-enterprise-visibility-structure
- name: Wikimedia Enterprise Wikidata Article Structure
  property_count: 13
  slug: wikimedia-enterprise-wikidata-article-structure
- name: Wikimedia Enterprise Wikidata Entity Property Structure
  property_count: 3
  slug: wikimedia-enterprise-wikidata-entity-property-structure
- name: Wikimedia Enterprise Wikidata Entity Qualifier Structure
  property_count: 2
  slug: wikimedia-enterprise-wikidata-entity-qualifier-structure
- name: Wikimedia Enterprise Wikidata Entity Reference Part Structure
  property_count: 2
  slug: wikimedia-enterprise-wikidata-entity-reference-part-structure
- name: Wikimedia Enterprise Wikidata Entity Statement Reference Structure
  property_count: 2
  slug: wikimedia-enterprise-wikidata-entity-statement-reference-structure
- name: Wikimedia Enterprise Wikidata Entity Structure
  property_count: 7
  slug: wikimedia-enterprise-wikidata-entity-structure
- name: Wikimedia Enterprise Wikidata Entity Value Structure
  property_count: 4
  slug: wikimedia-enterprise-wikidata-entity-value-structure
- name: Wikimedia Enterprise Wikidata Labels Structure
  property_count: 0
  slug: wikimedia-enterprise-wikidata-labels-structure
- name: Wikimedia Enterprise Wikidata Sitelinks Structure
  property_count: 3
  slug: wikimedia-enterprise-wikidata-sitelinks-structure
- name: Wikimedia Enterprise Wikidata Statement Structure
  property_count: 6
  slug: wikimedia-enterprise-wikidata-statement-structure
- name: Wikimedia Enterprise Wikidata Statements Structure
  property_count: 0
  slug: wikimedia-enterprise-wikidata-statements-structure
jsonld:
- class_count: 7
  name: Wikipedia Context
  property_count: 0
  slug: wikipedia-context
- class_count: 3
  name: Wikipedia Mediawiki Action Api Context
  property_count: 34
  slug: wikipedia-mediawiki-action-api-context
- class_count: 11
  name: Wikipedia Mediawiki Core Rest Context
  property_count: 45
  slug: wikipedia-mediawiki-core-rest-context
- class_count: 20
  name: Wikipedia Rest V1 Context
  property_count: 56
  slug: wikipedia-rest-v1-context
- class_count: 1
  name: Wikipedia Wikidata Sparql Context
  property_count: 5
  slug: wikipedia-wikidata-sparql-context
- class_count: 44
  name: Wikipedia Wikimedia Enterprise Context
  property_count: 87
  slug: wikipedia-wikimedia-enterprise-context
layout: provider
modified: '2026-05-29'
name: Wikipedia / MediaWiki
nav: Providers
network: true
overview: 'Wikipedia / MediaWiki publishes 33 APIs on the [APIs.io](https://apis.io/) network, including articles API, Authentication API, batches API, and 30 more. Tagged areas include Open Data, Public APIs, Open Knowledge, Encyclopedia, and Knowledge Graph.


  The Wikipedia / MediaWiki catalog on APIs.io includes 6 JSON-LD contexts and 2 Spectral governance rulesets.


  Wikipedia / MediaWiki''s developer surface includes authentication, documentation, status page, tooling, engineering blog, and 33 more developer resources.'
plans:
- name: Wikipedia Plans Pricing
  plan_count: 3
  slug: wikipedia-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 9
  name: Wikipedia Rate Limits
  slug: wikipedia-rate-limits
rules:
- name: Wikipedia / MediaWiki API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wikipedia-jsonschema-spectral-rules
- name: Wikipedia / MediaWiki API Rules
  rule_count: 29
  severity_counts:
    error: 8
    hint: 0
    info: 5
    warn: 16
  slug: wikipedia-spectral-rules
score:
  band: developing
  composite: 46.1
  delta: -5.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.0
    developer_ergonomics: 21.7
    discoverability: 87.0
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 33
      marker_coverage: 100.0
      total: 33
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wikipedia/refs/heads/main/screenshots/wikipedia-2026-06-20T201453.png
security:
- kind: authentication
  name: Wikipedia Authentication
  slug: wikipedia-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wikipedia Domain Security
  slug: wikipedia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wikipedia Vulnerability Disclosure
  slug: wikipedia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wikipedia
tags:
- Open Data
- Public APIs
- Open Knowledge
- Encyclopedia
- Knowledge Graph
- Open Source
- Non-Profit
website: https://www.wikipedia.org
---
