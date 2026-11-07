---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arketo provides a web‑based service that visualizes AI‑built application architecture.
  name: Arketo API
  slug: arketo-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/arketo-ai/plans/arketo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arketo-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/arketo-ai/security/arketo-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arketo-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arketo-ai/authentication/arketo-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arketo-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/arketo-ai/llms/arketo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arketo-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/arketo-ai/well-known/arketo-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arketo-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/arketo-ai/well-known/arketo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arketo-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/arketo-ai/hosts/arketo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arketo-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/arketo-ai/security/arketo-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arketo-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arketo-ai/security/arketo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arketo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arketo.ai/
- group: company
  title: ''
  type: Blog
  url: https://arketo.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://arketo.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://arketo.ai/signup
- group: start
  title: ''
  type: Login
  url: https://arketo.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arketo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arketo.ai/privacy
coverage:
  checked: '2026-11-02'
  detail: The provider's website offers documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://arketo.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Arketo is a web‑based developer application that connects AI assistants such as Claude, Code, Cursor, and others to automatically draw your app’s architecture live, flag potential breakages, and generate detailed reports. It helps prompt‑built applications visualize hidden architecture, identify bottlenecks, missing authentication checks, and single points of failure, enabling faster, more reliable releases. Free scans are available, with paid plans starting at $7 per month.
image: https://arketo.ai/images/logo.png
layout: provider
modified: '2026-11-01'
name: Arketo
nav: Providers
network: true
overview: 'Arketo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Architecture, Developer Tools, LLM, and Software Engineering.


  Arketo''s developer surface includes authentication, engineering blog, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Arketo Ai Plans Pricing
  plan_count: 1
  slug: arketo-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Arketo Ai Rate Limits
  slug: arketo-ai-rate-limits
scopes:
- name: Arketo Ai Scopes
  scope_count: 0
  slug: arketo-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 25.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arketo Ai Authentication
  slug: arketo-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arketo Ai Domain Security
  slug: arketo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arketo Ai Vulnerability Disclosure
  slug: arketo-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arketo-ai
tags:
- Artificial Intelligence
- Architecture
- Developer Tools
- LLM
- Software Engineering
website: https://arketo.ai/
---
