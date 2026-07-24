---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: Every Condé Nast brand site serves a top-level RSS 2.0 feed at `/feed/rss` covering the brand's most recent published articles, with Dublin Core (`dc:creator`, `dc:publisher`, `dc:subject`), Media RSS
  name: Condé Nast Brand RSS Feeds
  slug: brand-rss-feeds
- description: Every published article on every Condé Nast brand site embeds schema.org structured data as `<script type="application/ld+json">` blocks in the page head. The primary block is a `NewsArticle` carrying
  name: Condé Nast Article JSON-LD
  slug: article-json-ld
- description: Each brand site exposes an XML sitemap index at `/sitemap.xml` pointing to per-month sub-sitemaps (e.g. `/sitemap-2026-05.xml`). Sub-sitemaps list every URL published that month with `<lastmod>` times
  name: Condé Nast Brand Sitemap Index
  slug: brand-sitemaps
- description: 'Copilot is Condé Nast''s internally-developed editorial platform that powers every brand site. Surface evidence in the open: the GitHub repository `CondeNast/copilot-util` is described as "Condé Nast —'
  name: Condé Nast Copilot CMS (internal)
  slug: copilot-cms
- description: 'Condé Nast Entertainment, launched in 2011, develops film, TV, social and digital video, and VR. Video is distributed off-platform via brand-owned YouTube channels (WIRED, Vogue, GQ, Vanity Fair, Bon '
  name: Condé Nast Entertainment Video Distribution
  slug: video-distribution
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conde-nast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.condenast.com
- group: company
  title: ''
  type: About
  url: https://www.condenast.com/about
- group: other
  title: ''
  type: Brands
  url: https://www.condenast.com/brands
- group: company
  title: ''
  type: Newsroom
  url: https://www.condenast.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.condenast.com/careers
- group: other
  title: Content & syndication enquiries (no self-serve developer portal)
  type: ContentLicensing
  url: https://www.condenast.com/contact
- group: build
  title: 142 public repos as of May 2026 — mostly tooling, Puppet modules, Ember/React utilities, hackathon repos and the Copilot utilities; no public APIs.
  type: GitHubOrganization
  url: https://github.com/CondeNast
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conde-nast
- group: other
  title: Advance Publications (private holding company of S.I. Newhouse family)
  type: ParentOrganization
  url: https://www.advance.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.condenast.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.condenast.com/user-agreement
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.condenast.com/cookies-policy
- group: company
  title: ''
  type: Blog
  url: https://www.wired.com/feed/rss
- group: other
  title: ''
  type: Brands
  url: ''
- group: other
  title: ''
  type: ContentSurfaces
  url: ''
- group: other
  title: ''
  type: NoPublicAPI
  url: ''
- group: other
  title: ''
  type: Scale
  url: ''
created: '2026-05-23'
description: Condé Nast is a global media company owned by Advance Publications that produces editorial content across more than two dozen iconic brands — Vogue, GQ, The New Yorker, Wired, Vanity Fair, Bon Appétit, Architectural Digest, Pitchfork, Allure, Glamour, Self, Teen Vogue, Condé Nast Traveler, Epicurious, Tatler, House & Garden, The World of Interiors, Ars Technica, Vogue Business, La Cucina Italiana and Johansens. Public content surfaces are not a developer API but a federated set of brand-level RSS feeds, schema.org NewsArticle JSON-LD on every article, monthly XML sitemaps, syndicated video on YouTube and OTT, and a private editorial CMS (internally known as Copilot) that powers all sites.
examples:
- key_count: 14
  name: Epicurious Recipe Example
  slug: epicurious-recipe-example
- key_count: 15
  name: Wired Article Example
  slug: wired-article-example
graphqls:
- description: ''
  name: Condé Nast GraphQL API
  slug: conde-nast-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/conde-nast.png
json_schemas:
- name: Condé Nast Article
  property_count: 17
  slug: conde-nast-article
jsonld:
- class_count: 20
  name: Conde Nast Context
  property_count: 7
  slug: conde-nast-context
layout: provider
modified: '2026-05-23'
name: Condé Nast
nav: Providers
network: true
overview: 'Condé Nast publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Publishing, Magazines, News, and Journalism.


  The Condé Nast catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Condé Nast''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 35
rules:
- name: Condé Nast API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: conde-nast-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 15.1
    developer_ergonomics: 2.2
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 26.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Conde Nast Domain Security
  slug: conde-nast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conde-nast
tags:
- Media
- Publishing
- Magazines
- News
- Journalism
- RSS
- Video
- JSON-LD
- Schema.org
website: https://www.condenast.com
---
