---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://governance.taskhawktech.com
  baseurl_source: declared
  description: REST gateway for runtime enforcement of autonomous agent actions. POST /governance/verify returns a signed ALLOW/CONSTRAIN/DENY decision with a release token; /governance/attest appends a hash-chained
  name: Kevros Governance API
  slug: kevros-governance-api
- description: Hosted Streamable HTTP MCP server (protocol 2025-03-26, FastMCP, server version 0.4.1) at https://governance.taskhawktech.com/mcp/ exposing 9 tools (verify, attest, bind, verify-outcome, bundle, healt
  name: Kevros MCP Server
  slug: kevros-mcp-server
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://taskhawktech.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/security/taskhawktech-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/taskhawktech-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/security/taskhawktech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taskhawktech-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/authentication/taskhawktech-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/taskhawktech-com-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://governance.taskhawktech.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://governance.taskhawktech.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://governance.taskhawktech.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://governance.taskhawktech.com/for-agents.txt
- group: operate
  title: ''
  type: Support
  url: https://taskhawktech.com/legal/support
- group: commercial
  title: ''
  type: Pricing
  url: https://taskhawktech.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://governance.taskhawktech.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taskhawktech.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taskhawktech.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://governance.taskhawktech.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://taskhawktech.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taskhawk-systems
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/llms/taskhawktech-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/taskhawktech-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://taskhawktech.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/mcp/taskhawktech-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/taskhawktech-com-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/a2a/taskhawktech-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/taskhawktech-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/well-known/taskhawktech-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/taskhawktech-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/well-known/taskhawktech-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/taskhawktech-com-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/packages/taskhawktech-com-packages.yml
  title: ''
  type: Packages
  url: packages/taskhawktech-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/packages/taskhawktech-com-packages.yml
  title: ''
  type: SDKs
  url: packages/taskhawktech-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/conformance/taskhawktech-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/taskhawktech-com-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/conformance/taskhawktech-com-conformance.yml
  title: ''
  type: Compliance
  url: conformance/taskhawktech-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/errors/taskhawktech-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/taskhawktech-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/lifecycle/taskhawktech-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/taskhawktech-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/scopes/taskhawktech-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/taskhawktech-com-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/conventions/taskhawktech-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/taskhawktech-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/conventions/taskhawktech-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/taskhawktech-com-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/changelog/taskhawktech-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/taskhawktech-com-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/data-model/taskhawktech-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/taskhawktech-com-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/plans/taskhawktech-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/taskhawktech-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/rate-limits/taskhawktech-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/taskhawktech-com-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/security/taskhawktech-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/taskhawktech-com-vulnerability-disclosure.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://taskhawktech.com/legal/privacy
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/mcp/taskhawktech-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/taskhawktech-com-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/overlays/taskhawktech-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/taskhawktech-com-openapi-overlay.yaml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/taskhawktech-com/refs/heads/main/openapi/taskhawktech-com-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/taskhawktech-com-openapi.yml
created: '2026-09-19'
description: 'TaskHawk Systems, LLC (Charlottesville, Virginia) builds operational verification infrastructure for autonomous AI and software systems. Its commercial product, Kevros, is a verified release and evidence gateway: before an agent spends, deploys, sends or actuates, it POSTs the proposed action to the Kevros Governance API and receives a signed ALLOW, CONSTRAIN or DENY decision with a release token, recorded in a hash-chained, post-quantum-signed provenance ledger. The gateway at governance.taskhawktech.com publishes an OpenAPI 3.1 contract (23 operations: verify, attest, bind, verify-outcome, bundle, prompt-injection shield scan, media hash attestation, MPP payment sessions), a hosted Streamable HTTP MCP server with 9 tools, an A2A agent card, RFC 8414 authorization-server metadata, and per-call machine payment discovery over x402 (USDC on Base), L402 (Lightning) and MPP (Stripe) rails with a 1,000-call trial allowance via POST /signup.'
image: https://taskhawktech.com/assets/brand/wordmark-light.svg
layout: provider
mcp_servers:
- description: ''
  name: TaskHawk Systems MCP Server
  slug: taskhawk-systems-mcp-server
- description: ''
  name: TaskHawk Systems MCP Server
  slug: taskhawk-systems-mcp-server-2
modified: '2026-09-19'
name: TaskHawk Systems
nav: Providers
network: true
overview: 'TaskHawk Systems publishes 1 API on the [APIs.io](https://apis.io/) network: Kevros Governance API. Tagged areas include AI Governance, Agent Security, Runtime Enforcement, Policy Enforcement, and Provenance.


  TaskHawk Systems'' developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Taskhawktech Com Plans Pricing
  plan_count: 4
  slug: taskhawktech-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Taskhawktech Com Rate Limits
  slug: taskhawktech-com-rate-limits
scopes:
- name: Taskhawktech Com Scopes
  scope_count: 0
  slug: taskhawktech-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 75.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 57.4
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 78.9
  previous_composite: 75.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 85.2
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Taskhawktech Com Authentication
  slug: taskhawktech-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Taskhawktech Com Domain Security
  slug: taskhawktech-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Taskhawktech Com Vulnerability Disclosure
  slug: taskhawktech-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: taskhawktech-com
tags:
- AI Governance
- Agent Security
- Runtime Enforcement
- Policy Enforcement
- Provenance
- Compliance
- Prompt Injection Detection
- Media Attestation
- Post-Quantum Cryptography
- Formal Verification
- x402
- L402
- Machine Payments
- MCP
- A2A
- agent-native
- Government
- Defense
website: https://taskhawktech.com/
---
