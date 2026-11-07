---
access_model:
  confidence: high
  gated_conflict: 'x-api-posture: private but 6 published API entries'
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: An authenticated platform gateway on api.vice.com, running nginx in front of an Express service that identifies itself as "api-auth 1.13.2" in the x-app-version response header. Every path probed anon
  name: VICE Platform API
  slug: vice-media-platform-api
- description: 'The public WordPress REST API (wp-json) of the Vice Media website at www.vice.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Vice Media Website (WordPress REST)
  slug: vice-com-website-wordpress-rest
- baseURL: https://api.vice.com
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoints — discovery and proxy for embeddable representations of VICE articles and videos.
  name: Vice Media Oembed/1.0 API
  slug: vice-media-oembed-1-0-api
- baseURL: https://api.vice.com
  baseurl_source: declared
  description: REST API index / namespace and route discovery.
  name: Vice Media Root API
  slug: vice-media-root-api
- baseURL: https://api.vice.com
  baseurl_source: declared
  description: WordPress Abilities API — the registry of named abilities an agent can discover and run. Read and run are capability-gated (observed HTTP 401 anonymously).
  name: Vice Media Wp Abilities/v1 API
  slug: vice-media-wp-abilities-v1-api
- baseURL: https://api.vice.com
  baseurl_source: declared
  description: WordPress core content API — posts, pages, media, custom post types (sections, profiles, products), taxonomies (categories, tags, bylines, brands, platform languages), search, types, statuses and sett
  name: Vice Media Wp/v2 API
  slug: vice-media-wp-v2-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/vice-media/overlays/vice-media-video-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vice-media-video-wp-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.vice.com/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://www.vicemedia.com/
- group: company
  title: ''
  type: About
  url: https://www.vice.com/en/about-vice-digital-publishing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vice.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vice.com/en/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.vice.com/en/vice-responsible-disclosure-policy/
- group: auth
  href: https://artifacts.apis.io/vice-media/security/vice-media-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vice-media-vulnerability-disclosure.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VICEMedia
- group: company
  title: ''
  type: Blog
  url: https://www.vice.com/en/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vice.com/en/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vice.com/en/section/membership/
- group: start
  title: ''
  type: SignUp
  url: https://www.vice.com/en/section/membership/
- group: other
  title: ''
  type: Accessibility
  url: https://www.vice.com/en/vice-media-accessibility-statement/
- group: company
  title: ''
  type: Newsletter
  url: https://newsletter.vice.com
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/vice-media_stock/
- group: docs
  href: https://artifacts.apis.io/vice-media/openapi/_ae-authored/vice-media-wp-rest-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/vice-media-wp-rest-openapi.yml
- group: other
  href: https://artifacts.apis.io/vice-media/overlays/vice-media-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vice-media-wp-rest-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/vice-media/llms/vice-media-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vice-media-llms.txt
- group: agent
  href: https://artifacts.apis.io/vice-media/mcp/vice-media-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vice-media-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vice-media/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/vice-media/authentication/vice-media-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vice-media-authentication.yml
- group: design
  href: https://artifacts.apis.io/vice-media/conventions/vice-media-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vice-media-conventions.yml
- group: design
  href: https://artifacts.apis.io/vice-media/errors/vice-media-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vice-media-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vice-media/data-model/vice-media-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vice-media-data-model.yml
- group: design
  href: https://artifacts.apis.io/vice-media/lifecycle/vice-media-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vice-media-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/vice-media/conformance/vice-media-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vice-media-conformance.yml
- group: build
  href: https://artifacts.apis.io/vice-media/packages/vice-media-packages.yml
  title: ''
  type: Packages
  url: packages/vice-media-packages.yml
- group: commercial
  href: https://artifacts.apis.io/vice-media/plans/vice-media-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vice-media-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vice-media/rate-limits/vice-media-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vice-media-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/vice-media/security/vice-media-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vice-media-domain-security.yml
created: '2026-09-04'
description: Vice Media is the Brooklyn, New York youth-culture and news media company founded in 1994 in Montreal by Suroosh Alvi, Shane Smith and Gavin McInnes, which grew from the VICE magazine into a global multi-platform publisher, film and television studio and creative agency before filing for Chapter 11 in May 2023 and being acquired for $350 million by a consortium led by Fortress Investment Group. It operates today through Vice Studios Group, Vice TV, the Virtue creative agency and Vice Digital. Vice Media runs no developer programme, publishes no API documentation, portal, SDK or pricing, and sells no API product. It is catalogued here because its flagship editorial property, vice.com — owned and operated under the VICE brand by VICE Digital Publishing, LLC, the Savage Ventures joint venture Vice Media announced in 2024 — serves a live, anonymously readable WordPress REST API of 601 routes that the site advertises in the head of every page, exposing an editorial archive of 822,047
  posts across 20 language editions, plus an oEmbed 1.0 provider endpoint and RSS 2.0 syndication. A second WordPress install answers on video.vice.com, and a separate authenticated platform gateway on api.vice.com answers every anonymous request with HTTP 401.
image: https://www.vice.com/wp-content/uploads/sites/2/2024/08/VICE-logo.jpeg?w=1400
layout: provider
modified: '2026-09-04'
name: Vice Media
nav: Providers
network: true
overview: 'Vice Media is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Oembed/1.0 API, Root API, Wp Abilities/v1 API, and 3 more. Tagged areas include Company, Media, Publishing, News, and Digital Media.


  The Vice Media catalog on APIs.io includes 1 Spectral governance ruleset.


  Vice Media''s developer surface includes engineering blog, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Vice Media Plans Pricing
  plan_count: 3
  slug: vice-media-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Vice Media Rate Limits
  slug: vice-media-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Vice Media API Rules
  rule_count: 65
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 6
  slug: vice-media-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 51.5
    catalog_earned_first_party: 12.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 15.0
    developer_ergonomics: 20.8
    discoverability: 69.6
    operational_transparency: 13.2
  previous_composite: 38.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vice-media/vice-media-2026-10-11T132943.png
security:
- kind: authentication
  name: Vice Media Authentication
  slug: vice-media-authentication
  summary_line: http/apiKey/opaque-client-credential · 3 schemes
- kind: domain-security
  name: Vice Media Domain Security
  slug: vice-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vice Media Vulnerability Disclosure
  slug: vice-media-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 3
skills:
- name: Embed a VICE article with oEmbed
  slug: vice-media-embed-a-vice-article
- name: Search the VICE editorial archive
  slug: vice-media-search-the-archive
- name: Walk VICE editions, sections and bylines
  slug: vice-media-walk-editions-and-taxonomies
slug: vice-media
tags:
- Company
- Media
- Publishing
- News
- Digital Media
- Content
- Video
- Entertainment
- WordPress
- Syndication
- oEmbed
- Brooklyn
website: https://www.vice.com/
---
