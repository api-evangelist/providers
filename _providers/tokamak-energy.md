---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
api_count: 9
apis:
- description: Public, unauthenticated read access to the Tokamak Energy news archive behind tokamakenergy.com/latest-news/ via the WordPress core REST API. Verified live at 84 published posts on 2026-08-30.
  name: Tokamak Energy Posts API
  slug: tokamak-energy-posts-api
- description: Public, unauthenticated read access to the static pages of tokamakenergy.com — About Us, Our Fusion Energy and HTS Technology, TE Magnetics, Careers, Early Careers, Current Vacancies, STEM Outreach, W
  name: Tokamak Energy Pages API
  slug: tokamak-energy-pages-api
- description: Public, unauthenticated read access to the Tokamak Energy media library — images, diagrams, PDFs and video assets attached to news posts and pages, including ST40, Demo4 and TE Magnetics imagery. Veri
  name: Tokamak Energy Media API
  slug: tokamak-energy-media-api
- description: Public, unauthenticated read access to the site-specific `area-item` custom post type behind tokamakenergy.com — the structured content blocks Tokamak Energy uses to compose its technology, careers an
  name: Tokamak Energy Area Items API
  slug: tokamak-energy-area-items-api
- description: Public, unauthenticated read access to the classification terms Tokamak Energy applies to its news archive — the category taxonomy (8 terms live on 2026-08-30) and the post tag taxonomy (0 terms live;
  name: Tokamak Energy Taxonomy API
  slug: tokamak-energy-taxonomy-api
- description: Public, unauthenticated full-text search across every searchable object on tokamakenergy.com — posts, pages and the area-item custom type — returning a lightweight result envelope (id, title, url, typ
  name: Tokamak Energy Search API
  slug: tokamak-energy-search-api
- description: Public, unauthenticated read access to the post authors of the Tokamak Energy news archive. Verified live at 4 authors on 2026-08-30. WordPress exposes only the public author view — name, slug, descri
  name: Tokamak Energy Authors API
  slug: tokamak-energy-authors-api
- description: The machine-readable description of the Tokamak Energy content API itself — the REST root document, the registered content types (including the site-specific `portfolio` and `area-item` types), the re
  name: Tokamak Energy Discovery API
  slug: tokamak-energy-discovery-api
- description: 'Public, unauthenticated oEmbed 1.0 provider endpoint for tokamakenergy.com. Given the URL of any Tokamak Energy post or page it returns an oEmbed rich/link response suitable for embedding the item in '
  name: Tokamak Energy oEmbed API
  slug: tokamak-energy-oembed-api
artifact_total: 22
common:
- group: company
  title: ''
  type: Website
  url: https://tokamakenergy.com/
- group: company
  title: ''
  type: About
  url: https://tokamakenergy.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://tokamakenergy.com/latest-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://tokamakenergy.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://tokamakenergy.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tokamakenergy.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tokamak-energy
- group: company
  title: ''
  type: Careers
  url: https://tokamakenergy.com/careers-at-tokamak-energy-fusion-energy/
- group: other
  title: ''
  type: Technology
  url: https://tokamakenergy.com/our-fusion-energy-and-hts-technology/
- group: learn
  title: ''
  type: Videos
  url: https://tokamakenergy.com/videos/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tokamak-energy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tokamak-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tokamak-energy-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tokamak-energy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tokamak-energy-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tokamak-energy-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/tokamak-energy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tokamak-energy-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tokamak-energy-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-30'
description: 'Tokamak Energy is a private fusion energy company founded in 2009 as a spinout from the UK Atomic Energy Authority, headquartered at 173 Brook Drive, Milton Park, Oxfordshire OX14 4SD, with subsidiaries in the United States and Japan and more than 300 employees. It runs a two-track strategy: advancing commercial fusion energy through compact spherical tokamaks, and developing high temperature superconducting (HTS) magnet technology as a business in its own right. Its flagship device ST40 is the world''s highest field spherical tokamak and is undergoing a USD 52 million upgrade co-funded with the US Department of Energy and the UK Department for Energy Security and Net Zero. Demo4 became the first HTS fusion magnet system to achieve fusion-relevant magnetic fields in 2025, and the company was selected as Magnet Systems Partner for the UK''s STEP programme under a GBP 70 million contract running to 2029. The group is organised into three integrated businesses — TE Magnetics (HTS
  technology, established 2024), Ridgway Machines (manufacturing, acquired 2025) and Fusion. Tokamak Energy is a fusion and superconducting hardware company rather than a software vendor: it publishes no commercial or developer-facing product API, no developer portal, no SDKs and no OpenAPI of its own. The only machine-readable interface it exposes publicly is the WordPress REST content API behind its corporate website at tokamakenergy.com, which is anonymously readable, read-only for unauthenticated callers, and is captured here for discovery purposes. Its public engineering output is instead released as open-source plasma physics code — GSFit, RTGSFit and FORGE — through the tokamak-energy GitHub organisation.'
examples:
- key_count: 2
  name: Tokamak Energy Area Item Example
  slug: tokamak-energy-area-item-example
- key_count: 2
  name: Tokamak Energy Authors Example
  slug: tokamak-energy-authors-example
- key_count: 2
  name: Tokamak Energy Categories Example
  slug: tokamak-energy-categories-example
- key_count: 2
  name: Tokamak Energy Media Example
  slug: tokamak-energy-media-example
- key_count: 2
  name: Tokamak Energy Oembed Example
  slug: tokamak-energy-oembed-example
- key_count: 2
  name: Tokamak Energy Pages Example
  slug: tokamak-energy-pages-example
- key_count: 2
  name: Tokamak Energy Posts Example
  slug: tokamak-energy-posts-example
- key_count: 2
  name: Tokamak Energy Search Example
  slug: tokamak-energy-search-example
- key_count: 2
  name: Tokamak Energy Types Example
  slug: tokamak-energy-types-example
image: https://tokamakenergy.com/wp-content/uploads/2025/03/TE_symbol_orange.svg
layout: provider
modified: '2026-08-30'
name: Tokamak Energy
nav: Providers
network: true
overview: 'Tokamak Energy publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 6 more. Tagged areas include Company, Fusion Energy, Energy, Superconductors, and HTS Magnets.


  Tokamak Energy''s developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Tokamak Energy Plans Pricing
  plan_count: 0
  slug: tokamak-energy-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Tokamak Energy Rate Limits
  slug: tokamak-energy-rate-limits
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 57.9
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tokamak Energy Authentication
  slug: tokamak-energy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tokamak Energy Domain Security
  slug: tokamak-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tokamak-energy
tags:
- Company
- Fusion Energy
- Energy
- Superconductors
- HTS Magnets
- Advanced Manufacturing
- Deep Tech
- Plasma Physics
- Scientific Computing
- Research and Development
- Content
- United Kingdom
website: https://tokamakenergy.com/
---
