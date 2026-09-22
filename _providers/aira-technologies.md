---
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aira Technologies Agentic Access
  operation_count: 24
  slug: aira-technologies-agentic-access
  summary_line: 24 operations
api_count: 10
apis:
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Aira Technologies news, press-release and blog archive via the WordPress core REST API. Verified live at 50 published posts.
  name: Aira Technologies Posts API
  slug: aira-technologies-posts-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated read access to the static marketing and policy pages of aira-technology.com — Naavik, Vision, About, Leadership, Founding Team, Advisors & Investors, Partners, Videos, Blogs & '
  name: Aira Technologies Pages API
  slug: aira-technologies-pages-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the `article` custom post type behind aira-technology.com — long-form technical articles and whitepapers published separately from the news archive. Verified liv
  name: Aira Technologies Articles API
  slug: aira-technologies-articles-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the `events` custom post type behind aira-technology.com — the Aira Activate conferences and the Role of AI/GenAI in Wireless sessions. Verified live at 4 publis
  name: Aira Technologies Events API
  slug: aira-technologies-events-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the media library behind aira-technology.com — platform and product imagery, partner and press logos, event photography and document attachments with their gener
  name: Aira Technologies Media API
  slug: aira-technologies-media-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated cross-content search over aira-technology.com — posts, pages, articles and events — returning lightweight id / title / url / type / subtype records. Verified live: a query for '
  name: Aira Technologies Search API
  slug: aira-technologies-search-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated discovery metadata for aira-technology.com — the self-describing route index (206 routes across 21 namespaces at capture), the registered content types and taxonomies, and the '
  name: Aira Technologies Discovery API
  slug: aira-technologies-discovery-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the content categories applied across Aira Technologies posts and articles. Verified live at 5 categories.
  name: Aira Technologies Categories API
  slug: aira-technologies-categories-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the public author records behind aira-technology.com — the bylines attached to posts and articles. Verified live at 4 public authors.
  name: Aira Technologies Users API
  slug: aira-technologies-users-api
- baseURL: https://aira-technology.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint.
  name: Aira Technologies o Embed API
  slug: aira-technologies-o-embed-api
artifact_total: 15
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/overlays/aira-technologies-oembed-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aira-technologies-oembed-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://aira-technology.com/
- group: company
  title: ''
  type: About
  url: https://aira-technology.com/about/
- group: other
  title: ''
  type: Products
  url: https://aira-technology.com/naavik/
- group: company
  title: ''
  type: Blog
  url: https://aira-technology.com/blogs-whitepapers/
- group: company
  title: ''
  type: BlogRSS
  url: https://aira-technology.com/feed/
- group: company
  title: ''
  type: Press
  url: https://aira-technology.com/news/
- group: other
  title: ''
  type: Events
  url: https://aira-technology.com/events/
- group: company
  title: ''
  type: Partners
  url: https://aira-technology.com/partners/
- group: other
  title: ''
  type: Leadership
  url: https://aira-technology.com/leadership/
- group: company
  title: ''
  type: Investors
  url: https://aira-technology.com/advisors-investors/
- group: operate
  title: ''
  type: Contact
  url: https://aira-technology.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://aira-technology.com/join-the-team/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aira-technology.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aira-technologies/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/authentication/aira-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aira-technologies-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/errors/aira-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aira-technologies-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/conventions/aira-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aira-technologies-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/data-model/aira-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aira-technologies-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/conformance/aira-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aira-technologies-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/lifecycle/aira-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aira-technologies-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/rate-limits/aira-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aira-technologies-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/plans/aira-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aira-technologies-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/packages/aira-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/aira-technologies-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/llms/aira-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aira-technologies-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/examples/aira-technologies-examples.yml
  title: ''
  type: Examples
  url: examples/aira-technologies-examples.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/mcp/aira-technologies-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aira-technologies-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/agentic-access/aira-technologies-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aira-technologies-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aira-technologies/refs/heads/main/security/aira-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aira-technologies-domain-security.yml
created: '2026-09-14'
description: Aira Technologies is an AI-defined networking company founded in 2019 and headquartered in Saratoga, California, building machine-learning and generative-AI software for mobile network operators. Its platform, Naavik, is marketed as an Adaptive Intelligence Framework for the Radio Access Network, combining an Intent Manager that turns natural language into network actions, AppGen for no-code telecom application generation, a reasoning agent for anomaly detection and root-cause analysis, a telecom-specific AI/ML hub and a knowledge graph. Earlier work includes RANGPT, a GenAI utility for RAN observability, analysis, control and automation demonstrated with Broadcom and Tech Mahindra, and an AI-based channel estimation and prediction xApp. The company is a member of the O-RAN Alliance, the AI-RAN Alliance and TM Forum, and raised a $14.5M Series B from AT&T Ventures, Intel Capital and In-Q-Tel. Aira sells to operators through a demo and sales motion and publishes no developer
  program, no API documentation, no SDKs and no public specification for Naavik or RANGPT. The only machine-readable interface reachable at aira-technology.com is the WordPress REST content API behind the corporate website, captured here for discovery purposes; it is anonymously readable and read-only.
image: https://aira-technology.com/wp-content/uploads/2023/01/cropped-Aira-Black-1.png
layout: provider
modified: '2026-09-14'
name: Aira Technologies
nav: Providers
network: true
overview: 'Aira Technologies publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Articles API, and 7 more. Tagged areas include Company, Telecommunications, Wireless, Artificial Intelligence, and Machine-Learning.


  Aira Technologies'' developer surface includes engineering blog, authentication, code examples, and 27 more developer resources.'
plans:
- name: Aira Technologies Plans Pricing
  plan_count: 0
  slug: aira-technologies-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Aira Technologies Rate Limits
  slug: aira-technologies-rate-limits
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 16.0
    developer_ergonomics: 16.1
    discoverability: 74.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 37.5
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Aira Technologies Authentication
  slug: aira-technologies-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aira Technologies Domain Security
  slug: aira-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aira-technologies
tags:
- Company
- Telecommunications
- Wireless
- Artificial Intelligence
- Machine-Learning
- 5G
- Radio Access Network
- Network Automation
- Generative AI
- Observability
- Content
website: https://aira-technology.com/
---
