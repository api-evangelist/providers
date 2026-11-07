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
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trakkr Ai Agentic Access
  operation_count: 1
  slug: trakkr-ai-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Public API for Trakkr AI providing brand visibility and scoring data.
  name: Trakkr API
  slug: trakkr-api
artifact_total: 8
asyncapis:
- description: ''
  name: Trakkr Ai Webhooks
  slug: trakkr-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/trakkr-ai/agentic-access/trakkr-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trakkr-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/trakkr-ai/rate-limits/trakkr-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trakkr-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trakkr-ai/plans/trakkr-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trakkr-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/trakkr-ai/rules/trakkr-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/trakkr-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/trakkr-ai/vocabulary/trakkr-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trakkr-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/trakkr-ai/asyncapi/trakkr-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/trakkr-ai-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/trakkr-ai/authentication/trakkr-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trakkr-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/trakkr-ai/conformance/trakkr-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trakkr-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trakkr-ai/llms/trakkr-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trakkr-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/trakkr-ai/well-known/trakkr-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trakkr-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/trakkr-ai/hosts/trakkr-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trakkr-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/trakkr-ai/vendors/trakkr-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trakkr-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/trakkr-ai/security/trakkr-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trakkr-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trakkr.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://trakkr.ai/learn/api
- group: company
  title: ''
  type: Blog
  url: https://trakkr.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://trakkr.ai/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.trakkr.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://trakkr.ai/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://trakkr.ai/learn/docs/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://trakkr.ai/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://trakkr.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trakkr.ai/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://trakkr.ai/roadmap
- group: auth
  title: ''
  type: Security
  url: https://trakkr.ai/security
- group: operate
  title: ''
  type: StatusPage
  url: https://trakkr.ai/status
- group: operate
  title: ''
  type: Support
  url: https://trakkr.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trakkr.ai/terms
- group: design
  title: ''
  type: Webhooks
  url: https://trakkr.ai/learn/api/endpoints/webhooks
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://trakkr.ai/openapi.json
  - status: null
    url: https://trakkr.ai/api/mcp
  - status: 401
    url: https://api.trakkr.ai/mcp
  - status: 200
    url: https://trakkr.ai/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Trakkr AI provides an AI‑driven platform that helps businesses track, analyze, and visualize web traffic and visitor behavior. The service offers real‑time dashboards, detailed analytics, and integrations for marketing, SEO, and security teams. Documentation, pricing, and a public API are available at trakkr.ai, with an OpenAPI spec exposing 126 operations for data ingestion, querying, and webhook notifications.
image: https://trakkr.ai/og-image.png
layout: provider
modified: '2026-10-30'
name: trakkr-ai
nav: Providers
network: true
overview: 'trakkr-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Analytics, Traffic, and Web.


  The trakkr-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  trakkr-ai''s developer surface includes authentication, API reference, engineering blog, changelog, documentation, getting-started guide, pricing, and 22 more developer resources.'
plans:
- name: Trakkr Ai Plans Pricing
  plan_count: 4
  slug: trakkr-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 48
  name: Trakkr Ai Rate Limits
  slug: trakkr-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: trakkr-ai API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: trakkr-ai-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 24.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.2
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 39.0
    developer_ergonomics: 34.5
    discoverability: 73.2
    operational_transparency: 61.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: derived
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
screenshot: https://apis.io/screenshots/trakkr-ai/trakkr-ai-2026-11-03T145021.png
security:
- kind: authentication
  name: Trakkr Ai Authentication
  slug: trakkr-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Trakkr Ai Domain Security
  slug: trakkr-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trakkr-ai
tags:
- Company
- Artificial Intelligence
- Analytics
- Traffic
- Web
website: https://trakkr.ai/
---
