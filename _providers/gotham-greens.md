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
  band: agent-aware
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gotham Greens Agentic Access
  operation_count: 20
  slug: gotham-greens-agentic-access
  summary_line: 20 operations
api_count: 8
apis:
- baseURL: https://www.gothamgreens.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Gotham Greens Journal — recipes, company news and seasonal articles — via the WordPress core REST API. Verified live at 132 published posts.
  name: Gotham Greens Journal Posts API
  slug: gotham-greens-posts-api
- baseURL: https://www.gothamgreens.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static marketing pages of gothamgreens.com (Our Story, Our Farms, Our Products, Find Us, FAQ, Careers) via the WordPress core REST API.
  name: Gotham Greens Pages API
  slug: gotham-greens-pages-api
- baseURL: https://www.gothamgreens.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the media library behind gothamgreens.com — product photography, farm imagery and recipe images with their generated size variants.
  name: Gotham Greens Media API
  slug: gotham-greens-media-api
- baseURL: https://www.gothamgreens.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Journal taxonomy — categories (Recipes, For the Family, General) and tags — via the WordPress core REST API.
  name: Gotham Greens Taxonomy API
  slug: gotham-greens-taxonomy-api
- baseURL: https://www.gothamgreens.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated cross-content search over posts and pages on gothamgreens.com, returning lightweight id / title / url / subtype records.
  name: Gotham Greens Search API
  slug: gotham-greens-search-api
- baseURL: https://www.gothamgreens.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated site, content-type, taxonomy and status metadata — the self-describing route index that makes the whole surface machine-readable.
  name: Gotham Greens Discovery API
  slug: gotham-greens-discovery-api
- baseURL: https://www.gothamgreens.com/wp-json
  baseurl_source: declared
  description: Public oEmbed 1.0 provider endpoint for gothamgreens.com URLs, returning embeddable rich metadata for Journal posts and site pages.
  name: Gotham Greens oEmbed API
  slug: gotham-greens-oembed-api
- baseURL: https://www.gothamgreens.com/wp-json
  baseurl_source: declared
  description: Public Yoast SEO head endpoint returning the rendered SEO/head metadata and its JSON-LD schema graph for any gothamgreens.com URL.
  name: Gotham Greens SEO Metadata API
  slug: gotham-greens-seo-api
artifact_total: 19
collections:
- collection_type: open
  name: Gotham Greens Discovery API
  slug: open-gotham-greens-discovery-api
- collection_type: open
  name: Gotham Greens Media API
  slug: open-gotham-greens-media-api
- collection_type: open
  name: Gotham Greens oEmbed API
  slug: open-gotham-greens-oembed-api
- collection_type: open
  name: Gotham Greens Pages API
  slug: open-gotham-greens-pages-api
- collection_type: open
  name: Gotham Greens Journal Posts API
  slug: open-gotham-greens-posts-api
- collection_type: open
  name: Gotham Greens Search API
  slug: open-gotham-greens-search-api
- collection_type: open
  name: Gotham Greens SEO Metadata API
  slug: open-gotham-greens-seo-api
- collection_type: open
  name: Gotham Greens Taxonomy API
  slug: open-gotham-greens-taxonomy-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gotham-greens-capability-edges.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gotham-greens-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gotham-greens-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gotham-greens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gothamgreens.com/
- group: company
  title: ''
  type: About
  url: https://www.gothamgreens.com/our-story/
- group: company
  title: ''
  type: Blog
  url: https://www.gothamgreens.com/journal/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.gothamgreens.com/journal/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.gothamgreens.com/faq/
- group: operate
  title: ''
  type: Contact
  url: https://www.gothamgreens.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.gothamgreens.com/careers/
- group: company
  title: ''
  type: Press
  url: https://www.gothamgreens.com/recent-press/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gothamgreens.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gothamgreens.com/privacy-policy/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/GothamGreens/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/GothamGreens
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/gothamgreens
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gotham-greens-farms/
- group: auth
  title: ''
  type: Authentication
  url: authentication/gotham-greens-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gotham-greens-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gotham-greens-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gotham-greens-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gotham-greens-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gotham-greens-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gotham-greens-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gotham-greens-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/gotham-greens-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/gotham-greens-examples.yml
created: '2026-08-01'
description: Gotham Greens is an American fresh food and indoor farming company founded in 2009 by Viraj Puri and Eric Haley in Brooklyn, New York, where it built one of the first commercial-scale rooftop hydroponic greenhouses in the world. The company owns and operates a national network of climate-controlled hydroponic greenhouses across the United States, growing pesticide-free leafy greens, lettuces and herbs year-round using a fraction of the land and water of conventional field agriculture, and delivering them to retail, restaurant and foodservice customers within hours of harvest. Under its own brand it sells packaged salad greens, salad kits, fresh herbs, salad dressings, dips, pestos and cooking sauces. Gotham Greens is a consumer packaged goods and controlled-environment agriculture business rather than a software vendor, and publishes no commercial or developer-facing product API. The only machine-readable interface it exposes is the WordPress REST content API behind its corporate
  website at gothamgreens.com, captured here for discovery purposes.
image: https://www.gothamgreens.com/wp-content/uploads/2019/10/android-chrome-256x256-200x200.png
layout: provider
modified: '2026-08-01'
name: Gotham Greens
nav: Providers
network: true
overview: 'Gotham Greens publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Journal Posts API, Pages API, Media API, and 5 more. Tagged areas include Company, Agriculture, Controlled Environment Agriculture, Hydroponics, and Food.


  Gotham Greens'' developer surface includes engineering blog, support, authentication, code examples, and 25 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 55.4
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gotham-greens/refs/heads/main/screenshots/gotham-greens-2026-08-07T165809.png
security:
- kind: authentication
  name: Gotham Greens Authentication
  slug: gotham-greens-authentication
  summary_line: none/cookie · 2 schemes
- kind: domain-security
  name: Gotham Greens Domain Security
  slug: gotham-greens-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gotham-greens
tags:
- Company
- Agriculture
- Controlled Environment Agriculture
- Hydroponics
- Food
- Consumer Packaged Goods
- Fresh Produce
- Sustainability
- Urban Farming
- Content
website: https://www.gothamgreens.com/
---
