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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ieee Agentic Access
  operation_count: 1
  slug: ieee-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: REST endpoint for querying and retrieving metadata records and abstracts for more than 6 million documents in IEEE Xplore, including journals, conference proceedings, standards, books, and courses. Su
  name: IEEE Xplore Metadata Search API
  slug: ieee-xplore-metadata-search-api
- description: Batch metadata lookup endpoint that accepts up to 25 DOI (Digital Object Identifier) numbers per request and returns metadata records including abstracts for each resolved document. Useful for enrichi
  name: IEEE Xplore DOI API
  slug: ieee-xplore-doi-api
- description: 'Full-text retrieval endpoint for articles designated as IEEE Open Access or chargeable open content. Returns complete article text for documents that are freely available under open-access licensing. '
  name: IEEE Xplore Open Access API
  slug: ieee-xplore-open-access-api
- description: Full-text retrieval endpoint for chargeable IEEE articles accessible to institutional subscribers. Returns complete article content for documents covered under an organization's IEEE Xplore subscripti
  name: IEEE Xplore Full-Text Access API
  slug: ieee-xplore-full-text-access-api
- baseURL: https://ieeexploreapi.ieee.org/api/v1/search/articles
  baseurl_source: declared
  description: Query and retrieve metadata records and abstracts for IEEE documents
  name: IEEE Xplore Metadata Search API
  slug: ieee-metadata-search-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IEEE Xplore Metadata Search API
  slug: open-ieee-metadata-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ieee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ieee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ieee-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ieeexplore.ieee.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ieee.org/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ieee.org/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ieee.org/getting_started
- group: other
  title: ''
  type: Registration
  url: https://developer.ieee.org/member/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.ieee.org/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ieee.org/security-privacy.html
- group: operate
  title: ''
  type: Support
  url: mailto:onlinesupport@ieee.org
- group: build
  title: Python 3 SDK
  type: SDKs
  url: https://developer.ieee.org/Python3_Software_Development_Kit
- group: build
  title: Java SDK
  type: SDKs
  url: https://developer.ieee.org/Java_Software_Development_Kit
- group: commercial
  title: ''
  type: Plans
  url: plans/ieee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ieee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ieee-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://spectrum.ieee.org/feeds/feed.rss
created: '2026-06-13'
description: IEEE Xplore is the authoritative technical library operated by the Institute of Electrical and Electronics Engineers (IEEE), providing access to over 6 million documents spanning engineering, computer science, electronics, and technology. The IEEE Xplore API suite exposes a REST-based Metadata Search API for querying and retrieving abstracts and metadata across the full corpus, a DOI API for resolving up to 25 DOIs per request, an Open Access API for full-text retrieval of freely available articles, and a Full-Text Access API for institutional subscribers. API access requires key-based registration through the IEEE Developer Portal.
examples:
- key_count: 3
  name: Boolean Search Example
  slug: boolean-search-example
- key_count: 2
  name: Doi Lookup Example
  slug: doi-lookup-example
- key_count: 2
  name: Metadata Search Example
  slug: metadata-search-example
features:
- description: Query and retrieve metadata and abstracts for 6M+ IEEE documents including journals, conferences, standards, and books.
  name: Metadata Search
- description: Full AND, OR, NOT Boolean operator support with fielded search across title, author, abstract, affiliation, and more.
  name: Boolean Search
- description: Resolve up to 25 DOIs per request to retrieve metadata and abstracts in a single call.
  name: DOI Batch Lookup
- description: Retrieve full article text for openly licensed IEEE publications without institutional subscription.
  name: Open Access Full Text
- description: Full article retrieval for subscribing institutions via auth-token-gated full-text API.
  name: Institutional Full Text
- description: Default JSON responses with optional XML output format for all API endpoints.
  name: JSON and XML Responses
- description: Navigate large result sets using start_record parameter with up to 200 results per request.
  name: Pagination
- description: Filter results by content_type (Journals, Conferences, Standards, Books, Courses), date range, and other facets.
  name: Content Filtering
- description: Interactive web-based query builder at developer.ieee.org/io-docs for API exploration with pre-loaded credentials.
  name: Dynamic Query Tool
- description: Official SDKs available in Python 3 and Java for rapid integration.
  name: Multi-Language SDKs
finops:
- name: Ieee Finops
  service_category: ''
  slug: ieee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ieee.png
integrations:
- description: IEEE articles carry DOIs resolvable via the CrossRef and doi.org infrastructure.
  name: DOI Foundation / CrossRef
- description: IEEE Xplore metadata is indexed by major abstract and citation databases.
  name: Scopus and Web of Science
- description: IEEE publications surfaced via Semantic Scholar's open research graph.
  name: Semantic Scholar
- description: Author identifiers linked to IEEE contributor profiles.
  name: ORCID
- description: IEEE Xplore supports standard citation export formats compatible with reference managers.
  name: RIS / BibTeX Export
jsonld:
- class_count: 0
  name: Ieee Xplore Api Context
  property_count: 0
  slug: ieee-xplore-api
layout: provider
modified: '2026-06-13'
name: IEEE Xplore
nav: Providers
network: true
overview: 'IEEE Xplore publishes 1 API on the [APIs.io](https://apis.io/) network: Metadata Search API. Tagged areas include Science And Math, Scholarly Publishing, Engineering, Computer Science, and Standards.


  The IEEE Xplore catalog on APIs.io includes 1 JSON-LD context.


  IEEE Xplore''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 12 more developer resources.'
plans:
- name: Ieee Plans Pricing
  plan_count: 2
  slug: ieee-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Ieee Rate Limits
  slug: ieee-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 59.9
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 44.4
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ieee/refs/heads/main/screenshots/ieee-2026-06-20T183213.png
security:
- kind: authentication
  name: Ieee Authentication
  slug: ieee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ieee Domain Security
  slug: ieee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ieee
tags:
- Science And Math
- Scholarly Publishing
- Engineering
- Computer Science
- Standards
- Research
- Academic
- Technology
use_cases:
- description: Build search interfaces and recommendation engines over IEEE's 6M+ technical documents.
  name: Academic Research Discovery
- description: Enrich reference lists and bibliographic databases with IEEE metadata via DOI batch lookup.
  name: Citation Management
- description: Sync IEEE metadata into library catalogs, institutional repositories, and research management systems.
  name: Institutional Repository Integration
- description: Query and surface relevant IEEE standards for compliance documentation and engineering workflows.
  name: Standards Compliance Tooling
- description: Build retrieval-augmented generation pipelines over IEEE abstracts and metadata for domain-specific AI assistants.
  name: AI and RAG Applications
- description: Aggregate metadata to analyze publication trends, author networks, and citation patterns across IEEE disciplines.
  name: Publication Analytics
- description: Integrate full-text access APIs into reading platforms for institutional subscribers.
  name: Content Licensing Platforms
website: https://ieeexplore.ieee.org
---
