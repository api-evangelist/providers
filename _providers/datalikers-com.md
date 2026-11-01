---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Datalikers Com Agentic Access
  operation_count: 32
  slug: datalikers-com-agentic-access
  summary_line: 32 operations
api_count: 2
apis:
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Instagram comments — lookup by PK. Cache-only, no live fallback.
  name: datalikers-com Comment API
  slug: datalikers-com-comment-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Instagram hashtags — lookup by PK or name.
  name: datalikers-com Hashtag API
  slug: datalikers-com-hashtag-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Instagram story highlights — lookup by PK or URL.
  name: datalikers-com Highlight API
  slug: datalikers-com-highlight-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Instagram locations — lookup by PK or name search.
  name: datalikers-com Location API
  slug: datalikers-com-location-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Instagram posts, reels, and carousels — lookup by PK, shortcode, or full URL.
  name: datalikers-com Media API
  slug: datalikers-com-media-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Instagram stories — lookup by PK or story URL.
  name: datalikers-com Story API
  slug: datalikers-com-story-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Service health check and account balance.
  name: datalikers-com System API
  slug: datalikers-com-system-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: TikTok comments — lookup by PK or by author user_pk. Cache-only.
  name: datalikers-com TikTok Comment API
  slug: datalikers-com-tiktok-comment-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: TikTok hashtags (challenges) — lookup by PK or name.
  name: datalikers-com TikTok Hashtag API
  slug: datalikers-com-tiktok-hashtag-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: TikTok videos — lookup by PK or by owner user_pk.
  name: datalikers-com TikTok Media API
  slug: datalikers-com-tiktok-media-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: TikTok playlists (mixes) — lookup by PK or by owner user_pk.
  name: datalikers-com TikTok Playlist API
  slug: datalikers-com-tiktok-playlist-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: TikTok user profiles — lookup by PK or unique_id (handle).
  name: datalikers-com TikTok User API
  slug: datalikers-com-tiktok-user-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Instagram audio tracks used in reels — lookup by PK.
  name: datalikers-com Track API
  slug: datalikers-com-track-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: Instagram user profiles — lookup by PK or username, extended about info, AI face analysis, best-effort followers list.
  name: datalikers-com User API
  slug: datalikers-com-user-api
- baseURL: https://api.datalikers.com
  baseurl_source: declared
  description: The User v2 API from datalikers-com — 1 operation(s) for user v2.
  name: datalikers-com User v2 API
  slug: datalikers-com-user-v2-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/datalikers-com/agentic-access/datalikers-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datalikers-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/datalikers-com/plans/datalikers-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datalikers-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datalikers-com/rules/datalikers-com-rules.yml
  title: ''
  type: Spectral
  url: rules/datalikers-com-rules.yml
- group: design
  href: https://artifacts.apis.io/datalikers-com/json-ld/datalikers-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datalikers-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/datalikers-com/vocabulary/datalikers-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datalikers-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datalikers-com/data-model/datalikers-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datalikers-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/datalikers-com/security/datalikers-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/datalikers-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datalikers-com/authentication/datalikers-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datalikers-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/datalikers-com/lifecycle/datalikers-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/datalikers-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/datalikers-com/lifecycle/datalikers-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/datalikers-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/datalikers-com/errors/datalikers-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datalikers-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/datalikers-com/conformance/datalikers-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datalikers-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datalikers-com/llms/datalikers-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datalikers-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/datalikers-com/well-known/datalikers-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datalikers-com-security.txt
- group: agent
  href: https://artifacts.apis.io/datalikers-com/well-known/datalikers-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datalikers-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datalikers-com/hosts/datalikers-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datalikers-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datalikers-com/vendors/datalikers-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datalikers-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://datalikers.com/status
- group: start
  title: ''
  type: Login
  url: https://datalikers.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://datalikers.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://api.datalikers.com/redoc
- group: auth
  href: https://artifacts.apis.io/datalikers-com/security/datalikers-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datalikers-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datalikers-com/security/datalikers-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datalikers-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datalikers.com/
- group: docs
  title: ''
  type: Documentation
  url: https://datalikers.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://datalikers.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://datalikers.com/blog
- group: operate
  title: ''
  type: Support
  url: https://datalikers.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datalikers.com/help/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datalikers.com/help/privacy-policy
created: '2026-10-30'
description: DataLikers provides a developer platform offering RESTful APIs and MCP server access to Instagram and TikTok data at scale. It includes a fast cache API, AI‑powered MCP server for Claude, and ready‑made datasets covering user profiles, posts, comments, hashtags, and more. The service emphasizes no rate limits, transparent pricing starting at $0.0003 per request, and tools for dataset building and face analysis, targeting developers and businesses needing large‑scale social media data.
image: https://datalikers.com/assets/img/og-card.jpg
jsonld:
- class_count: 2
  name: Datalikers Com Context
  property_count: 4
  slug: datalikers-com-context
layout: provider
modified: '2026-10-30'
name: datalikers-com
nav: Providers
network: true
overview: 'datalikers-com publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comment API, Hashtag API, Highlight API, and 12 more. Tagged areas include Company, Data, Social Media, API, and Developer Platform.


  The datalikers-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  datalikers-com''s developer surface includes authentication, changelog, API reference, documentation, pricing, engineering blog, support, and 23 more developer resources.'
plans:
- name: Datalikers Com Plans Pricing
  plan_count: 1
  slug: datalikers-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Datalikers Com Rate Limits
  slug: datalikers-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: datalikers-com API Rules
  rule_count: 16
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 0
  slug: datalikers-com-rules
scopes:
- name: Datalikers Com Scopes
  scope_count: 0
  slug: datalikers-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 78.0
    catalog_earned_first_party: 0.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 70.9
    contract_quality: 47.3
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 78.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datalikers Com Authentication
  slug: datalikers-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Datalikers Com Domain Security
  slug: datalikers-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Datalikers Com Vulnerability Disclosure
  slug: datalikers-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-user-by-username
  slug: datalikers-com-get_user_by_username
slug: datalikers-com
tags:
- Company
- Data
- Social Media
- API
- Developer Platform
website: https://datalikers.com/
---
