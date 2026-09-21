---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: 'Resource-oriented REST API to manage integrations, providers, sessions, portals, skills, identities and MCP access programmatically. Bearer API-key auth, cursor pagination, date-based versioning; 466 '
  name: Metorial API
  slug: metorial-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.metorial.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/security/metorial-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/metorial-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://metorial.com/security
- group: auth
  title: ''
  type: SecurityCenter
  url: https://metorial.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/security/metorial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metorial-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.metorial.com
- group: docs
  title: ''
  type: Documentation
  url: https://metorial.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://metorial.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://metorial.com/docs/api-getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://metorial.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.metorial.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metorial
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metorial.com
- group: company
  title: ''
  type: Blog
  url: https://metorial.com/blog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/llms/metorial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metorial-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/packages/metorial-packages.yml
  title: ''
  type: Packages
  url: packages/metorial-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/packages/metorial-packages.yml
  title: ''
  type: SDKs
  url: packages/metorial-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/cli/metorial-cli.yml
  title: ''
  type: CLI
  url: cli/metorial-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/mcp/metorial-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/metorial-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/authentication/metorial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/metorial-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/conventions/metorial-conventions.yml
  title: ''
  type: Conventions
  url: conventions/metorial-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/errors/metorial-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/metorial-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/lifecycle/metorial-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/metorial-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/lifecycle/metorial-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/metorial-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/rate-limits/metorial-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/metorial-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/conformance/metorial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metorial-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/data-model/metorial-data-model.yml
  title: ''
  type: DataModel
  url: data-model/metorial-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/sandbox/metorial-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/metorial-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/well-known/metorial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/metorial-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/well-known/metorial-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/metorial-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Metorial is agentic infrastructure for AI-native companies — "the Vercel for MCP." It hosts 1,200+ Model Context Protocol (MCP) servers serverlessly, giving AI agents and clients like Claude, ChatGPT, Cursor, Copilot and Codex one place to connect approved apps, tools and shared skills. Its hibernation technology makes every MCP server serverless (sub-second cold starts, pay-per-request), and it handles production OAuth, per-user isolation, tracing, access control (SSO/SAML) and ProtoGuard request safety. Developers integrate through a resource-oriented REST API (api.metorial.com) with official Node.js, Python and Go SDKs, a CLI, and standard MCP URLs. Founded 2025, San Francisco; backed by Y Combinator (F25).
image: https://metorial.com/logo/logo.svg
layout: provider
modified: '2026-07-20'
name: Metorial
nav: Providers
network: true
overview: 'Metorial publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, AI Agents, Agentic Infrastructure, and Integration.


  Metorial''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, CLI, and 24 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 3
  name: Metorial Rate Limits
  slug: metorial-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 50.0
  previous_composite: 34.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/screenshots/metorial-2026-08-07T172725.png
security:
- kind: authentication
  name: Metorial Authentication
  slug: metorial-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Metorial Domain Security
  slug: metorial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Metorial Trust Center
  slug: metorial-trust-center
  summary_line: SOC 2, GDPR
slug: metorial
tags:
- Company
- MCP
- AI Agents
- Agentic Infrastructure
- Integration
- Developer Tools
- Serverless
website: https://www.metorial.com/
---
