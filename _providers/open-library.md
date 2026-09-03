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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Library Agentic Access
  operation_count: 9
  slug: open-library-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: Search Open Library's catalog of books, authors, lists, and subjects. Returns JSON results for full-text and faceted queries, with options for pagination, field selection, and language filtering.
  name: Open Library Search API
  slug: open-library-search-api
- description: Full-text search across the millions of digitized books in the Internet Archive's collection, returning matching passages and book identifiers.
  name: Open Library Search Inside API
  slug: open-library-search-inside-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: Retrieve work-level records (the abstract concept of a book independent of edition) by Open Library Work ID. Returns JSON, YAML, or RDF/XML.
  name: Open Library Works API
  slug: open-library-works-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: Retrieve edition-level records (specific printings, ISBNs, formats) by Open Library Edition ID, ISBN-10, ISBN-13, OCLC, or LCCN.
  name: Open Library Editions API
  slug: open-library-editions-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: Fetch author records and their works by Open Library Author ID. Supports JSON, YAML, and RDF/XML representations.
  name: Open Library Authors API
  slug: open-library-authors-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: Retrieve books, works, and metadata grouped by subject (genre, topic, place, time, person) with paging and faceting.
  name: Open Library Subjects API
  slug: open-library-subjects-api
- description: Retrieve book and author cover images by Open Library ID, ISBN, OCLC, LCCN, or Goodreads ID, in small, medium, and large sizes.
  name: Open Library Covers API
  slug: open-library-covers-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: Read and manage user-curated reading lists. Authenticated patrons can create lists and add or remove works, editions, and subjects.
  name: Open Library Lists API
  slug: open-library-lists-api
- description: 'Access a patron''s public reading log: Want to Read, Currently Reading, and Already Read shelves for a given Open Library account.'
  name: Open Library My Books API
  slug: open-library-mybooks-api
- description: Stream recent edits across the Open Library catalog including works, editions, authors, lists, and subjects, with filtering by kind and time range.
  name: Open Library Recent Changes API
  slug: open-library-recent-changes-api
- description: Legacy partner API that returns availability and read URLs for books matched by ISBN, OCLC, LCCN, or OLID identifiers across libraries and the Internet Archive.
  name: Open Library Read API
  slug: open-library-read-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: The Authors API from Open Library — 1 operation(s) for authors.
  name: Open Library Authors API
  slug: open-library-authors-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: The Editions API from Open Library — 1 operation(s) for editions.
  name: Open Library Editions API
  slug: open-library-editions-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: The Lists API from Open Library — 1 operation(s) for lists.
  name: Open Library Lists API
  slug: open-library-lists-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: The Recentchanges.json API from Open Library — 1 operation(s) for recentchanges.json.
  name: Open Library Recentchanges.json API
  slug: open-library-recentchanges-json-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: The Search API from Open Library — 2 operation(s) for search.
  name: Open Library Search API
  slug: open-library-search-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: The Search.json API from Open Library — 1 operation(s) for search.json.
  name: Open Library Search.json API
  slug: open-library-search-json-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: The Subjects API from Open Library — 1 operation(s) for subjects.
  name: Open Library Subjects API
  slug: open-library-subjects-api
- baseURL: https://openlibrary.org
  baseurl_source: spec
  description: The Works API from Open Library — 1 operation(s) for works.
  name: Open Library Works API
  slug: open-library-works-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Library Authors API
  slug: open-open-library-authors-api
- collection_type: open
  name: Open Library Authors Editions API
  slug: open-open-library-editions-api
- collection_type: open
  name: Open Library Authors Lists API
  slug: open-open-library-lists-api
- collection_type: open
  name: Open Library Authors Recentchanges.json API
  slug: open-open-library-recentchanges-json-api
- collection_type: open
  name: Open Library Authors Search API
  slug: open-open-library-search-api
- collection_type: open
  name: Open Library Authors Search.json API
  slug: open-open-library-search-json-api
- collection_type: open
  name: Open Library Authors Subjects API
  slug: open-open-library-subjects-api
- collection_type: open
  name: Open Library Authors Works API
  slug: open-open-library-works-api
- collection_type: open
  name: Open Library API
  slug: open-open-library
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/open-library-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-library-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-library-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openlibrary.org/
- group: docs
  title: ''
  type: Documentation
  url: https://openlibrary.org/developers/api
- group: other
  title: ''
  type: Bulk Data Dumps
  url: https://openlibrary.org/developers/dumps
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/internetarchive/openlibrary
- group: operate
  title: ''
  type: Issues
  url: https://github.com/internetarchive/openlibrary/issues
- group: company
  title: ''
  type: Blog
  url: https://blog.openlibrary.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://archive.org/about/terms.php
created: '2025-02-06'
description: Open Library offers a suite of APIs to help developers get up and running with its data. This includes RESTful APIs that make Open Library data available in JSON, YAML, and RDF/XML formats, plus a Search Inside full-text search service, cover image endpoints, and read-protocol library lookup APIs. Most resources also expose machine-readable representations by appending .json, .yml, or .rdf to any Open Library URL.
finops:
- name: Open Library Finops
  service_category: API
  slug: open-library-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-library.png
layout: provider
modified: '2026-04-28'
name: Open Library
nav: Providers
network: true
overview: 'Open Library publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Search API, Works API, Editions API, and 11 more. Tagged areas include Authors, Books, Catalog, Covers, and Libraries.


  Open Library''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Open Library Plans Pricing
  plan_count: 3
  slug: open-library-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Open Library Rate Limits
  slug: open-library-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 65.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 0.0
    contract_quality: 43.4
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-library/refs/heads/main/screenshots/open-library-2026-06-20T190844.png
security:
- kind: domain-security
  name: Open Library Domain Security
  slug: open-library-domain-security
  summary_line: TLSv1.3
slug: open-library
tags:
- Authors
- Books
- Catalog
- Covers
- Libraries
- Open Data
- Reading Lists
- Search
- Subjects
website: https://openlibrary.org/
---
