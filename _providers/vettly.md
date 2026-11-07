---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.vettly.dev
  baseurl_source: declared
  description: Content moderation endpoints. Use POST /v1/check to moderate user-generated content (text, images, video) and get allow/flag/block decisions.
  name: Vettly Moderation API
  slug: vettly-moderation-api
- baseURL: https://api.vettly.dev
  baseurl_source: declared
  description: Health checks and monitoring
  name: Vettly System API
  slug: vettly-system-api
artifact_total: 14
asyncapis:
- description: ''
  name: Vettly Webhooks
  slug: vettly-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/vettly/rate-limits/vettly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vettly-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/vettly/overlays/vettly-content-moderation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vettly-content-moderation-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/vettly/mcp/vettly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vettly-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vettly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://vettly.dev
- group: auth
  href: https://artifacts.apis.io/vettly/security/vettly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vettly-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vettly/security/vettly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vettly-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vettly/authentication/vettly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vettly-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vettly/security/vettly-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/vettly-vulnerability-disclosure.yml
- group: build
  href: https://artifacts.apis.io/vettly/packages/vettly-packages.yml
  title: ''
  type: Packages
  url: packages/vettly-packages.yml
- group: build
  href: https://artifacts.apis.io/vettly/packages/vettly-packages.yml
  title: ''
  type: SDKs
  url: packages/vettly-packages.yml
- group: agent
  href: https://artifacts.apis.io/vettly/well-known/vettly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vettly-well-known.yml
- group: auth
  href: https://artifacts.apis.io/vettly/well-known/vettly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vettly-security.txt
- group: agent
  href: https://artifacts.apis.io/vettly/llms/vettly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vettly-llms.txt
- group: design
  href: https://artifacts.apis.io/vettly/conformance/vettly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vettly-conformance.yml
- group: design
  href: https://artifacts.apis.io/vettly/lifecycle/vettly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vettly-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vettly.dev
- group: operate
  href: https://artifacts.apis.io/vettly/changelog/vettly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vettly-changelog.yml
- group: design
  href: https://artifacts.apis.io/vettly/components/vettly-components.yml
  title: ''
  type: Components
  url: components/vettly-components.yml
- group: design
  href: https://artifacts.apis.io/vettly/data-model/vettly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vettly-data-model.yml
- group: start
  href: https://artifacts.apis.io/vettly/sandbox/vettly-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/vettly-sandbox.yml
- group: design
  href: https://artifacts.apis.io/vettly/conventions/vettly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vettly-conventions.yml
- group: design
  href: https://artifacts.apis.io/vettly/conventions/vettly-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/vettly-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/vettly/plans/vettly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vettly-plans-pricing.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vettly.dev/guide/getting-started.html
- group: company
  title: ''
  type: Blog
  url: https://vettly.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://vettly.dev/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://vettly.dev/sign-up
- group: start
  title: ''
  type: Login
  url: https://vettly.dev/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vettly.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vettly.dev/privacy
created: '2026-09-06'
description: Developer-first content moderation for text, images, and video with policy versioning, appeals, and audit trails. Also offers OpenClaw Guardrails for vetting agent skills and authorizing runtime actions.
finops:
- has_sources: true
  method: derived
  name: Vettly Finops
  primary_unit: decisions
  service_category: ''
  slug: vettly-finops
  template: false
image: https://vettly.dev/vettly-logo.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 5 tools listed.
  name: Vettly MCP Server
  slug: vettly-mcp-server
modified: '2026-09-07'
name: Vettly
nav: Providers
network: true
overview: 'Vettly publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Moderation API and System API. Tagged areas include Content Moderation, Trust and Safety, Security, Text Analysis, and Image Moderation.


  The Vettly catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Vettly''s developer surface includes authentication, changelog, sandbox, getting-started guide, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Vettly Plans Pricing
  plan_count: 3
  slug: vettly-plans-pricing
- name: Vettly Price Estimates
  plan_count: 0
  slug: vettly-price-estimates
random_paper: 8
rate_limits:
- limit_count: 0
  name: Vettly Rate Limits
  slug: vettly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Vettly API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: vettly-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 72.4
    contract_governance: 18.2
    contract_quality: 55.5
    developer_ergonomics: 58.9
    discoverability: 71.7
    operational_transparency: 42.1
  previous_composite: 56.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vettly/vettly-2026-10-11T132925.png
security:
- kind: authentication
  name: Vettly Authentication
  slug: vettly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vettly Domain Security
  slug: vettly-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vettly Vulnerability Disclosure
  slug: vettly-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: vettly-moderate-content
  slug: vettly-moderate-content
- name: vettly-test-policy-dry-run
  slug: vettly-test-policy-dry-run
slug: vettly
tags:
- Content Moderation
- Trust and Safety
- Security
- Text Analysis
- Image Moderation
- video-moderation
- UGC
- Compliance
- agent-guardrails
- MCP
website: https://vettly.dev
---
