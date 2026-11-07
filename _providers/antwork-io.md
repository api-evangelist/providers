---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Antwork Io Agentic Access
  operation_count: 28
  slug: antwork-io-agentic-access
  summary_line: 28 operations · 15 acting
api_count: 1
apis:
- baseURL: https://antwork.io/api/v1
  baseurl_source: declared
  description: The Accounts API from Antwork — 3 operation(s) for accounts.
  name: Antwork Accounts API
  slug: antwork-io-accounts-api
- baseURL: https://antwork.io/api/v1
  baseurl_source: declared
  description: The Analytics API from Antwork — 2 operation(s) for analytics.
  name: Antwork Analytics API
  slug: antwork-io-analytics-api
- baseURL: https://antwork.io/api/v1
  baseurl_source: declared
  description: The Campaigns API from Antwork — 2 operation(s) for campaigns.
  name: Antwork Campaigns API
  slug: antwork-io-campaigns-api
- baseURL: https://antwork.io/api/v1
  baseurl_source: declared
  description: The Media API from Antwork — 2 operation(s) for media.
  name: Antwork Media API
  slug: antwork-io-media-api
- baseURL: https://antwork.io/api/v1
  baseurl_source: declared
  description: The Platforms API from Antwork — 1 operation(s) for platforms.
  name: Antwork Platforms API
  slug: antwork-io-platforms-api
- baseURL: https://antwork.io/api/v1
  baseurl_source: declared
  description: The Posts API from Antwork — 7 operation(s) for posts.
  name: Antwork Posts API
  slug: antwork-io-posts-api
- baseURL: https://antwork.io/api/v1
  baseurl_source: declared
  description: The Usage API from Antwork — 1 operation(s) for usage.
  name: Antwork Usage API
  slug: antwork-io-usage-api
- baseURL: https://antwork.io/api/v1
  baseurl_source: declared
  description: The Workspaces API from Antwork — 3 operation(s) for workspaces.
  name: Antwork Workspaces API
  slug: antwork-io-workspaces-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/antwork-io/agentic-access/antwork-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/antwork-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/antwork-io/rules/antwork-io-rules.yml
  title: ''
  type: Spectral
  url: rules/antwork-io-rules.yml
- group: design
  href: https://artifacts.apis.io/antwork-io/json-ld/antwork-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/antwork-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/antwork-io/vocabulary/antwork-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/antwork-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/antwork-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/antwork-io/data-model/antwork-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/antwork-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/antwork-io/conventions/antwork-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/antwork-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/antwork-io/conventions/antwork-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/antwork-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/antwork-io/errors/antwork-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/antwork-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/antwork-io/conformance/antwork-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/antwork-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/antwork-io/llms/antwork-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/antwork-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/antwork-io/well-known/antwork-io-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/antwork-io-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/antwork-io/well-known/antwork-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/antwork-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/antwork-io/hosts/antwork-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antwork-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/antwork-io/packages/antwork-io-packages.yml
  title: ''
  type: SDKs
  url: packages/antwork-io-packages.yml
- group: build
  href: https://artifacts.apis.io/antwork-io/packages/antwork-io-packages.yml
  title: ''
  type: Packages
  url: packages/antwork-io-packages.yml
- group: start
  title: ''
  type: Login
  url: https://antwork.io/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://antwork.io/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://antwork.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://antwork.io/blog
- group: auth
  href: https://artifacts.apis.io/antwork-io/authentication/antwork-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/antwork-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/antwork-io/security/antwork-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antwork-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://antwork.io/
- group: docs
  title: ''
  type: Documentation
  url: https://antwork.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://antwork.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://antwork.io/#how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://antwork.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antwork.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antwork.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/antwork
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://antwork.io/openapi.json
  - status: 401
    url: https://api.antwork.io/mcp
  - status: 401
    url: https://dev.antwork.io/mcp
  - status: 200
    url: https://antwork.io/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: 'Antwork is the agentic social media scheduler: your AI agent, like Claude, Claude Code or ChatGPT, drafts in your voice and publishes to all your accounts on Instagram, TikTok, YouTube and 10 more. You approve every post.'
image: https://antwork.io/logo.svg
json_schemas:
- name: AccountDetail
  property_count: 18
  slug: antwork-io-account-detail
- name: CommentList
  property_count: 9
  slug: antwork-io-comment-list
- name: EngagementHistory
  property_count: 14
  slug: antwork-io-engagement-history
- name: Performance
  property_count: 10
  slug: antwork-io-performance
- name: PostUpdate
  property_count: 8
  slug: antwork-io-post-update
- name: Usage
  property_count: 5
  slug: antwork-io-usage
jsonld:
- class_count: 44
  name: Antwork Io Context
  property_count: 153
  slug: antwork-io-context
layout: provider
modified: '2026-11-01'
name: Antwork
nav: Providers
network: true
overview: 'Antwork publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, Campaigns API, and 5 more. Tagged areas include Artificial Intelligence, Social Media, Automation, Scheduler, and Marketing.


  The Antwork catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Antwork''s developer surface includes changelog, engineering blog, authentication, documentation, API reference, getting-started guide, pricing, and 23 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Antwork API Rules
  rule_count: 61
  severity_counts:
    error: 51
    hint: 0
    info: 2
    warn: 8
  slug: antwork-io-rules
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 64.2
    developer_ergonomics: 45.7
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Antwork Io Authentication
  slug: antwork-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Antwork Io Domain Security
  slug: antwork-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: schedule-post
  slug: schedule-post
slug: antwork-io
tags:
- Artificial Intelligence
- Social Media
- Automation
- Scheduler
- Marketing
website: https://antwork.io/
---
