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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://infer.flow7.org/v1
  baseurl_source: declared
  description: Model selectors, published prices, and route capability metadata.
  name: Infer by Flow7 Catalog API
  slug: infer-by-flow7-catalog-api
- baseURL: https://infer.flow7.org/v1
  baseurl_source: declared
  description: Authenticated customer inference operations.
  name: Infer by Flow7 Inference API
  slug: infer-by-flow7-inference-api
- baseURL: https://infer.flow7.org/v1
  baseurl_source: declared
  description: Customer-facing service state without private routing topology.
  name: Infer by Flow7 Status API
  slug: infer-by-flow7-status-api
artifact_total: 11
collections:
- collection_type: open
  name: Infer by Flow7 Public API
  slug: open-infer-by-flow7-public-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: https://infer.flow7.org/.well-known/agent-skills/index.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/infer-by-flow7-public-api-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/infer-by-flow7-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infer-by-flow7-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://infer.flow7.org/
- group: docs
  title: ''
  type: Documentation
  url: https://infer.flow7.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://infer.flow7.org/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://infer.flow7.org/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://infer.flow7.org/support
- group: company
  title: ''
  type: BlogRSS
  url: https://infer.flow7.org/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://infer.flow7.org/models
- group: start
  title: ''
  type: SignUp
  url: https://infer.flow7.org/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infer.flow7.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infer.flow7.org/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://infer.flow7.org/status
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/infer-by-flow7-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/infer-by-flow7-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://infer.flow7.org/.well-known/api-catalog
- group: other
  title: ''
  type: APIsJSON
  url: https://infer.flow7.org/.well-known/apis.json
- group: auth
  title: ''
  type: Security
  url: security/infer-by-flow7-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infer-by-flow7-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/infer-by-flow7-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/infer-by-flow7-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infer-by-flow7-changelog.yml
created: '2026-08-11'
description: 'A single Responses-compatible inference API that fronts multiple model families through a private, opaque supplier pool. Public paid beta offering a prepaid-wallet billing model, locked prices, spending limits, and per-call receipts for accountable coding-agent inference. Four operations — two of them unauthenticated — cover a machine-readable price catalog, per-model route status with p95 latency, an authenticated selector list, and the Responses endpoint itself. Distinguished by an unusually legible commercial surface: the full rate card, including per-tier margin floors and dated market-reference discounts, is served as JSON without a key, and every completed request returns a receipt with the locked price version and the exact charge.'
image: https://infer.flow7.org/assets/og-infer.png?v=20260811
layout: provider
modified: '2026-08-11'
name: Infer by Flow7
nav: Providers
network: true
overview: 'Infer by Flow7 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API, Inference API, and Status API. Tagged areas include AI/ML inference, LLM API gateway, Responses-compatible API, Coding-agent tooling, and Developer Tools.


  Infer by Flow7''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 18 more developer resources.'
plans:
- name: Infer By Flow7 Plans Pricing
  plan_count: 4
  slug: infer-by-flow7-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Infer By Flow7 Rate Limits
  slug: infer-by-flow7-rate-limits
scopes:
- name: Infer By Flow7 Scopes
  scope_count: 0
  slug: infer-by-flow7-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 46.0
    catalog_earned_first_party: 12.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 60.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infer-by-flow7/refs/heads/main/screenshots/infer-by-flow7-2026-08-17T080956.png
security:
- kind: authentication
  name: Infer By Flow7 Authentication
  slug: infer-by-flow7-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Infer By Flow7 Domain Security
  slug: infer-by-flow7-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Infer By Flow7 Vulnerability Disclosure
  slug: infer-by-flow7-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Infer By Flow7 Trust Center
  slug: infer-by-flow7-trust-center
  summary_line: trust center published
slug: infer-by-flow7
tags:
- AI/ML inference
- LLM API gateway
- Responses-compatible API
- Coding-agent tooling
- Developer Tools
- Usage-Based Billing
- Prepaid billing
- agent-native
- Agent Skills
- Model Routing
website: https://infer.flow7.org/
---
