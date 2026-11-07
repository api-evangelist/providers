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
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Chat completions endpoint for building AI agents.
  name: Builder API
  slug: builder-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/chipp-ai/rate-limits/chipp-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chipp-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chipp-ai/plans/chipp-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chipp-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://chipp.ai/security
- group: auth
  href: https://artifacts.apis.io/chipp-ai/authentication/chipp-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chipp-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/chipp-ai/errors/chipp-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chipp-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/chipp-ai/llms/chipp-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chipp-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/chipp-ai/well-known/chipp-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chipp-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/chipp-ai/hosts/chipp-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chipp-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/chipp-ai/vendors/chipp-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chipp-ai-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://chipp.ai/ai/glossary/webhook
- group: auth
  title: ''
  type: Security
  url: https://chipp.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://chipp.ai/media
- group: other
  title: ''
  type: Leadership
  url: https://chipp.ai/team/scott-meyer
- group: operate
  title: ''
  type: ChangeLog
  url: https://chipp.ai/docs/api/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://chipp.ai/docs/guides/alchemist-getting-started
- group: auth
  href: https://artifacts.apis.io/chipp-ai/security/chipp-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chipp-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/chipp-ai/security/chipp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chipp-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chipp.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chipp.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://chipp.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://chipp.ai/docs/api/reference
- group: operate
  title: ''
  type: Support
  url: https://chipp.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://chipp.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chipp-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://chipp.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://build.chipp.ai/#/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chipp.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chipp.ai/privacy
- group: company
  title: ''
  type: Website
  url: https://chipp.ai/
coverage:
  checked: '2026-10-30'
  detail: OpenAPI spec at https://build.chipp.ai/api/v1/openapi.json returns 401 Unauthorized, requiring authentication.
  evidence:
  - status: 401
    url: https://build.chipp.ai/api/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Chipp is a platform that builds AI agents and custom software to automate busywork for businesses. It offers a no‑code builder and a set of APIs that let developers programmatically create, manage, and retrieve AI‑driven workflows. The service includes HIPAA and SOC 2 compliance, enterprise‑grade security, and a marketplace of templates. Founded in 2023 and based in Fargo, ND, Chipp targets enterprises seeking to offload repetitive tasks to autonomous agents. The platform provides a Builder API, an Agentic Commerce Protocol, and extensive documentation for developers.
image: https://chipp.ai/assets/icons/chipp-logo.svg
layout: provider
modified: '2026-10-29'
name: chipp-ai
nav: Providers
network: true
overview: 'chipp-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Software-as-a-Service, and HIPAA.


  chipp-ai''s developer surface includes authentication, changelog, getting-started guide, documentation, API reference, support, engineering blog, and 22 more developer resources.'
plans:
- name: Chipp Ai Plans Pricing
  plan_count: 3
  slug: chipp-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Chipp Ai Rate Limits
  slug: chipp-ai-rate-limits
scopes:
- name: Chipp Ai Scopes
  scope_count: 0
  slug: chipp-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.4
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 75.0
    operational_transparency: 40.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chipp-ai/chipp-ai-2026-11-03T124051.png
security:
- kind: authentication
  name: Chipp Ai Authentication
  slug: chipp-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chipp Ai Domain Security
  slug: chipp-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Chipp Ai Trust Center
  slug: chipp-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: chipp-ai
tags:
- Company
- Artificial Intelligence
- Automation
- Software-as-a-Service
- HIPAA
- SOC 2
website: https://chipp.ai/
---
