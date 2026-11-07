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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
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
  score: 46.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for Amdahl, an eval harness for GTM outputs. Provides Evals, Search, and Agents surfaces.
  name: Amdahl Platform API
  slug: amdahl-platform-api
- baseURL: /
  baseurl_source: declared
  description: 'REST API for Amdahl, an eval harness for GTM outputs. Three surfaces: **Evals** grades what your agents write against your own customer conversations, **Search** answers questions over the same corpus'
  name: Amdahl Platform API API
  slug: amdahl-platform-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/amdahl-ai/rules/amdahl-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/amdahl-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/amdahl-ai/vocabulary/amdahl-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amdahl-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/amdahl-ai/conformance/amdahl-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amdahl-ai-conformance.yml
- group: operate
  href: https://artifacts.apis.io/amdahl-ai/rate-limits/amdahl-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amdahl-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amdahl-ai/plans/amdahl-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amdahl-ai-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/amdahl-ai/cli/amdahl-ai-cli.yml
  title: ''
  type: CLI
  url: cli/amdahl-ai-cli.yml
- group: operate
  href: https://artifacts.apis.io/amdahl-ai/changelog/amdahl-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/amdahl-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/amdahl-ai/conventions/amdahl-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/amdahl-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/amdahl-ai/conventions/amdahl-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amdahl-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.amdahl.ai/
- group: auth
  href: https://artifacts.apis.io/amdahl-ai/authentication/amdahl-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amdahl-ai-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.amdahl.ai/versioning
- group: design
  href: https://artifacts.apis.io/amdahl-ai/lifecycle/amdahl-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amdahl-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/amdahl-ai/errors/amdahl-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amdahl-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/amdahl-ai/llms/amdahl-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amdahl-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/amdahl-ai/a2a/amdahl-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/amdahl-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/amdahl-ai/well-known/amdahl-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amdahl-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/amdahl-ai/well-known/amdahl-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amdahl-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/amdahl-ai/hosts/amdahl-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amdahl-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/amdahl-ai/vendors/amdahl-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amdahl-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://amdahl.ai/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.amdahl.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amdahl.ai/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amdahl.ai/develop/using-the-api
- group: auth
  href: https://artifacts.apis.io/amdahl-ai/security/amdahl-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amdahl-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amdahl-ai/security/amdahl-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amdahl-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amdahl-ai/security/amdahl-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amdahl-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amdahl.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amdahl.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.amdahl.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://amdahl.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://amdahl.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amdahl.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amdahl.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://amdahl.ai/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.amdahl.ai/openapi.json
  - status: null
    url: https://docs.amdahl.ai/mcp
  - status: 401
    url: https://app.amdahl.ai/mcp
  - status: 200
    url: https://amdahl.ai/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Amdahl provides AI-powered marketing automation, offering a one‑click plugin for Claude and ChatGPT that connects to its platform via a custom connector. The service includes an optimizer skill, a suite of cookbooks, and a REST API for message grading, prompt improvement, and research. Amdahl aims to help businesses generate better content, improve outreach, and streamline GTM workflows through AI assistance.
image: https://amdahl.ai/opengraph-image
layout: provider
modified: '2026-11-01'
name: Amdahl
nav: Providers
network: true
overview: 'Amdahl publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Platform API API, and 1 more. Tagged areas include Artificial Intelligence, Marketing, Automation, GPT, and Plugins.


  The Amdahl catalog on APIs.io includes 1 Spectral governance ruleset.


  Amdahl''s developer surface includes CLI, changelog, authentication, getting-started guide, API reference, documentation, pricing, and 28 more developer resources.'
plans:
- name: Amdahl Ai Plans Pricing
  plan_count: 5
  slug: amdahl-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Amdahl Ai Rate Limits
  slug: amdahl-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Amdahl API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: amdahl-ai-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 66.0
    catalog_earned_first_party: 24.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.6
  facets:
    access_clarity: 59.2
    contract_governance: 19.7
    contract_quality: 24.0
    developer_ergonomics: 41.7
    discoverability: 66.1
    operational_transparency: 48.7
  previous_composite: 54.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Amdahl Ai Authentication
  slug: amdahl-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Amdahl Ai Domain Security
  slug: amdahl-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amdahl Ai Vulnerability Disclosure
  slug: amdahl-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amdahl Ai Trust Center
  slug: amdahl-ai-trust-center
  summary_line: SOC 2, GDPR
slug: amdahl-ai
tags:
- Artificial Intelligence
- Marketing
- Automation
- GPT
- Plugins
website: https://amdahl.ai/
---
