---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Wiktionary Agentic Access
  operation_count: 24
  slug: wiktionary-agentic-access
  summary_line: 24 operations · 3 acting
api_count: 11
apis:
- description: Wiktionary-specific structured multilingual definition endpoint
  name: Wiktionary Definition API
  slug: wiktionary-definition-api
- description: action=expandtemplates — Expand wikitext templates server-side
  name: Wiktionary ExpandTemplates API
  slug: wiktionary-expandtemplates-api
- description: File and media metadata
  name: Wiktionary File API
  slug: wiktionary-file-api
- description: Page history and revision details
  name: Wiktionary History API
  slug: wiktionary-history-api
- description: action=opensearch — OpenSearch suggestions protocol
  name: Wiktionary OpenSearch API
  slug: wiktionary-opensearch-api
- description: Page content, source, and HTML
  name: Wiktionary Page API
  slug: wiktionary-page-api
- description: Page HTML, summary, title metadata, and mobile-optimised HTML
  name: Wiktionary Page Content API
  slug: wiktionary-page-content-api
- description: action=parse — Render wikitext to HTML and parse section trees
  name: Wiktionary Parse API
  slug: wiktionary-parse-api
- description: action=query — Fetch wikitext, extracts, revisions, and search results
  name: Wiktionary Query API
  slug: wiktionary-query-api
- description: Title-prefix and full-text search
  name: Wiktionary Search API
  slug: wiktionary-search-api
- description: Parsoid wikitext ↔ HTML transforms and lint
  name: Wiktionary Transform API
  slug: wiktionary-transform-api
artifact_total: 154
collections:
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition API
  slug: postman-wiktionary-definition-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition ExpandTemplates API
  slug: postman-wiktionary-expandtemplates-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition File API
  slug: postman-wiktionary-file-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition History API
  slug: postman-wiktionary-history-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition OpenSearch API
  slug: postman-wiktionary-opensearch-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition Page API
  slug: postman-wiktionary-page-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition Page Content API
  slug: postman-wiktionary-page-content-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition Parse API
  slug: postman-wiktionary-parse-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition Query API
  slug: postman-wiktionary-query-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition Search API
  slug: postman-wiktionary-search-api
- collection_type: postman
  name: Wiktionary MediaWiki Core REST Definition Transform API
  slug: postman-wiktionary-transform-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wiktionary/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wiktionary-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wiktionary-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wiktionary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wiktionary-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wiktionary-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://en.wiktionary.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.wikimedia.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mediawiki.org/wiki/API
- group: docs
  title: ''
  type: APIReference
  url: https://www.mediawiki.org/wiki/API:Main_page
- group: build
  title: Wikimedia GitHub Mirror
  type: GitHubOrganization
  url: https://github.com/wikimedia
- group: build
  title: Wikimedia Gerrit (Canonical)
  type: GitHubOrganization
  url: https://gerrit.wikimedia.org/
- group: auth
  title: ''
  type: Authentication
  url: https://api.wikimedia.org/wiki/Authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://api.wikimedia.org/wiki/Rate_limits
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundation.wikimedia.org/wiki/Terms_of_Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foundation.wikimedia.org/wiki/Privacy_policy
- group: commercial
  title: Free (CC BY-SA 4.0)
  type: Pricing
  url: https://en.wiktionary.org/wiki/Wiktionary:About
- group: operate
  title: ''
  type: StatusPage
  url: https://www.wikimediastatus.net/
- group: company
  title: ''
  type: Blog
  url: https://diff.wikimedia.org/
- group: operate
  title: ''
  type: Support
  url: https://www.mediawiki.org/wiki/Project:Support_desk
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mediawiki.org/wiki/MediaWiki_1.42
- group: build
  title: Pywikibot (Python)
  type: SDKs
  url: https://www.mediawiki.org/wiki/Manual:Pywikibot
- group: build
  title: mwclient (Python)
  type: SDKs
  url: https://github.com/mwclient/mwclient
- group: build
  title: mwn (TypeScript/Node.js)
  type: SDKs
  url: https://github.com/siddharthvp/mwn
- group: build
  title: nodemw (Node.js)
  type: SDKs
  url: https://github.com/nodemw/nodemw
- group: build
  title: wikitools3 (Python)
  type: SDKs
  url: https://github.com/dmwilcox/wikitools3
- group: build
  title: wiki-java (Java)
  type: SDKs
  url: https://github.com/MER-C/wiki-java
- group: build
  title: jwiki (Java)
  type: SDKs
  url: https://github.com/Fastily/jwiki
- group: build
  title: mediawiki-api-base (PHP)
  type: SDKs
  url: https://github.com/addshore/mediawiki-api-base
- group: build
  title: mediawiki-ruby-api (Ruby)
  type: SDKs
  url: https://github.com/wikimedia/mediawiki-ruby-api
- group: build
  title: mwparserfromhell (Python wikitext parser)
  type: SDKs
  url: https://github.com/sadnub/mwparserfromhell
- group: build
  title: Pywikibot CLI
  type: CLI
  url: https://www.mediawiki.org/wiki/Manual:Pywikibot
- group: build
  title: Wikidata Query Service
  type: Tools
  url: https://github.com/Professor-G/MediaWikiAPI
- group: build
  title: MediaWiki Core
  type: GitHubRepository
  url: https://github.com/wikimedia/mediawiki
- group: build
  title: RESTBase
  type: GitHubRepository
  url: https://github.com/wikimedia/restbase
- group: build
  title: Parsoid (Wikitext ↔ HTML)
  type: GitHubRepository
  url: https://github.com/wikimedia/parsoid
- group: build
  title: Pywikibot
  type: GitHubRepository
  url: https://github.com/wikimedia/pywikibot
- group: design
  title: ''
  type: SpectralRules
  url: rules/wiktionary-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wiktionary-vocabulary.yml
created: '2026-05-28'
description: Wiktionary is the free, collaborative multilingual dictionary project of the Wikimedia Foundation, the dictionary sibling of Wikipedia. Programmatic access is exposed through the MediaWiki Action API at en.wiktionary.org/w/api.php, the older Wikimedia REST API at en.wiktionary.org/api/rest_v1/ (which provides Wiktionary-specific endpoints like /page/definition/{term}), and the newer MediaWiki Core REST API at en.wiktionary.org/w/rest.php. All Wiktionary content is licensed CC BY-SA 4.0 (and GFDL) and hosted by the Wikimedia Foundation.
examples:
- key_count: 5
  name: Core Rest Api File Metadata Example
  slug: core-rest-api-file-metadata-example
- key_count: 2
  name: Core Rest Api History Count Response Example
  slug: core-rest-api-history-count-response-example
- key_count: 4
  name: Core Rest Api History Response Example
  slug: core-rest-api-history-response-example
- key_count: 2
  name: Core Rest Api Latest Revision Example
  slug: core-rest-api-latest-revision-example
- key_count: 2
  name: Core Rest Api License Info Example
  slug: core-rest-api-license-info-example
- key_count: 7
  name: Core Rest Api Page Source Response Example
  slug: core-rest-api-page-source-response-example
- key_count: 8
  name: Core Rest Api Page With Html Response Example
  slug: core-rest-api-page-with-html-response-example
- key_count: 10
  name: Core Rest Api Revision Detail Example
  slug: core-rest-api-revision-detail-example
- key_count: 7
  name: Core Rest Api Search Page Example
  slug: core-rest-api-search-page-example
- key_count: 1
  name: Core Rest Api Search Response Example
  slug: core-rest-api-search-response-example
- key_count: 6
  name: Mediawiki Action Api Action Api Response Example
  slug: mediawiki-action-api-action-api-response-example
- key_count: 1
  name: Mediawiki Action Api Expand Templates Response Example
  slug: mediawiki-action-api-expand-templates-response-example
- key_count: 4
  name: Mediawiki Action Api Extract Page Example
  slug: mediawiki-action-api-extract-page-example
- key_count: 1
  name: Mediawiki Action Api Parse Response Example
  slug: mediawiki-action-api-parse-response-example
- key_count: 7
  name: Mediawiki Action Api Parse Section Example
  slug: mediawiki-action-api-parse-section-example
- key_count: 1
  name: Mediawiki Action Api Query Extracts Response Example
  slug: mediawiki-action-api-query-extracts-response-example
- key_count: 2
  name: Mediawiki Action Api Query Revisions Response Example
  slug: mediawiki-action-api-query-revisions-response-example
- key_count: 3
  name: Mediawiki Action Api Query Search Response Example
  slug: mediawiki-action-api-query-search-response-example
- key_count: 3
  name: Mediawiki Action Api Revision Example
  slug: mediawiki-action-api-revision-example
- key_count: 4
  name: Mediawiki Action Api Revision Page Example
  slug: mediawiki-action-api-revision-page-example
- key_count: 7
  name: Mediawiki Action Api Search Hit Example
  slug: mediawiki-action-api-search-hit-example
- key_count: 2
  name: Rest Api Content Urls Example
  slug: rest-api-content-urls-example
- key_count: 3
  name: Rest Api Definition Entry Example
  slug: rest-api-definition-entry-example
- key_count: 1
  name: Rest Api Definition Response Example
  slug: rest-api-definition-response-example
- key_count: 2
  name: Rest Api Html Transform Request Example
  slug: rest-api-html-transform-request-example
- key_count: 3
  name: Rest Api Language Entry Example
  slug: rest-api-language-entry-example
- key_count: 4
  name: Rest Api Lint Error Example
  slug: rest-api-lint-error-example
- key_count: 8
  name: Rest Api Page Summary Example
  slug: rest-api-page-summary-example
- key_count: 12
  name: Rest Api Revision Item Example
  slug: rest-api-revision-item-example
- key_count: 1
  name: Rest Api Revision Metadata Example
  slug: rest-api-revision-metadata-example
- key_count: 3
  name: Rest Api Wikitext Transform Request Example
  slug: rest-api-wikitext-transform-request-example
features:
- description: /page/definition/{term} returns dictionary entries broken down by source language, part of speech, definitions, and usage examples in structured JSON.
  name: Multilingual Definitions
- description: action=query&prop=wikitext returns raw wikitext for any page, enabling clients to build their own parsers and extractors.
  name: Wikitext Access
- description: /page/html/{title} and action=parse return Parsoid-generated HTML suitable for direct rendering in client apps.
  name: Rendered HTML
- description: action=opensearch implements the OpenSearch suggestions protocol so Wiktionary can power autocomplete in any search UI.
  name: OpenSearch Suggestions
- description: action=query&list=search and /v1/search/page expose the same ElasticSearch-backed full-text search Wiktionary uses internally.
  name: Full-Text Search
- description: Both APIs expose full revision history, supporting time-travel reads and change-detection workflows.
  name: Page Revisions and History
- description: Parsoid /transform/* endpoints convert between wikitext and HTML round-trip-safely, useful for visual editors and bots.
  name: Wikitext ↔ HTML Transforms
- description: Authenticated calls support OAuth 2.0 (via api.wikimedia.org), legacy OAuth 1.0a, and BotPassword scoped credentials.
  name: OAuth 2.0 and BotPasswords
- description: All Wiktionary content can be reused for any purpose with attribution and share-alike, including in commercial AI training corpora.
  name: CC BY-SA 4.0 License
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wiktionary.png
integrations:
- description: Shares infrastructure, accounts, and most APIs with Wikipedia; both run on MediaWiki under the Wikimedia Foundation.
  name: Wikipedia
- description: Wiktionary lexemes are increasingly linked to structured Wikidata lexeme entities (Lexeme namespace, Q-IDs, L-IDs).
  name: Wikidata
- description: Pronunciation audio files and images embedded in Wiktionary pages live on Commons and are reachable via the same APIs.
  name: Wikimedia Commons
- description: The reference bot framework for automated edits, dumps, and maintenance scripts against Wiktionary.
  name: Pywikibot
- description: Commercial high-volume snapshots of Wikimedia content (Wikipedia first, with broader project coverage expanding); useful when REST rate limits are insufficient.
  name: Wikimedia Enterprise
- description: Wikimedia-hosted PaaS for community tools that consume the Wiktionary APIs at scale without bringing your own infrastructure.
  name: Toolforge
- description: Pre-processed Wiktionary dumps are available on Hugging Face for immediate use in ML training pipelines.
  name: Hugging Face Datasets
json_schemas:
- name: FileMetadata
  property_count: 5
  slug: core-rest-api-file-metadata
- name: HistoryCountResponse
  property_count: 2
  slug: core-rest-api-history-count-response
- name: HistoryResponse
  property_count: 4
  slug: core-rest-api-history-response
- name: LatestRevision
  property_count: 2
  slug: core-rest-api-latest-revision
- name: LicenseInfo
  property_count: 2
  slug: core-rest-api-license-info
- name: PageSourceResponse
  property_count: 7
  slug: core-rest-api-page-source-response
- name: PageWithHtmlResponse
  property_count: 8
  slug: core-rest-api-page-with-html-response
- name: RevisionDetail
  property_count: 10
  slug: core-rest-api-revision-detail
- name: SearchPage
  property_count: 7
  slug: core-rest-api-search-page
- name: SearchResponse
  property_count: 1
  slug: core-rest-api-search-response
- name: ActionApiResponse
  property_count: 6
  slug: mediawiki-action-api-action-api-response
- name: ExpandTemplatesResponse
  property_count: 1
  slug: mediawiki-action-api-expand-templates-response
- name: ExtractPage
  property_count: 4
  slug: mediawiki-action-api-extract-page
- name: OpenSearchResponse
  property_count: 0
  slug: mediawiki-action-api-open-search-response
- name: ParseResponse
  property_count: 1
  slug: mediawiki-action-api-parse-response
- name: ParseSection
  property_count: 7
  slug: mediawiki-action-api-parse-section
- name: QueryExtractsResponse
  property_count: 1
  slug: mediawiki-action-api-query-extracts-response
- name: QueryRevisionsResponse
  property_count: 2
  slug: mediawiki-action-api-query-revisions-response
- name: QuerySearchResponse
  property_count: 3
  slug: mediawiki-action-api-query-search-response
- name: RevisionPage
  property_count: 4
  slug: mediawiki-action-api-revision-page
- name: Revision
  property_count: 3
  slug: mediawiki-action-api-revision
- name: SearchHit
  property_count: 7
  slug: mediawiki-action-api-search-hit
- name: ContentUrls
  property_count: 2
  slug: rest-api-content-urls
- name: DefinitionEntry
  property_count: 3
  slug: rest-api-definition-entry
- name: DefinitionResponse
  property_count: 0
  slug: rest-api-definition-response
- name: HtmlTransformRequest
  property_count: 2
  slug: rest-api-html-transform-request
- name: LanguageEntry
  property_count: 3
  slug: rest-api-language-entry
- name: LintError
  property_count: 4
  slug: rest-api-lint-error
- name: PageSummary
  property_count: 8
  slug: rest-api-page-summary
- name: RevisionItem
  property_count: 12
  slug: rest-api-revision-item
- name: RevisionMetadata
  property_count: 1
  slug: rest-api-revision-metadata
- name: WikitextTransformRequest
  property_count: 3
  slug: rest-api-wikitext-transform-request
json_structures:
- name: Core Rest Api File Metadata Structure
  property_count: 5
  slug: core-rest-api-file-metadata-structure
- name: Core Rest Api History Count Response Structure
  property_count: 2
  slug: core-rest-api-history-count-response-structure
- name: Core Rest Api History Response Structure
  property_count: 4
  slug: core-rest-api-history-response-structure
- name: Core Rest Api Latest Revision Structure
  property_count: 2
  slug: core-rest-api-latest-revision-structure
- name: Core Rest Api License Info Structure
  property_count: 2
  slug: core-rest-api-license-info-structure
- name: Core Rest Api Page Source Response Structure
  property_count: 7
  slug: core-rest-api-page-source-response-structure
- name: Core Rest Api Page With Html Response Structure
  property_count: 8
  slug: core-rest-api-page-with-html-response-structure
- name: Core Rest Api Revision Detail Structure
  property_count: 10
  slug: core-rest-api-revision-detail-structure
- name: Core Rest Api Search Page Structure
  property_count: 7
  slug: core-rest-api-search-page-structure
- name: Core Rest Api Search Response Structure
  property_count: 1
  slug: core-rest-api-search-response-structure
- name: Mediawiki Action Api Action Api Response Structure
  property_count: 6
  slug: mediawiki-action-api-action-api-response-structure
- name: Mediawiki Action Api Expand Templates Response Structure
  property_count: 1
  slug: mediawiki-action-api-expand-templates-response-structure
- name: Mediawiki Action Api Extract Page Structure
  property_count: 4
  slug: mediawiki-action-api-extract-page-structure
- name: Mediawiki Action Api Open Search Response Structure
  property_count: 0
  slug: mediawiki-action-api-open-search-response-structure
- name: Mediawiki Action Api Parse Response Structure
  property_count: 1
  slug: mediawiki-action-api-parse-response-structure
- name: Mediawiki Action Api Parse Section Structure
  property_count: 7
  slug: mediawiki-action-api-parse-section-structure
- name: Mediawiki Action Api Query Extracts Response Structure
  property_count: 1
  slug: mediawiki-action-api-query-extracts-response-structure
- name: Mediawiki Action Api Query Revisions Response Structure
  property_count: 2
  slug: mediawiki-action-api-query-revisions-response-structure
- name: Mediawiki Action Api Query Search Response Structure
  property_count: 3
  slug: mediawiki-action-api-query-search-response-structure
- name: Mediawiki Action Api Revision Page Structure
  property_count: 4
  slug: mediawiki-action-api-revision-page-structure
- name: Mediawiki Action Api Revision Structure
  property_count: 3
  slug: mediawiki-action-api-revision-structure
- name: Mediawiki Action Api Search Hit Structure
  property_count: 7
  slug: mediawiki-action-api-search-hit-structure
- name: Rest Api Content Urls Structure
  property_count: 2
  slug: rest-api-content-urls-structure
- name: Rest Api Definition Entry Structure
  property_count: 3
  slug: rest-api-definition-entry-structure
- name: Rest Api Definition Response Structure
  property_count: 0
  slug: rest-api-definition-response-structure
- name: Rest Api Html Transform Request Structure
  property_count: 2
  slug: rest-api-html-transform-request-structure
- name: Rest Api Language Entry Structure
  property_count: 3
  slug: rest-api-language-entry-structure
- name: Rest Api Lint Error Structure
  property_count: 4
  slug: rest-api-lint-error-structure
- name: Rest Api Page Summary Structure
  property_count: 8
  slug: rest-api-page-summary-structure
- name: Rest Api Revision Item Structure
  property_count: 12
  slug: rest-api-revision-item-structure
- name: Rest Api Revision Metadata Structure
  property_count: 1
  slug: rest-api-revision-metadata-structure
- name: Rest Api Wikitext Transform Request Structure
  property_count: 3
  slug: rest-api-wikitext-transform-request-structure
jsonld:
- class_count: 10
  name: Wiktionary Core Rest Api Context
  property_count: 34
  slug: wiktionary-core-rest-api-context
- class_count: 12
  name: Wiktionary Mediawiki Action Api Context
  property_count: 28
  slug: wiktionary-mediawiki-action-api-context
- class_count: 10
  name: Wiktionary Rest Api Context
  property_count: 36
  slug: wiktionary-rest-api-context
layout: provider
modified: '2026-05-30'
name: Wiktionary
nav: Providers
network: true
overview: 'Wiktionary publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Definition API, ExpandTemplates API, File API, and 8 more. Tagged areas include Dictionaries, Open Source, Wikimedia, MediaWiki, and Linguistics.


  The Wiktionary catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Wiktionary''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, changelog, and 32 more developer resources.'
random_paper: 78
rules:
- name: Wiktionary API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: wiktionary-jsonschema-spectral-rules
- name: Wiktionary API Rules
  rule_count: 47
  severity_counts:
    error: 14
    hint: 0
    info: 11
    warn: 22
  slug: wiktionary-spectral-rules
scopes:
- name: Wiktionary Scopes
  scope_count: 3
  slug: wiktionary-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 59.6
  delta: -7.3
  facets:
    commercial_clarity: 31.6
    contract_quality: 65.0
    developer_ergonomics: 67.4
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wiktionary/refs/heads/main/screenshots/wiktionary-2026-06-20T201458.png
security:
- kind: authentication
  name: Wiktionary Authentication
  slug: wiktionary-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Wiktionary Domain Security
  slug: wiktionary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wiktionary Vulnerability Disclosure
  slug: wiktionary-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wiktionary
solutions:
- description: The MediaWiki Action API, Wikimedia REST API, and MediaWiki Core REST API are all free to use without registration, subject to the 200 req/s shared limit and User-Agent requirement.
  name: Free Public APIs
- description: dumps.wikimedia.org provides full XML and SQL exports of every Wikimedia project, refreshed at least monthly; the preferred channel for whole-corpus processing.
  name: Bulk Dumps
- description: Paid SLA-backed snapshots and streaming APIs for commercial reusers who need throughput, freshness, or attribution guarantees beyond what the free APIs provide.
  name: Wikimedia Enterprise
tags:
- Dictionaries
- Open Source
- Wikimedia
- MediaWiki
- Linguistics
- Open Data
- Public APIs
use_cases:
- description: Embed definitions, etymologies, pronunciations, and translations directly into mobile or desktop dictionary apps.
  name: Dictionary Apps
- description: Power vocabulary lookups, flashcards, and reading-assistance browser extensions for learners of any language.
  name: Language-Learning Tools
- description: Use bulk wikitext dumps and the definition API to build morphology, inflection, and word-sense datasets for NLP research.
  name: NLP and Linguistics Datasets
- description: Mine cross-language Wiktionary translation tables to seed bilingual dictionaries and translation memories.
  name: Translation Memory
- description: Use the OpenSearch and search endpoints to validate word existence and segment text in tokenizers.
  name: Spell-Checkers and Tokenizers
- description: Retrieve authoritative definitions to ground LLM responses about word meaning, etymology, and usage.
  name: AI Grounding and RAG
- description: Generate clues, anagrams, and puzzle answers from Wiktionary's definitions and word lists.
  name: Crossword and Game Generation
- description: Query etymologies, declensions, pronunciations, and historical usage across hundreds of languages.
  name: Linguistic Research
website: https://en.wiktionary.org/
---
