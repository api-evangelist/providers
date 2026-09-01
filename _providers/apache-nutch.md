---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Apache Nutch Agentic Access
  operation_count: 24
  slug: apache-nutch-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 1
apis:
- description: Server administration operations
  name: Apache Nutch Admin API
  slug: apache-nutch-admin-api
- description: Manage Nutch configurations
  name: Apache Nutch Configuration API
  slug: apache-nutch-configuration-api
- description: Query the CrawlDB and FetchDB
  name: Apache Nutch Database API
  slug: apache-nutch-database-api
- description: Manage crawl jobs
  name: Apache Nutch Job API
  slug: apache-nutch-job-api
- description: Read sequence files and webgraph data
  name: Apache Nutch Reader API
  slug: apache-nutch-reader-api
- description: Manage seed URL lists
  name: Apache Nutch Seed API
  slug: apache-nutch-seed-api
- description: Auxiliary service operations such as CommonCrawl data dumps
  name: Apache Nutch Services API
  slug: apache-nutch-services-api
artifact_total: 101
collections:
- collection_type: postman
  name: Apache Nutch REST Admin API
  slug: postman-apache-nutch-admin-api
- collection_type: postman
  name: Apache Nutch REST Admin Configuration API
  slug: postman-apache-nutch-configuration-api
- collection_type: postman
  name: Apache Nutch REST Admin Database API
  slug: postman-apache-nutch-database-api
- collection_type: postman
  name: Apache Nutch REST Admin Job API
  slug: postman-apache-nutch-job-api
- collection_type: postman
  name: Apache Nutch REST Admin Reader API
  slug: postman-apache-nutch-reader-api
- collection_type: postman
  name: Apache Nutch REST Admin Seed API
  slug: postman-apache-nutch-seed-api
- collection_type: postman
  name: Apache Nutch REST Admin Services API
  slug: postman-apache-nutch-services-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Nutch REST Admin API
  slug: open-apache-nutch-admin-api
- collection_type: open
  name: Apache Nutch REST Admin Configuration API
  slug: open-apache-nutch-configuration-api
- collection_type: open
  name: Apache Nutch REST Admin Database API
  slug: open-apache-nutch-database-api
- collection_type: open
  name: Apache Nutch REST Admin Job API
  slug: open-apache-nutch-job-api
- collection_type: open
  name: Apache Nutch REST Admin Reader API
  slug: open-apache-nutch-reader-api
- collection_type: open
  name: Apache Nutch REST Admin Seed API
  slug: open-apache-nutch-seed-api
- collection_type: open
  name: Apache Nutch REST Admin Services API
  slug: open-apache-nutch-services-api
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/nutch/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/nutch/blob/master/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apache-nutch/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-nutch-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-nutch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-nutch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-nutch-authentication.yml
- group: build
  title: Apache Nutch GitHub Repository
  type: GitHubRepository
  url: https://github.com/apache/nutch
- group: build
  title: Apache Software Foundation GitHub
  type: GitHubOrganization
  url: https://github.com/apache
- group: docs
  title: Apache Nutch Documentation
  type: Documentation
  url: https://nutch.apache.org/documentation/
- group: start
  title: Nutch Tutorial
  type: GettingStarted
  url: https://cwiki.apache.org/confluence/display/NUTCH/NutchTutorial
- group: learn
  title: Apache Nutch Tutorials
  type: Tutorials
  url: https://nutch.apache.org/documentation/tutorials/
- group: operate
  title: Apache Nutch FAQs
  type: FAQ
  url: https://nutch.apache.org/documentation/faqs/
- group: operate
  title: Nutch Release Notes
  type: ReleaseNotes
  url: https://github.com/apache/nutch/blob/master/CHANGES.md
- group: commercial
  title: Apache License 2.0
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: operate
  title: Mailing Lists
  type: Support
  url: https://nutch.apache.org/community/mailing-lists/
- group: operate
  title: Nutch on Stack Overflow
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/nutch
- group: design
  title: Apache Nutch Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/rules/apache-nutch-spectral-rules.yml
- group: design
  title: Apache Nutch Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/vocabulary/apache-nutch-vocabulary.yaml
- group: design
  title: Apache Nutch JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/json-ld/apache-nutch-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://nutch.apache.org/index.xml
created: '2026-03-16'
description: Apache Nutch is a highly extensible and scalable open-source web crawler software project built on Apache Hadoop data structures for batch processing. It provides a pluggable architecture supporting custom parse filters, scoring filters, index writers, and protocol implementations. Nutch integrates with Apache Solr and Elasticsearch for full-text search and exposes a REST API for managing crawl jobs, configurations, seed lists, and database queries. Governed by the Apache Software Foundation under the Apache License 2.0.
examples:
- key_count: 2
  name: Apache Nutch Child Node Example
  slug: apache-nutch-child-node-example
- key_count: 4
  name: Apache Nutch Db Query Example
  slug: apache-nutch-db-query-example
- key_count: 4
  name: Apache Nutch Fetch Node Db Info Example
  slug: apache-nutch-fetch-node-db-info-example
- key_count: 5
  name: Apache Nutch Job Config Example
  slug: apache-nutch-job-config-example
- key_count: 8
  name: Apache Nutch Job Info Example
  slug: apache-nutch-job-info-example
- key_count: 0
  name: Apache Nutch Job Type Example
  slug: apache-nutch-job-type-example
- key_count: 6
  name: Apache Nutch Link Schema Example
  slug: apache-nutch-link-schema-example
- key_count: 6
  name: Apache Nutch Node Schema Example
  slug: apache-nutch-node-schema-example
- key_count: 3
  name: Apache Nutch Nutch Config Example
  slug: apache-nutch-nutch-config-example
- key_count: 4
  name: Apache Nutch Nutch Server Info Example
  slug: apache-nutch-nutch-server-info-example
- key_count: 1
  name: Apache Nutch Reader Config Example
  slug: apache-nutch-reader-config-example
- key_count: 4
  name: Apache Nutch Seed List Example
  slug: apache-nutch-seed-list-example
- key_count: 2
  name: Apache Nutch Seed Url Example
  slug: apache-nutch-seed-url-example
- key_count: 3
  name: Apache Nutch Service Config Example
  slug: apache-nutch-service-config-example
- key_count: 1
  name: Apache Nutch Service Info Example
  slug: apache-nutch-service-info-example
- key_count: 0
  name: Apache Nutch State Example
  slug: apache-nutch-state-example
features:
- description: Leverages Apache Hadoop data structures for distributed, large-scale web crawling batch processing.
  name: Scalable Batch Crawling
- description: Extensible plugin system supporting custom parse filters, scoring filters, index writers, protocol plugins, and URL filters.
  name: Pluggable Architecture
- description: Full REST API for managing crawl jobs, configurations, seed lists, CrawlDB/FetchDB queries, and sequence file readers.
  name: REST API for Crawl Management
- description: Built-in index writers for Apache Solr and Elasticsearch to enable full-text search over crawled content.
  name: Full-Text Search Integration
- description: Uses Apache Tika for parsing a wide variety of document formats during the crawl pipeline.
  name: Apache Tika Parsing
- description: Built-in deduplication support to identify and remove duplicate content from the crawl database and search index.
  name: Duplicate Detection
- description: Regex-based and custom URL filter plugins to control crawl scope and exclusions.
  name: Configurable URL Filtering
- description: Supports multi-round incremental crawling workflows to keep the crawl database fresh.
  name: Incremental Crawling
- description: Service operations for exporting crawl data in CommonCrawl-compatible formats.
  name: CommonCrawl Export
- description: Configurable HTTP authentication schemes for crawling password-protected sites.
  name: HTTP Authentication Support
finops:
- name: Apache Nutch Finops
  service_category: API
  slug: apache-nutch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-nutch.png
integrations:
- description: Native index writer plugin for indexing crawled content into Apache Solr for full-text search.
  name: Apache Solr
- description: Index writer plugin for sending crawled content to Elasticsearch clusters.
  name: Elasticsearch
- description: Core dependency providing distributed storage and processing via HDFS and MapReduce.
  name: Apache Hadoop
- description: Used for content detection and extraction from a wide range of document formats during parsing.
  name: Apache Tika
- description: Support for SolrCloud distributed search clusters for scalable indexing.
  name: SolrCloud
json_schemas:
- name: ChildNode
  property_count: 2
  slug: apache-nutch-child-node
- name: DbQuery
  property_count: 4
  slug: apache-nutch-db-query
- name: FetchNodeDbInfo
  property_count: 4
  slug: apache-nutch-fetch-node-db-info
- name: JobConfig
  property_count: 5
  slug: apache-nutch-job-config
- name: JobInfo
  property_count: 8
  slug: apache-nutch-job-info
- name: JobType
  property_count: 0
  slug: apache-nutch-job-type
- name: LinkSchema
  property_count: 6
  slug: apache-nutch-link-schema
- name: NodeSchema
  property_count: 6
  slug: apache-nutch-node-schema
- name: NutchConfig
  property_count: 3
  slug: apache-nutch-nutch-config
- name: NutchServerInfo
  property_count: 4
  slug: apache-nutch-nutch-server-info
- name: ReaderConfig
  property_count: 1
  slug: apache-nutch-reader-config
- name: SeedList
  property_count: 4
  slug: apache-nutch-seed-list
- name: SeedUrl
  property_count: 2
  slug: apache-nutch-seed-url
- name: ServiceConfig
  property_count: 3
  slug: apache-nutch-service-config
- name: ServiceInfo
  property_count: 1
  slug: apache-nutch-service-info
- name: State
  property_count: 0
  slug: apache-nutch-state
json_structures:
- name: Apache Nutch Child Node Structure
  property_count: 2
  slug: apache-nutch-child-node-structure
- name: Apache Nutch Db Query Structure
  property_count: 4
  slug: apache-nutch-db-query-structure
- name: Apache Nutch Fetch Node Db Info Structure
  property_count: 4
  slug: apache-nutch-fetch-node-db-info-structure
- name: Apache Nutch Job Config Structure
  property_count: 5
  slug: apache-nutch-job-config-structure
- name: Apache Nutch Job Info Structure
  property_count: 8
  slug: apache-nutch-job-info-structure
- name: Apache Nutch Job Type Structure
  property_count: 0
  slug: apache-nutch-job-type-structure
- name: Apache Nutch Link Schema Structure
  property_count: 6
  slug: apache-nutch-link-schema-structure
- name: Apache Nutch Node Schema Structure
  property_count: 6
  slug: apache-nutch-node-schema-structure
- name: Apache Nutch Nutch Config Structure
  property_count: 3
  slug: apache-nutch-nutch-config-structure
- name: Apache Nutch Nutch Server Info Structure
  property_count: 4
  slug: apache-nutch-nutch-server-info-structure
- name: Apache Nutch Reader Config Structure
  property_count: 1
  slug: apache-nutch-reader-config-structure
- name: Apache Nutch Seed List Structure
  property_count: 4
  slug: apache-nutch-seed-list-structure
- name: Apache Nutch Seed Url Structure
  property_count: 2
  slug: apache-nutch-seed-url-structure
- name: Apache Nutch Service Config Structure
  property_count: 3
  slug: apache-nutch-service-config-structure
- name: Apache Nutch Service Info Structure
  property_count: 1
  slug: apache-nutch-service-info-structure
- name: Apache Nutch State Structure
  property_count: 0
  slug: apache-nutch-state-structure
jsonld:
- class_count: 16
  name: Apache Nutch Context
  property_count: 35
  slug: apache-nutch-context
layout: provider
modified: '2026-05-19'
name: Apache Nutch
nav: Providers
network: true
overview: 'Apache Nutch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Configuration API, Database API, and 4 more. Tagged areas include Web Crawler, Indexing, Search, Apache, and Java.


  The Apache Nutch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Nutch''s developer surface includes authentication, documentation, getting-started guide, FAQ, release notes, support, Stack Overflow tag, and 15 more developer resources.'
plans:
- name: Apache Nutch Plans Pricing
  plan_count: 3
  slug: apache-nutch-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Apache Nutch Rate Limits
  slug: apache-nutch-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Nutch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-nutch-jsonschema-spectral-rules
- effective_rule_count: 80
  extends:
  - spectral:oas
  name: Apache Nutch API Rules
  rule_count: 39
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 24
  slug: apache-nutch-spectral-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 67.0
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 50.0
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/screenshots/apache-nutch-2026-06-20T172129.png
security:
- kind: authentication
  name: Apache Nutch Authentication
  slug: apache-nutch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Nutch Domain Security
  slug: apache-nutch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Nutch Vulnerability Disclosure
  slug: apache-nutch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-nutch
tags:
- Web Crawler
- Indexing
- Search
- Apache
- Java
- Hadoop
- Open-Source
use_cases:
- description: Build enterprise search engines over internal or external web content using Nutch as the crawler and Solr/Elasticsearch as the search backend.
  name: Enterprise Search
- description: Academic and research teams use Nutch for large-scale systematic web data collection and indexing.
  name: Research Data Collection
- description: Crawl and index intranet sites, wikis, and document repositories for internal enterprise search.
  name: Intranet Document Search
- description: Create structured web archives compatible with CommonCrawl format for long-term data preservation.
  name: Web Archive Creation
- description: Monitor web content changes, track competitor sites, and analyze web structure at scale.
  name: SEO and Content Monitoring
- description: Build custom extraction pipelines using Nutch plugin architecture for targeted data acquisition tasks.
  name: Custom Data Extraction Pipelines
---
