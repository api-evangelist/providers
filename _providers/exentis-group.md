---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Exentis Group Agentic Access
  operation_count: 14
  slug: exentis-group-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- baseURL: https://www.exentis-group.com/wp-json
  baseurl_source: declared
  description: The Posts API from Exentis Group — news, press releases and article records served as JSON by the WordPress REST API on www.exentis-group.com, filterable by date, slug, category and full text, and ava
  name: Exentis Group Posts API
  slug: exentis-group-posts-api
- baseURL: https://www.exentis-group.com/wp-json
  baseurl_source: declared
  description: The Blog API from Exentis Group — the `blog` custom post type behind /en/media/blog/, served as JSON at the `blogposts` REST base and grouped by the `blogkategorie` taxonomy. 16 blog entries were read
  name: Exentis Group Blog API
  slug: exentis-group-blog-api
- baseURL: https://www.exentis-group.com/wp-json
  baseurl_source: declared
  description: The Pages API from Exentis Group — corporate website pages covering the 3D screen printing technology platform, materials, applications, certifications, sustainability, investors, careers and contact,
  name: Exentis Group Pages API
  slug: exentis-group-pages-api
- baseURL: https://www.exentis-group.com/wp-json
  baseurl_source: declared
  description: The Media API from Exentis Group — the media library of product photography, trade-fair assets, technical diagrams and documents attached to pages, posts and blog entries, with rendered source URLs, M
  name: Exentis Group Media API
  slug: exentis-group-media-api
- baseURL: https://www.exentis-group.com/wp-json
  baseurl_source: declared
  description: The Categories API from Exentis Group — the `category` taxonomy that posts are filed under, with parent/child nesting and post counts. 27 categories were readable anonymously at probe time.
  name: Exentis Group Categories API
  slug: exentis-group-categories-api
- baseURL: https://www.exentis-group.com/wp-json
  baseurl_source: declared
  description: 'The Search API from Exentis Group — full-text search across every publicly readable object on www.exentis-group.com, returning id, title, url, type and subtype, filterable by object type and subtype. '
  name: Exentis Group Search API
  slug: exentis-group-search-api
- baseURL: https://www.exentis-group.com/wp-json
  baseurl_source: declared
  description: The Languages API from Exentis Group — the Polylang language configuration for the site, returning locale, slug, default flag, home and search URLs and per-language content counts for German (de_CH, d
  name: Exentis Group Languages API
  slug: exentis-group-languages-api
- description: An MCP (Model Context Protocol) server endpoint mounted on www.exentis-group.com by the WordPress MCP adapter, alongside the WordPress Abilities API. The endpoint is really served — GET /wp-json/mcp e
  name: Exentis Group MCP Server
  slug: exentis-group-mcp-server
- baseURL: https://www.exentis-group.com/wp-json
  baseurl_source: declared
  description: The Taxonomy API from Exentis Group — 2 operation(s) for taxonomy.
  name: Exentis Group Taxonomy API
  slug: exentis-group-taxonomy-api
artifact_total: 23
collections:
- collection_type: open
  name: Exentis Group Blog API
  slug: open-exentis-group-blog-api
- collection_type: open
  name: Exentis Group Blog Categories API
  slug: open-exentis-group-blog-categories-api
- collection_type: open
  name: Exentis Group Categories API
  slug: open-exentis-group-categories-api
- collection_type: open
  name: Exentis Group Languages API
  slug: open-exentis-group-languages-api
- collection_type: open
  name: Exentis Group Media API
  slug: open-exentis-group-media-api
- collection_type: open
  name: Exentis Group Pages API
  slug: open-exentis-group-pages-api
- collection_type: open
  name: Exentis Group Posts API
  slug: open-exentis-group-posts-api
- collection_type: open
  name: Exentis Group Search API
  slug: open-exentis-group-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/exentis-group-blog-categories-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exentis-group-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.exentis-group.com/en/
- group: company
  title: ''
  type: About
  url: https://www.exentis-group.com/en/about-exentis/who-we-are/
- group: other
  title: ''
  type: Technology
  url: https://www.exentis-group.com/en/technology/exentis-technology/
- group: other
  title: ''
  type: Applications
  url: https://www.exentis-group.com/en/applications/applications-examples/
- group: company
  title: ''
  type: Blog
  url: https://www.exentis-group.com/en/media/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.exentis-group.com/en/feed/
- group: company
  title: ''
  type: News
  url: https://www.exentis-group.com/en/media/recent-news/
- group: company
  title: ''
  type: Press
  url: https://www.exentis-group.com/en/media/press-releases/
- group: company
  title: ''
  type: Investors
  url: https://www.exentis-group.com/en/investors/recent-information/
- group: company
  title: ''
  type: Careers
  url: https://www.exentis-group.com/en/careers/vacancies/
- group: operate
  title: ''
  type: Support
  url: https://www.exentis-group.com/en/contact/
- group: auth
  title: ''
  type: Compliance
  url: https://www.exentis-group.com/en/about-exentis/our-certifications/
- group: other
  title: ''
  type: Sustainability
  url: https://www.exentis-group.com/en/sustainability/sustainability-at-exentis/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exentis-group.com/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exentis-group.com/en/privacy-notice/
- group: other
  title: ''
  type: Imprint
  url: https://www.exentis-group.com/en/imprint/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exentis-group-ag/
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@exentisgroupag1372
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/exentis-group_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/exentis-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exentis-group-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/exentis-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exentis-group-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exentis-group-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exentis-group-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/exentis-group-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/exentis-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/exentis-group-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/exentis-group-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/exentis-group-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/exentis-group-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/exentis-group-posts-api-overlay.yaml
created: '2026-08-12'
description: 'Exentis Group AG is a Swiss industrial technology company headquartered at Im Stetterfeld 2 in Stetten (canton Aargau), near Zurich, with facilities and subsidiaries in Switzerland, Germany and the United States. It develops and sells the Exentis 3D Screen Printing platform — an additive manufacturing technology that builds parts layer by layer at room temperature through screen printing followed by sintering, with no lasers, no support structures and no rework, reaching wall thicknesses and cavities down to roughly 70 micrometres and producing undercuts and closed cavities. The company positions the platform for industrial series production rather than prototyping: a single production system is marketed as capable of millions of components per year, and in pharmaceuticals the process is used to mass-produce tablets with adjustable, controlled drug-release profiles. Its named market segments are pharma, new energy and ultra-fine industrial structures, in metals, technical ceramics
  and polymers, alongside cleanroom and bioprinting configurations. Exentis holds ISO 9001:2015 certification for its Stetten head office and all German locations, and in Q4 2024 reported roughly USD 22 million in orders for nine production systems shipping to United States customers. It is a manufacturing-equipment vendor, not a software company: it publishes no developer portal, no product API, no SDKs, no pricing and no status page. The only machine-readable API surface on its public host is the WordPress REST API behind www.exentis-group.com, which serves the press room, blog, corporate pages, media library, taxonomies, site search and Polylang language configuration as JSON, read-only without credentials — plus an MCP server endpoint mounted by the WordPress MCP adapter, which is present but returns 401 to anonymous callers.'
image: https://www.exentis-group.com/app/uploads/2022/11/Logo-exentis.svg
layout: provider
mcp_servers:
- description: ''
  name: Exentis Group MCP Server
  slug: exentis-group-mcp-server
modified: '2026-08-12'
name: Exentis Group
nav: Providers
network: true
overview: 'Exentis Group publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Blog API, Pages API, and 5 more. Tagged areas include Company, Additive Manufacturing, 3D Printing, Industrial Manufacturing, and Advanced Materials.


  Exentis Group''s developer surface includes engineering blog, product news, support, YouTube channel, authentication, code examples, and 29 more developer resources.'
plans:
- name: Exentis Group Plans Pricing
  plan_count: 0
  slug: exentis-group-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Exentis Group Rate Limits
  slug: exentis-group-rate-limits
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 16.5
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 25.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exentis-group/refs/heads/main/screenshots/exentis-group-2026-09-02T145447.png
security:
- kind: authentication
  name: Exentis Group Authentication
  slug: exentis-group-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Exentis Group Domain Security
  slug: exentis-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: exentis-group
tags:
- Company
- Additive Manufacturing
- 3D Printing
- Industrial Manufacturing
- Advanced Materials
- Technical Ceramics
- Metals
- Pharmaceutical Manufacturing
- New Energy
- Switzerland
- Hardware
- Content
website: https://www.exentis-group.com/en/
---
