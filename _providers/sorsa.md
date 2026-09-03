---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Sorsa Agentic Access
  operation_count: 40
  slug: sorsa-agentic-access
  summary_line: 40 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.sorsa.io/v3
  baseurl_source: declared
  description: Twitter/X Community tweets, members, and community search
  name: Sorsa Community API
  slug: sorsa-community-api
- baseURL: https://api.sorsa.io/v3
  baseurl_source: declared
  description: Twitter/X List tweets, members, and followers
  name: Sorsa Lists API
  slug: sorsa-lists-api
- baseURL: https://api.sorsa.io/v3
  baseurl_source: declared
  description: Search tweets, users, mentions, and Twitter Spaces (Places)
  name: Sorsa Search API
  slug: sorsa-search-api
- baseURL: https://api.sorsa.io/v3
  baseurl_source: declared
  description: The Sorsa Info Crypto Related API from Sorsa — 7 operation(s) for sorsa info crypto related.
  name: Sorsa Sorsa Info Crypto Related API
  slug: sorsa-sorsa-info-crypto-related-api
- baseURL: https://api.sorsa.io/v3
  baseurl_source: declared
  description: The Technical Endpoints API from Sorsa — 4 operation(s) for technical endpoints.
  name: Sorsa Technical Endpoints API
  slug: sorsa-technical-endpoints-api
- baseURL: https://api.sorsa.io/v3
  baseurl_source: declared
  description: Tweet data (single and batch), articles, user timelines, quotes, retweets, comments, trends
  name: Sorsa Tweets API
  slug: sorsa-tweets-api
- baseURL: https://api.sorsa.io/v3
  baseurl_source: declared
  description: User profile, followers, following, verified followers, About metadata
  name: Sorsa Users Data API
  slug: sorsa-users-data-api
- baseURL: https://api.sorsa.io/v3
  baseurl_source: declared
  description: Verify follow, comment, retweet, quote and community-membership relationships
  name: Sorsa Verification API
  slug: sorsa-verification-api
artifact_total: 97
collections:
- collection_type: postman
  name: Sorsa Community API
  slug: postman-sorsa-community-api
- collection_type: postman
  name: Sorsa Community Lists API
  slug: postman-sorsa-lists-api
- collection_type: postman
  name: Sorsa Community Search API
  slug: postman-sorsa-search-api
- collection_type: postman
  name: Sorsa Community Sorsa Info Crypto Related API
  slug: postman-sorsa-sorsa-info-crypto-related-api
- collection_type: postman
  name: Sorsa Community Technical Endpoints API
  slug: postman-sorsa-technical-endpoints-api
- collection_type: postman
  name: Sorsa Community Tweets API
  slug: postman-sorsa-tweets-api
- collection_type: postman
  name: Sorsa Community Users Data API
  slug: postman-sorsa-users-data-api
- collection_type: postman
  name: Sorsa Community Verification API
  slug: postman-sorsa-verification-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sorsa Community API
  slug: open-sorsa-community-api
- collection_type: open
  name: Sorsa Community Lists API
  slug: open-sorsa-lists-api
- collection_type: open
  name: Sorsa Community Search API
  slug: open-sorsa-search-api
- collection_type: open
  name: Sorsa Community Sorsa Info Crypto Related API
  slug: open-sorsa-sorsa-info-crypto-related-api
- collection_type: open
  name: Sorsa Community Technical Endpoints API
  slug: open-sorsa-technical-endpoints-api
- collection_type: open
  name: Sorsa Community Tweets API
  slug: open-sorsa-tweets-api
- collection_type: open
  name: Sorsa Community Users Data API
  slug: open-sorsa-users-data-api
- collection_type: open
  name: Sorsa Community Verification API
  slug: open-sorsa-verification-api
- collection_type: open
  name: Sorsa API
  slug: open-sorsa
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sorsa/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sorsa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sorsa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sorsa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sorsa.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sorsa.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sorsa.io/
- group: other
  title: ''
  type: APIsJSON
  url: https://api.sorsa.io/apis.json
- group: start
  title: ''
  type: Signup
  url: https://app.sorsa.io/
- group: start
  title: ''
  type: Login
  url: https://app.sorsa.io/
- group: start
  title: ''
  type: Console
  url: https://app.sorsa.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.sorsa.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/sorsa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sorsa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sorsa-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sorsa-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sorsa-vocabulary.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.sorsa.io/status/v3
- group: operate
  title: ''
  type: Support
  url: https://docs.sorsa.io/support
- group: operate
  title: ''
  type: Contact
  url: mailto:contacts@sorsa.io
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/uwAefKCj7X
- group: company
  title: ''
  type: Twitter
  url: https://x.com/SorsaApp
- group: other
  title: ''
  type: Glossary
  url: https://docs.sorsa.io/use-cases-overview
- group: other
  title: ''
  type: BestPractices
  url: https://docs.sorsa.io/optimizing-api-usage
- group: agent
  title: ''
  type: LlmsText
  url: https://api.sorsa.io/llms.txt
created: '2026-05-16'
description: Sorsa Labs operates a real-time X (Twitter) data API providing developers access to tweets, profiles, search, mentions, lists, communities, engagement verification, and Sorsa Score crypto-influence analytics through 40 REST endpoints. It markets itself as an affordable alternative to the official X API and was formerly known as Tweetscout.
examples:
- key_count: 2
  name: Sorsa Check Follow Example
  slug: sorsa-check-follow-example
- key_count: 4
  name: Sorsa Community User Example
  slug: sorsa-community-user-example
- key_count: 8
  name: Sorsa Follower Example
  slug: sorsa-follower-example
- key_count: 2
  name: Sorsa Followers Example
  slug: sorsa-followers-example
- key_count: 2
  name: Sorsa Follows Example
  slug: sorsa-follows-example
- key_count: 2
  name: Sorsa Info Example
  slug: sorsa-info-example
- key_count: 2
  name: Sorsa Key Usage Info Example
  slug: sorsa-key-usage-info-example
- key_count: 2
  name: Sorsa Mentions Example
  slug: sorsa-mentions-example
- key_count: 6
  name: Sorsa Place Example
  slug: sorsa-place-example
- key_count: 2
  name: Sorsa Score Example
  slug: sorsa-score-example
- key_count: 2
  name: Sorsa Search Tweets Example
  slug: sorsa-search-tweets-example
- key_count: 6
  name: Sorsa Top Follower Example
  slug: sorsa-top-follower-example
- key_count: 3
  name: Sorsa Trend Example
  slug: sorsa-trend-example
- key_count: 3
  name: Sorsa Tweet Entity Example
  slug: sorsa-tweet-entity-example
- key_count: 11
  name: Sorsa Tweet Example
  slug: sorsa-tweet-example
- key_count: 2
  name: Sorsa Tweet Info Bulk Example
  slug: sorsa-tweet-info-bulk-example
- key_count: 2
  name: Sorsa Tweet Info Example
  slug: sorsa-tweet-info-example
- key_count: 12
  name: Sorsa User Example
  slug: sorsa-user-example
features:
- description: Live tweet, profile, follower, and engagement data pulled directly from X.
  name: Real-Time X (Twitter) Data
- description: One `ApiKey` header — no OAuth flow, bearer rotation, or callback URLs.
  name: Simple API Key Authentication
- description: Bulk profile and tweet endpoints accept up to 100 items per request for cost efficiency.
  name: Batch Endpoints
- description: Mirrors X advanced-search syntax (`from:`, `to:`, `since:`, `until:`, phrase and hashtag operators).
  name: Advanced Search Operators
- description: Filterable mentions feed with minimum likes/replies/retweets and date-range filters.
  name: Mentions Tracking
- description: Read List feeds, List members and followers, plus Community feeds, members, and in-community search.
  name: Lists and Communities Coverage
- description: Check follow, comment, retweet, quote, and community-membership relationships with boolean responses.
  name: Engagement Verification
- description: Influence score among crypto influencers, projects, and VCs, with 7-day/30-day deltas and top-follower lists.
  name: Sorsa Score Crypto Analytics
- description: Categorize an account's followers into influencers, projects, and venture capital employees.
  name: Follower Category Breakdown
- description: Convert between usernames and stable numeric user IDs; parse profile URLs to user IDs.
  name: ID and Handle Utilities
- description: The /key-usage-info endpoint reports total allocated requests, remaining balance, and quota expiration.
  name: Key Usage Visibility
- description: 1 API call = 1 request from the quota, regardless of which endpoint is hit.
  name: Flat-Rate Pricing
finops:
- name: Sorsa Finops
  service_category: ''
  slug: sorsa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sorsa.png
integrations:
- description: Primary upstream data source — Sorsa surfaces public X data via REST.
  name: X (Twitter)
- description: Community and support channel for developers using Sorsa.
  name: Discord
- description: Documentation references real-time monitoring patterns built on polling today.
  name: Webhooks (planned)
json_schemas:
- name: CommunityUser
  property_count: 6
  slug: sorsa-community-user
- name: Follower
  property_count: 19
  slug: sorsa-follower
- name: Place
  property_count: 12
  slug: sorsa-place
- name: TopFollower
  property_count: 14
  slug: sorsa-top-follower
- name: Trend
  property_count: 3
  slug: sorsa-trend
- name: TweetEntity
  property_count: 3
  slug: sorsa-tweet-entity
- name: Tweet
  property_count: 20
  slug: sorsa-tweet
- name: User
  property_count: 19
  slug: sorsa-user
json_structures:
- name: Sorsa Community User Structure
  property_count: 0
  slug: sorsa-community-user-structure
- name: Sorsa Follower Structure
  property_count: 0
  slug: sorsa-follower-structure
- name: Sorsa Place Structure
  property_count: 0
  slug: sorsa-place-structure
- name: Sorsa Top Follower Structure
  property_count: 0
  slug: sorsa-top-follower-structure
- name: Sorsa Trend Structure
  property_count: 0
  slug: sorsa-trend-structure
- name: Sorsa Tweet Entity Structure
  property_count: 0
  slug: sorsa-tweet-entity-structure
- name: Sorsa Tweet Structure
  property_count: 0
  slug: sorsa-tweet-structure
- name: Sorsa User Structure
  property_count: 0
  slug: sorsa-user-structure
jsonld:
- class_count: 36
  name: Sorsa Context
  property_count: 11
  slug: sorsa-context
- class_count: 8
  name: Sorsa Security Context
  property_count: 0
  slug: sorsa-security-context
layout: provider
modified: '2026-05-19'
name: Sorsa
nav: Providers
network: true
overview: 'Sorsa publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Community API, Lists API, Search API, and 5 more. Tagged areas include twitter, X, Social-Media, Data Extraction, and Real-Time.


  The Sorsa catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Sorsa''s developer surface includes authentication, documentation, signup flow, developer console, pricing, support, and 19 more developer resources.'
plans:
- name: Sorsa Plans Pricing
  plan_count: 4
  slug: sorsa-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Sorsa Rate Limits
  slug: sorsa-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sorsa API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sorsa-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Sorsa API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 1
    info: 0
    warn: 2
  slug: sorsa-rules
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 28.8
    contract_quality: 74.1
    developer_ergonomics: 66.7
    discoverability: 70.4
    governance: 28.8
    operational_transparency: 15.8
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sorsa/refs/heads/main/screenshots/sorsa-2026-06-20T194217.png
security:
- kind: authentication
  name: Sorsa Authentication
  slug: sorsa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sorsa Domain Security
  slug: sorsa-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sorsa
solutions:
- description: 10,000 monthly requests at $49/mo — entry tier for individual developers.
  name: Starter
- description: 100,000 monthly requests at $199/mo — for production integrations and agencies.
  name: Pro
- description: 500,000 monthly requests at $899/mo — for high-volume crypto-intel platforms.
  name: Enterprise
- description: Volume arrangements beyond 500K monthly requests via sales@sorsa.io with dedicated rate-limit profiles.
  name: Custom
tags:
- twitter
- X
- Social-Media
- Data Extraction
- Real-Time
use_cases:
- description: Track crypto influencers, projects, and VC activity in real time.
  name: Crypto Twitter Intelligence
- description: Verify follows, likes, retweets, quotes, and community membership for airdrop or campaign rules.
  name: Marketing Campaign Verification
- description: Combine About metadata and follower categories to map audience composition.
  name: Audience Geography Analysis
- description: Compare follower growth, Sorsa Score, and top-follower overlap between accounts.
  name: Competitor Analysis
- description: Real-time alerting on @-mentions filtered by engagement thresholds and date ranges.
  name: Mention Monitoring
- description: Find high-Sorsa-Score followers and following relationships to seed outreach lists.
  name: Target Audience Discovery
- description: Drop-in replacement for read-only X API workflows at a fraction of the cost.
  name: Migration from Official X API
- description: Pull trending topics by WOEID for region-specific monitoring.
  name: Trend Surveillance
website: https://sorsa.io/
---
