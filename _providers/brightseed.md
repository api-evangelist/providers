---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Brightseed Agentic Access
  operation_count: 84
  slug: brightseed-agentic-access
  summary_line: 84 operations · 51 acting
api_count: 11
apis:
- description: The posts API from Brightseed — 13 operation(s) for posts, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed posts API
  slug: brightseed-posts-api
- description: The pages API from Brightseed — 13 operation(s) for pages, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed pages API
  slug: brightseed-pages-api
- description: The media API from Brightseed — 9 operation(s) for media, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed media API
  slug: brightseed-media-api
- description: The categories API from Brightseed — 7 operation(s) for categories, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed categories API
  slug: brightseed-categories-api
- description: The tags API from Brightseed — 7 operation(s) for tags, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed tags API
  slug: brightseed-tags-api
- description: The users API from Brightseed — 21 operation(s) for users, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed users API
  slug: brightseed-users-api
- description: The comments API from Brightseed — 7 operation(s) for comments, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed comments API
  slug: brightseed-comments-api
- description: The search API from Brightseed — 1 operation(s) for search, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed search API
  slug: brightseed-search-api
- description: The taxonomies API from Brightseed — 2 operation(s) for taxonomies, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed taxonomies API
  slug: brightseed-taxonomies-api
- description: The types API from Brightseed — 2 operation(s) for types, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed types API
  slug: brightseed-types-api
- description: The statuses API from Brightseed — 2 operation(s) for statuses, served by the WordPress REST API wp/v2 namespace on www.brightseedbio.com.
  name: Brightseed statuses API
  slug: brightseed-statuses-api
artifact_total: 26
collections:
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) categories API
  slug: open-brightseed-categories-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) comments API
  slug: open-brightseed-comments-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) media API
  slug: open-brightseed-media-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) pages API
  slug: open-brightseed-pages-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) posts API
  slug: open-brightseed-posts-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) search API
  slug: open-brightseed-search-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) statuses API
  slug: open-brightseed-statuses-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) tags API
  slug: open-brightseed-tags-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) taxonomies API
  slug: open-brightseed-taxonomies-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) types API
  slug: open-brightseed-types-api
- collection_type: open
  name: Brightseed Site Content API (WordPress REST API) users API
  slug: open-brightseed-users-api
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/brightseed-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brightseed-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brightseed-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brightseed-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brightseed-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brightseed-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brightseed-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brightseed-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/brightseed-browse-site-content.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/brightseed-search-site-content.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brightseed-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brightseed-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightseed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightseedbio.com/
- group: company
  title: ''
  type: About
  url: https://www.brightseedbio.com/team/
- group: other
  title: ''
  type: Team
  url: https://www.brightseedbio.com/team/
- group: company
  title: ''
  type: Blog
  url: https://resources.brightseedbio.com/knowledgebase
- group: company
  title: ''
  type: BlogFeeds
  url: https://www.brightseedbio.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://www.brightseedbio.com/newsroom/
- group: company
  title: ''
  type: Careers
  url: https://www.brightseedbio.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.brightseedbio.com/contact-us/
- group: other
  title: ''
  type: Patents
  url: https://www.brightseedbio.com/patents/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brightseed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brightseedinc
- group: company
  title: ''
  type: Twitter
  url: https://x.com/brightseedbio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightseedbio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightseedbio.com/terms-of-use/
created: '2026-07-31'
description: Brightseed is a bioactives and AI company founded in 2017 (San Francisco, CA, with operations in Durham, NC) that uses its Forager AI platform to map the compounds in plants to human biological pathways and health benefits. Forager draws on a proprietary dataset the company describes as the world's largest — 21 million bioactive compounds and hundreds of biological receptors spanning 23 health areas — combining high-resolution omics, high-throughput robotics and machine learning to predict which natural compounds confer a benefit and where to source them at commercial scale. Hummingbird, launched in 2026, layers an agentic AI system on top of Forager to carry partners from discovery through development. Brightseed sells discovery services (Bioactive Profiler, Bioactive Ingredient Finder) and market-ready ingredients (Bio Gut Fiber, Bio Meta Control, Bio Gut Core) to food, supplement and health-science companies. Brightseed publishes no product or developer API for Forager or
  Hummingbird — those are sold as enterprise engagements through a contact form. The single machine-readable surface the company operates is the WordPress REST API (wp/v2) behind its corporate site at www.brightseedbio.com, which exposes anonymous read access to posts, pages, categories, tags, users, media, comments, search, taxonomies, types and statuses, plus authenticated write operations via WordPress application passwords. This profile was enriched by the API Evangelist pipeline from that live surface.
image: https://www.brightseedbio.com/wp-content/uploads/2025/07/cropped-Logo-1-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: brightseed-mcp.yml
  slug: brightseed-mcpyml
modified: '2026-07-31'
name: Brightseed
nav: Providers
network: true
overview: 'Brightseed publishes 11 APIs on the [APIs.io](https://apis.io/) network, including posts API, pages API, media API, and 8 more. Tagged areas include Company, Bioactives, Artificial Intelligence, Life Sciences, and Nutrition.


  Brightseed''s developer surface includes authentication, engineering blog, and 25 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 32.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 57.4
    developer_ergonomics: 16.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brightseed/refs/heads/main/screenshots/brightseed-2026-08-07T162813.png
security:
- kind: authentication
  name: Brightseed Authentication
  slug: brightseed-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brightseed Domain Security
  slug: brightseed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brightseed
tags:
- Company
- Bioactives
- Artificial Intelligence
- Life Sciences
- Nutrition
- Ingredients
- Drug Discovery
- Agrifood
- Content API
- WordPress
website: https://www.brightseedbio.com/
---
