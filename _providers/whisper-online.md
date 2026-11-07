---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Whisper Online Agentic Access
  operation_count: 13
  slug: whisper-online-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 1
apis:
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
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The A2a API from Whisper Security — 1 operation(s) for a2a.
  name: Whisper Security A2a API
  slug: whisper-online-a2a-api
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The Checkpoint API from Whisper Security — 4 operation(s) for checkpoint.
  name: Whisper Security Checkpoint API
  slug: whisper-online-checkpoint-api
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The Consistency API from Whisper Security — 1 operation(s) for consistency.
  name: Whisper Security Consistency API
  slug: whisper-online-consistency-api
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The Inclusion API from Whisper Security — 1 operation(s) for inclusion.
  name: Whisper Security Inclusion API
  slug: whisper-online-inclusion-api
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The Menu API from Whisper Security — 1 operation(s) for menu.
  name: Whisper Security Menu API
  slug: whisper-online-menu-api
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The Query API from Whisper Security — 1 operation(s) for query.
  name: Whisper Security Query API
  slug: whisper-online-query-api
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The Tile API from Whisper Security — 1 operation(s) for tile.
  name: Whisper Security Tile API
  slug: whisper-online-tile-api
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The Verify Identity API from Whisper Security — 1 operation(s) for verify identity.
  name: Whisper Security Verify Identity API
  slug: whisper-online-verify-identity-api
- baseURL: https://graph.whisper.online
  baseurl_source: declared
  description: The .well Known API from Whisper Security — 2 operation(s) for .well known.
  name: Whisper Security .well Known API
  slug: whisper-online-well-known-api
artifact_total: 26
common:
- group: other
  href: https://artifacts.apis.io/whisper-online/capabilities/whisper-online-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/whisper-online-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/whisper-online/overlays/whisper-online-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/whisper-online-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/whisper-online/changelog/whisper-online-changelog.yml
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
  href: https://artifacts.apis.io/whisper-online/llms/whisper-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whisper-online-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://whisper.online/llms.txt
- group: other
  href: https://artifacts.apis.io/whisper-online/a2a/whisper-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/whisper-online-a2a.yml
- group: agent
  href: https://artifacts.apis.io/whisper-online/mcp/whisper-online-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/whisper-online-mcp.yml
- group: build
  href: https://artifacts.apis.io/whisper-online/mcp/whisper-online-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/whisper-online-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/whisper-online/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://whisper.online/.well-known/skills/whisper-identity/SKILL.md
- group: agent
  href: https://artifacts.apis.io/whisper-online/well-known/whisper-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whisper-online-well-known.yml
- group: auth
  href: https://artifacts.apis.io/whisper-online/well-known/whisper-online-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/whisper-online-security.txt
- group: build
  href: https://artifacts.apis.io/whisper-online/packages/whisper-online-packages.yml
  title: ''
  type: Packages
  url: packages/whisper-online-packages.yml
- group: build
  href: https://artifacts.apis.io/whisper-online/packages/whisper-online-packages.yml
  title: ''
  type: SDKs
  url: packages/whisper-online-packages.yml
- group: build
  href: https://artifacts.apis.io/whisper-online/cli/whisper-online-cli.yml
  title: ''
  type: CLI
  url: cli/whisper-online-cli.yml
- group: design
  href: https://artifacts.apis.io/whisper-online/conformance/whisper-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whisper-online-conformance.yml
- group: design
  href: https://artifacts.apis.io/whisper-online/lifecycle/whisper-online-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/whisper-online-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/whisper-online/lifecycle/whisper-online-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/whisper-online-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/whisper-online/plans/whisper-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/whisper-online-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/whisper-online/rate-limits/whisper-online-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/whisper-online-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/whisper-online/conventions/whisper-online-conventions.yml
  title: ''
  type: Conventions
  url: conventions/whisper-online-conventions.yml
- group: start
  href: https://artifacts.apis.io/whisper-online/sandbox/whisper-online-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/whisper-online-sandbox.yml
- group: design
  href: https://artifacts.apis.io/whisper-online/data-model/whisper-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whisper-online-data-model.yml
- group: auth
  href: https://artifacts.apis.io/whisper-online/authentication/whisper-online-authentication.yml
  title: ''
  type: Authentication
  url: authentication/whisper-online-authentication.yml
- group: auth
  href: https://artifacts.apis.io/whisper-online/scopes/whisper-online-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/whisper-online-scopes.yml
- group: design
  href: https://artifacts.apis.io/whisper-online/errors/whisper-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whisper-online-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/whisper-online/security/whisper-online-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/whisper-online-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/whisper-online/security/whisper-online-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/whisper-online-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/whisper-online/security/whisper-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whisper-online-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/whisper-online/agentic-access/whisper-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/whisper-online-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/whisper-online/regulatory/whisper-online-regulatory-posture.yml
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
finops:
- has_sources: true
  method: derived
  name: Whisper Online Finops
  primary_unit: ''
  service_category: ''
  slug: whisper-online-finops
  template: true
image: https://whisper.online/logo.png
layout: provider
mcp_servers:
- description: Whisper Security ships two MCP surfaces over one graph. (1) A hosted remote server at https://mcp.whisper.security (Streamable HTTP, protocol revisions negotiated up to 2025-11-25) that advertises sev
  name: Whisper Security MCP Server
  slug: whisper-graph
modified: '2026-09-19'
name: Whisper Security
nav: Providers
network: true
overview: 'Whisper Security publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Checkpoint API, Consistency API, and 10 more. Tagged areas include Agent Identity, Agents, IPv6, DNS, and DNSSEC.


  The Whisper Security catalog on APIs.io includes 1 Spectral governance ruleset.


  Whisper Security''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, changelog, support, and 47 more developer resources.'
plans:
- name: Whisper Online Plans Pricing
  plan_count: 0
  slug: whisper-online-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Whisper Online Rate Limits
  slug: whisper-online-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Whisper Security API Rules
  rule_count: 59
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 2
  slug: whisper-online-rules
scopes:
- name: Whisper Online Scopes
  scope_count: 4
  slug: whisper-online-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 27.6
    contract_governance: 31.8
    contract_quality: 55.1
    developer_ergonomics: 76.2
    discoverability: 75.0
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 63.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/whisper-online/whisper-online-2026-10-11T194341.png
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
skill_count: 3
skills:
- name: Assess a destination before connecting to it
  slug: whisper-online-assess-before-connect
- name: Verify an agent identity keylessly and check it against the ledger
  slug: whisper-online-verify-agent-identity
- name: whisper-identity
  slug: whisper-online-whisper-identity
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
