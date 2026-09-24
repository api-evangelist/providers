---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.2
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Whisper Online Agentic Access
  operation_count: 13
  slug: whisper-online-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 5
apis:
- baseURL: https://whisper.online
  baseurl_source: declared
  description: The keyless half of the platform as an OpenAPI 3.1.0 contract (info.version 1.1.0, 13 operations, served at https://whisper.online/openapi.json and byte-identically on agents. and endpoint.whisper.onl
  name: Whisper API
  slug: whisper-api
- description: 'The documented front door for both halves of the platform: POST https://graph.whisper.online/api/query runs openCypher against WhisperGraph (41 node labels, 52 edge types; identify, assess, explain, w'
  name: WhisperGraph and Control Plane (Cypher API)
  slug: whispergraph-control-plane
- description: 'Hosted remote MCP server at https://mcp.whisper.security (Streamable HTTP, protocol revisions up to 2025-11-25) advertising seven read-only tools (query, explain_indicator, explain_schema, read_docs, '
  name: WhisperGraph MCP Server
  slug: whispergraph-mcp-server
- description: 'Agent2Agent surface: an A2A 1.0-shaped card at https://whisper.online/.well-known/agent-card.json (version 0.219.2, provider Whisper Security, JSONRPC binding, capabilities object, 37 skills — 15 keyl'
  name: Whisper A2A Agent
  slug: whisper-a2a-agent
- description: RFC 9083 Registration Data Access Protocol for agent identities (application/rdap+json, rdapConformance rdap_level_0) at https://rdap.whisper.online/ip/{address}, with /help, a per-agent /transparency
  name: Whisper RDAP and Identity Verification
  slug: whisper-rdap
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://whisper.online/
- group: docs
  title: ''
  type: Documentation
  url: https://whisper.online/docs
- group: docs
  title: ''
  type: APIReference
  url: https://whisper.online/docs/control-plane
- group: start
  title: ''
  type: GettingStarted
  url: https://whisper.online/docs/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.whisper.security
- group: start
  title: ''
  type: SignUp
  url: https://console.whisper.security/sign-up
- group: start
  title: ''
  type: Login
  url: https://console.whisper.online
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whisper-sec
- group: company
  title: ''
  type: Blog
  url: https://www.whisper.security/resources/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.whisper.security/docs/reference/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/changelog/whisper-online-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/whisper-online-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.whisper.security
- group: operate
  title: ''
  type: Support
  url: https://www.whisper.security/docs/reference/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whisper.online/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whisper.online/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/whispersecurity/
- group: other
  title: ''
  type: X
  url: https://x.com/WhisperSecTech
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Whisper-Security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/llms/whisper-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whisper-online-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://whisper.online/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/a2a/whisper-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/whisper-online-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/mcp/whisper-online-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/whisper-online-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/mcp/whisper-online-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/whisper-online-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://whisper.online/.well-known/skills/whisper-identity/SKILL.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/well-known/whisper-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whisper-online-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/well-known/whisper-online-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/whisper-online-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/packages/whisper-online-packages.yml
  title: ''
  type: Packages
  url: packages/whisper-online-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/packages/whisper-online-packages.yml
  title: ''
  type: SDKs
  url: packages/whisper-online-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/cli/whisper-online-cli.yml
  title: ''
  type: CLI
  url: cli/whisper-online-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/conformance/whisper-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whisper-online-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/lifecycle/whisper-online-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/whisper-online-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/lifecycle/whisper-online-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/whisper-online-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/plans/whisper-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/whisper-online-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/rate-limits/whisper-online-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/whisper-online-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/conventions/whisper-online-conventions.yml
  title: ''
  type: Conventions
  url: conventions/whisper-online-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/sandbox/whisper-online-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/whisper-online-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/data-model/whisper-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whisper-online-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/authentication/whisper-online-authentication.yml
  title: ''
  type: Authentication
  url: authentication/whisper-online-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/scopes/whisper-online-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/whisper-online-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/errors/whisper-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whisper-online-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/security/whisper-online-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/whisper-online-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/security/whisper-online-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/whisper-online-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/security/whisper-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whisper-online-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/agentic-access/whisper-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/whisper-online-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/whisper-online/refs/heads/main/regulatory/whisper-online-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/whisper-online-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://whisper.online/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://www.whisper.security/privacy-policy
- group: other
  title: ''
  type: DataResidency
  url: https://whisper.online/privacy
- group: operate
  title: ''
  type: IncidentNotification
  url: https://whisper.online/privacy
- group: operate
  title: ''
  type: SupportLifetime
  url: https://www.whisper.security/docs/ai/mcp/deprecation
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://www.whisper.security/privacy-policy
created: '2026-09-19'
description: Whisper Security (viaGraph B.V., Amsterdam; AS219419) gives AI agents a real, routable IPv6 /128 address as their identity — allocated from its own 2a04:2a01::/32, published in reverse DNS, RDAP/WHOIS and an RFC 6962 transparency log, and DANE-pinned in DNSSEC-signed DNS so anyone can verify an agent with dig, whois and curl and no Whisper account. One Cypher endpoint (POST /api/query) carries both the keyless WhisperGraph — an internet-infrastructure and threat-intelligence graph answering who runs a host and whether it is safe, with the evidence chain — and the keyed control plane CALL whisper.agents (register, connect, policy, logs, revoke). The same surface is published as an OpenAPI 3.1 contract, an A2A 1.0 agent card with 37 skills, a hosted OAuth MCP server, a stdio MCP server inside the MIT whisper CLI, npm/PyPI SDKs, and llms.txt.
image: https://whisper.online/logo.png
layout: provider
mcp_servers:
- description: Whisper Security ships two MCP surfaces over one graph. (1) A hosted remote server at https://mcp.whisper.security (Streamable HTTP, protocol revisions negotiated up to 2025-11-25) that advertises sev
  name: Whisper Security MCP Server
  slug: whisper-security-mcp-server
- description: ''
  name: WhisperGraph MCP endpoint (Streamable HTTP, OAuth)
  slug: whispergraph-mcp-endpoint-streamable-http-oauth
modified: '2026-09-19'
name: Whisper Security
nav: Providers
network: true
overview: 'Whisper Security publishes 1 API on the [APIs.io](https://apis.io/) network: Whisper API. Tagged areas include Agent Identity, Agents, IPv6, DNS, and DNSSEC.


  Whisper Security''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, changelog, support, and 45 more developer resources.'
plans:
- name: Whisper Online Plans Pricing
  plan_count: 0
  slug: whisper-online-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Whisper Online Rate Limits
  slug: whisper-online-rate-limits
scopes:
- name: Whisper Online Scopes
  scope_count: 4
  slug: whisper-online-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 76.2
    discoverability: 81.5
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  name: Whisper Online Authentication
  slug: whisper-online-authentication
  summary_line: apiKey/http-bearer/oauth2/network-identity · 5 schemes
- kind: domain-security
  name: Whisper Online Domain Security
  slug: whisper-online-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Whisper Online Vulnerability Disclosure
  slug: whisper-online-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: whisper-online
tags:
- Agent Identity
- Agents
- IPv6
- DNS
- DNSSEC
- Threat Intelligence
- Security
- Egress
- A2A
- MCP
- RDAP
- Transparency Log
- Graph Database
- Agent-Native
- Netherlands
website: https://whisper.online/
---
