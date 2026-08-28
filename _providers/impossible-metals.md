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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-26'
api_count: 10
apis:
- description: Public, unauthenticated read access to the Impossible Metals news, blog and press archive via the WordPress core REST API — testimony, policy positions, Eureka programme updates and partnership announ
  name: Impossible Metals Posts API
  slug: impossible-metals-posts-api
- description: Public, unauthenticated read access to the static pages of impossiblemetals.com — Technology, Sustainability, About, Markets, Partners, Board & Advisors, Policies & Reports, Careers and Contact. Verif
  name: Impossible Metals Pages API
  slug: impossible-metals-pages-api
- description: Public, unauthenticated read access to the Impossible Metals frequently-asked-questions knowledge base — the company's own structured position on nodule collection, environmental impact, regulation an
  name: Impossible Metals FAQ API
  slug: impossible-metals-faq-api
- description: Public, unauthenticated read access to the media library behind impossiblemetals.com — Eureka vehicle photography, seabed and nodule imagery, technical diagrams, report PDFs and press assets with thei
  name: Impossible Metals Media API
  slug: impossible-metals-media-api
- description: 'Public, unauthenticated read access to the classification vocabularies behind impossiblemetals.com: post categories, post tags, the registered post types and the registered taxonomies. Verified live a'
  name: Impossible Metals Taxonomy API
  slug: impossible-metals-taxonomy-api
- description: Public, unauthenticated cross-content search over impossiblemetals.com — posts, pages, FAQ entries and events — returning lightweight id / title / url / type / subtype records. Verified live at 586 se
  name: Impossible Metals Search API
  slug: impossible-metals-search-api
- description: Public, unauthenticated read access to the Impossible Metals events calendar — conference appearances, webinars, demo days and the venues and organizers behind them — served by The Events Calendar plu
  name: Impossible Metals Events API
  slug: impossible-metals-events-api
- description: The successor events surface at /wp-json/tec/v1/, described by an OpenAPI 3.0.4 document the host publishes at /wp-json/tec/v1/docs and captured verbatim here. The contract is published but the surfac
  name: Impossible Metals Events API (TEC v1, experimental)
  slug: impossible-metals-events-tec-api
- description: 'Public, unauthenticated discovery surface for the impossiblemetals.com WordPress REST API: the API root, which enumerates 269 routes across 23 namespaces along with site identity and the advertised au'
  name: Impossible Metals Discovery API
  slug: impossible-metals-discovery-api
- description: Public, unauthenticated oEmbed 1.0 provider for impossiblemetals.com. Returns oEmbed rich/link responses in JSON or XML for any URL on the site, so third-party surfaces can embed Impossible Metals pos
  name: Impossible Metals oEmbed API
  slug: impossible-metals-oembed-api
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://impossiblemetals.com/
- group: company
  title: ''
  type: Blog
  url: https://impossiblemetals.com/news/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://impossiblemetals.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://impossiblemetals.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impossiblemetals.com/policies-reports/privacy-statement/
- group: company
  title: ''
  type: About
  url: https://impossiblemetals.com/about/
- group: other
  title: ''
  type: Technology
  url: https://impossiblemetals.com/technology/robotic-collection-system/
- group: operate
  title: ''
  type: FAQ
  url: https://impossiblemetals.com/frequently-asked-questions/
- group: company
  title: ''
  type: Press
  url: https://impossiblemetals.com/news/press-releases/
- group: company
  title: ''
  type: Careers
  url: https://impossiblemetals.com/join-us/
- group: company
  title: ''
  type: Partners
  url: https://impossiblemetals.com/about/partners/
- group: other
  title: ''
  type: Events
  url: https://impossiblemetals.com/impossible-metals-events/
- group: other
  title: ''
  type: Sustainability
  url: https://impossiblemetals.com/sustainability/
- group: other
  title: ''
  type: OpenData
  url: https://impossiblemetals.com/sustainability/public-data/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/impossible-metals/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@impossiblemetals
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ImpossMetals
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impossible-metals-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/impossible-metals-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impossible-metals-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/impossible-metals-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/impossible-metals-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/impossible-metals-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impossible-metals-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impossible-metals-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/impossible-metals-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/impossible-metals-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/impossible-metals-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/impossible-metals-examples.yml
created: '2026-08-23'
description: 'Impossible Metals is a deep-ocean robotics and critical-minerals company founded in 2020 by CEO Oliver Gunasekara, headquartered in San Jose, California with a robotics lab in Canada, and a member of Y Combinator''s W22 cohort. It builds the Eureka autonomous underwater vehicle, a hovering AUV that uses computer vision and robotic arms to pick polymetallic nodules from the seabed one at a time — leaving visible fauna and the sediment layer in place — as an alternative to the dredge-and-riser designs used elsewhere in deep-sea mining. Eureka I and Eureka II have been sea-tested, Eureka III is slated for a 2026 test in the BGR contract area of the Clarion-Clipperton Zone, and the company has applied for a deep-sea mining lease in U.S. federal waters and for observer status with the International Seabed Authority. It is a certified B Corp and publishes environmental data, policy positions and testimony alongside its technical work. Impossible Metals is a robotics and mining company
  rather than a software vendor: it operates no developer program, publishes no product API, SDKs or developer portal, and hosts no api. or developer. subdomain. The only machine-readable interfaces it serves are the WordPress REST content API behind impossiblemetals.com and the two OpenAPI documents its events plugin publishes on that same host, which are captured here for discovery purposes and are anonymously readable and read-only.'
image: https://impossiblemetals.com/wp-content/uploads/2022/09/ImpossibleMetals_logo_REVERSE_RGB.svg
layout: provider
modified: '2026-08-23'
name: Impossible Metals
nav: Providers
network: true
overview: 'Impossible Metals publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, FAQ API, and 7 more. Tagged areas include Company, Deep Sea Mining, Critical Minerals, Battery Metals, and Robotics.


  Impossible Metals'' developer surface includes engineering blog, support, FAQ, YouTube channel, authentication, code examples, and 24 more developer resources.'
plans:
- name: Impossible Metals Plans Pricing
  plan_count: 0
  slug: impossible-metals-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Impossible Metals Rate Limits
  slug: impossible-metals-rate-limits
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 55.6
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 29.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Impossible Metals Authentication
  slug: impossible-metals-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Impossible Metals Domain Security
  slug: impossible-metals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: impossible-metals
tags:
- Company
- Deep Sea Mining
- Critical Minerals
- Battery Metals
- Robotics
- Autonomous Underwater Vehicles
- Ocean Technology
- Mining
- Sustainability
- Climate Tech
- Content
- Events
website: https://impossiblemetals.com/
---
