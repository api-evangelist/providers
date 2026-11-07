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
  band: human-only
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Prometheus Fuels website at prometheusfuels.ai: the route index of the site''s content management system, catalogued as one site surface rather than as se'
  name: Prometheus Fuels Website (WordPress REST)
  slug: prometheusfuels-ai-website-wordpress-rest
artifact_total: 5
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://prometheusfuels.ai/feed/
- group: auth
  href: https://artifacts.apis.io/prometheus-fuels/authentication/prometheus-fuels-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prometheus-fuels-authentication.yml
- group: design
  href: https://artifacts.apis.io/prometheus-fuels/conventions/prometheus-fuels-conventions.yml
  title: ''
  type: Conventions
  url: conventions/prometheus-fuels-conventions.yml
- group: design
  href: https://artifacts.apis.io/prometheus-fuels/errors/prometheus-fuels-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prometheus-fuels-problem-types.yml
- group: design
  href: https://artifacts.apis.io/prometheus-fuels/data-model/prometheus-fuels-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prometheus-fuels-data-model.yml
- group: design
  href: https://artifacts.apis.io/prometheus-fuels/lifecycle/prometheus-fuels-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/prometheus-fuels-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/prometheus-fuels/conformance/prometheus-fuels-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prometheus-fuels-conformance.yml
- group: agent
  href: https://artifacts.apis.io/prometheus-fuels/mcp/prometheus-fuels-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/prometheus-fuels-mcp.yml
- group: agent
  href: https://artifacts.apis.io/prometheus-fuels/skills/prometheus-fuels-browse-news-articles.md
  title: ''
  type: AgentSkill
  url: skills/prometheus-fuels-browse-news-articles.md
- group: agent
  href: https://artifacts.apis.io/prometheus-fuels/skills/prometheus-fuels-search-site-content.md
  title: ''
  type: AgentSkill
  url: skills/prometheus-fuels-search-site-content.md
- group: agent
  href: https://artifacts.apis.io/prometheus-fuels/llms/prometheus-fuels-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prometheus-fuels-llms.txt
- group: auth
  href: https://artifacts.apis.io/prometheus-fuels/security/prometheus-fuels-domain-security.yml
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
modified: '2026-10-06'
name: Prometheus Fuels
nav: Providers
network: true
overview: 'Prometheus Fuels is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Climate Tech, Carbon Capture, and Synthetic Fuels.


  Prometheus Fuels'' developer surface includes authentication, YouTube channel, and 18 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 18.5
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 11.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/prometheus-fuels/prometheus-fuels-2026-09-02T152142.png
security:
- kind: authentication
  name: Prometheus Fuels Authentication
  slug: prometheus-fuels-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Prometheus Fuels Domain Security
  slug: prometheus-fuels-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: Browse Prometheus Fuels news and press articles
  slug: prometheus-fuels-browse-news-articles
- name: Search Prometheus Fuels site content
  slug: prometheus-fuels-search-site-content
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
