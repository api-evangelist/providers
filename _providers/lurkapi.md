---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lurkapi Agentic Access
  operation_count: 178
  slug: lurkapi-agentic-access
  summary_line: 178 operations
api_count: 1
apis:
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Your LurkAPI credit balance.
  name: LurkAPI Account API
  slug: lurkapi-account-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Profiles, posts and full threads from any public Bluesky account.
  name: LurkAPI Bluesky API
  slug: lurkapi-bluesky-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: 'eBay search results and listing details: prices, bids, condition, sellers, shipping and item specifics.'
  name: LurkAPI eBay API
  slug: lurkapi-ebay-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Public Pages and profiles with their contact details, posts, events and comments, plus the ads in Meta's Ad Library.
  name: LurkAPI Facebook API
  slug: lurkapi-facebook-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Google Maps places and reviews, Google News, search suggestions, and the ads in Google's Ads Transparency Center.
  name: LurkAPI Google API
  slug: lurkapi-google-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Public profiles, posts, reels and comments with media and engagement counts, plus reel search, similar accounts and reel transcripts.
  name: LurkAPI Instagram API
  slug: lurkapi-instagram-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: 'A creator''s Linktree page: their links, social accounts and listed email.'
  name: LurkAPI Link In Bio API
  slug: lurkapi-link-in-bio-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Posts, comments, search and community stats from any public subreddit.
  name: LurkAPI Reddit API
  slug: lurkapi-reddit-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Public profiles, live stories, highlights and Spotlight videos from Snapchat.
  name: LurkAPI Snapchat API
  slug: lurkapi-snapchat-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Public channel profiles, their posts and single posts, with views, media and reactions.
  name: LurkAPI Telegram API
  slug: lurkapi-telegram-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Public Threads profiles, an account's posts and single posts, with text, media and engagement.
  name: LurkAPI Threads API
  slug: lurkapi-threads-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Profiles, videos, transcripts and comments from any public TikTok account.
  name: LurkAPI Tik Tok API
  slug: lurkapi-tiktok-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Any public web page as HTML, markdown or plain text, even past bot checks and captchas.
  name: LurkAPI Web API
  slug: lurkapi-web-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Tweets, profiles and recent posts from any public X account.
  name: LurkAPI X (Twitter) API
  slug: lurkapi-x-twitter-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Videos, Shorts, transcripts, comments and channel stats from any public YouTube channel.
  name: LurkAPI YouTube API
  slug: lurkapi-youtube-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Public profiles, company pages and their updates, job listings, and ads from LinkedIn's Ad Library.
  name: LurkAPI Linked In API
  slug: lurkapi-linked-in-api
- baseURL: https://api.lurkapi.com
  baseurl_source: declared
  description: Profiles and posts from public Truth Social accounts.
  name: LurkAPI Truthsocial API
  slug: lurkapi-truthsocial-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/lurkapi/agentic-access/lurkapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lurkapi-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/lurkapi/plans/lurkapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lurkapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lurkapi/rules/lurkapi-rules.yml
  title: ''
  type: Spectral
  url: rules/lurkapi-rules.yml
- group: design
  href: https://artifacts.apis.io/lurkapi/json-ld/lurkapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lurkapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/lurkapi/vocabulary/lurkapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lurkapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lurkapi/data-model/lurkapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lurkapi-data-model.yml
- group: operate
  href: https://artifacts.apis.io/lurkapi/changelog/lurkapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lurkapi-changelog.yml
- group: auth
  href: https://artifacts.apis.io/lurkapi/authentication/lurkapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lurkapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/lurkapi/errors/lurkapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lurkapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lurkapi/conformance/lurkapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lurkapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lurkapi/llms/lurkapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lurkapi-llms.txt
- group: agent
  href: https://artifacts.apis.io/lurkapi/mcp/lurkapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lurkapi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lurkapi/well-known/lurkapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lurkapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/lurkapi/hosts/lurkapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lurkapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/lurkapi/vendors/lurkapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lurkapi-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://lurkapi.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.lurkapi.com`
- group: auth
  href: https://artifacts.apis.io/lurkapi/security/lurkapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lurkapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lurkapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://lurkapi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://lurkapi.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://lurkapi.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lurkapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lurkapi.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://lurkapi.com/status
- group: operate
  title: ''
  type: Changelog
  url: https://lurkapi.com/changelog
- group: agent
  title: ''
  type: llms.txt
  url: https://lurkapi.com/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: https://lurkapi.com/openapi.json
created: '2026-11-02'
description: LurkAPI provides social media data APIs that enable AI applications to access posts, ads, and profiles from sixteen major platforms. The service offers clean JSON outputs for ads, posts, and user profiles, with flexible pricing per call and no subscription required. It supports tools for searching, retrieving, and analyzing social content across Facebook, Instagram, Reddit, YouTube, TikTok, Google News, and more, helping developers integrate real‑time social insights into their products.
image: https://lurkapi.com/og.png
json_schemas:
- name: BlueskyReply
  property_count: 21
  slug: lurkapi-bluesky-reply
- name: RedditComment
  property_count: 22
  slug: lurkapi-reddit-comment
jsonld:
- class_count: 3
  name: Lurkapi Context
  property_count: 45
  slug: lurkapi-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.lurkapi.com.
  name: LurkAPI MCP Server
  slug: lurkapi-mcp-yml
modified: '2026-11-02'
name: LurkAPI
nav: Providers
network: true
overview: 'LurkAPI publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Bluesky API, eBay API, and 14 more. Tagged areas include Social Media, Data API, AI Integration, Advertising, and Analytics.


  The LurkAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LurkAPI''s developer surface includes changelog, authentication, documentation, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Lurkapi Plans Pricing
  plan_count: 3
  slug: lurkapi-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: LurkAPI API Rules
  rule_count: 56
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 5
  slug: lurkapi-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 62.3
    developer_ergonomics: 22.6
    discoverability: 65.0
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lurkapi Authentication
  slug: lurkapi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Lurkapi Domain Security
  slug: lurkapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lurkapi
tags:
- Social Media
- Data API
- AI Integration
- Advertising
- Analytics
website: https://lurkapi.com
---
