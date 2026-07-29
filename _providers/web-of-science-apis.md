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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Web Of Science Apis Agentic Access
  operation_count: 14
  slug: web-of-science-apis-agentic-access
  summary_line: 14 operations · 1 acting
api_count: 6
apis:
- description: The citations API from Web of Science APIs — 3 operation(s) for citations.
  name: Web of Science APIs citations API
  slug: web-of-science-apis-citations-api
- description: The documents API from Web of Science APIs — 2 operation(s) for documents.
  name: Web of Science APIs documents API
  slug: web-of-science-apis-documents-api
- description: The journals API from Web of Science APIs — 2 operation(s) for journals.
  name: Web of Science APIs journals API
  slug: web-of-science-apis-journals-api
- description: The records API from Web of Science APIs — 1 operation(s) for records.
  name: Web of Science APIs records API
  slug: web-of-science-apis-records-api
- description: The reports API from Web of Science APIs — 2 operation(s) for reports.
  name: Web of Science APIs reports API
  slug: web-of-science-apis-reports-api
- description: The search API from Web of Science APIs — 3 operation(s) for search.
  name: Web of Science APIs search API
  slug: web-of-science-apis-search-api
artifact_total: 122
collections:
- collection_type: postman
  name: Web of Science API Expanded citations API
  slug: postman-web-of-science-apis-citations-api
- collection_type: postman
  name: Web of Science API Expanded citations documents API
  slug: postman-web-of-science-apis-documents-api
- collection_type: postman
  name: Web of Science API Expanded citations journals API
  slug: postman-web-of-science-apis-journals-api
- collection_type: postman
  name: Web of Science API Expanded citations records API
  slug: postman-web-of-science-apis-records-api
- collection_type: postman
  name: Web of Science API Expanded citations reports API
  slug: postman-web-of-science-apis-reports-api
- collection_type: postman
  name: Web of Science API Expanded citations search API
  slug: postman-web-of-science-apis-search-api
- collection_type: open
  name: Web of Science API Expanded
  slug: open-web-of-science-expanded
- collection_type: open
  name: Web of Science Starter API
  slug: open-web-of-science-starter
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/web-of-science-apis/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/web-of-science-apis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/web-of-science-apis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/web-of-science-apis-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clarivate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/clarivateacademiagovernment
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clarivate.com/apis/wos-starter
- group: company
  title: ''
  type: Website
  url: https://clarivate.com/products/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clarivate.com
- group: operate
  title: ''
  type: Support
  url: https://developer.clarivate.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clarivate.com/legal/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarivate.com/privacy-statement/
- group: company
  title: ''
  type: Blog
  url: https://clarivate.com/blog/
- group: design
  title: ''
  type: SpectralRules
  url: rules/web-of-science-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/web-of-science-vocabulary.yml
created: '2025-02-06'
description: The Web of Science APIs provide programmatic access to Clarivate's Web of Science databases, the world's leading citation index covering over 21,000 peer-reviewed journals across the sciences, social sciences, and humanities. The API suite includes the Starter API for basic bibliographic metadata and journal discovery, and the Expanded API for advanced search, citation tracking, related records, and bibliometric reporting with h-index and year-by-year citation analysis.
examples:
- key_count: 3
  name: Web Of Science Author Example
  slug: web-of-science-author-example
- key_count: 1
  name: Web Of Science Category Context Example
  slug: web-of-science-category-context-example
- key_count: 2
  name: Web Of Science Category Count Example
  slug: web-of-science-category-count-example
- key_count: 2
  name: Web Of Science Citation Count Example
  slug: web-of-science-citation-count-example
- key_count: 6
  name: Web Of Science Citation Report Example
  slug: web-of-science-citation-report-example
- key_count: 10
  name: Web Of Science Document Example
  slug: web-of-science-document-example
- key_count: 4
  name: Web Of Science Document Identifiers Example
  slug: web-of-science-document-identifiers-example
- key_count: 2
  name: Web Of Science Document Keywords Example
  slug: web-of-science-document-keywords-example
- key_count: 3
  name: Web Of Science Document Links Example
  slug: web-of-science-document-links-example
- key_count: 1
  name: Web Of Science Document Names Example
  slug: web-of-science-document-names-example
- key_count: 4
  name: Web Of Science Document Pages Example
  slug: web-of-science-document-pages-example
- key_count: 8
  name: Web Of Science Document Source Example
  slug: web-of-science-document-source-example
- key_count: 4
  name: Web Of Science Documents Search Response Example
  slug: web-of-science-documents-search-response-example
- key_count: 1
  name: Web Of Science Dynamic Data Example
  slug: web-of-science-dynamic-data-example
- key_count: 2
  name: Web Of Science Error Response Example
  slug: web-of-science-error-response-example
- key_count: 4
  name: Web Of Science Full Record Metadata Example
  slug: web-of-science-full-record-metadata-example
- key_count: 10
  name: Web Of Science Journal Example
  slug: web-of-science-journal-example
- key_count: 4
  name: Web Of Science Journals Search Response Example
  slug: web-of-science-journals-search-response-example
- key_count: 5
  name: Web Of Science Pub Info Example
  slug: web-of-science-pub-info-example
- key_count: 3
  name: Web Of Science Query Result Example
  slug: web-of-science-query-result-example
- key_count: 2
  name: Web Of Science Record Ids Response Example
  slug: web-of-science-record-ids-response-example
- key_count: 5
  name: Web Of Science Record Summary Example
  slug: web-of-science-record-summary-example
- key_count: 1
  name: Web Of Science Records Example
  slug: web-of-science-records-example
- key_count: 7
  name: Web Of Science Search Request Example
  slug: web-of-science-search-request-example
- key_count: 2
  name: Web Of Science Search Response Example
  slug: web-of-science-search-response-example
- key_count: 2
  name: Web Of Science Static Data Example
  slug: web-of-science-static-data-example
- key_count: 2
  name: Web Of Science Time Span Example
  slug: web-of-science-time-span-example
- key_count: 3
  name: Web Of Science Wos Record Example
  slug: web-of-science-wos-record-example
- key_count: 2
  name: Web Of Science Year Count Example
  slug: web-of-science-year-count-example
features:
- description: Search over 100 million records using Web of Science Advanced Query Syntax with 16 searchable field tags including topic, author, DOI, organization, and funding agency.
  name: Advanced Document Search
- description: Track forward citations (articles citing a paper) and backward citations (reference list) to understand the full citation network of any paper.
  name: Citation Tracking
- description: Generate citation reports with h-index, total citations, average citations per item, and year-by-year citation and publication counts.
  name: Bibliometric Reporting
- description: Find research papers related to a given article by identifying records that share cited references.
  name: Related Records Discovery
- description: Retrieve journal information including ISSN, publisher, subject categories, and Journal Citation Reports profile URL.
  name: Journal Metadata
- description: Search across 12 Web of Science databases including Core Collection, MEDLINE, BIOSIS, and Zoological Record.
  name: Multi-Database Search
- description: Access real-time times-cited counts for documents across Web of Science databases for impact assessment.
  name: Times-Cited Counts
finops:
- name: Web Of Science Apis Finops
  service_category: API
  slug: web-of-science-apis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/web-of-science-apis.png
json_schemas:
- name: Author
  property_count: 3
  slug: web-of-science-author
- name: CategoryContext
  property_count: 1
  slug: web-of-science-category-context
- name: CategoryCount
  property_count: 2
  slug: web-of-science-category-count
- name: CitationCount
  property_count: 2
  slug: web-of-science-citation-count
- name: CitationReport
  property_count: 6
  slug: web-of-science-citation-report
- name: DocumentIdentifiers
  property_count: 4
  slug: web-of-science-document-identifiers
- name: DocumentKeywords
  property_count: 2
  slug: web-of-science-document-keywords
- name: DocumentLinks
  property_count: 3
  slug: web-of-science-document-links
- name: DocumentNames
  property_count: 1
  slug: web-of-science-document-names
- name: DocumentPages
  property_count: 4
  slug: web-of-science-document-pages
- name: Document
  property_count: 10
  slug: web-of-science-document
- name: DocumentSource
  property_count: 8
  slug: web-of-science-document-source
- name: DocumentsSearchResponse
  property_count: 4
  slug: web-of-science-documents-search-response
- name: DynamicData
  property_count: 1
  slug: web-of-science-dynamic-data
- name: ErrorResponse
  property_count: 2
  slug: web-of-science-error-response
- name: FullRecordMetadata
  property_count: 4
  slug: web-of-science-full-record-metadata
- name: Journal
  property_count: 10
  slug: web-of-science-journal
- name: JournalsSearchResponse
  property_count: 4
  slug: web-of-science-journals-search-response
- name: PubInfo
  property_count: 5
  slug: web-of-science-pub-info
- name: QueryResult
  property_count: 3
  slug: web-of-science-query-result
- name: RecordIdsResponse
  property_count: 2
  slug: web-of-science-record-ids-response
- name: RecordSummary
  property_count: 5
  slug: web-of-science-record-summary
- name: Records
  property_count: 1
  slug: web-of-science-records
- name: SearchRequest
  property_count: 7
  slug: web-of-science-search-request
- name: SearchResponse
  property_count: 2
  slug: web-of-science-search-response
- name: StaticData
  property_count: 2
  slug: web-of-science-static-data
- name: TimeSpan
  property_count: 2
  slug: web-of-science-time-span
- name: WosRecord
  property_count: 3
  slug: web-of-science-wos-record
- name: YearCount
  property_count: 2
  slug: web-of-science-year-count
json_structures:
- name: Web Of Science Author Structure
  property_count: 3
  slug: web-of-science-author-structure
- name: Web Of Science Category Context Structure
  property_count: 1
  slug: web-of-science-category-context-structure
- name: Web Of Science Category Count Structure
  property_count: 2
  slug: web-of-science-category-count-structure
- name: Web Of Science Citation Count Structure
  property_count: 2
  slug: web-of-science-citation-count-structure
- name: Web Of Science Citation Report Structure
  property_count: 6
  slug: web-of-science-citation-report-structure
- name: Web Of Science Document Identifiers Structure
  property_count: 4
  slug: web-of-science-document-identifiers-structure
- name: Web Of Science Document Keywords Structure
  property_count: 2
  slug: web-of-science-document-keywords-structure
- name: Web Of Science Document Links Structure
  property_count: 3
  slug: web-of-science-document-links-structure
- name: Web Of Science Document Names Structure
  property_count: 1
  slug: web-of-science-document-names-structure
- name: Web Of Science Document Pages Structure
  property_count: 4
  slug: web-of-science-document-pages-structure
- name: Web Of Science Document Source Structure
  property_count: 8
  slug: web-of-science-document-source-structure
- name: Web Of Science Document Structure
  property_count: 10
  slug: web-of-science-document-structure
- name: Web Of Science Documents Search Response Structure
  property_count: 4
  slug: web-of-science-documents-search-response-structure
- name: Web Of Science Dynamic Data Structure
  property_count: 1
  slug: web-of-science-dynamic-data-structure
- name: Web Of Science Error Response Structure
  property_count: 2
  slug: web-of-science-error-response-structure
- name: Web Of Science Full Record Metadata Structure
  property_count: 4
  slug: web-of-science-full-record-metadata-structure
- name: Web Of Science Journal Structure
  property_count: 10
  slug: web-of-science-journal-structure
- name: Web Of Science Journals Search Response Structure
  property_count: 4
  slug: web-of-science-journals-search-response-structure
- name: Web Of Science Pub Info Structure
  property_count: 5
  slug: web-of-science-pub-info-structure
- name: Web Of Science Query Result Structure
  property_count: 3
  slug: web-of-science-query-result-structure
- name: Web Of Science Record Ids Response Structure
  property_count: 2
  slug: web-of-science-record-ids-response-structure
- name: Web Of Science Record Summary Structure
  property_count: 5
  slug: web-of-science-record-summary-structure
- name: Web Of Science Records Structure
  property_count: 1
  slug: web-of-science-records-structure
- name: Web Of Science Search Request Structure
  property_count: 7
  slug: web-of-science-search-request-structure
- name: Web Of Science Search Response Structure
  property_count: 2
  slug: web-of-science-search-response-structure
- name: Web Of Science Static Data Structure
  property_count: 2
  slug: web-of-science-static-data-structure
- name: Web Of Science Time Span Structure
  property_count: 2
  slug: web-of-science-time-span-structure
- name: Web Of Science Wos Record Structure
  property_count: 3
  slug: web-of-science-wos-record-structure
- name: Web Of Science Year Count Structure
  property_count: 2
  slug: web-of-science-year-count-structure
jsonld:
- class_count: 0
  name: Web Of Science Context
  property_count: 113
  slug: web-of-science-context
layout: provider
modified: '2026-05-19'
name: Web of Science APIs
nav: Providers
network: true
overview: 'Web of Science APIs publishes 6 APIs on the [APIs.io](https://apis.io/) network, including citations API, documents API, journals API, and 3 more. Tagged areas include Research, Academic, Bibliometrics, Citations, and Science.


  The Web of Science APIs catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Web of Science APIs'' developer surface includes authentication, documentation, support, engineering blog, and 11 more developer resources.'
plans:
- name: Web Of Science Apis Plans Pricing
  plan_count: 3
  slug: web-of-science-apis-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Web Of Science Apis Rate Limits
  slug: web-of-science-apis-rate-limits
rules:
- name: Web of Science APIs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: web-of-science-apis-jsonschema-spectral-rules
- name: Web of Science APIs API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: web-of-science-apis-spectral-rules
- name: Web of Science APIs API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 7
    warn: 7
  slug: web-of-science-spectral-rules
score:
  band: strong
  composite: 56.2
  delta: -4.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.9
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/web-of-science-apis/refs/heads/main/screenshots/web-of-science-apis-2026-06-20T201320.png
security:
- kind: authentication
  name: Web Of Science Apis Authentication
  slug: web-of-science-apis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Web Of Science Apis Domain Security
  slug: web-of-science-apis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: web-of-science-apis
tags:
- Research
- Academic
- Bibliometrics
- Citations
- Science
- Scholarly
use_cases:
- description: Automate systematic literature review by programmatically searching and retrieving bibliographic metadata from Web of Science.
  name: Literature Review Automation
- description: Analyze the impact of publications or researchers using citation counts, h-index, and bibliometric reports.
  name: Research Impact Analysis
- description: Build citation networks by tracing forward and backward citations to map the intellectual lineage of research topics.
  name: Citation Network Analysis
- description: Identify appropriate journals for manuscript submission by searching journal metadata and impact metrics.
  name: Journal Selection
website: https://clarivate.com/products/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/
---
