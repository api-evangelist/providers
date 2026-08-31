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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: 4Chan Agentic Access
  operation_count: 6
  slug: 4chan-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: Per-board list of OP numbers for closed, archived threads.
  name: 4chan Archive API
  slug: 4chan-archive-api
- description: List of all boards on 4chan and 4channel and their per-board settings.
  name: 4chan Boards API
  slug: 4chan-boards-api
- description: Per-board catalog snapshot containing every OP and its preview replies, grouped by index page.
  name: 4chan Catalog API
  slug: 4chan-catalog-api
- description: Per-board, per-page index document of threads (each with a posts array including the OP and a small number of preview replies).
  name: 4chan Indexes API
  slug: 4chan-indexes-api
- description: Per-board summary list of every live thread (id, last-modified, reply count) grouped by index page.
  name: 4chan Threadlist API
  slug: 4chan-threadlist-api
- description: Single-thread document containing the OP and every reply.
  name: 4chan Threads API
  slug: 4chan-threads-api
artifact_total: 58
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 4chan Read-Only JSON API
  slug: open-4chan-api
- collection_type: open
  name: 4chan Read-Only JSON Archive API
  slug: open-4chan-archive-api
- collection_type: open
  name: 4chan Read-Only JSON Archive Boards API
  slug: open-4chan-boards-api
- collection_type: open
  name: 4chan Read-Only JSON Archive Catalog API
  slug: open-4chan-catalog-api
- collection_type: open
  name: 4chan Read-Only JSON Archive Indexes API
  slug: open-4chan-indexes-api
- collection_type: open
  name: 4chan Read-Only JSON Archive Threadlist API
  slug: open-4chan-threadlist-api
- collection_type: open
  name: 4chan Read-Only JSON Archive Threads API
  slug: open-4chan-threads-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/4chan/4chan-JS/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/4chan-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/4chan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4chan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.4chan.org
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/4chan/4chan-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/4chan
- group: build
  title: 4chan native browser extension source
  type: SourceCode
  url: https://github.com/4chan/4chan-JS
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:api@4chan.org
- group: build
  title: MCP Server (community, unofficial)
  type: Tools
  url: https://github.com/sh0n0/chan-mcp-server
- group: build
  title: Python Wrapper (BASC-py4chan, community)
  type: SDKs
  url: https://github.com/bibanon/BASC-py4chan
- group: build
  title: Python Wrapper (py-4chan, community)
  type: SDKs
  url: https://github.com/e000/py-4chan
- group: build
  title: Node.js Client (4chanjs, community)
  type: SDKs
  url: https://github.com/yocontra/4chanjs
- group: build
  title: Go Client (go-4chan-api, community)
  type: SDKs
  url: https://github.com/moshee/go-4chan-api
- group: build
  title: Rust Client (rchan, community)
  type: SDKs
  url: https://github.com/insomnimus/rchan
- group: build
  title: Racket Client (yotsubAPI, community)
  type: SDKs
  url: https://github.com/g-gundam/yotsubAPI
- group: build
  title: BA Thread Archiver (community)
  type: Tools
  url: https://github.com/hydrusnetwork/BA-4chan-thread-archiver
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/4chan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4chan-rate-limits.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/4chan-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/4chan-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/4chan-context.jsonld
created: '2026-05-28'
description: 4chan is a simple image-based bulletin board where anyone can post comments and share images across topic-specific boards. 4chan exposes a read-only JSON API (launched September 2012) that serves the same board, thread, catalog, and archive data consumed by the public site via static JSON files at a.4cdn.org. The API supports GET/HEAD/OPTIONS only — there is no posting, authentication, or write surface.
examples:
- key_count: 29
  name: 4Chan Api Board Example
  slug: 4chan-api-board-example
- key_count: 1
  name: 4Chan Api Boards Response Example
  slug: 4chan-api-boards-response-example
- key_count: 2
  name: 4Chan Api Catalog Page Example
  slug: 4chan-api-catalog-page-example
- key_count: 3
  name: 4Chan Api Cooldowns Example
  slug: 4chan-api-cooldowns-example
- key_count: 1
  name: 4Chan Api Index Page Response Example
  slug: 4chan-api-index-page-response-example
- key_count: 1
  name: 4Chan Api Index Page Thread Example
  slug: 4chan-api-index-page-thread-example
- key_count: 43
  name: 4Chan Api Post Example
  slug: 4chan-api-post-example
- key_count: 1
  name: 4Chan Api Thread Response Example
  slug: 4chan-api-thread-response-example
- key_count: 3
  name: 4Chan Api Threadlist Entry Example
  slug: 4chan-api-threadlist-entry-example
- key_count: 2
  name: 4Chan Api Threadlist Page Example
  slug: 4chan-api-threadlist-page-example
image: https://s.4cdn.org/image/fp/logo-transparent.png
json_schemas:
- name: ArchiveResponse
  property_count: 0
  slug: 4chan-api-archive-response
- name: Board
  property_count: 29
  slug: 4chan-api-board
- name: BoardsResponse
  property_count: 1
  slug: 4chan-api-boards-response
- name: CatalogPage
  property_count: 2
  slug: 4chan-api-catalog-page
- name: CatalogResponse
  property_count: 0
  slug: 4chan-api-catalog-response
- name: Cooldowns
  property_count: 3
  slug: 4chan-api-cooldowns
- name: IndexPageResponse
  property_count: 1
  slug: 4chan-api-index-page-response
- name: IndexPageThread
  property_count: 1
  slug: 4chan-api-index-page-thread
- name: Post
  property_count: 43
  slug: 4chan-api-post
- name: ThreadResponse
  property_count: 1
  slug: 4chan-api-thread-response
- name: ThreadlistEntry
  property_count: 3
  slug: 4chan-api-threadlist-entry
- name: ThreadlistPage
  property_count: 2
  slug: 4chan-api-threadlist-page
- name: ThreadlistResponse
  property_count: 0
  slug: 4chan-api-threadlist-response
json_structures:
- name: 4Chan Api Archive Response Structure
  property_count: 0
  slug: 4chan-api-archive-response-structure
- name: 4Chan Api Board Structure
  property_count: 29
  slug: 4chan-api-board-structure
- name: 4Chan Api Boards Response Structure
  property_count: 1
  slug: 4chan-api-boards-response-structure
- name: 4Chan Api Catalog Page Structure
  property_count: 2
  slug: 4chan-api-catalog-page-structure
- name: 4Chan Api Catalog Response Structure
  property_count: 0
  slug: 4chan-api-catalog-response-structure
- name: 4Chan Api Cooldowns Structure
  property_count: 3
  slug: 4chan-api-cooldowns-structure
- name: 4Chan Api Index Page Response Structure
  property_count: 1
  slug: 4chan-api-index-page-response-structure
- name: 4Chan Api Index Page Thread Structure
  property_count: 1
  slug: 4chan-api-index-page-thread-structure
- name: 4Chan Api Post Structure
  property_count: 43
  slug: 4chan-api-post-structure
- name: 4Chan Api Thread Response Structure
  property_count: 1
  slug: 4chan-api-thread-response-structure
- name: 4Chan Api Threadlist Entry Structure
  property_count: 3
  slug: 4chan-api-threadlist-entry-structure
- name: 4Chan Api Threadlist Page Structure
  property_count: 2
  slug: 4chan-api-threadlist-page-structure
- name: 4Chan Api Threadlist Response Structure
  property_count: 0
  slug: 4chan-api-threadlist-response-structure
jsonld:
- class_count: 10
  name: 4Chan Context
  property_count: 76
  slug: 4chan-context
layout: provider
modified: '2026-05-28'
name: 4chan
nav: Providers
network: true
overview: '4chan publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Archive API, Boards API, Catalog API, and 3 more. Tagged areas include Social, Bulletin Board, Imageboard, Read Only, and JSON.


  The 4chan catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  4chan''s developer surface includes documentation, tooling, and 21 more developer resources.'
plans:
- name: 4Chan Plans Pricing
  plan_count: 2
  slug: 4chan-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: 4Chan Rate Limits
  slug: 4chan-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: 4chan API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: 4chan-jsonschema-spectral-rules
- effective_rule_count: 86
  extends:
  - spectral:oas
  name: 4chan API Rules
  rule_count: 45
  severity_counts:
    error: 14
    hint: 0
    info: 8
    warn: 23
  slug: 4chan-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 34.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 28.8
    contract_quality: 21.3
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/4chan/refs/heads/main/screenshots/4chan-2026-06-20T162723.png
security:
- kind: domain-security
  name: 4Chan Domain Security
  slug: 4chan-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 4Chan Vulnerability Disclosure
  slug: 4chan-vulnerability-disclosure
  summary_line: Hackerone
slug: 4chan
tags:
- Social
- Bulletin Board
- Imageboard
- Read Only
- JSON
- Public APIs
- Community
website: https://www.4chan.org
---
