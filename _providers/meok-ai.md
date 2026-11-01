---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: OpenAI-compatible chat completions endpoint hosted on Hugging Face Space, providing a free overlay model.
  name: Overlay API
  slug: overlay-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Security
  url: https://meok.ai/verify.html
- group: design
  href: https://artifacts.apis.io/meok-ai/lifecycle/meok-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/meok-ai-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/meok-ai/llms/meok-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meok-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/meok-ai/a2a/meok-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/meok-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/meok-ai/well-known/meok-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/meok-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/meok-ai/well-known/meok-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meok-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/meok-ai/hosts/meok-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meok-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/meok-ai/vendors/meok-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meok-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/meok-ai/packages/meok-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/meok-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/meok-ai/packages/meok-ai-packages.yml
  title: ''
  type: Packages
  url: packages/meok-ai-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://meok.ai/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://meok.ai/pricing
- group: auth
  href: https://artifacts.apis.io/meok-ai/security/meok-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/meok-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/meok-ai/security/meok-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meok-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meok.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://meok.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://meok.ai/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meok.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meok.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://meok.ai/docs#status
coverage:
  checked: '2026-10-29'
  detail: Provider docs list the OpenAI-compatible overlay endpoint but no machine-readable OpenAPI or other contract is published.
  evidence:
  - status: 200
    url: https://meok.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: MEOK is a public‑source conversational workspace powered by the Council of AI. It lets users ask questions that are answered using publicly available evidence without any private AI inference. The platform records the evidence, provides a brief summary, and allows reopening later. MEOK is a product of CSOAI Ltd, offering transparent, source‑backed interactions.
image: https://meok.ai/favicon.svg
layout: provider
modified: '2026-10-29'
name: meok-ai
nav: Providers
network: true
overview: 'meok-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Conversation, PublicEvidence, Workspace, and CSOAI.


  meok-ai''s developer surface includes sandbox, pricing, documentation, API reference, and 16 more developer resources.'
plans:
- name: Meok Ai Plans Pricing
  plan_count: 0
  slug: meok-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Meok Ai Rate Limits
  slug: meok-ai-rate-limits
scopes:
- name: Meok Ai Scopes
  scope_count: 0
  slug: meok-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Meok Ai Authentication
  slug: meok-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Meok Ai Domain Security
  slug: meok-ai-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Meok Ai Vulnerability Disclosure
  slug: meok-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meok-ai
tags:
- AI
- Conversation
- PublicEvidence
- Workspace
- CSOAI
website: https://meok.ai/
---
