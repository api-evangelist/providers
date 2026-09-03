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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The categories API from Leapcure — 2 operation(s) for categories.
  name: Leapcure categories API
  slug: leapcure-categories-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The comments API from Leapcure — 2 operation(s) for comments.
  name: Leapcure comments API
  slug: leapcure-comments-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The media API from Leapcure — 6 operation(s) for media.
  name: Leapcure media API
  slug: leapcure-media-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The pages API from Leapcure — 6 operation(s) for pages.
  name: Leapcure pages API
  slug: leapcure-pages-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The posts API from Leapcure — 6 operation(s) for posts.
  name: Leapcure posts API
  slug: leapcure-posts-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The search API from Leapcure — 1 operation(s) for search.
  name: Leapcure search API
  slug: leapcure-search-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The statuses API from Leapcure — 2 operation(s) for statuses.
  name: Leapcure statuses API
  slug: leapcure-statuses-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The tags API from Leapcure — 2 operation(s) for tags.
  name: Leapcure tags API
  slug: leapcure-tags-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The taxonomies API from Leapcure — 2 operation(s) for taxonomies.
  name: Leapcure taxonomies API
  slug: leapcure-taxonomies-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The types API from Leapcure — 2 operation(s) for types.
  name: Leapcure types API
  slug: leapcure-types-api
- baseURL: https://blog.leapcure.com/wp-json
  baseurl_source: declared
  description: The users API from Leapcure — 6 operation(s) for users.
  name: Leapcure users API
  slug: leapcure-users-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories API
  slug: open-leapcure-categories-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories comments API
  slug: open-leapcure-comments-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories media API
  slug: open-leapcure-media-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories pages API
  slug: open-leapcure-pages-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories posts API
  slug: open-leapcure-posts-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories search API
  slug: open-leapcure-search-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories statuses API
  slug: open-leapcure-statuses-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories tags API
  slug: open-leapcure-tags-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories taxonomies API
  slug: open-leapcure-taxonomies-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories types API
  slug: open-leapcure-types-api
- collection_type: open
  name: Leapcure Blog Content API (WordPress REST API) categories users API
  slug: open-leapcure-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/leapcure-blog-content-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leapcure-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leapcure-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leapcure-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leapcure-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leapcure-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leapcure-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leapcure-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/leapcure-browse-blog-content.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/leapcure-search-content.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leapcure-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leapcure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leapcure.com
- group: company
  title: ''
  type: Blog
  url: https://blog.leapcure.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leapcure.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leapcure.com/terms-of-service
created: '2026-07-17'
description: Leapcure is a clinical-trial patient recruitment company whose mission is "where patient advocacy meets research" — connecting patients with clinical studies and helping research sites and sponsors reach and enroll participants. Leapcure was surfaced as a portfolio company of 500 Global and added to the API Evangelist network. The company publishes no product API of its own; the single machine-readable surface it operates is the WordPress REST API (wp/v2) behind its blog at blog.leapcure.com, which exposes read access to posts, pages, categories, tags, users, media, comments and search, plus authenticated write operations via WordPress application passwords. This profile was enriched by the API Evangelist pipeline from that live surface.
image: https://blog.leapcure.com/wp-content/uploads/2022/10/cropped-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Leapcure MCP Server
  slug: leapcure-mcp-server
modified: '2026-07-20'
name: Leapcure
nav: Providers
network: true
overview: 'Leapcure publishes 11 APIs on the [APIs.io](https://apis.io/) network, including categories API, comments API, media API, and 8 more. Tagged areas include Company, Clinical Trials, Patient Recruitment, Healthcare, and Blog.


  Leapcure''s developer surface includes authentication, engineering blog, and 14 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 55.7
    developer_ergonomics: 32.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 34.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leapcure/refs/heads/main/screenshots/leapcure-2026-07-25T224748.png
security:
- kind: authentication
  name: Leapcure Authentication
  slug: leapcure-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Leapcure Domain Security
  slug: leapcure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leapcure
tags:
- Company
- Clinical Trials
- Patient Recruitment
- Healthcare
- Blog
- content-api
- WordPress
website: https://leapcure.com
---
