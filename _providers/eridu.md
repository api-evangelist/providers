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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Eridu Agentic Access
  operation_count: 20
  slug: eridu-agentic-access
  summary_line: 20 operations
api_count: 7
apis:
- description: Anonymous, unauthenticated read access to the Eridu news and press archive published at eridu.ai, served by the WordPress core REST API. Verified live at 1 published post on 2026-08-12.
  name: Eridu Content API
  slug: eridu-content-api
- description: Anonymous, unauthenticated read access to the static marketing and policy pages of eridu.ai — Company, Leadership, Careers, Contact, Resources, Newsletter, Terms of Use, Sales Terms and Privacy Policy
  name: Eridu Pages API
  slug: eridu-pages-api
- description: Anonymous, unauthenticated read access to the eridu.ai media library — leadership portraits, careers and team photography, investor logos and press imagery, each with its generated size variants. X-WP
  name: Eridu Media API
  slug: eridu-media-api
- description: 'Anonymous, unauthenticated read access to the classification vocabularies behind eridu.ai — post categories and post tags as registered in the WordPress core REST API. Verified live at 1 category and '
  name: Eridu Taxonomy API
  slug: eridu-taxonomy-api
- description: Anonymous, unauthenticated cross-content search over eridu.ai — posts and pages — returning lightweight id / title / url / type / subtype records. Verified live at 14 searchable objects on 2026-08-12.
  name: Eridu Search API
  slug: eridu-search-api
- description: Anonymous, unauthenticated discovery metadata for eridu.ai — the self-describing route index (167 routes across 7 namespaces at capture), the registered content types and taxonomies, the publication s
  name: Eridu Discovery API
  slug: eridu-discovery-api
- description: Public oEmbed 1.0 provider endpoint for eridu.ai URLs, returning embeddable rich metadata — title, author, thumbnail and iframe HTML — for any published post or page.
  name: Eridu oEmbed API
  slug: eridu-oembed-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://eridu.ai/
- group: company
  title: ''
  type: About
  url: https://eridu.ai/company/
- group: other
  title: ''
  type: Leadership
  url: https://eridu.ai/company/leadership/
- group: company
  title: ''
  type: Blog
  url: https://eridu.ai/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://eridu.ai/feed/
- group: company
  title: ''
  type: Press
  url: https://eridu.ai/resources/press-releases/
- group: company
  title: ''
  type: News
  url: https://eridu.ai/resources/
- group: operate
  title: ''
  type: Contact
  url: https://eridu.ai/contact/
- group: company
  title: ''
  type: Careers
  url: https://ats.rippling.com/eridu-ai/jobs
- group: company
  title: ''
  type: Newsletter
  url: https://eridu.ai/newsletter/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eridu.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eridu.ai/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eridu-ai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/EriduAI
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/watch?v=ouGlu_Xdggg
- group: other
  title: ''
  type: Sitemap
  url: https://eridu.ai/wp-sitemap.xml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eridu-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eridu-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eridu-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eridu-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eridu-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eridu-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eridu-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eridu-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/eridu-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eridu-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/eridu-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/eridu-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eridu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eridu-domain-security.yml
created: '2026-08-12'
description: 'Eridu is an AI networking infrastructure company founded in 2024 and headquartered at 12900 Saratoga Ave in Saratoga, California. It is building a clean-sheet network switch architecture — silicon, systems and software together — aimed at the interconnect bottleneck that limits how efficiently GPUs exchange data inside large AI training clusters and data centers. The company was co-founded by CEO Drew Perkins, who previously co-founded Lightera Networks (acquired by Ciena) and Infinera, alongside Chief Product Officer Omar Hassen, and emerged from stealth in March 2026 with an oversubscribed Series A of more than $200M led by Socratic Partners, bringing total funding to approximately $230M with participation from John Doerr, Kleiner Perkins, Hudson River Trading, Capricorn Investment Group, Matter Venture Partners and Fusion Fund. Eridu is a semiconductor and systems company rather than a software vendor: it publishes no developer program, no developer portal, no product API,
  no SDKs and no pricing. The only machine-readable interface it serves is the WordPress core REST API behind its corporate site at eridu.ai, captured here for discovery purposes and anonymously readable but effectively read-only.'
image: https://eridu.ai/apple-touch-icon.png
layout: provider
modified: '2026-08-12'
name: Eridu
nav: Providers
network: true
overview: 'Eridu publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Content API, Pages API, Media API, and 4 more. Tagged areas include Company, Artificial Intelligence, AI Infrastructure, Networking, and Semiconductors.


  Eridu''s developer surface includes engineering blog, product news, YouTube channel, authentication, code examples, and 26 more developer resources.'
plans:
- name: Eridu Plans Pricing
  plan_count: 0
  slug: eridu-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 0
  name: Eridu Rate Limits
  slug: eridu-rate-limits
score:
  band: thin
  composite: 33.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.7
    developer_ergonomics: 19.6
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Eridu Authentication
  slug: eridu-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eridu Domain Security
  slug: eridu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eridu
tags:
- Company
- Artificial Intelligence
- AI Infrastructure
- Networking
- Semiconductors
- Data Centers
- Silicon
- Network Switching
- Interconnect
- Hardware
- Content
website: https://eridu.ai/
---
