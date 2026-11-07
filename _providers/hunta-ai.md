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
  - scopes
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 4
  name: Hunta Ai Agentic Access
  operation_count: 33
  slug: hunta-ai-agentic-access
  summary_line: 33 operations · 21 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: REST API for Hunta's Attestable Memory service, hosted at mcp.hunta.ai. Uses Bearer JWT authentication; the tenant is bound to the token.
  name: Hunta API
  slug: hunta-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Admin API from hunta-ai — 7 operation(s) for admin.
  name: hunta-ai Admin API
  slug: hunta-ai-admin-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Candidates API from hunta-ai — 3 operation(s) for candidates.
  name: hunta-ai Candidates API
  slug: hunta-ai-candidates-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Errata API from hunta-ai — 2 operation(s) for errata.
  name: hunta-ai Errata API
  slug: hunta-ai-errata-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Export API from hunta-ai — 1 operation(s) for export.
  name: hunta-ai Export API
  slug: hunta-ai-export-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Facts API from hunta-ai — 5 operation(s) for facts.
  name: hunta-ai Facts API
  slug: hunta-ai-facts-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Memories API from hunta-ai — 4 operation(s) for memories.
  name: hunta-ai Memories API
  slug: hunta-ai-memories-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Metrics API from hunta-ai — 1 operation(s) for metrics.
  name: hunta-ai Metrics API
  slug: hunta-ai-metrics-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Reckon API from hunta-ai — 4 operation(s) for reckon.
  name: hunta-ai Reckon API
  slug: hunta-ai-reckon-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Reconcile API from hunta-ai — 1 operation(s) for reconcile.
  name: hunta-ai Reconcile API
  slug: hunta-ai-reconcile-api
- baseURL: https://mcp.hunta.ai
  baseurl_source: declared
  description: The Whoami API from hunta-ai — 1 operation(s) for whoami.
  name: hunta-ai Whoami API
  slug: hunta-ai-whoami-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/hunta-ai/agentic-access/hunta-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hunta-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/hunta-ai/plans/hunta-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hunta-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hunta-ai/rules/hunta-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/hunta-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/hunta-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/hunta-ai/cli/hunta-ai-cli.yml
  title: ''
  type: CLI
  url: cli/hunta-ai-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://hunta.ai/trust
- group: auth
  href: https://artifacts.apis.io/hunta-ai/authentication/hunta-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hunta-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hunta-ai/scopes/hunta-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hunta-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/hunta-ai/errors/hunta-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hunta-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hunta-ai/conformance/hunta-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hunta-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hunta-ai/llms/hunta-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hunta-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/hunta-ai/well-known/hunta-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hunta-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/hunta-ai/hosts/hunta-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hunta-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/hunta-ai/vendors/hunta-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hunta-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/hunta-ai/packages/hunta-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/hunta-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/hunta-ai/packages/hunta-ai-packages.yml
  title: ''
  type: Packages
  url: packages/hunta-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hunta.ai/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://hunta.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hunta.ai/legal/privacy
- group: auth
  href: https://artifacts.apis.io/hunta-ai/security/hunta-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hunta-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hunta-ai/security/hunta-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hunta-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hunta.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hunta.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hunta.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hunta.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://hunta.ai/get-started
- group: operate
  title: ''
  type: Support
  url: https://hunta.ai/connect
- group: company
  title: ''
  type: Blog
  url: https://hunta.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hunta-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://hunta.ai/pricing
coverage:
  checked: '2026-10-31'
  detail: The public API reference page describes the REST surface at mcp.hunta.ai but no OpenAPI or other machine‑readable specification is published.
  evidence:
  - status: 200
    url: https://docs.hunta.ai/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Hunta provides an Attestable Memory API for AI agents, enabling per‑tenant isolated agent memory over the MCP (Memory Control Protocol). The Gather service records everything an agent takes in, while the Instinct service ensures data that must never be forgotten is retained. The platform offers a free tier, supports bi‑temporal records, and provides a secure, signed isolation attestation for each memory. Documentation, API reference, pricing, and a quick start guide are available on the website. Hunta’s API is designed for developers building AI agents that need provable, auditable memory.
image: https://hunta.ai/og.png
layout: provider
modified: '2026-10-30'
name: hunta-ai
nav: Providers
network: true
overview: 'hunta-ai publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Candidates API, Errata API, and 8 more. Tagged areas include Company, Artificial Intelligence, Memory, MCP, and Attestable.


  The hunta-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  hunta-ai''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 23 more developer resources.'
plans:
- name: Hunta Ai Plans Pricing
  plan_count: 3
  slug: hunta-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Hunta Ai Rate Limits
  slug: hunta-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: hunta-ai API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: hunta-ai-rules
scopes:
- name: Hunta Ai Scopes
  scope_count: 4
  slug: hunta-ai-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 59.2
    contract_governance: 15.9
    contract_quality: 44.6
    developer_ergonomics: 55.2
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hunta-ai/hunta-ai-2026-11-03T133540.png
security:
- kind: authentication
  name: Hunta Ai Authentication
  slug: hunta-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hunta Ai Domain Security
  slug: hunta-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Hunta Ai Trust Center
  slug: hunta-ai-trust-center
  summary_line: SOC 2, ISO 27001
slug: hunta-ai
tags:
- Company
- Artificial Intelligence
- Memory
- MCP
- Attestable
website: https://hunta.ai/
---
