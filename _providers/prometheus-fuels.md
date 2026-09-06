---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-05'
api_count: 12
apis:
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The news-articles API from Prometheus Fuels — 10 operation(s) over the site's `news-articles` custom post type, the company's published press and news coverage. Read operations respond anonymously; wr
  name: Prometheus Fuels news-articles API
  slug: prometheus-fuels-news-articles-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The pages API from Prometheus Fuels — 13 operation(s) for pages, including revisions and autosaves.
  name: Prometheus Fuels pages API
  slug: prometheus-fuels-pages-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The posts API from Prometheus Fuels — 13 operation(s) for posts, including revisions and autosaves.
  name: Prometheus Fuels posts API
  slug: prometheus-fuels-posts-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The media API from Prometheus Fuels — 9 operation(s) for the site's media library.
  name: Prometheus Fuels media API
  slug: prometheus-fuels-media-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The categories API from Prometheus Fuels — 7 operation(s) for categories.
  name: Prometheus Fuels categories API
  slug: prometheus-fuels-categories-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The tags API from Prometheus Fuels — 7 operation(s) for tags.
  name: Prometheus Fuels tags API
  slug: prometheus-fuels-tags-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The comments API from Prometheus Fuels — 7 operation(s) for comments.
  name: Prometheus Fuels comments API
  slug: prometheus-fuels-comments-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The users API from Prometheus Fuels — 21 operation(s) for users and application-password management. The collection read is anonymous; everything else requires authentication.
  name: Prometheus Fuels users API
  slug: prometheus-fuels-users-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The search API from Prometheus Fuels — 1 operation for cross-type site search.
  name: Prometheus Fuels search API
  slug: prometheus-fuels-search-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The taxonomies API from Prometheus Fuels — 2 operation(s) describing the site's taxonomies.
  name: Prometheus Fuels taxonomies API
  slug: prometheus-fuels-taxonomies-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The types API from Prometheus Fuels — 2 operation(s) describing the site's content types.
  name: Prometheus Fuels types API
  slug: prometheus-fuels-types-api
- baseURL: https://prometheusfuels.ai/wp-json
  baseurl_source: declared
  description: The statuses API from Prometheus Fuels — 2 operation(s) describing publication statuses.
  name: Prometheus Fuels statuses API
  slug: prometheus-fuels-statuses-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Categories API
  slug: open-prometheus-fuels-categories-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Comments API
  slug: open-prometheus-fuels-comments-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Media API
  slug: open-prometheus-fuels-media-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) News Articles API
  slug: open-prometheus-fuels-news-articles-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Pages API
  slug: open-prometheus-fuels-pages-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Posts API
  slug: open-prometheus-fuels-posts-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Search API
  slug: open-prometheus-fuels-search-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Statuses API
  slug: open-prometheus-fuels-statuses-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Tags API
  slug: open-prometheus-fuels-tags-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Taxonomies API
  slug: open-prometheus-fuels-taxonomies-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Types API
  slug: open-prometheus-fuels-types-api
- collection_type: open
  name: Prometheus Fuels Website Content API (WordPress REST API) Users API
  slug: open-prometheus-fuels-users-api
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/prometheus-fuels-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prometheus-fuels-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prometheus-fuels-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prometheus-fuels-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prometheus-fuels-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prometheus-fuels-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/prometheus-fuels-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/prometheus-fuels-browse-news-articles.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/prometheus-fuels-search-site-content.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prometheus-fuels-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prometheus-fuels-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prometheusfuels.ai/
- group: company
  title: ''
  type: About
  url: https://prometheusfuels.ai/about/
- group: other
  title: ''
  type: Technology
  url: https://prometheusfuels.ai/technology/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Prometheus-Fuels
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prometheusfuels
- group: company
  title: ''
  type: Twitter
  url: https://x.com/prometheusfuels
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@PrometheusFuels
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/prometheus-fuels_stock/
created: '2026-08-05'
description: Prometheus Fuels is a Santa Cruz, California energy company founded in 2019 by Rob McGinnis and launched out of Y Combinator, producing carbon-neutral electrofuels from atmospheric CO2. Its "no-desorb" direct air capture system dissolves CO2 into carbonate ions in water, and its Faraday Reactor hydrocarbon electrolyzer converts that carbon into methanol, gasoline, diesel, jet fuel and renewable natural gas at room temperature and atmospheric pressure using off-grid solar power. The company also markets an Ultra Long Duration Energy Storage (ULDES) product aimed at data-center power, and operates the Titan Forge Alpha pilot plant in Santa Cruz. It is backed by BMW i Ventures, Maersk Growth and Y Combinator. Prometheus Fuels publishes no product API, developer portal or SDK — it is a physical fuels manufacturer. The single machine-readable surface it operates is the WordPress REST API (wp/v2) behind its corporate site at prometheusfuels.ai, which serves anonymous read access to
  pages, posts, the site's `news-articles` custom post type, categories, tags, media, comments, users, search, taxonomies, types and statuses, with write operations gated behind WordPress application passwords. This profile was enriched by the API Evangelist pipeline from that live surface.
image: https://prometheusfuels.ai/wp-content/uploads/2026/03/logo_favicon-300x300.png
layout: provider
modified: '2026-08-05'
name: Prometheus Fuels
nav: Providers
network: true
overview: 'Prometheus Fuels publishes 12 APIs on the [APIs.io](https://apis.io/) network, including news-articles API, pages API, posts API, and 9 more. Tagged areas include Company, Energy, Climate Tech, Carbon Capture, and Synthetic Fuels.


  Prometheus Fuels'' developer surface includes authentication, YouTube channel, and 17 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prometheus-fuels/refs/heads/main/screenshots/prometheus-fuels-2026-09-02T152142.png
security:
- kind: authentication
  name: Prometheus Fuels Authentication
  slug: prometheus-fuels-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Prometheus Fuels Domain Security
  slug: prometheus-fuels-domain-security
  summary_line: TLSv1.3
slug: prometheus-fuels
tags:
- Company
- Energy
- Climate Tech
- Carbon Capture
- Synthetic Fuels
- Direct Air Capture
- Energy Storage
- content-api
- WordPress
website: https://prometheusfuels.ai/
---
