---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Breakreach Com Agentic Access
  operation_count: 38
  slug: breakreach-com-agentic-access
  summary_line: 38 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Accounts API from Breakreach — 3 operation(s) for accounts.
  name: Breakreach Accounts API
  slug: breakreach-com-accounts-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Analytics API from Breakreach — 1 operation(s) for analytics.
  name: Breakreach Analytics API
  slug: breakreach-com-analytics-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Comment Dm Rules API from Breakreach — 4 operation(s) for comment dm rules.
  name: Breakreach Comment Dm Rules API
  slug: breakreach-com-comment-dm-rules-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Comments API from Breakreach — 3 operation(s) for comments.
  name: Breakreach Comments API
  slug: breakreach-com-comments-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Connect Links API from Breakreach — 2 operation(s) for connect links.
  name: Breakreach Connect Links API
  slug: breakreach-com-connect-links-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Dm Automations API from Breakreach — 3 operation(s) for dm automations.
  name: Breakreach Dm Automations API
  slug: breakreach-com-dm-automations-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Inbox API from Breakreach — 2 operation(s) for inbox.
  name: Breakreach Inbox API
  slug: breakreach-com-inbox-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Media API from Breakreach — 2 operation(s) for media.
  name: Breakreach Media API
  slug: breakreach-com-media-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Next Slot API from Breakreach — 1 operation(s) for next slot.
  name: Breakreach Next Slot API
  slug: breakreach-com-next-slot-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Performance API from Breakreach — 1 operation(s) for performance.
  name: Breakreach Performance API
  slug: breakreach-com-performance-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Pinterest Boards API from Breakreach — 1 operation(s) for pinterest boards.
  name: Breakreach Pinterest Boards API
  slug: breakreach-com-pinterest-boards-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Post Insights API from Breakreach — 1 operation(s) for post insights.
  name: Breakreach Post Insights API
  slug: breakreach-com-post-insights-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Posts API from Breakreach — 4 operation(s) for posts.
  name: Breakreach Posts API
  slug: breakreach-com-posts-api
- baseURL: https://api.breakreach.com
  baseurl_source: declared
  description: The Workspaces API from Breakreach — 1 operation(s) for workspaces.
  name: Breakreach Workspaces API
  slug: breakreach-com-workspaces-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/breakreach-com/agentic-access/breakreach-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/breakreach-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/breakreach-com/rate-limits/breakreach-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/breakreach-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/breakreach-com/plans/breakreach-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/breakreach-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/breakreach-com/rules/breakreach-com-rules.yml
  title: ''
  type: Spectral
  url: rules/breakreach-com-rules.yml
- group: design
  href: https://artifacts.apis.io/breakreach-com/json-ld/breakreach-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/breakreach-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/breakreach-com/vocabulary/breakreach-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/breakreach-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/breakreach-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/breakreach-com/data-model/breakreach-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/breakreach-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/breakreach-com/conventions/breakreach-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/breakreach-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/breakreach-com/conventions/breakreach-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/breakreach-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/breakreach-com/authentication/breakreach-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/breakreach-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/breakreach-com/errors/breakreach-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/breakreach-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/breakreach-com/conformance/breakreach-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/breakreach-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/breakreach-com/llms/breakreach-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breakreach-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/breakreach-com/well-known/breakreach-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breakreach-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/breakreach-com/hosts/breakreach-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breakreach-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/breakreach-com/vendors/breakreach-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breakreach-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breakreach.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.breakreach.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breakreach.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.breakreach.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.breakreach.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.breakreach.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://www.breakreach.com/developers
- group: auth
  href: https://artifacts.apis.io/breakreach-com/security/breakreach-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breakreach-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.breakreach.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.breakreach.com/v1/openapi.json
  - status: 401
    url: https://api.breakreach.com/mcp
  - status: 401
    url: https://api.breakreach.com/v1/graphql
  - status: 200
    url: https://breakreach.com/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Breakreach provides an AI‑powered social media scheduling platform that integrates with ChatGPT, Claude and major networks like Instagram, TikTok, LinkedIn, and more. Users can automate post creation, schedule publishing, and manage engagement through a unified calendar, leveraging AI assistants to draft content and analyze performance. The service offers a REST API, webhooks for post events, and a developer portal for integration.
image: https://www.breakreach.com/og/default.jpg
json_schemas:
- name: ArticleSettings
  property_count: 6
  slug: breakreach-com-article-settings
- name: CommentDmEvent
  property_count: 15
  slug: breakreach-com-comment-dm-event
- name: CommentDmRuleInput
  property_count: 9
  slug: breakreach-com-comment-dm-rule-input
- name: CommentDmRule
  property_count: 15
  slug: breakreach-com-comment-dm-rule
- name: Comment
  property_count: 18
  slug: breakreach-com-comment
- name: DmAutomationRun
  property_count: 13
  slug: breakreach-com-dm-automation-run
jsonld:
- class_count: 17
  name: Breakreach Com Context
  property_count: 88
  slug: breakreach-com-context
layout: provider
modified: '2026-11-03'
name: Breakreach
nav: Providers
network: true
overview: 'Breakreach publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, Comment Dm Rules API, and 11 more. Tagged areas include Artificial Intelligence, Social Media, Automation, Scheduling, and Marketing.


  The Breakreach catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Breakreach''s developer surface includes authentication, support, pricing, documentation, API reference, and 21 more developer resources.'
plans:
- name: Breakreach Com Plans Pricing
  plan_count: 3
  slug: breakreach-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 8
  name: Breakreach Com Rate Limits
  slug: breakreach-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Breakreach API Rules
  rule_count: 49
  severity_counts:
    error: 42
    hint: 0
    info: 3
    warn: 4
  slug: breakreach-com-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 62.1
    developer_ergonomics: 24.4
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Breakreach Com Authentication
  slug: breakreach-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Breakreach Com Domain Security
  slug: breakreach-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: breakreach-com-create-and-schedule-post
  slug: breakreach-com-create-and-schedule-post
slug: breakreach-com
tags:
- Artificial Intelligence
- Social Media
- Automation
- Scheduling
- Marketing
website: https://www.breakreach.com/
---
