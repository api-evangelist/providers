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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Threadsnoop Com Agentic Access
  operation_count: 7
  slug: threadsnoop-com-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.threadsnoop.com
  baseurl_source: declared
  description: The Account API from threadsnoop-com — 1 operation(s) for account.
  name: threadsnoop-com Account API
  slug: threadsnoop-com-account-api
- baseURL: https://api.threadsnoop.com
  baseurl_source: declared
  description: The Comments API from threadsnoop-com — 2 operation(s) for comments.
  name: threadsnoop-com Comments API
  slug: threadsnoop-com-comments-api
- baseURL: https://api.threadsnoop.com
  baseurl_source: declared
  description: The Posts API from threadsnoop-com — 1 operation(s) for posts.
  name: threadsnoop-com Posts API
  slug: threadsnoop-com-posts-api
- baseURL: https://api.threadsnoop.com
  baseurl_source: declared
  description: The Subreddits API from threadsnoop-com — 2 operation(s) for subreddits.
  name: threadsnoop-com Subreddits API
  slug: threadsnoop-com-subreddits-api
- baseURL: https://api.threadsnoop.com
  baseurl_source: declared
  description: The Users API from threadsnoop-com — 1 operation(s) for users.
  name: threadsnoop-com Users API
  slug: threadsnoop-com-users-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/threadsnoop-com/agentic-access/threadsnoop-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/threadsnoop-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/threadsnoop-com/rate-limits/threadsnoop-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/threadsnoop-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/threadsnoop-com/plans/threadsnoop-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/threadsnoop-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/threadsnoop-com/rules/threadsnoop-com-rules.yml
  title: ''
  type: Spectral
  url: rules/threadsnoop-com-rules.yml
- group: design
  href: https://artifacts.apis.io/threadsnoop-com/json-ld/threadsnoop-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/threadsnoop-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/threadsnoop-com/vocabulary/threadsnoop-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/threadsnoop-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/threadsnoop-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/threadsnoop-com/data-model/threadsnoop-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/threadsnoop-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/threadsnoop-com/security/threadsnoop-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/threadsnoop-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/threadsnoop-com/authentication/threadsnoop-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/threadsnoop-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/threadsnoop-com/errors/threadsnoop-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/threadsnoop-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/threadsnoop-com/conformance/threadsnoop-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/threadsnoop-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/threadsnoop-com/llms/threadsnoop-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/threadsnoop-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/threadsnoop-com/well-known/threadsnoop-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/threadsnoop-com-security.txt
- group: auth
  href: https://artifacts.apis.io/threadsnoop-com/well-known/threadsnoop-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/threadsnoop-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/threadsnoop-com/well-known/threadsnoop-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/threadsnoop-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/threadsnoop-com/hosts/threadsnoop-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/threadsnoop-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://threadsnoop.com/terms
- group: start
  title: ''
  type: Sandbox
  url: https://threadsnoop.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://threadsnoop.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://threadsnoop.com/subreddits/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://threadsnoop.com/developer
- group: auth
  href: https://artifacts.apis.io/threadsnoop-com/security/threadsnoop-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/threadsnoop-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/threadsnoop-com/security/threadsnoop-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/threadsnoop-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://threadsnoop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://threadsnoop.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://threadsnoop.com/docs#openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://threadsnoop.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://threadsnoop.com/#pricing
- group: company
  title: ''
  type: Blog
  url: https://threadsnoop.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/threadsnoop
- group: start
  title: ''
  type: SignUp
  url: https://threadsnoop.com/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://threadsnoop.com/openapi.json
  - status: null
    url: https://api.threadsnoop.com/openapi.json
  - status: 401
    url: https://threadsnoop.com/mcp
  - status: 401
    url: https://api.threadsnoop.com/mcp
  - status: 200
    url: https://threadsnoop.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: ThreadSnoop provides a pay‑per‑read Reddit API designed for AI agents and developers. It offers read‑only access to Reddit posts, comments, comment trees, subreddit searches, subreddit rules, and user profiles via a simple REST or MCP interface. The service is built for Claude, Claude Desktop, claude.ai, and any AI agent needing reliable Reddit data without authentication or write capabilities. Pricing is usage‑based, starting at $0.0015 per read, with free credits on signup. Documentation includes quick‑start guides, authentication details, rate limits, error handling, and pagination conventions.
image: https://threadsnoop.com/logo.png
json_schemas:
- name: AccountEnvelope
  property_count: 2
  slug: threadsnoop-com-account-envelope
- name: CommentListEnvelope
  property_count: 2
  slug: threadsnoop-com-comment-list-envelope
- name: CommentTreeEnvelope
  property_count: 2
  slug: threadsnoop-com-comment-tree-envelope
- name: SubredditRulesEnvelope
  property_count: 2
  slug: threadsnoop-com-subreddit-rules-envelope
- name: SubredditSearchEnvelope
  property_count: 2
  slug: threadsnoop-com-subreddit-search-envelope
- name: UserProfileEnvelope
  property_count: 2
  slug: threadsnoop-com-user-profile-envelope
jsonld:
- class_count: 15
  name: Threadsnoop Com Context
  property_count: 29
  slug: threadsnoop-com-context
layout: provider
modified: '2026-10-31'
name: threadsnoop-com
nav: Providers
network: true
overview: 'threadsnoop-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Comments API, Posts API, and 2 more. Tagged areas include Reddit, API, AI, MCP, and Read‑only.


  The threadsnoop-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  threadsnoop-com''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Threadsnoop Com Plans Pricing
  plan_count: 1
  slug: threadsnoop-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Threadsnoop Com Rate Limits
  slug: threadsnoop-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: threadsnoop-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: threadsnoop-com-rules
scopes:
- name: Threadsnoop Com Scopes
  scope_count: 0
  slug: threadsnoop-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 92.1
    catalog_earned_first_party: 0.0
    catalog_gap: 22.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 64.4
    developer_ergonomics: 66.0
    discoverability: 67.9
    operational_transparency: 34.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Threadsnoop Com Authentication
  slug: threadsnoop-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Threadsnoop Com Domain Security
  slug: threadsnoop-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Threadsnoop Com Vulnerability Disclosure
  slug: threadsnoop-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: list-posts
  slug: threadsnoop-com-listPosts-skill
slug: threadsnoop-com
tags:
- Reddit
- API
- AI
- MCP
- Read‑only
website: https://threadsnoop.com/
---
