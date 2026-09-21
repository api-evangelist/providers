---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 68.9
  scored_at: '2026-09-20'
api_count: 3
apis:
- baseURL: https://tooloracle.io
  baseurl_source: declared
  description: 'The provider''s root OpenAPI 3.0.0 contract (version 4.2.0): a discovery index of forty hosted MCP endpoints (POST /<oracle>/mcp/), nineteen x402-priced /v2 REST routes (agent preflight, MiCA stablecoi'
  name: ToolOracle MCP Platform API
  slug: tooloracle-mcp-platform-api
- baseURL: https://tooloracle.io
  baseurl_source: declared
  description: 'Account-less pay-per-call REST API (OpenAPI 3.1.0 with schemas and examples on every operation): agent action preflight, MiCA stablecoin compliance, AML/sanctions screening, CVE lookup, UVO claim and '
  name: ToolOracle x402 v2 Compliance, Evidence & Agent-Safety API
  slug: tooloracle-x402-v2-api
- description: 'The hosted MCP mesh: ninety-two endpoints under tooloracle.io (plus five on feedoracle.io / mcp.feedoracle.io) answered an anonymous tools/list on 2026-09-19/20 with 1,178 tool entries and 919 unique '
  name: OracleNet MCP Servers
  slug: oraclenet-mcp-servers
- description: A2A 0.3 JSON-RPC agent at https://tooloracle.io/a2a/jsonrpc (message/send, tasks/*, push-notification configs, authenticated extended card) fronting ten category-level skills that route to the MCP mes
  name: OracleNet A2A Agent
  slug: oraclenet-a2a-agent
- baseURL: https://api.feedoracle.io
  baseurl_source: declared
  description: 'The sibling brand''s REST contract (OpenAPI 3.1.0, version 8.4.1, 227 paths at https://api.feedoracle.io): DORA, MiCA, AMLR and CSRD compliance evidence, macro data, carbon and L2 feeds, attestation ve'
  name: FeedOracle Compliance Evidence API
  slug: feedoracle-compliance-evidence-api
artifact_total: 15
asyncapis:
- description: ''
  name: Tooloracle Io Webhooks
  slug: tooloracle-io-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/security/tooloracle-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tooloracle-io-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/security/tooloracle-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tooloracle-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tooloracle.io/
- group: company
  title: ''
  type: Website
  url: https://feedoracle.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tooloracle.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://tooloracle.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://tooloracle.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://tooloracle.io/docs/mcp-auth.html
- group: operate
  title: ''
  type: Support
  url: https://feedoracle.io/contact.html
- group: company
  title: ''
  type: Blog
  url: https://tooloracle.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ToolOracle
- group: commercial
  title: ''
  type: Pricing
  url: https://tooloracle.io/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://feedoracle.io/console/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tooloracle.io/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tooloracle.io/datenschutz.html
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.feedoracle.io/status/feedoracle
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/llms/tooloracle-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tooloracle-io-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://tooloracle.io/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/mcp/tooloracle-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tooloracle-io-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/mcp/tooloracle-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tooloracle-io-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/a2a/tooloracle-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tooloracle-io-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/well-known/tooloracle-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tooloracle-io-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/well-known/tooloracle-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tooloracle-io-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/well-known/tooloracle-io-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/tooloracle-io-api-catalog.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/authentication/tooloracle-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tooloracle-io-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/scopes/tooloracle-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tooloracle-io-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/conformance/tooloracle-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tooloracle-io-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/errors/tooloracle-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tooloracle-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/lifecycle/tooloracle-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tooloracle-io-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/changelog/tooloracle-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tooloracle-io-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/conventions/tooloracle-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tooloracle-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/conventions/tooloracle-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tooloracle-io-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/rate-limits/tooloracle-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tooloracle-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/plans/tooloracle-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tooloracle-io-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/sandbox/tooloracle-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tooloracle-io-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/data-model/tooloracle-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tooloracle-io-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/asyncapi/tooloracle-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tooloracle-io-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://tooloracle.io/responsible-disclosure
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://tooloracle.io/datenschutz.html
- group: other
  title: ''
  type: Subprocessors
  url: https://feedoracle.io/assets/dpa-feedoracle.html
- group: other
  title: ''
  type: DataResidency
  url: https://tooloracle.io/datenschutz.html
- group: operate
  title: ''
  type: IncidentNotification
  url: https://feedoracle.io/assets/dpa-feedoracle.html
- group: other
  title: ''
  type: AITransparency
  url: https://tooloracle.io/terms.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/regulatory/tooloracle-io-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/tooloracle-io-regulatory-posture.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tooloracle-io/refs/heads/main/packages/tooloracle-io-packages.yml
  title: ''
  type: Packages
  url: packages/tooloracle-io-packages.yml
created: '2026-09-19'
description: FeedOracle Technologies (Herford, Germany) operates two agent-facing brands on one shared OAuth 2.1 identity layer. ToolOracle / OracleNet at tooloracle.io is a capability router and hosted mesh of about ninety Model Context Protocol servers for autonomous agents (1,178 tool entries across blockchain intelligence, EU regulatory compliance, finance, business intelligence, travel and agent trust), reachable over MCP Streamable HTTP, an A2A 0.3 agent with a published Agent Card, a free ANP soft-handshake router, and x402 v2 pay-per-call settlement in USDC on Base for eighteen priced /v2 compliance and agent-safety REST routes. FeedOracle at feedoracle.io is the sibling compliance-evidence API (227-path OpenAPI 3.1 at api.feedoracle.io, ES256K-signed responses) and hosts the RFC 8414 / RFC 7591 authorization server both brands use.
image: https://tooloracle.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: FeedOracle Technologies MCP Server
  slug: feedoracle-technologies-mcp-server
- description: ''
  name: main endpoint (Streamable HTTP)
  slug: main-endpoint-streamable-http
- description: ''
  name: OracleNet mesh front door (quantum)
  slug: oraclenet-mesh-front-door-quantum
modified: '2026-09-19'
name: FeedOracle Technologies
nav: Providers
network: true
overview: 'FeedOracle Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network: ToolOracle MCP Platform API, ToolOracle x402 v2 Compliance, Evidence & Agent-Safety API, and FeedOracle Compliance Evidence API. Tagged areas include Company, MCP, Agent Infrastructure, A2A, and x402.


  The FeedOracle Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FeedOracle Technologies'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
plans:
- name: Tooloracle Io Plans Pricing
  plan_count: 9
  slug: tooloracle-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 8
  name: Tooloracle Io Rate Limits
  slug: tooloracle-io-rate-limits
scopes:
- name: Tooloracle Io Scopes
  scope_count: 8
  slug: tooloracle-io-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: strong
  composite: 65.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 62.5
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 59.4
    developer_ergonomics: 71.4
    discoverability: 81.5
    operational_transparency: 86.8
  previous_composite: 2.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Tooloracle Io Authentication
  slug: tooloracle-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tooloracle Io Domain Security
  slug: tooloracle-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tooloracle Io Vulnerability Disclosure
  slug: tooloracle-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tooloracle-io
tags:
- Company
- MCP
- Agent Infrastructure
- A2A
- x402
- Micropayments
- Compliance
- RegTech
- Blockchain
- Sanctions Screening
- Agent Discovery
- Germany
website: https://tooloracle.io/
---
