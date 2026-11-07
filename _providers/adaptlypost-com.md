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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for posting to social media platforms.
  name: AdaptlyPost API
  slug: adaptlypost-api
- baseURL: https://post.adaptlypost.com/post/api/v1
  baseurl_source: declared
  description: REST API for creating, scheduling, and managing social media posts across Facebook, Instagram, Threads, TikTok, X (Twitter), Bluesky, Mastodon, LinkedIn, Pinterest, YouTube, Google Business Profile, T
  name: AdaptlyPost Public API API
  slug: adaptlypost-public-api-api
artifact_total: 14
asyncapis:
- description: ''
  name: Adaptlypost Com Webhooks
  slug: adaptlypost-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/adaptlypost-com/plans/adaptlypost-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adaptlypost-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adaptlypost-com/rules/adaptlypost-com-rules.yml
  title: ''
  type: Spectral
  url: rules/adaptlypost-com-rules.yml
- group: design
  href: https://artifacts.apis.io/adaptlypost-com/json-ld/adaptlypost-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adaptlypost-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/adaptlypost-com/vocabulary/adaptlypost-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adaptlypost-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/adaptlypost-com/asyncapi/adaptlypost-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/adaptlypost-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/adaptlypost-com/data-model/adaptlypost-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adaptlypost-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/adaptlypost-com/changelog/adaptlypost-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adaptlypost-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/adaptlypost-com/authentication/adaptlypost-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adaptlypost-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/adaptlypost-com/errors/adaptlypost-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adaptlypost-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adaptlypost-com/conformance/adaptlypost-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adaptlypost-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adaptlypost-com/llms/adaptlypost-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adaptlypost-com-llms.txt
- group: other
  href: https://artifacts.apis.io/adaptlypost-com/hosts/adaptlypost-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adaptlypost-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adaptlypost-com/vendors/adaptlypost-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adaptlypost-com-vendors.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://adaptlypost.com/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TarasShyn
- group: operate
  title: ''
  type: ChangeLog
  url: https://adaptlypost.com/changelog
- group: auth
  href: https://artifacts.apis.io/adaptlypost-com/security/adaptlypost-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adaptlypost-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adaptlypost.com/
- group: docs
  title: ''
  type: Documentation
  url: https://adaptlypost.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://adaptlypost.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://adaptlypost.com/docs/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://adaptlypost.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adaptlypost.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adaptlypost.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://adaptlypost.com/support
- group: company
  title: ''
  type: Blog
  url: https://adaptlypost.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://adaptlypost.com/signup
- group: start
  title: ''
  type: Login
  url: https://adaptlypost.com/signin
created: '2026-10-31'
description: AdaptlyPost is a social media scheduling platform that lets users post to multiple networks via a unified dashboard or API. It supports Instagram, TikTok, YouTube, X, Facebook, LinkedIn, Pinterest, Threads, Bluesky, Mastodon, Telegram, Google Business Profile, and Tumblr. Plans range from $19 to $89 per month with a 7‑day free trial, and all plans include API access for AI agents to automate posting.
image: https://adaptlypost.com/opengraph-image.png
json_schemas:
- name: BulkSchedulePostsRequest
  property_count: 25
  slug: adaptlypost-com-bulk-schedule-posts-request
- name: CreateConnectLinkRequest
  property_count: 6
  slug: adaptlypost-com-create-connect-link-request
- name: CreateSocialPostRequest
  property_count: 41
  slug: adaptlypost-com-create-social-post-request
- name: RecurringPost
  property_count: 24
  slug: adaptlypost-com-recurring-post
- name: RssFeed
  property_count: 26
  slug: adaptlypost-com-rss-feed
- name: UpdateSocialPostRequest
  property_count: 38
  slug: adaptlypost-com-update-social-post-request
jsonld:
- class_count: 89
  name: Adaptlypost Com Context
  property_count: 326
  slug: adaptlypost-com-context
layout: provider
modified: '2026-10-31'
name: AdaptlyPost
nav: Providers
network: true
overview: 'AdaptlyPost publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public API API, and 1 more. Tagged areas include Company, Social Media, Scheduling, and AI Agents.


  The AdaptlyPost catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AdaptlyPost''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 21 more developer resources.'
plans:
- name: Adaptlypost Com Plans Pricing
  plan_count: 2
  slug: adaptlypost-com-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: AdaptlyPost API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: adaptlypost-com-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 54.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adaptlypost Com Authentication
  slug: adaptlypost-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adaptlypost Com Domain Security
  slug: adaptlypost-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaptlypost-com
tags:
- Company
- Social Media
- Scheduling
- AI Agents
website: https://adaptlypost.com/
---
