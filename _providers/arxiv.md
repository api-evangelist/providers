---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Arxiv Agentic Access
  operation_count: 3
  slug: arxiv-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 4
apis:
- description: Daily RSS feeds of new arXiv submissions, organised by archive and subject category. Primarily intended for human consumption; the OAI-PMH and query APIs are recommended for machine integration.
  name: arXiv RSS Feeds
  slug: arxiv-rss-feeds
- description: 'Full-text and source bulk distribution channels: an Amazon S3 Requester-Pays bucket containing every arXiv PDF and source archive, plus a periodically refreshed Kaggle dataset of the complete metadata'
  name: arXiv Bulk Data
  slug: arxiv-bulk-data
- description: OAI-PMH v2.0 verbs for metadata harvesting.
  name: arXiv OAI-PMH API
  slug: arxiv-oai-pmh-api
- description: Search and retrieve article metadata from arXiv.
  name: arXiv Query API
  slug: arxiv-query-api
artifact_total: 42
collections:
- collection_type: open
  name: arXiv OAI-PMH API
  slug: open-arxiv-oaipmh
- collection_type: open
  name: arXiv Query API
  slug: open-arxiv-query
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arxiv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arxiv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arxiv.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://info.arxiv.org/help/api/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://info.arxiv.org/help/api/user-manual.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://info.arxiv.org/help/api/tou.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://info.arxiv.org/help/policies/privacy_policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arxiv.org/
- group: company
  title: ''
  type: Blog
  url: https://blog.arxiv.org/
- group: operate
  title: ''
  type: Support
  url: https://info.arxiv.org/help/contact.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arXiv
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/arXiv/arxiv-docs/commits/develop
- group: commercial
  title: ''
  type: Plans
  url: plans/arxiv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arxiv-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/arxiv-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/arxiv-vocabulary.yml
- group: design
  title: arXiv JSON-LD Context
  type: JSONLD
  url: json-ld/arxiv-context.jsonld
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: arXiv MCP Server (blazickjp)
  type: Tools
  url: https://github.com/blazickjp/arxiv-mcp-server
- group: build
  title: arXiv MCP (shoumikdc)
  type: Tools
  url: https://github.com/shoumikdc/arXiv-mcp
- group: build
  title: arXiv MCP (Tejas242)
  type: Tools
  url: https://github.com/Tejas242/arxiv-mcp
- group: build
  title: arXiv MCP Server in Java (glaforge)
  type: Tools
  url: https://github.com/glaforge/arxiv-mcp-server
- group: build
  title: arXiv MCP (kelvingao)
  type: Tools
  url: https://github.com/kelvingao/arxiv-mcp
- group: build
  title: arxiv Python wrapper (lukasschwab/arxiv.py)
  type: SDKs
  url: https://pypi.org/project/arxiv/
- group: build
  title: arxivpy Python client (titipata/arxivpy)
  type: SDKs
  url: https://github.com/titipata/arxivpy
- group: build
  title: arxiv-search (Search UI and APIs)
  type: GitHubRepository
  url: https://github.com/arXiv/arxiv-search
- group: build
  title: oaipmh (OAI-PMH service)
  type: GitHubRepository
  url: https://github.com/arXiv/oaipmh
- group: build
  title: arxiv-feed (Atom and RSS service)
  type: GitHubRepository
  url: https://github.com/arXiv/arxiv-feed
- group: build
  title: arxiv-canonical (JSON schema for arXiv metadata)
  type: GitHubRepository
  url: https://github.com/arXiv/arxiv-canonical
created: '2026-05-28'
description: 'arXiv is the open-access e-print repository operated by Cornell Tech, hosting more than two million preprints across physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering, and economics. arXiv exposes two principal programmatic interfaces: a REST Query API that returns Atom 1.0 XML and an OAI-PMH v2.0 endpoint for bulk metadata harvesting, plus daily RSS feeds and Amazon S3 / Kaggle distributions for full-text corpora.'
examples:
- key_count: 2
  name: Arxiv Oaipmh Listrecords Example
  slug: arxiv-oaipmh-listrecords-example
- key_count: 2
  name: Arxiv Query Articles Example
  slug: arxiv-query-articles-example
features:
- description: Targeted search across title, author, abstract, comment, journal reference, category, report number, and ID.
  name: Field-Prefix Search
- description: AND, OR, and ANDNOT operators with phrase grouping and parentheses.
  name: Boolean Query Composition
- description: submittedDate and lastUpdatedDate ranges in UTC.
  name: Date-Range Filtering
- description: Sort by relevance, lastUpdatedDate, or submittedDate, ascending or descending.
  name: Sort Control
- description: Fetch metadata for an explicit comma-separated list of arXiv IDs.
  name: ID-Lookup Mode
- description: Industry-standard metadata harvesting with resumption tokens and incremental from-date queries.
  name: OAI-PMH Bulk Harvest
- description: oai_dc, arXiv, and arXivRaw exposed via OAI-PMH.
  name: Three Metadata Formats
- description: Amazon S3 Requester-Pays buckets and periodic Kaggle dataset.
  name: Bulk Full-Text
- description: arXiv operates its services from a public GitHub organization (arXiv) with 50+ active repositories.
  name: Open Source Stack
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arxiv.png
integrations:
- description: Citation graph and paper-similarity overlay used by community tooling.
  name: Semantic Scholar
- description: Cross-references and bibliography overlay used in arXiv-bib-overlay.
  name: NASA ADS
- description: Articles surface DOIs once a publisher version of record exists.
  name: DOI / CrossRef
- description: Bulk PDF and source distribution through Requester-Pays buckets.
  name: Amazon S3
- description: Periodically refreshed full metadata dataset.
  name: Kaggle
- description: Multiple community MCP servers expose arXiv search to AI assistants.
  name: Model Context Protocol
json_schemas:
- name: Article
  property_count: 14
  slug: arxiv-article
json_structures:
- name: Arxiv Article Structure
  property_count: 14
  slug: arxiv-article-structure
jsonld:
- class_count: 15
  name: Arxiv Context
  property_count: 3
  slug: arxiv-context
layout: provider
modified: '2026-05-29'
name: arXiv
nav: Providers
network: true
overview: 'arXiv publishes 2 APIs on the [APIs.io](https://apis.io/) network: OAI-PMH API and Query API. Tagged areas include Science And Math, Scholarly Publishing, Preprints, Open Access, and Research.


  The arXiv catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  arXiv''s developer surface includes documentation, engineering blog, support, changelog, tooling, and 24 more developer resources.'
plans:
- name: Arxiv Plans Pricing
  plan_count: 1
  slug: arxiv-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 0
  name: Arxiv Rate Limits
  slug: arxiv-rate-limits
rules:
- name: arXiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: arxiv-jsonschema-spectral-rules
- name: arXiv API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: arxiv-rules
score:
  band: developing
  composite: 52.9
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 69.0
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arxiv/refs/heads/main/screenshots/arxiv-2026-06-20T172448.png
security:
- kind: domain-security
  name: Arxiv Domain Security
  slug: arxiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arxiv
solutions:
- description: Programmatic search and metadata retrieval.
  name: Query API
- description: Bulk metadata sync for downstream indexes.
  name: OAI-PMH Harvest
- description: Daily new-submission feeds per archive or subject.
  name: RSS Feeds
- description: S3 and Kaggle distributions for corpus-scale work.
  name: Bulk Full-Text
tags:
- Science And Math
- Scholarly Publishing
- Preprints
- Open Access
- Research
- Open Source
- Public APIs
use_cases:
- description: Build search and recommendation interfaces over the arXiv corpus.
  name: Research Discovery Tools
- description: Pull metadata, DOIs, and journal references for reference managers.
  name: Citation And Bibliographic Apps
- description: Build domain corpora for retrieval-augmented generation across scientific literature.
  name: AI Training And RAG
- description: Schedule incremental harvests and notify users of new submissions in a category.
  name: Topic Watching And Alerts
- description: Aggregate metadata to study research trends, author networks, and category growth.
  name: Bibliometrics And Trend Analysis
- description: Embed arXiv search into LaTeX editors, IDEs, note-taking tools, and chat assistants via MCP.
  name: Academic Workflow Integration
website: https://arxiv.org
---
