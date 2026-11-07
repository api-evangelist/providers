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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Octopost Ink Agentic Access
  operation_count: 11
  slug: octopost-ink-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- baseURL: https://octopost.ink
  baseurl_source: declared
  description: The Accounts API from octopost-ink — 1 operation(s) for accounts.
  name: octopost-ink Accounts API
  slug: octopost-ink-accounts-api
- baseURL: https://octopost.ink
  baseurl_source: declared
  description: The Posts API from octopost-ink — 5 operation(s) for posts.
  name: octopost-ink Posts API
  slug: octopost-ink-posts-api
- baseURL: https://octopost.ink
  baseurl_source: declared
  description: The Queue Settings API from octopost-ink — 1 operation(s) for queue settings.
  name: octopost-ink Queue Settings API
  slug: octopost-ink-queue-settings-api
artifact_total: 15
asyncapis:
- description: ''
  name: Octopost Ink Webhooks
  slug: octopost-ink-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/octopost-ink/agentic-access/octopost-ink-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/octopost-ink-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/octopost-ink/plans/octopost-ink-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/octopost-ink-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/octopost-ink/rules/octopost-ink-rules.yml
  title: ''
  type: Spectral
  url: rules/octopost-ink-rules.yml
- group: design
  href: https://artifacts.apis.io/octopost-ink/json-ld/octopost-ink-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/octopost-ink-context.jsonld
- group: design
  href: https://artifacts.apis.io/octopost-ink/vocabulary/octopost-ink-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/octopost-ink-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/octopost-ink/asyncapi/octopost-ink-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/octopost-ink-webhooks.yml
- group: design
  href: https://artifacts.apis.io/octopost-ink/data-model/octopost-ink-data-model.yml
  title: ''
  type: DataModel
  url: data-model/octopost-ink-data-model.yml
- group: operate
  href: https://artifacts.apis.io/octopost-ink/changelog/octopost-ink-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/octopost-ink-changelog.yml
- group: auth
  href: https://artifacts.apis.io/octopost-ink/authentication/octopost-ink-authentication.yml
  title: ''
  type: Authentication
  url: authentication/octopost-ink-authentication.yml
- group: design
  href: https://artifacts.apis.io/octopost-ink/errors/octopost-ink-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/octopost-ink-problem-types.yml
- group: design
  href: https://artifacts.apis.io/octopost-ink/conformance/octopost-ink-conformance.yml
  title: ''
  type: Conformance
  url: conformance/octopost-ink-conformance.yml
- group: agent
  href: https://artifacts.apis.io/octopost-ink/llms/octopost-ink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/octopost-ink-llms.txt
- group: agent
  href: https://artifacts.apis.io/octopost-ink/well-known/octopost-ink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/octopost-ink-well-known.yml
- group: other
  href: https://artifacts.apis.io/octopost-ink/hosts/octopost-ink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octopost-ink-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octopost.ink/terms
- group: operate
  title: ''
  type: Roadmap
  url: https://octopost.ink/roadmap
- group: auth
  href: https://artifacts.apis.io/octopost-ink/security/octopost-ink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octopost-ink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octopost.ink/
- group: docs
  title: ''
  type: Documentation
  url: https://octopost.ink/docs
- group: docs
  title: ''
  type: APIReference
  url: https://octopost.ink/docs/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://octopost.ink/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://octopost.ink/pricing
- group: company
  title: ''
  type: Blog
  url: https://octopost.ink/blog
- group: operate
  title: ''
  type: Support
  url: https://octopost.ink/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://octopost.ink/openapi.json
  - status: 401
    url: https://octopost.ink/mcp
  - status: 200
    url: https://octopost.ink/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Octopost Ink is a technology company specializing in automated social media posting solutions for businesses. Their platform enables users to schedule, manage, and analyze multi‑channel content distribution, integrating with major networks such as Instagram, Twitter, and LinkedIn. Octopost Ink provides robust APIs for developers to embed posting capabilities into custom applications, offering features like media asset handling, analytics dashboards, and compliance tools. The company focuses on scalability, security, and ease of integration for marketing teams and SaaS providers.
image: https://octopost.ink/opengraph-image?da33169deca2abd2
json_schemas:
- name: Account
  property_count: 4
  slug: octopost-ink-account
- name: CreatePost
  property_count: 8
  slug: octopost-ink-create-post
- name: Post
  property_count: 8
  slug: octopost-ink-post
- name: PublishResult
  property_count: 4
  slug: octopost-ink-publish-result
- name: QueueSettings
  property_count: 5
  slug: octopost-ink-queue-settings
jsonld:
- class_count: 7
  name: Octopost Ink Context
  property_count: 24
  slug: octopost-ink-context
layout: provider
modified: '2026-10-30'
name: octopost-ink
nav: Providers
network: true
overview: 'octopost-ink publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Accounts API, Posts API, and Queue Settings API. Tagged areas include Company, Social Media, Automation, and Marketing.


  The octopost-ink catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  octopost-ink''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Octopost Ink Plans Pricing
  plan_count: 3
  slug: octopost-ink-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: octopost-ink API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: octopost-ink-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 42.1
    contract_governance: 19.7
    contract_quality: 69.3
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 26.3
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/octopost-ink/octopost-ink-2026-11-03T140427.png
security:
- kind: authentication
  name: Octopost Ink Authentication
  slug: octopost-ink-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Octopost Ink Domain Security
  slug: octopost-ink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: octopost-ink
tags:
- Company
- Social Media
- Automation
- Marketing
website: https://octopost.ink/
---
