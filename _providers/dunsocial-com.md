---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.dunsocial.com
  baseurl_source: declared
  description: 'DunSocial API as documented publicly: 85 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: DunSocial API
  slug: dunsocial-com-api
artifact_total: 14
asyncapis:
- description: ''
  name: Dunsocial Com Webhooks
  slug: dunsocial-com-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/dunsocial-com/rate-limits/dunsocial-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dunsocial-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dunsocial-com/plans/dunsocial-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dunsocial-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dunsocial-com/rules/dunsocial-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dunsocial-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dunsocial-com/json-ld/dunsocial-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dunsocial-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dunsocial-com/vocabulary/dunsocial-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dunsocial-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dunsocial-com/asyncapi/dunsocial-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dunsocial-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dunsocial-com/data-model/dunsocial-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dunsocial-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/dunsocial-com/cli/dunsocial-com-cli.yml
  title: ''
  type: CLI
  url: cli/dunsocial-com-cli.yml
- group: design
  href: https://artifacts.apis.io/dunsocial-com/conventions/dunsocial-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dunsocial-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dunsocial-com/authentication/dunsocial-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dunsocial-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dunsocial-com/conformance/dunsocial-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dunsocial-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dunsocial-com/llms/dunsocial-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dunsocial-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dunsocial-com/well-known/dunsocial-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dunsocial-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dunsocial-com/hosts/dunsocial-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dunsocial-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dunsocial-com/vendors/dunsocial-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dunsocial-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dunsocial.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.dunsocial.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dunsocial.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.dunsocial.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.dunsocial.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.dunsocial.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dunsocial.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dunsocial.com/faq/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://www.dunsocial.com/api.md
- group: auth
  href: https://artifacts.apis.io/dunsocial-com/security/dunsocial-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dunsocial-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dunsocial.com/
coverage:
  checked: '2026-11-06'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.dunsocial.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: DunSocial is an AI-first social media management tool. It plans, writes, schedules and publishes posts to X (Twitter), LinkedIn, Instagram, Threads, Bluesky, Reddit, Pinterest, YouTube Shorts, Discord and Slack in your own brand voice. Use the web app, REST API, CLI or hosted MCP server for Claude, ChatGPT, Cursor and other AI assistants. Founded in December 2025, the company is based in Chennai, India, and offers a $20/mo plan.
image: https://www.dunsocial.com/og-image.png
json_schemas:
- name: GetApiSocialAccountsResponse
  property_count: 6
  slug: dunsocial-com-get-api-social-accounts-response
- name: GetApiWorkspacesIdSocialAccountsResponse
  property_count: 6
  slug: dunsocial-com-get-api-workspaces-id-social-accounts-response
- name: PatchApiDraftsIdRequest
  property_count: 8
  slug: dunsocial-com-patch-api-drafts-id-request
- name: PostApiAiChatRequest
  property_count: 4
  slug: dunsocial-com-post-api-ai-chat-request
- name: PostApiAiTranscribeRequest
  property_count: 4
  slug: dunsocial-com-post-api-ai-transcribe-request
- name: PostApiMediaCompleteRequest
  property_count: 8
  slug: dunsocial-com-post-api-media-complete-request
jsonld:
- class_count: 62
  name: Dunsocial Com Context
  property_count: 89
  slug: dunsocial-com-context
layout: provider
modified: '2026-11-06'
name: DunSocial
nav: Providers
network: true
overview: 'DunSocial is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Social Media, Scheduler, Marketing, and Automation.


  The DunSocial catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DunSocial''s developer surface includes CLI, authentication, support, documentation, engineering blog, pricing, getting-started guide, and 19 more developer resources.'
plans:
- name: Dunsocial Com Plans Pricing
  plan_count: 3
  slug: dunsocial-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Dunsocial Com Rate Limits
  slug: dunsocial-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: DunSocial API Rules
  rule_count: 46
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 2
  slug: dunsocial-com-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 64.3
    discoverability: 66.1
    operational_transparency: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dunsocial Com Authentication
  slug: dunsocial-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dunsocial Com Domain Security
  slug: dunsocial-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dunsocial-com
tags:
- Artificial Intelligence
- Social Media
- Scheduler
- Marketing
- Automation
website: https://dunsocial.com/
---
