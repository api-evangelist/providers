---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hydrostor Agentic Access
  operation_count: 26
  slug: hydrostor-agentic-access
  summary_line: 26 operations
api_count: 9
apis:
- description: 'Public, unauthenticated read access to Hydrostor''s Advanced Compressed Air Energy Storage project portfolio — the site-specific `project` custom post type behind hydrostor.ca/projects/. Verified live '
  name: Hydrostor Projects API
  slug: hydrostor-projects-api
- description: Public, unauthenticated read access to the Hydrostor newsroom archive — press releases, company insights and featured media coverage — via the WordPress core REST API behind hydrostor.ca. Verified liv
  name: Hydrostor Posts API
  slug: hydrostor-posts-api
- description: Public, unauthenticated read access to the static marketing and policy pages of hydrostor.ca — the company, technology and geology explainers, the project index, use cases, careers, contact, media kit
  name: Hydrostor Pages API
  slug: hydrostor-pages-api
- description: Public, unauthenticated read access to the media library behind hydrostor.ca — project renders, facility and geology photography, technology diagrams and press assets, each with its generated size var
  name: Hydrostor Media API
  slug: hydrostor-media-api
- description: 'Public, unauthenticated read access to the classification vocabularies behind hydrostor.ca: newsroom categories and tags, plus the site-specific `project_category` and `project_tag` taxonomies registe'
  name: Hydrostor Taxonomy API
  slug: hydrostor-taxonomy-api
- description: Public, unauthenticated cross-content search over hydrostor.ca — newsroom posts, static pages and the A-CAES project portfolio in one result set, each result carrying its id, title, canonical URL, typ
  name: Hydrostor Search API
  slug: hydrostor-search-api
- description: Public, unauthenticated discovery metadata for hydrostor.ca — the self-describing route index (340 routes across 18 namespaces at capture), the registered content types and taxonomies, the publication
  name: Hydrostor Discovery API
  slug: hydrostor-discovery-api
- description: Public oEmbed 1.0 provider endpoint for hydrostor.ca URLs, returning embeddable rich metadata — title, author, thumbnail and iframe HTML — for any newsroom post, static page or A-CAES project page. Re
  name: Hydrostor oEmbed API
  slug: hydrostor-oembed-api
- description: Public Yoast SEO head endpoint returning the rendered head metadata and its parsed schema.org JSON-LD graph for any hydrostor.ca URL — a structured-data view of every newsroom post, page and A-CAES pr
  name: Hydrostor SEO Metadata API
  slug: hydrostor-seo-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hydrostor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hydrostor.ca/
- group: company
  title: ''
  type: About
  url: https://hydrostor.ca/our-company/
- group: other
  title: ''
  type: Team
  url: https://hydrostor.ca/our-company/
- group: other
  title: ''
  type: Technology
  url: https://hydrostor.ca/technology/
- group: other
  title: ''
  type: Projects
  url: https://hydrostor.ca/projects/
- group: company
  title: ''
  type: Blog
  url: https://hydrostor.ca/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://hydrostor.ca/feed/
- group: company
  title: ''
  type: Newsletter
  url: https://hydrostor.ca/newsletter/
- group: other
  title: ''
  type: MediaKit
  url: https://hydrostor.ca/media-kit/
- group: operate
  title: ''
  type: Contact
  url: https://hydrostor.ca/contact/
- group: company
  title: ''
  type: Careers
  url: https://hydrostor.ca/careers/
- group: other
  title: ''
  type: Suppliers
  url: https://hydrostor.ca/vendor-interest-form/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hydrostor.ca/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hydrostor.ca/privacy-policy/
- group: auth
  title: ''
  type: Disclosure
  url: https://hydrostor.ca/ab1305-disclosure/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hydrostor-inc-
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Hydrostor
- group: auth
  title: ''
  type: Authentication
  url: authentication/hydrostor-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hydrostor-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hydrostor-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hydrostor-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hydrostor-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hydrostor-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hydrostor-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hydrostor-plans-pricing.yml
- group: build
  title: ''
  type: Examples
  url: examples/hydrostor-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hydrostor-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hydrostor-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hydrostor-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/hydrostor-packages.yml
created: '2026-08-22'
description: 'Hydrostor is a Canadian long-duration energy storage developer founded in 2010 and headquartered in Toronto, with offices in Denver, Colorado and Melbourne and Adelaide, Australia. It builds and operates Advanced Compressed Air Energy Storage (A-CAES) facilities: surplus grid electricity runs a compressor, the heat of compression is captured and stored, and the cooled compressed air is sent into a purpose-built underground cavern held at constant pressure by a water column. On discharge the water weight pushes the air back to surface, where it is recombined with the stored heat and expanded through a turbine, giving eight or more hours of emissions-free storage from a plant with a multi-decade asset life. The company is backed by Goldman Sachs Alternatives, CPP Investments, the Canada Growth Fund, Canoe Financial and Arctern Ventures, operates a commercially contracted utility-scale facility in Goderich, Ontario, and is advancing a roughly 7 GW pipeline including the Willow
  Rock and Copper Valley centers in California, Silver City in New South Wales, and Quinte and Wellington in Ontario. Hydrostor is an energy infrastructure developer rather than a software vendor: it publishes no developer portal, no SDKs, no product API and no machine-readable specification of its own. The only machine-readable interface it exposes is the WordPress core REST content API behind hydrostor.ca, which is anonymously readable, read-only without credentials, and carries the project portfolio, the newsroom archive and the media library. That surface is profiled here for discovery purposes and is described from the site''s own self-describing route index.'
image: https://hydrostor.ca/wp-content/uploads/2026/06/cropped-HDS-Favicon-2026.png
layout: provider
modified: '2026-08-22'
name: Hydrostor
nav: Providers
network: true
overview: 'Hydrostor publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Projects API, Posts API, Pages API, and 6 more. Tagged areas include Company, Energy, Energy Storage, Long Duration Energy Storage, and Compressed Air Energy Storage.


  Hydrostor''s developer surface includes engineering blog, YouTube channel, authentication, code examples, and 28 more developer resources.'
plans:
- name: Hydrostor Plans Pricing
  plan_count: 0
  slug: hydrostor-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Hydrostor Rate Limits
  slug: hydrostor-rate-limits
score:
  band: thin
  composite: 36.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 54.3
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Hydrostor Authentication
  slug: hydrostor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hydrostor Domain Security
  slug: hydrostor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hydrostor
tags:
- Company
- Energy
- Energy Storage
- Long Duration Energy Storage
- Compressed Air Energy Storage
- Grid Infrastructure
- Renewable Energy
- Clean Energy
- Utilities
- Climate Tech
- Canada
- Content
website: https://hydrostor.ca/
---
