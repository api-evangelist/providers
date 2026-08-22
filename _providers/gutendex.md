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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gutendex Agentic Access
  operation_count: 2
  slug: gutendex-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Query and retrieve metadata for Project Gutenberg ebooks.
  name: Gutendex Books API
  slug: gutendex-books-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gutendex API
  slug: open-gutendex-api
- collection_type: open
  name: Gutendex Books API
  slug: open-gutendex-books-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/garethbjohnson/gutendex/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/garethbjohnson/gutendex/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gutendex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gutendex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gutendex.com
- group: docs
  title: ''
  type: Documentation
  url: https://gutendex.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/gutendex-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gutendex-book-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/gutendex-context.jsonld
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/garethbjohnson/gutendex
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/gutendex-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: plans/gutendex-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gutendex-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/gutendex-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/gutendex-vocabulary.yml
- group: auth
  title: ''
  type: Authentication
  url: https://gutendex.com
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/garethbjohnson/gutendex/wiki/Installation-Guide
- group: build
  title: Project Gutenberg MCP Server (bobbyhouse)
  type: Tools
  url: https://github.com/bobbyhouse/project-gutenberg-mcp
- group: build
  title: Project Gutenberg MCP Server (vellankis-space)
  type: Tools
  url: https://github.com/vellankis-space/project-gutenberg-mcp-server
- group: build
  title: Gutenberg MCP Server (nasimcoderex)
  type: Tools
  url: https://github.com/nasimcoderex/gutenberg-mcp-server
created: '2026-05-28'
description: Gutendex is a simple, self-hosted JSON-based web API for serving book catalog information from Project Gutenberg, providing structured metadata for over 70,000 free ebooks including titles, authors, subjects, bookshelves, languages, copyright status, media types, downloadable formats, and download counts. The hosted instance at gutendex.com runs the open-source Django project by Gareth B. Johnson under the MIT license.
examples:
- key_count: 13
  name: Gutendex Book Example
  slug: gutendex-book-example
- key_count: 1
  name: Gutendex Error Example
  slug: gutendex-error-example
- key_count: 6
  name: Gutendex Format Example
  slug: gutendex-format-example
- key_count: 13
  name: Gutendex Get Book Example
  slug: gutendex-get-book-example
- key_count: 4
  name: Gutendex List Books Example
  slug: gutendex-list-books-example
- key_count: 3
  name: Gutendex Person Example
  slug: gutendex-person-example
features:
- description: No API key, no signup, no rate limit documented; gutendex.com is openly available.
  name: Free Public API
- description: Mirrors the full Project Gutenberg catalog of free public-domain ebooks.
  name: 70,000+ Ebook Catalog
- description: Filter by author birth/death year, copyright status, language, MIME type, IDs, search keywords, and topic.
  name: Rich Filtering
- description: Sort results by popularity (default), ascending ID, or descending ID.
  name: Multiple Sort Orders
- description: Each book exposes a Format object mapping MIME types (HTML, EPUB, MOBI, plain text, JPEG) to direct download URLs.
  name: Multi-format Downloads
- description: Books are tagged with Library of Congress subject headings and curated Project Gutenberg bookshelves.
  name: Bookshelves and Subjects
- description: Books are indexed by two-character ISO language codes; filter by multiple languages at once.
  name: Multi-language Support
- description: MIT-licensed Django app that operators can run on their own infrastructure with nightly Project Gutenberg catalog sync.
  name: Self-Hostable
image: https://gutendex.com/static/images/gutendex.png
integrations:
- description: Upstream source. Gutendex nightly-ingests the official Project Gutenberg XML catalog and republishes it as JSON.
  name: Project Gutenberg
- description: Built on Django + Django REST Framework. Operators can extend the API with additional viewsets.
  name: Django REST Framework
- description: Community-maintained MCP servers expose Project Gutenberg / Gutendex to LLM agents (bobbyhouse, vellankis-space, nasimcoderex).
  name: Model Context Protocol
- description: Default Django storage backends used by self-hosted instances for catalog persistence.
  name: PostgreSQL / SQLite
json_schemas:
- name: BookList
  property_count: 4
  slug: gutendex-book-list
- name: Book
  property_count: 13
  slug: gutendex-book
- name: Error
  property_count: 1
  slug: gutendex-error
- name: Format
  property_count: 0
  slug: gutendex-format
- name: Person
  property_count: 3
  slug: gutendex-person
json_structures:
- name: Gutendex Book List Structure
  property_count: 4
  slug: gutendex-book-list-structure
- name: Gutendex Book Structure
  property_count: 13
  slug: gutendex-book-structure
- name: Gutendex Error Structure
  property_count: 1
  slug: gutendex-error-structure
- name: Gutendex Format Structure
  property_count: 0
  slug: gutendex-format-structure
- name: Gutendex Person Structure
  property_count: 3
  slug: gutendex-person-structure
jsonld:
- class_count: 12
  name: Gutendex Context
  property_count: 12
  slug: gutendex-context
layout: provider
modified: '2026-05-29'
name: Gutendex
nav: Providers
network: true
overview: 'Gutendex publishes 1 API on the [APIs.io](https://apis.io/) network: Books API. Tagged areas include Books, Catalog, Ebooks, Library, and Literature.


  The Gutendex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Gutendex''s developer surface includes documentation, pricing, authentication, getting-started guide, tooling, and 16 more developer resources.'
plans:
- name: Gutendex Plans Pricing
  plan_count: 2
  slug: gutendex-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Gutendex Rate Limits
  slug: gutendex-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Gutendex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gutendex-jsonschema-spectral-rules
- effective_rule_count: 13
  extends: []
  name: Gutendex API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 4
  slug: gutendex-rules
score:
  band: developing
  composite: 45.3
  delta: -4.8
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 25.0
    contract_quality: 71.3
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 31.6
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gutendex/refs/heads/main/screenshots/gutendex-2026-06-20T182442.png
security:
- kind: domain-security
  name: Gutendex Domain Security
  slug: gutendex-domain-security
  summary_line: TLSv1.3
slug: gutendex
tags:
- Books
- Catalog
- Ebooks
- Library
- Literature
- Metadata
- Open Source
- Project Gutenberg
- Public APIs
- Public Domain
use_cases:
- description: Power large-scale analysis of public-domain literature by ingesting the structured Project Gutenberg catalog.
  name: Literature Analytics
- description: Build classroom or self-study apps that surface public-domain texts by subject, author, or reading level.
  name: Educational Apps
- description: Use the download_count and bookshelf data to recommend popular classics or themed reading lists.
  name: Reading Recommendation Engines
- description: Power library catalog interfaces and ebook reader apps with a clean JSON facade over Project Gutenberg's XML archives.
  name: Digital Library Backends
- description: Use the catalog to discover bulk text downloads for training language models on public-domain corpora.
  name: Natural Language Processing Datasets
- description: Power author/title lookup widgets in citation managers and academic writing tools.
  name: Citation and Reference Tools
website: https://gutendex.com
---
