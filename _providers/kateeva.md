---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kateeva Agentic Access
  operation_count: 21
  slug: kateeva-agentic-access
  summary_line: 21 operations
api_count: 8
apis:
- baseURL: https://kateeva.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Kateeva newsroom archive via the WordPress core REST API — press releases, in-the-news coverage, event notices and the Kateeva Blog. Verified live at 152 pub
  name: Kateeva Posts API
  slug: kateeva-posts-api
- baseURL: https://kateeva.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static pages of kateeva.com — Company, About, Leadership, History & Awards, Regions, Sustainability, Solutions, Technology, YIELDjet Platform, Products, Appl
  name: Kateeva Pages API
  slug: kateeva-pages-api
- baseURL: https://kateeva.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated read access to the media library behind kateeva.com — YIELDjet product photography, facility and event imagery, leadership headshots and press assets with their generated size '
  name: Kateeva Media API
  slug: kateeva-media-api
- baseURL: https://kateeva.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the classification vocabularies behind the kateeva.com newsroom — the eight post categories (Press releases, In the news, Kateeva Blog, Spotlight on People, Spot
  name: Kateeva Taxonomy API
  slug: kateeva-taxonomy-api
- baseURL: https://kateeva.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated cross-content search over kateeva.com — the newsroom archive and the static pages — returning lightweight id / title / url / type / subtype records. Verified live at 181 search
  name: Kateeva Search API
  slug: kateeva-search-api
- baseURL: https://kateeva.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated discovery metadata for kateeva.com — the self-describing route index (271 routes across 17 namespaces at capture), the registered content types and taxonomies, the publication '
  name: Kateeva Discovery API
  slug: kateeva-discovery-api
- baseURL: https://kateeva.com/wp-json
  baseurl_source: declared
  description: Public oEmbed 1.0 provider endpoint for kateeva.com URLs, returning embeddable rich metadata — title, author, provider, thumbnail and iframe HTML — for any post or page on the site.
  name: Kateeva oEmbed API
  slug: kateeva-oembed-api
- baseURL: https://kateeva.com/wp-json
  baseurl_source: declared
  description: Public Yoast SEO head endpoint returning the rendered head metadata and its parsed JSON-LD schema.org graph for any kateeva.com URL — a structured-data view of every page without scraping the HTML. Th
  name: Kateeva SEO Metadata API
  slug: kateeva-seo-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kateeva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kateeva.com/
- group: company
  title: ''
  type: About
  url: https://kateeva.com/company/about/overview/
- group: other
  title: ''
  type: Leadership
  url: https://kateeva.com/company/about/leadership/
- group: other
  title: ''
  type: History
  url: https://kateeva.com/company/about/history-awards/
- group: other
  title: ''
  type: Regions
  url: https://kateeva.com/company/about/regions/
- group: other
  title: ''
  type: Sustainability
  url: https://kateeva.com/company/sustainability/
- group: other
  title: ''
  type: Products
  url: https://kateeva.com/solutions/products/
- group: other
  title: ''
  type: Technology
  url: https://kateeva.com/solutions/technology/yieldjet-platform/
- group: other
  title: ''
  type: Applications
  url: https://kateeva.com/solutions/applications/
- group: company
  title: ''
  type: Partners
  url: https://kateeva.com/solutions/collaborations/
- group: other
  title: ''
  type: Services
  url: https://kateeva.com/services/
- group: company
  title: ''
  type: Blog
  url: https://kateeva.com/company/newsroom/kateeva-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://kateeva.com/feed/
- group: company
  title: ''
  type: Press
  url: https://kateeva.com/company/newsroom/press-releases/
- group: company
  title: ''
  type: News
  url: https://kateeva.com/company/newsroom/in-the-news/
- group: other
  title: ''
  type: Events
  url: https://kateeva.com/company/newsroom/events/
- group: operate
  title: ''
  type: Contact
  url: https://kateeva.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://kateeva.com/careers/job-openings/
- group: other
  title: ''
  type: SiteMap
  url: https://kateeva.com/site-map/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kateeva.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kateeva.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kateeva
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/KateevaInc
- group: auth
  title: ''
  type: Authentication
  url: authentication/kateeva-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kateeva-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kateeva-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kateeva-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kateeva-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kateeva-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kateeva-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kateeva-plans-pricing.yml
- group: build
  title: ''
  type: Examples
  url: examples/kateeva-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kateeva-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kateeva-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kateeva-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/kateeva-packages.yml
created: '2026-08-23'
description: 'Kateeva is a Silicon Valley capital-equipment company that builds inkjet printing systems for manufacturing advanced displays. It was co-founded in 2008 by Conor Madigan, PhD, Valerie Gassend, PhD, and Gerry Chen, PhD, on the conviction that precision inkjet deposition could make OLED displays mass-producible at cost. The company introduced its YIELDjet platform in 2013 — the display industry''s first inkjet equipment solution for depositing the organic thin film encapsulation (TFE) layer of an OLED panel — and shipped the first commercial YIELDjet FLEX system a year later, which became the market-leading tool for flexible mobile OLED mass production. Its current product line is the YIELDjet Lassen, Jarvis, Tioga and Kuna printers, spanning substrate sizes and applications from TFE to OLED RGB pixel deposition and microlens planarization. Kateeva moved its global headquarters to Newark, California in 2015 and operates in China, Korea, Japan and Taiwan; it raised roughly $200
  million through a 2016 Series E backed by BOE, TCL Capital, Redview Capital, Samsung Venture Investment, Sigma Partners, Spark Capital, Madrone Capital Partners, DBL Partners and Veeco. Kateeva sells machines to display panel makers, not software: it publishes no developer program, no developer portal, no SDKs and no API documentation of any kind. The only machine-readable interface it exposes is the WordPress REST content API behind its corporate website at kateeva.com, which is captured here for discovery purposes and is anonymously readable but read-only.'
image: https://kateeva.com/wp-content/uploads/2021/10/Kateeva_Logo_RGB.svg
layout: provider
modified: '2026-08-23'
name: Kateeva
nav: Providers
network: true
overview: 'Kateeva publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 5 more. Tagged areas include Company, Display Manufacturing, OLED, Semiconductor Equipment, and Capital Equipment.


  Kateeva''s developer surface includes engineering blog, product news, authentication, code examples, and 34 more developer resources.'
plans:
- name: Kateeva Plans Pricing
  plan_count: 0
  slug: kateeva-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Kateeva Rate Limits
  slug: kateeva-rate-limits
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 16.0
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 20.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kateeva/refs/heads/main/screenshots/kateeva-2026-09-02T150024.png
security:
- kind: authentication
  name: Kateeva Authentication
  slug: kateeva-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kateeva Domain Security
  slug: kateeva-domain-security
  summary_line: TLSv1.2 · DMARC
slug: kateeva
tags:
- Company
- Display Manufacturing
- OLED
- Semiconductor Equipment
- Capital Equipment
- Inkjet Printing
- Thin Film Encapsulation
- Advanced Manufacturing
- Materials Deposition
- Consumer Electronics
- Hardware
- Content
website: https://kateeva.com/
---
