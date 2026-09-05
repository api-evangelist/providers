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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-04'
api_count: 3
apis:
- baseURL: https://www.vice.com/wp-json
  baseurl_source: declared
  description: The live WordPress REST API served by vice.com. 601 routes are declared by the route-discovery document at https://www.vice.com/wp-json/, which the site advertises in the head of every page as <link r
  name: VICE WordPress REST API
  slug: vice-media-wordpress-rest-api
- baseURL: https://video.vice.com/wp-json
  baseurl_source: declared
  description: 'A second WordPress install answering on video.vice.com with 586 declared routes and the same core content namespaces, advertised the same way in the page head. Its public archive is effectively empty '
  name: VICE Video WordPress REST API
  slug: vice-media-video-wordpress-rest-api
- description: An authenticated platform gateway on api.vice.com, running nginx in front of an Express service that identifies itself as "api-auth 1.13.2" in the x-app-version response header. Every path probed anon
  name: VICE Platform API
  slug: vice-media-platform-api
artifact_total: 8
common:
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
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/vice-media-wp-rest-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vice-media-wp-rest-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vice-media-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vice-media-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vice-media-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vice-media-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vice-media-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vice-media-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vice-media-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vice-media-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/vice-media-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vice-media-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vice-media-rate-limits.yml
- group: auth
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
overview: 'Vice Media publishes 2 APIs on the [APIs.io](https://apis.io/) network: VICE WordPress REST API and VICE Video WordPress REST API. Tagged areas include Company, Media, Publishing, News, and Digital Media.


  Vice Media''s developer surface includes engineering blog, pricing, signup flow, authentication, and 26 more developer resources.'
plans:
- name: Vice Media Plans Pricing
  plan_count: 3
  slug: vice-media-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Vice Media Rate Limits
  slug: vice-media-rate-limits
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 12.9
    developer_ergonomics: 16.1
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
