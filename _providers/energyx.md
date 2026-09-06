---
access_model:
  confidence: high
  label: Public read-only content API, no signup
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
  score: 36.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Energyx Agentic Access
  operation_count: 59
  slug: energyx-agentic-access
  summary_line: 59 operations
api_count: 18
apis:
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the EnergyX blog and article archive at energyx.com/blog/ via the WordPress core REST API. Verified live at 69 published posts, filterable by category, author, d
  name: EnergyX Posts API
  slug: energyx-posts-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static marketing, product, investor and policy pages of energyx.com — Technology, Lithium, Battery, Nuclear, Membranes, Projects, Sustainability, Careers, In
  name: EnergyX Pages API
  slug: energyx-pages-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the EnergyX leadership roster — executives, board members and advisors behind energyx.com/company/ — classified by the site-specific leadership-type taxonomy. Ve
  name: EnergyX Leadership API
  slug: energyx-leadership-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the EnergyX partner roster — the operators, institutions and research bodies EnergyX names as partners — classified by the site-specific partner-type taxonomy. V
  name: EnergyX Partners API
  slug: energyx-partners-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the EnergyX video library behind energyx.com/videos/ — technology explainers, facility tours, investor updates and media appearances. Verified live at 61 publish
  name: EnergyX Videos API
  slug: energyx-videos-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the EnergyX resource guides behind energyx.com/resources/ — long-form explainers on direct lithium extraction, brine chemistry, battery materials and the lithium
  name: EnergyX Resource Guides API
  slug: energyx-resource-guides-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the media library behind energyx.com — facility and laboratory photography, technology diagrams, leadership headshots and press assets, each with its generated s
  name: EnergyX Media API
  slug: energyx-media-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated read access to the eleven classification vocabularies behind energyx.com: post categories and tags, the site-specific leadership-type, position-area, position-location, partner'
  name: EnergyX Taxonomy API
  slug: energyx-taxonomy-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated cross-content search over energyx.com — posts, pages, press releases, in-the-news coverage, leadership, job positions, partners, videos, resource guides and products — returnin
  name: EnergyX Search API
  slug: energyx-search-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated discovery metadata for energyx.com — the self-describing route index (1,233 routes across 36 namespaces at capture), the 26 registered content types, the 13 registered taxonomi
  name: EnergyX Discovery API
  slug: energyx-discovery-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated read access to the EnergyX merchandise catalog behind energyx.com/shop/, exposed twice: through the WooCommerce Store API (wc/store/v1), which is the anonymous storefront contr'
  name: EnergyX Store API
  slug: energyx-store-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public oEmbed 1.0 provider endpoint for energyx.com URLs, returning embeddable rich metadata — title, author, thumbnail and iframe HTML — for any post, page, press release, video or product on the sit
  name: EnergyX oEmbed API
  slug: energyx-oembed-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Public Yoast SEO head endpoint returning the rendered head metadata and its parsed JSON-LD schema.org graph for any energyx.com URL — a structured-data view of every page without scraping the HTML.
  name: EnergyX SEO Metadata API
  slug: energyx-seo-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Third-party media coverage of EnergyX.
  name: EnergyX In The News API
  slug: energyx-in-the-news-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Curated lithium and energy-transition industry news.
  name: EnergyX Industry News API
  slug: energyx-industry-news-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: Open EnergyX roles, by function and location.
  name: EnergyX Job Positions API
  slug: energyx-job-positions-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: First-party EnergyX press releases.
  name: EnergyX Press Releases API
  slug: energyx-press-releases-api
- baseURL: https://energyx.com/wp-json
  baseurl_source: declared
  description: The product catalog as WordPress core content records.
  name: EnergyX Products API
  slug: energyx-products-api
artifact_total: 38
collections:
- collection_type: open
  name: EnergyX Careers API
  slug: open-energyx-careers-api
- collection_type: open
  name: EnergyX Discovery API
  slug: open-energyx-discovery-api
- collection_type: open
  name: EnergyX Leadership API
  slug: open-energyx-leadership-api
- collection_type: open
  name: EnergyX Media API
  slug: open-energyx-media-api
- collection_type: open
  name: EnergyX oEmbed API
  slug: open-energyx-oembed-api
- collection_type: open
  name: EnergyX Pages API
  slug: open-energyx-pages-api
- collection_type: open
  name: EnergyX Partners API
  slug: open-energyx-partners-api
- collection_type: open
  name: EnergyX Posts API
  slug: open-energyx-posts-api
- collection_type: open
  name: EnergyX Press and News API
  slug: open-energyx-press-api
- collection_type: open
  name: EnergyX Resource Guides API
  slug: open-energyx-resource-guides-api
- collection_type: open
  name: EnergyX Search API
  slug: open-energyx-search-api
- collection_type: open
  name: EnergyX SEO Metadata API
  slug: open-energyx-seo-api
- collection_type: open
  name: EnergyX Store API
  slug: open-energyx-store-api
- collection_type: open
  name: EnergyX Taxonomy API
  slug: open-energyx-taxonomy-api
- collection_type: open
  name: EnergyX Videos API
  slug: open-energyx-videos-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/energyx-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/energyx-press-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/energyx-careers-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://energyx.com/
- group: company
  title: ''
  type: About
  url: https://energyx.com/company/
- group: company
  title: ''
  type: Blog
  url: https://energyx.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://energyx.com/feed/
- group: company
  title: ''
  type: Press
  url: https://energyx.com/press/
- group: company
  title: ''
  type: News
  url: https://energyx.com/in-the-news/
- group: operate
  title: ''
  type: Contact
  url: https://energyx.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://energyx.com/careers/
- group: operate
  title: ''
  type: FAQ
  url: https://energyx.com/faq/
- group: learn
  title: ''
  type: Videos
  url: https://energyx.com/videos/
- group: other
  title: ''
  type: Resources
  url: https://energyx.com/resources/
- group: other
  title: ''
  type: Technology
  url: https://energyx.com/technology/
- group: other
  title: ''
  type: Sustainability
  url: https://energyx.com/sustainability/
- group: company
  title: ''
  type: Investors
  url: https://energyx.com/investor-portal/
- group: other
  title: ''
  type: Store
  url: https://energyx.com/shop/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://energyx.com/privacy-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://energyx.com/disclaimer/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energyx-inc/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/energyx/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/energyx/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/profile.php?id=61560013780545
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@EnergyXOfficial
- group: auth
  title: ''
  type: Authentication
  url: authentication/energyx-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/energyx-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/energyx-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/energyx-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/energyx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/energyx-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/energyx-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/energyx-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/energyx-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/energyx-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/energyx-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/energyx-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/energyx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energyx-domain-security.yml
created: '2026-08-12'
description: 'EnergyX (Energy Exploration Technologies, Inc.) is a critical-materials technology company founded in 2018 by Teague Egan and headquartered in Austin, Texas, with operations in Texarkana, Antofagasta in Chile, and San Juan, Puerto Rico. It develops direct lithium extraction (DLE) technology — a modular, brine-agnostic flow sheet combining adsorbents, solvent extraction and its own selective membranes under the GET-Lit platform — together with SoLiS lithium-metal battery technology and NUKE-it membranes for lithium-6/7 isotope separation and nuclear fuel-cycle applications. The company produces lithium hydroxide, lithium carbonate and lithium dihydrogen phosphate, holds a large patent portfolio, and controls lithium resources in Chile and the United States including the Black Giant project. EnergyX is a materials and process-technology company rather than a software vendor: it publishes no developer program, no API documentation, no SDKs and no developer portal. The only machine-readable
  interface it exposes is the WordPress REST content API behind its corporate website at energyx.com, which is captured here for discovery purposes and is anonymously readable but read-only.'
image: https://energyx.com/app/uploads/2020/03/android-chrome-384x384-1.png
layout: provider
modified: '2026-08-12'
name: EnergyX
nav: Providers
network: true
overview: 'EnergyX publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Leadership API, and 15 more. Tagged areas include Company, Lithium, Direct Lithium Extraction, Critical Minerals, and Battery Technology.


  EnergyX''s developer surface includes engineering blog, product news, FAQ, YouTube channel, authentication, code examples, and 34 more developer resources.'
plans:
- name: Energyx Plans Pricing
  plan_count: 0
  slug: energyx-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Energyx Rate Limits
  slug: energyx-rate-limits
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 16.5
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 20
      marker_coverage: 100.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/energyx/refs/heads/main/screenshots/energyx-2026-09-02T145402.png
security:
- kind: authentication
  name: Energyx Authentication
  slug: energyx-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Energyx Domain Security
  slug: energyx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: energyx
tags:
- Company
- Lithium
- Direct Lithium Extraction
- Critical Minerals
- Battery Technology
- Energy Transition
- Cleantech
- Materials Science
- Mining
- Chemicals
- Nuclear Materials
- Manufacturing
- Content
website: https://energyx.com/
---
