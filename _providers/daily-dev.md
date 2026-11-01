---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 48
  human_in_the_loop: 3
  name: Daily Dev Agentic Access
  operation_count: 83
  slug: daily-dev-agentic-access
  summary_line: 83 operations · 48 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The bookmarks API from daily-dev — 5 operation(s) for bookmarks.
  name: daily-dev Bookmarks API
  slug: daily-dev-bookmarks-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The custom-feeds API from daily-dev — 5 operation(s) for custom-feeds.
  name: daily-dev Custom Feeds API
  slug: daily-dev-custom-feeds-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The experiences API from daily-dev — 2 operation(s) for experiences.
  name: daily-dev Experiences API
  slug: daily-dev-experiences-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The feed-filters API from daily-dev — 18 operation(s) for feed-filters.
  name: daily-dev Feed Filters API
  slug: daily-dev-feed-filters-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The feeds API from daily-dev — 5 operation(s) for feeds.
  name: daily-dev Feeds API
  slug: daily-dev-feeds-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The for-you API from daily-dev — 15 operation(s) for for-you.
  name: daily-dev For You API
  slug: daily-dev-for-you-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The notifications API from daily-dev — 3 operation(s) for notifications.
  name: daily-dev Notifications API
  slug: daily-dev-notifications-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The plugins API from daily-dev — 2 operation(s) for plugins.
  name: daily-dev Plugins API
  slug: daily-dev-plugins-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The posts API from daily-dev — 2 operation(s) for posts.
  name: daily-dev Posts API
  slug: daily-dev-posts-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The profile API from daily-dev — 1 operation(s) for profile.
  name: daily-dev Profile API
  slug: daily-dev-profile-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The recommend API from daily-dev — 2 operation(s) for recommend.
  name: daily-dev Recommend API
  slug: daily-dev-recommend-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The search API from daily-dev — 3 operation(s) for search.
  name: daily-dev Search API
  slug: daily-dev-search-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The stack API from daily-dev — 4 operation(s) for stack.
  name: daily-dev Stack API
  slug: daily-dev-stack-api
- baseURL: https://api.daily.dev/public/v1
  baseurl_source: declared
  description: The tags API from daily-dev — 1 operation(s) for tags.
  name: daily-dev Tags API
  slug: daily-dev-tags-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/daily-dev/agentic-access/daily-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/daily-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/daily-dev/rate-limits/daily-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/daily-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/daily-dev/plans/daily-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/daily-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/daily-dev/rules/daily-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/daily-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/daily-dev/json-ld/daily-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/daily-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/daily-dev/vocabulary/daily-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/daily-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/daily-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/daily-dev/data-model/daily-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/daily-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/daily-dev/components/daily-dev-components.yml
  title: ''
  type: Components
  url: components/daily-dev-components.yml
- group: build
  href: https://artifacts.apis.io/daily-dev/cli/daily-dev-cli.yml
  title: ''
  type: CLI
  url: cli/daily-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/daily-dev/conventions/daily-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/daily-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/daily-dev/authentication/daily-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/daily-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/daily-dev/scopes/daily-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/daily-dev-scopes.yml
- group: design
  href: https://artifacts.apis.io/daily-dev/errors/daily-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/daily-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/daily-dev/conformance/daily-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/daily-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/daily-dev/llms/daily-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daily-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/daily-dev/mcp/daily-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/daily-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/daily-dev/well-known/daily-dev-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daily-dev-www-security.txt
- group: agent
  href: https://artifacts.apis.io/daily-dev/well-known/daily-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daily-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/daily-dev/hosts/daily-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daily-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/daily-dev/vendors/daily-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daily-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://daily.dev/categories/security/
- group: company
  title: ''
  type: Newsroom
  url: https://daily.dev/categories/news/
- group: auth
  href: https://artifacts.apis.io/daily-dev/security/daily-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daily-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daily.dev/
- group: company
  title: ''
  type: Blog
  url: https://daily.dev/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.daily.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.daily.dev/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://daily.dev/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daily.dev/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://r.daily.dev/tos
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.daily.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://api.daily.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dailydotdev
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.daily.dev/openapi.json
  - status: 401
    url: https://api.daily.dev/mcp
  - status: 200
    url: https://daily.dev/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: daily.dev is a free, personalized developer news aggregator that curates daily updates from trusted sources across software development, AI coding tools, and web development. It offers a community-driven platform where developers can discover articles, tutorials, and resources tailored to their interests, fostering continuous learning and staying up‑to‑date with industry trends.
image: https://daily.dev/og-image.png?v=a830cdf1
json_schemas:
- name: ProfileUpdated
  property_count: 16
  slug: daily-dev-def-12
- name: FeedPostExplain
  property_count: 11
  slug: daily-dev-def-19
- name: PostDetail
  property_count: 18
  slug: daily-dev-def-21
- name: PluginSummary
  property_count: 11
  slug: daily-dev-def-25
- name: PluginDetail
  property_count: 12
  slug: daily-dev-def-26
- name: UserExperience
  property_count: 21
  slug: daily-dev-def-40
jsonld:
- class_count: 40
  name: Daily Dev Context
  property_count: 116
  slug: daily-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.daily.dev.
  name: daily-dev MCP Server
  slug: daily-dev-mcp-yml
modified: '2026-10-30'
name: daily-dev
nav: Providers
network: true
overview: 'daily-dev publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bookmarks API, Custom Feeds API, Experiences API, and 11 more. Tagged areas include Company, DeveloperTools, NewsAggregator, AI, and Community.


  The daily-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  daily-dev''s developer surface includes CLI, authentication, engineering blog, documentation, getting-started guide, pricing, API reference, and 27 more developer resources.'
plans:
- name: Daily Dev Plans Pricing
  plan_count: 1
  slug: daily-dev-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Daily Dev Rate Limits
  slug: daily-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: daily-dev API Rules
  rule_count: 19
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 3
  slug: daily-dev-rules
scopes:
- name: Daily Dev Scopes
  scope_count: 0
  slug: daily-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 92.1
    catalog_earned_first_party: 0.0
    catalog_gap: 22.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 59.7
    developer_ergonomics: 66.0
    discoverability: 66.7
    operational_transparency: 34.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Daily Dev Authentication
  slug: daily-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Daily Dev Domain Security
  slug: daily-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: daily-dev-ask
  slug: daily-dev-ask-skill
- name: daily-dev
  slug: daily-dev-skill
slug: daily-dev
tags:
- Company
- DeveloperTools
- NewsAggregator
- AI
- Community
website: https://daily.dev/
---
