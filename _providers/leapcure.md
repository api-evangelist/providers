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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
api_count: 11
apis:
- description: The categories API from Leapcure — 2 operation(s) for categories.
  name: Leapcure categories API
  slug: leapcure-categories-api
- description: The comments API from Leapcure — 2 operation(s) for comments.
  name: Leapcure comments API
  slug: leapcure-comments-api
- description: The media API from Leapcure — 6 operation(s) for media.
  name: Leapcure media API
  slug: leapcure-media-api
- description: The pages API from Leapcure — 6 operation(s) for pages.
  name: Leapcure pages API
  slug: leapcure-pages-api
- description: The posts API from Leapcure — 6 operation(s) for posts.
  name: Leapcure posts API
  slug: leapcure-posts-api
- description: The search API from Leapcure — 1 operation(s) for search.
  name: Leapcure search API
  slug: leapcure-search-api
- description: The statuses API from Leapcure — 2 operation(s) for statuses.
  name: Leapcure statuses API
  slug: leapcure-statuses-api
- description: The tags API from Leapcure — 2 operation(s) for tags.
  name: Leapcure tags API
  slug: leapcure-tags-api
- description: The taxonomies API from Leapcure — 2 operation(s) for taxonomies.
  name: Leapcure taxonomies API
  slug: leapcure-taxonomies-api
- description: The types API from Leapcure — 2 operation(s) for types.
  name: Leapcure types API
  slug: leapcure-types-api
- description: The users API from Leapcure — 6 operation(s) for users.
  name: Leapcure users API
  slug: leapcure-users-api
artifact_total: 14
common:
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
  name: leapcure-mcp.yml
  slug: leapcure-mcpyml
modified: '2026-07-20'
name: Leapcure
nav: Providers
network: true
overview: 'Leapcure publishes 11 APIs on the [APIs.io](https://apis.io/) network, including categories API, comments API, media API, and 8 more. Tagged areas include Company, Clinical Trials, Patient Recruitment, Healthcare, and Blog.


  Leapcure''s developer surface includes authentication, engineering blog, and 13 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 32.8
  delta: -3.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.3
    developer_ergonomics: 23.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 36.2
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Content API
- WordPress
website: https://leapcure.com
---
