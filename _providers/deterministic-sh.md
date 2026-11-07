---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides endpoints for validation, reports, pricing and MCP operations as documented in the API reference.
  name: Deterministic HTTP API
  slug: deterministic-http-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/deterministic-sh/plans/deterministic-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deterministic-sh-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deterministic-sh/conformance/deterministic-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deterministic-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deterministic-sh/llms/deterministic-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deterministic-sh-llms.txt
- group: auth
  href: https://artifacts.apis.io/deterministic-sh/well-known/deterministic-sh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deterministic-sh-security.txt
- group: agent
  href: https://artifacts.apis.io/deterministic-sh/well-known/deterministic-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deterministic-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/deterministic-sh/hosts/deterministic-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deterministic-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/deterministic-sh/vendors/deterministic-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deterministic-sh-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://deterministic.sh/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deterministic.sh/terms
- group: auth
  title: ''
  type: Security
  url: https://deterministic.sh/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deterministic.sh/docs/security/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://deterministic.sh/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://deterministic.sh/docs/changelog/
- group: company
  title: ''
  type: Blog
  url: https://deterministic.sh/blog
- group: start
  title: ''
  type: SignUp
  url: https://deterministic.sh/signup?ref=start
- group: start
  title: ''
  type: GettingStarted
  url: https://deterministic.sh/llms-onboard.txt
- group: auth
  href: https://artifacts.apis.io/deterministic-sh/security/deterministic-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deterministic-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deterministic-sh/security/deterministic-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deterministic-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deterministic.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://deterministic.sh/docs
coverage:
  checked: '2026-11-05'
  detail: API reference lists endpoints but no OpenAPI or other machine‑readable contract is provided.
  evidence:
  - status: 200
    url: https://deterministic.sh/docs/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Deterministic provides a physics‑based validation platform for simulation results. Users submit evidence and receive detailed receipts with per‑check verdicts, rationale, and provenance, ensuring trustworthy outcomes without model‑generated opinions. The service offers HTTP API, MCP server, CLI, and agent skills for seamless integration.
image: https://deterministic.sh/simple-gray-logo.svg
layout: provider
modified: '2026-11-05'
name: Deterministic
nav: Providers
network: true
overview: 'Deterministic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Physics, Validation, and Simulation.


  Deterministic''s developer surface includes pricing, changelog, engineering blog, signup flow, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Deterministic Sh Plans Pricing
  plan_count: 3
  slug: deterministic-sh-plans-pricing
random_paper: 4
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deterministic Sh Domain Security
  slug: deterministic-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deterministic Sh Vulnerability Disclosure
  slug: deterministic-sh-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deterministic-sh
tags:
- Company
- Physics
- Validation
- Simulation
website: https://deterministic.sh/
---
