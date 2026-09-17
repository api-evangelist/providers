---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-09-16'
api_count: 5
apis:
- description: An authenticated platform gateway on api.vice.com, running nginx in front of an Express service that identifies itself as "api-auth 1.13.2" in the x-app-version response header. Every path probed anon
  name: VICE Platform API
  slug: vice-media-platform-api
- baseURL: https://www.vice.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoints — discovery and proxy for embeddable representations of VICE articles and videos.
  name: Vice Media Oembed/1.0 API
  slug: vice-media-oembed-1-0-api
- baseURL: https://www.vice.com/wp-json
  baseurl_source: declared
  description: REST API index / namespace and route discovery.
  name: Vice Media Root API
  slug: vice-media-root-api
- baseURL: https://www.vice.com/wp-json
  baseurl_source: declared
  description: WordPress Abilities API — the registry of named abilities an agent can discover and run. Read and run are capability-gated (observed HTTP 401 anonymously).
  name: Vice Media Wp Abilities/v1 API
  slug: vice-media-wp-abilities-v1-api
- baseURL: https://www.vice.com/wp-json
  baseurl_source: declared
  description: WordPress core content API — posts, pages, media, custom post types (sections, profiles, products), taxonomies (categories, tags, bylines, brands, platform languages), search, types, statuses and sett
  name: Vice Media Wp/v2 API
  slug: vice-media-wp-v2-api
artifact_total: 10
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/overlays/vice-media-video-wp-rest-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/security/vice-media-vulnerability-disclosure.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/openapi/_ae-authored/vice-media-wp-rest-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/vice-media-wp-rest-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/overlays/vice-media-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vice-media-wp-rest-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/llms/vice-media-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vice-media-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/mcp/vice-media-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vice-media-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/authentication/vice-media-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vice-media-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/conventions/vice-media-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vice-media-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/errors/vice-media-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vice-media-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/data-model/vice-media-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vice-media-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/lifecycle/vice-media-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vice-media-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/conformance/vice-media-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vice-media-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/packages/vice-media-packages.yml
  title: ''
  type: Packages
  url: packages/vice-media-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/plans/vice-media-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vice-media-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/rate-limits/vice-media-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vice-media-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vice-media/refs/heads/main/security/vice-media-domain-security.yml
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
overview: 'Vice Media publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Oembed/1.0 API, Root API, Wp Abilities/v1 API, and 1 more. Tagged areas include Company, Media, Publishing, News, and Digital Media.


  Vice Media''s developer surface includes engineering blog, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Vice Media Plans Pricing
  plan_count: 3
  slug: vice-media-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Vice Media Rate Limits
  slug: vice-media-rate-limits
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 17.2
    developer_ergonomics: 16.1
    discoverability: 81.5
    operational_transparency: 13.2
  previous_composite: 33.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
