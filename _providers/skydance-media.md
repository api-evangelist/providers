---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Skydance Media Agentic Access
  operation_count: 65
  slug: skydance-media-agentic-access
  summary_line: 65 operations · 42 acting
api_count: 1
apis:
- description: The anonymously readable WordPress REST API that skydance.com serves at /wp-json/wp/v2 — marketing and legal pages, the media library, categories, tags, comments, post types and a site-wide search end
  name: Skydance Media Content API (WordPress REST wp/v2)
  slug: content
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skydance-media-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/skydance-media-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skydance-media-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skydance-media-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skydance-media-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skydance-media-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/skydance-media-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skydance-media-llms.txt
- group: company
  title: ''
  type: Website
  url: https://skydance.com/
- group: company
  title: ''
  type: About
  url: https://skydance.com/about/
- group: company
  title: ''
  type: Blog
  url: https://skydance.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://skydance.com/feed/
- group: operate
  title: ''
  type: FAQ
  url: https://skydance.com/faq/
- group: company
  title: ''
  type: Careers
  url: https://skydance.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skydance.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skydance.com/privacy/
- group: other
  title: ''
  type: Patents
  url: https://skydance.com/patents/
- group: other
  title: ''
  type: Film
  url: https://skydance.com/film/
- group: other
  title: ''
  type: Television
  url: https://skydance.com/tv/
- group: other
  title: ''
  type: Animation
  url: https://skydance.com/animation/
- group: other
  title: ''
  type: Interactive
  url: https://skydance.com/interactive/
- group: other
  title: ''
  type: Sports
  url: https://skydance.com/sports/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.paramount.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skydancemedia
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Skydance
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/SkydanceMedia
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/skydance/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/skydance
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/skydance-media_stock/
created: '2026-08-05'
description: 'Skydance Media is a Santa Monica, California diversified entertainment company founded in 2010 by David Ellison, producing event-scale film, television, animation, sports and interactive entertainment — Top Gun: Maverick, the Mission: Impossible films, Reacher, Grace and Frankie, Spellbound, and the VR titles The Walking Dead: Saints & Sinners and Behemoth through Skydance Interactive and Skydance New Media. Skydance completed its merger with Paramount Global on 7 August 2025 to form Paramount Skydance Corporation, and skydance.com continues to operate as the label site for the Animation, Film, Television, Sports, Interactive and New Media divisions. Skydance publishes no developer program, no API documentation, no SDK and no OpenAPI of its own. The only machine-readable, anonymously readable surface on its own host is the WordPress REST API at skydance.com/wp-json — the CMS content API behind the label site, which serves pages, the media library, categories and site search
  as JSON.'
image: https://skydance.com/wp-content/uploads/2023/03/cropped-skydance.png
layout: provider
modified: '2026-08-05'
name: Skydance Media
nav: Providers
network: true
overview: 'Skydance Media publishes 1 API on the [APIs.io](https://apis.io/) network: Content API (WordPress REST wp/v2). Tagged areas include Company, Entertainment, Media, Film, and Television.


  Skydance Media''s developer surface includes authentication, engineering blog, FAQ, YouTube channel, and 26 more developer resources.'
random_paper: 51
score:
  band: emerging
  composite: 21.0
  delta: -11.2
  facets:
    commercial_clarity: 21.1
    contract_quality: 15.1
    developer_ergonomics: 14.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: falling
security:
- kind: authentication
  name: Skydance Media Authentication
  slug: skydance-media-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Skydance Media Domain Security
  slug: skydance-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skydance-media
tags:
- Company
- Entertainment
- Media
- Film
- Television
- Animation
- Video Games
- Sports
- Content
- WordPress
website: https://skydance.com/
---
