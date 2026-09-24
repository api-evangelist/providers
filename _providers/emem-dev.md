---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.5
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://emem.dev
  baseurl_source: declared
  description: 'The /v1 REST surface of the emem responder: locate a place to a cell64, recall signed facts, ask free-text questions routed over an algorithm registry, mint and resolve emem: citation tokens, verify r'
  name: emem REST API
  slug: emem-rest-api
- description: 'Remote MCP server (JSON-RPC 2.0 over Streamable HTTP) at https://emem.dev/mcp exposing 110 tools; /mcp lists an 18-tool core loop and /mcp/full the complete set. No authentication to read; every tool '
  name: emem MCP Server
  slug: emem-mcp-server
- description: 'Agent-to-agent surface: synchronous JSON-RPC message/send at POST /a2a/tasks, an async task extension at /v1/a2a/tasks with polling and cancel, and a skill query at /v1/a2a/skills. Every MCP tool is p'
  name: emem A2A Agent
  slug: emem-a2a-agent
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://emem.dev/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/security/emem-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/emem-dev-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/security/emem-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/emem-dev-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/security/emem-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emem-dev-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/authentication/emem-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emem-dev-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vortx.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://emem.dev/reference
- group: docs
  title: ''
  type: Documentation
  url: https://emem.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://emem.dev/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://emem.dev/docs/quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://emem.dev/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vortx-AI
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Vortx-AI/emem
- group: operate
  title: ''
  type: Roadmap
  url: https://emem.dev/docs/roadmap.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emem.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emem.dev/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Vortx-AI/emem/blob/main/CHANGELOG.md
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/changelog/emem-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/emem-dev-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/llms/emem-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emem-dev-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/a2a/emem-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/emem-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/well-known/emem-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/emem-dev-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/well-known/emem-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/emem-dev-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/well-known/emem-dev-oauth-authorization-server.json
  title: ''
  type: OpenIDConnect
  url: well-known/emem-dev-oauth-authorization-server.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/packages/emem-dev-packages.yml
  title: ''
  type: Packages
  url: packages/emem-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/packages/emem-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/emem-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/cli/emem-dev-cli.yml
  title: ''
  type: CLI
  url: cli/emem-dev-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/conformance/emem-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/emem-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/lifecycle/emem-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/emem-dev-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/lifecycle/emem-dev-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/emem-dev-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/conventions/emem-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/emem-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/conventions/emem-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/emem-dev-conventions.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/plans/emem-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/emem-dev-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/rate-limits/emem-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/emem-dev-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/regulatory/emem-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/emem-dev-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/regulatory/emem-dev-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/emem-dev-regulatory-posture.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/regulatory/emem-dev-regulatory-posture.yml
  title: ''
  type: SupportLifetime
  url: regulatory/emem-dev-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/emem-dev/refs/heads/main/regulatory/emem-dev-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/emem-dev-regulatory-posture.yml
created: '2026-09-19'
description: Vortx AI Private Limited is a spatial AI lab based in India that builds and operates emem (emem.dev), an Apache-2.0 protocol and hosted responder providing shared, verifiable memory for AI agents. Every place on Earth has one 64-bit address (cell64), every observation is an ed25519-signed, content-addressed fact materialised from satellite and open Earth-observation archives, and any agent can read without a key or account and verify the receipt offline. The surface is published as an OpenAPI 3.1 contract (196 operations), a remote MCP server (110 tools), an A2A 1.0 agent card, an llms.txt, RFC 8414 / RFC 9728 discovery documents, and first-party Python and TypeScript clients.
image: https://emem.dev/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Vortx AI Private Limited MCP Server
  slug: vortx-ai-private-limited-mcp-server
modified: '2026-09-19'
name: Vortx AI Private Limited
nav: Providers
network: true
overview: 'Vortx AI Private Limited publishes 1 API on the [APIs.io](https://apis.io/) network: emem REST API. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Memory, and Geospatial.


  Vortx AI Private Limited''s developer surface includes authentication, documentation, API reference, getting-started guide, support, GitHub presence, changelog, and 31 more developer resources.'
plans:
- name: Emem Dev Plans Pricing
  plan_count: 2
  slug: emem-dev-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Emem Dev Rate Limits
  slug: emem-dev-rate-limits
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 76.2
    discoverability: 75.9
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 49.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Emem Dev Authentication
  slug: emem-dev-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Emem Dev Domain Security
  slug: emem-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Emem Dev Vulnerability Disclosure
  slug: emem-dev-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: emem-dev
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Memory
- Geospatial
- Earth Observation
- Satellite Imagery
- Provenance
- Cryptography
- MCP
- Open Source
- India
- A2A
website: https://emem.dev/
---
