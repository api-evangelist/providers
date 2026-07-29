---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Lucene provides a comprehensive Java API for full-text indexing, searching, faceting, hit highlighting, spatial search, vector nearest-neighbor search, and text analysis with support for custom analyz
  name: Apache Lucene
  slug: apache-lucene
artifact_total: 28
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-lucene-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-lucene-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://lucene.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/lucene
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/lucenenet
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/lucene/issues
- group: company
  title: ''
  type: Blog
  url: https://lucene.apache.org/news.html
- group: other
  title: ''
  type: MailingList
  url: https://lists.apache.org/list.html?dev@lucene.apache.org
- group: operate
  title: ''
  type: Slack
  url: https://the-asf.slack.com/messages/CE70MDPMF
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2026-03-16'
description: Apache Lucene is a high-performance, full-featured text search engine library written entirely in Java. It provides indexing and search technology, as well as spellchecking, hit highlighting, faceting, vector similarity search, and advanced analysis and tokenization capabilities. Lucene is the foundation for many popular search applications including Apache Solr.
features:
- description: High-performance full-text indexing with over 800GB/hour throughput on modern hardware with minimal RAM requirements.
  name: Full-Text Indexing
- description: Native support for approximate and exact k-nearest-neighbor vector similarity search alongside traditional keyword search.
  name: Vector Nearest-Neighbor Search
- description: Supports phrase queries, wildcard, proximity, range, fuzzy, and fielded queries with pluggable query parsers.
  name: Advanced Query Types
- description: Built-in faceted search and result grouping capabilities for navigation and aggregation.
  name: Faceting and Grouping
- description: Highlights search keywords in result snippets using the Highlighter and UnifiedHighlighter modules.
  name: Hit Highlighting
- description: Auto-suggest and spell-checking support via the Suggest module with multiple suggester implementations.
  name: Spell Checking and Suggestions
- description: Extensive analyzer ecosystem supporting dozens of languages including ICU, Kuromoji (Japanese), Nori (Korean), OpenNLP, and more.
  name: Pluggable Analyzers
- description: Supports Vector Space Model, Okapi BM25, and custom pluggable similarity implementations.
  name: Pluggable Ranking Models
- description: Geospatial search capabilities via the Spatial and Spatial3D modules.
  name: Spatial Search
- description: Index replication support via the Replicator module for leader-follower architectures.
  name: Replication Support
finops:
- name: Apache Lucene Finops
  service_category: API
  slug: apache-lucene-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-lucene.png
integrations:
- description: Apache Solr is built on top of Lucene and adds distributed search, REST API, and enterprise features.
  name: Apache Solr
- description: Elasticsearch and OpenSearch use Lucene as their underlying search engine.
  name: Elasticsearch/OpenSearch
- description: Lucene integrates with Hadoop for large-scale distributed indexing pipelines.
  name: Apache Hadoop
- description: Apache Tika extracts text from thousands of file formats for indexing into Lucene.
  name: Apache Tika
- description: OpenNLP provides NLP analysis capabilities integrated through Lucene analyzers.
  name: Apache OpenNLP
- description: Apache Nutch is a web crawler that stores and indexes content via Lucene.
  name: Apache Nutch
- description: Official .NET port of Apache Lucene, maintained in the apache/lucenenet repository.
  name: Lucene.NET
layout: provider
modified: '2026-04-19'
name: Apache Lucene
nav: Providers
network: true
overview: 'Apache Lucene publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Full-Text Search, Indexing, Java, Search, and Text Analysis.


  Apache Lucene''s developer surface includes developer portal, engineering blog, and 9 more developer resources.'
plans:
- name: Apache Lucene Plans Pricing
  plan_count: 3
  slug: apache-lucene-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Apache Lucene Rate Limits
  slug: apache-lucene-rate-limits
score:
  band: emerging
  composite: 22.9
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-lucene/refs/heads/main/screenshots/apache-lucene-2026-06-20T172117.png
security:
- kind: domain-security
  name: Apache Lucene Domain Security
  slug: apache-lucene-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Lucene Vulnerability Disclosure
  slug: apache-lucene-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-lucene
tags:
- Full-Text Search
- Indexing
- Java
- Search
- Text Analysis
- Vector Search
use_cases:
- description: Power full-text search across enterprise documents, emails, databases, and file systems.
  name: Enterprise Search
- description: Implement fast, relevant product search with facets, autocomplete, and spell correction.
  name: E-Commerce Product Search
- description: Index and search structured and unstructured log data for observability and security analytics.
  name: Log and Event Search
- description: Combine keyword search with vector embeddings for hybrid semantic and lexical retrieval.
  name: Semantic Search
- description: Build searchable knowledge bases and documentation portals with rich query capabilities.
  name: Knowledge Base Search
website: https://lucene.apache.org/
---
