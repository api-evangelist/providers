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
    idempotency: documented
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
  score: 37.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.boxcompute.ai
  baseurl_source: declared
  description: Public customer contract for /api/v2.
  name: BoxCompute Customer Sandbox API
  slug: boxcompute-customer-sandbox-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/boxcompute-ai/plans/boxcompute-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boxcompute-ai-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/boxcompute-ai/cli/boxcompute-ai-cli.yml
  title: ''
  type: CLI
  url: cli/boxcompute-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/boxcompute-ai/conventions/boxcompute-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/boxcompute-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/boxcompute-ai/conventions/boxcompute-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/boxcompute-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/boxcompute-ai/authentication/boxcompute-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boxcompute-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/boxcompute-ai/conformance/boxcompute-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boxcompute-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boxcompute-ai/llms/boxcompute-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boxcompute-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/boxcompute-ai/well-known/boxcompute-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boxcompute-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/boxcompute-ai/hosts/boxcompute-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boxcompute-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/boxcompute-ai/vendors/boxcompute-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boxcompute-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/boxcompute-ai/security/boxcompute-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boxcompute-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boxcompute.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://boxcompute.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://boxcompute.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://boxcompute.ai/#use-cases
- group: commercial
  title: ''
  type: Pricing
  url: https://boxcompute.ai/#pricing
- group: company
  title: ''
  type: Blog
  url: https://boxcompute.ai/blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.boxcompute.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boxcompute.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boxcompute.ai/privacy/
created: '2026-11-02'
description: BoxCompute provides cloud computers tailored for AI agents. Users can connect Claude, Codex, Cursor, or Claude Code via MCP, build on the API, or chat with an agent. The service offers full Linux VMs in Cyberjaya, Malaysia, with live previews, a browser, and pricing starting at $5 free credit. It targets developers needing scalable AI compute resources.
image: https://boxcompute.ai/boxcompute-og-computer.png
layout: provider
modified: '2026-11-02'
name: BoxCompute
nav: Providers
network: true
overview: 'BoxCompute is listed with 1 API on the [APIs.io](https://apis.io/) network: Customer Sandbox API. Tagged areas include AI Agents, Pay-as-you-go, and Sandbox.


  BoxCompute''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Boxcompute Ai Plans Pricing
  plan_count: 3
  slug: boxcompute-ai-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 34.4
    developer_ergonomics: 34.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Boxcompute Ai Authentication
  slug: boxcompute-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Boxcompute Ai Domain Security
  slug: boxcompute-ai-domain-security
  summary_line: TLSv1.3
slug: boxcompute-ai
tags:
- AI Agents
- Pay-as-you-go
- Sandbox
website: https://boxcompute.ai/
---
