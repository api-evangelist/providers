---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Paidsync Ai Agentic Access
  operation_count: 5
  slug: paidsync-ai-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://paidsync.ai
  baseurl_source: declared
  description: The Billing API from paidsync-ai — 1 operation(s) for billing.
  name: paidsync-ai Billing API
  slug: paidsync-ai-billing-api
- baseURL: https://paidsync.ai
  baseurl_source: declared
  description: The Mcp API from paidsync-ai — 1 operation(s) for mcp.
  name: paidsync-ai MCP API
  slug: paidsync-ai-mcp-api
- baseURL: https://paidsync.ai
  baseurl_source: declared
  description: The PaidSync API API from paidsync-ai — 1 operation(s) for paidsync api.
  name: paidsync-ai PaidSync API
  slug: paidsync-ai-paidsync-api-api
- baseURL: https://paidsync.ai
  baseurl_source: declared
  description: The Payment API from paidsync-ai — 1 operation(s) for payment.
  name: paidsync-ai Payment API
  slug: paidsync-ai-payment-api
- baseURL: https://paidsync.ai
  baseurl_source: declared
  description: The Subscribe API from paidsync-ai — 1 operation(s) for subscribe.
  name: paidsync-ai Subscribe API
  slug: paidsync-ai-subscribe-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/paidsync-ai/agentic-access/paidsync-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paidsync-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/paidsync-ai/plans/paidsync-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/paidsync-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/paidsync-ai/rules/paidsync-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/paidsync-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/paidsync-ai/errors/paidsync-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paidsync-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/paidsync-ai/conformance/paidsync-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paidsync-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/paidsync-ai/llms/paidsync-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paidsync-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/paidsync-ai/a2a/paidsync-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/paidsync-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/paidsync-ai/well-known/paidsync-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/paidsync-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/paidsync-ai/well-known/paidsync-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/paidsync-ai-app-security.txt
- group: agent
  href: https://artifacts.apis.io/paidsync-ai/well-known/paidsync-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paidsync-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/paidsync-ai/hosts/paidsync-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paidsync-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/paidsync-ai/vendors/paidsync-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paidsync-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://paidsync.ai/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paidsync.ai/terms
- group: auth
  title: ''
  type: Security
  url: https://paidsync.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paidsync.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://paidsync.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://paidsync.ai/press
- group: start
  title: ''
  type: Login
  url: https://paidsync.ai/signin
- group: docs
  title: ''
  type: Documentation
  url: https://paidsync.ai/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://paidsync.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://paidsync.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://paidsync.ai/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/paidsync-ai/scopes/paidsync-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/paidsync-ai-scopes.yml
- group: auth
  href: https://artifacts.apis.io/paidsync-ai/authentication/paidsync-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paidsync-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/paidsync-ai/security/paidsync-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/paidsync-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/paidsync-ai/security/paidsync-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paidsync-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paidsync.ai/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://paidsync.ai/openapi.json
  - status: null
    url: https://app.paidsync.ai/openapi.json
  - status: 401
    url: https://paidsync.ai/mcp
  - status: 401
    url: https://api.paidsync.ai/mcp
  - status: 200
    url: https://paidsync.ai/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: PaidSync.ai provides an AI‑driven automation platform that manages and optimizes advertising campaigns across major ad networks such as Google, Meta, LinkedIn, and TikTok. By integrating large language models like Claude, ChatGPT, Gemini, and Copilot, the service offers autonomous ad operations, real‑time performance insights, and a unified MCP (Multi‑Channel Platform) server to streamline campaign creation, monitoring, and scaling for agencies and enterprises. The platform emphasizes AI‑enhanced decision making, cross‑platform connectivity, and enterprise‑grade security, aiming to boost ROAS and reduce manual workload for marketers.
image: https://paidsync.ai/og-image.png
layout: provider
modified: '2026-10-30'
name: paidsync-ai
nav: Providers
network: true
overview: 'paidsync-ai publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, MCP API, PaidSync API, and 2 more. Tagged areas include Company, Artificial Intelligence, Advertising, Automation, and Marketing.


  The paidsync-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  paidsync-ai''s developer surface includes pricing, documentation, changelog, engineering blog, API reference, authentication, and 22 more developer resources.'
plans:
- name: Paidsync Ai Plans Pricing
  plan_count: 4
  slug: paidsync-ai-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: paidsync-ai API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: paidsync-ai-rules
scopes:
- name: Paidsync Ai Scopes
  scope_count: 4
  slug: paidsync-ai-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 50.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/paidsync-ai/paidsync-ai-2026-11-03T140855.png
security:
- kind: authentication
  name: Paidsync Ai Authentication
  slug: paidsync-ai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Paidsync Ai Domain Security
  slug: paidsync-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Paidsync Ai Vulnerability Disclosure
  slug: paidsync-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: paidsync-ai
tags:
- Company
- Artificial Intelligence
- Advertising
- Automation
- Marketing
website: https://paidsync.ai/
---
