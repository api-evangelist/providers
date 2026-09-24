---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Horizonshield Dev Agentic Access
  operation_count: 25
  slug: horizonshield-dev-agentic-access
  summary_line: 25 operations · 4 acting
api_count: 7
apis:
- description: 'Remote Model Context Protocol server at https://mcp.horizonshield.dev/ (Streamable HTTP, POST only, protocol 2025-06-18, serverInfo horizon-shield 1.0.9, listed on registry.modelcontextprotocol.io as '
  name: HORIZON SHIELD KIRA MCP Server
  slug: horizon-shield-kira-mcp-server
- description: 'Agent2Agent surface of the same service: a JWS-signed agent card at https://mcp.horizonshield.dev/.well-known/agent-card.json (protocolVersion 0.3.0 with 1.0-style supportedInterfaces, JSONRPC, versio'
  name: HORIZON SHIELD KIRA A2A Agent
  slug: horizon-shield-kira-a2a-agent
- baseURL: https://gate.horizonshield.dev
  baseurl_source: declared
  description: 'Read-only, keyless REST API at https://gate.horizonshield.dev described by an OpenAPI 3.1.0 document (25 operations, version 0.4.7): the public register of MCP endpoints measured nightly against five '
  name: MCP Verification Gate (MCP conduct register) API
  slug: mcp-verification-gate-api
- description: 'Append-only, Bitcoin-anchored (OpenTimestamps) public ledger of the verification process at https://ledger.horizonshield.dev: an index of anchored entries, per-entry raw bytes and .ots proofs, citatio'
  name: JIDEC Verification Ledger API
  slug: jidec-verification-ledger-api
- description: 'Remote MCP server at https://hearing.horizonshield.dev/mcp (serverInfo HORIZON SHIELD YAKUMO 2.3.1, protocol 2025-06-18) exposing six read-only tools over the Yakumo mall, where only contractors that '
  name: Yakumo Verified-Contractor Directory MCP
  slug: yakumo-verified-contractor-mcp
- description: A second public MCP endpoint at https://web.horizonshield.dev/mcp (serverInfo hs-webmcp 1.0.4, protocol 2025-06-18; server.json published at shield.the-horizons-innovation.com/server-webmcp.json) acti
  name: HORIZON SHIELD WebMCP Intake Server
  slug: webmcp-intake-server
- description: 'A separate product line by the same company: a neutral, verifiable registry of femtech information sources exposed as a remote MCP server at https://femtech.horizonshield.dev/mcp (hs-femtech-mcp 0.4.1'
  name: HORIZON SHIELD Femtech Source Registry MCP
  slug: femtech-source-registry-mcp
artifact_total: 20
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/security/horizonshield-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/horizonshield-dev-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/agentic-access/horizonshield-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/horizonshield-dev-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://shield.the-horizons-innovation.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/ogasurfproject-jpg/horizon-shield#readme
- group: docs
  title: ''
  type: APIReference
  url: https://gate.horizonshield.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/ogasurfproject-jpg/horizon-shield/blob/main/plugin/README.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ogasurfproject-jpg
- group: company
  title: ''
  type: Blog
  url: https://shield.the-horizons-innovation.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://shield.the-horizons-innovation.com/faq/
- group: other
  title: ''
  type: Leadership
  url: https://shield.the-horizons-innovation.com/about-founder.html
- group: commercial
  title: ''
  type: Pricing
  url: https://shield.the-horizons-innovation.com/yakumo/plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shield.the-horizons-innovation.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shield.the-horizons-innovation.com/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/llms/horizonshield-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/horizonshield-dev-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://shield.the-horizons-innovation.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/a2a/horizonshield-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/horizonshield-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/mcp/horizonshield-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/horizonshield-dev-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/mcp/horizonshield-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/horizonshield-dev-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/well-known/horizonshield-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/horizonshield-dev-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/well-known/horizonshield-dev-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/horizonshield-dev-api-catalog.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/well-known/horizonshield-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/horizonshield-dev-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/security/horizonshield-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/horizonshield-dev-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/security/horizonshield-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/horizonshield-dev-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/authentication/horizonshield-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/horizonshield-dev-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/conventions/horizonshield-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/horizonshield-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/errors/horizonshield-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/horizonshield-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/lifecycle/horizonshield-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/horizonshield-dev-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/changelog/horizonshield-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/horizonshield-dev-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/conformance/horizonshield-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/horizonshield-dev-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/packages/horizonshield-dev-packages.yml
  title: ''
  type: Packages
  url: packages/horizonshield-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/packages/horizonshield-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/horizonshield-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/cli/horizonshield-dev-cli.yml
  title: ''
  type: CLI
  url: cli/horizonshield-dev-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/skills/horizonshield-dev-horizon-shield.md
  title: ''
  type: AgentSkill
  url: skills/horizonshield-dev-horizon-shield.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/skills/horizonshield-dev-conduct-witness.md
  title: ''
  type: AgentSkill
  url: skills/horizonshield-dev-conduct-witness.md
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/plans/horizonshield-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/horizonshield-dev-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/rate-limits/horizonshield-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/horizonshield-dev-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/horizonshield-dev/refs/heads/main/data-model/horizonshield-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/horizonshield-dev-data-model.yml
- group: other
  title: ''
  type: AITransparency
  url: https://shield.the-horizons-innovation.com/index_en.html
created: '2026-09-19'
description: The HORIZ音s株式会社 (The HORIZONs Co., Ltd., Hiratsuka, Kanagawa) operates HORIZON SHIELD, a buyer-side, agent-native fair-price verification service for Japanese construction and renovation estimates, built by a 30-year master carpenter on the open JCCDB dataset (95,403 items, CC BY 4.0). Its flagship KIRA server at mcp.horizonshield.dev is a free, anonymous remote MCP server (15 tools, 5 prompts) and A2A agent that audits a quoted price against fair ranges, flags overcharge tactics, and issues SHA-256 receipts anchored to Bitcoin via OpenTimestamps; a FairPriceAttestation tool bridges to Google's AP2 Cart Mandate. Around it sit a public MCP Verification Gate (the family's one OpenAPI, plus MCP and A2A) that measures other people's MCP servers against an A2A Conduct Extension the company authors, the JIDEC append-only verification ledger with an RFC 9727 api-catalog, the Yakumo verified-contractor directory MCP, a WebMCP intake server and a femtech source registry — every card
  JWS-signed, every surface unauthenticated by design, and paid for by buyers rather than contractors.
image: https://shield.the-horizons-innovation.com/horizon_shield_logo_512.png
layout: provider
mcp_servers:
- description: ''
  name: The HORIZ音s株式会社 MCP Server
  slug: the-horiz音s株式会社-mcp-server
- description: ''
  name: KIRA MCP endpoint (Streamable HTTP, POST)
  slug: kira-mcp-endpoint-streamable-http-post
- description: ''
  name: Gate MCP endpoint (Streamable HTTP, POST)
  slug: gate-mcp-endpoint-streamable-http-post
- description: ''
  name: JIDEC read-only MCP endpoint
  slug: jidec-read-only-mcp-endpoint
- description: ''
  name: Yakumo MCP endpoint (Streamable HTTP, POST)
  slug: yakumo-mcp-endpoint-streamable-http-post
- description: ''
  name: WebMCP intake endpoint (Streamable HTTP, POST)
  slug: webmcp-intake-endpoint-streamable-http-post
- description: ''
  name: Femtech registry MCP endpoint
  slug: femtech-registry-mcp-endpoint
modified: '2026-09-19'
name: The HORIZ音s株式会社
nav: Providers
network: true
overview: 'The HORIZ音s株式会社 publishes 1 API on the [APIs.io](https://apis.io/) network: MCP Verification Gate (MCP conduct register) API. Tagged areas include Construction, Renovation, Cost Estimation, Fair Pricing, and Consumer Protection.


  The HORIZ音s株式会社''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 32 more developer resources.'
plans:
- name: Horizonshield Dev Plans Pricing
  plan_count: 7
  slug: horizonshield-dev-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Horizonshield Dev Rate Limits
  slug: horizonshield-dev-rate-limits
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 40.1
    developer_ergonomics: 69.0
    discoverability: 92.6
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 56.7
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Horizonshield Dev Authentication
  slug: horizonshield-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Horizonshield Dev Domain Security
  slug: horizonshield-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Horizonshield Dev Vulnerability Disclosure
  slug: horizonshield-dev-vulnerability-disclosure
  summary_line: Hackerone
slug: horizonshield-dev
tags:
- Construction
- Renovation
- Cost Estimation
- Fair Pricing
- Consumer Protection
- Verification
- Transparency Ledger
- Open Data
- MCP
- A2A
- AP2
- Agents
- Agent-Native
- Japan
website: https://shield.the-horizons-innovation.com/
---
