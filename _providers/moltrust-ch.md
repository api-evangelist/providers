---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 101
  human_in_the_loop: 6
  name: Moltrust Ch Agentic Access
  operation_count: 257
  slug: moltrust-ch-agentic-access
  summary_line: 257 operations · 101 acting · 6 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: 'REST trust-registry API (FastAPI, v2.5, 186 operations): agent registration and DID resolution, W3C VC issue/verify, AAE delegation configuration, UCAN 0.10.0 delegation create/verify, stateless /enfo'
  name: MolTrust API
  slug: moltrust-api
- baseURL: https://api.moltrust.ch/guard
  baseurl_source: declared
  description: 'Trust and integrity sub-API of MolTrust (Hono/Node, v1.5.0, 71 operations across 14 capability clusters): Base wallet risk scoring and sybil-cluster detection, Polymarket market-integrity checks and M'
  name: MoltGuard API
  slug: moltguard-api
- description: Hosted streamable-HTTP Model Context Protocol server (serverInfo moltrust 1.28.1, protocol 2025-06-18) exposing 53 tools over the MolTrust and MoltGuard APIs - identity and credentials, MoltGuard scor
  name: MolTrust MCP Server
  slug: moltrust-mcp-server
- description: DIF Universal Resolver deployment for the did:moltrust method (and bridged did:moltrust:ext_* identifiers), returning W3C DID Documents at the standard /1.0/identifiers/{did} path. The did:moltrust me
  name: MolTrust DID Universal Resolver
  slug: moltrust-did-universal-resolver
artifact_total: 13
asyncapis:
- description: ''
  name: Moltrust Ch Event Surface
  slug: moltrust-ch-event-surface
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/agentic-access/moltrust-ch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moltrust-ch-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/security/moltrust-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moltrust-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moltrust.ch/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://moltrust.ch/developers.html
- group: docs
  title: ''
  type: Documentation
  url: https://api.moltrust.ch/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.moltrust.ch/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://moltrust.ch/developers.html
- group: operate
  title: ''
  type: Support
  url: https://moltrust.ch/contact.html
- group: company
  title: ''
  type: Blog
  url: https://moltrust.ch/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MoltyCel
- group: commercial
  title: ''
  type: Pricing
  url: https://moltrust.ch/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://moltrust.ch/developers.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moltrust.ch/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moltrust.ch/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moltrust.ch/
- group: auth
  title: ''
  type: Compliance
  url: https://moltrust.ch/compliance.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/a2a/moltrust-ch-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/moltrust-ch-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/mcp/moltrust-ch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moltrust-ch-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/mcp/moltrust-ch-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/moltrust-ch-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/llms/moltrust-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moltrust-ch-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://moltrust.ch/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/well-known/moltrust-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moltrust-ch-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/packages/moltrust-ch-packages.yml
  title: ''
  type: Packages
  url: packages/moltrust-ch-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/packages/moltrust-ch-packages.yml
  title: ''
  type: SDKs
  url: packages/moltrust-ch-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/conventions/moltrust-ch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moltrust-ch-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/conformance/moltrust-ch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moltrust-ch-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/errors/moltrust-ch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moltrust-ch-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/lifecycle/moltrust-ch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moltrust-ch-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/changelog/moltrust-ch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/moltrust-ch-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/plans/moltrust-ch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moltrust-ch-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/rate-limits/moltrust-ch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moltrust-ch-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/sandbox/moltrust-ch-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/moltrust-ch-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/components/moltrust-ch-components.yml
  title: ''
  type: Components
  url: components/moltrust-ch-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/data-model/moltrust-ch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moltrust-ch-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/regulatory/moltrust-ch-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/moltrust-ch-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/regulatory/moltrust-ch-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/moltrust-ch-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/regulatory/moltrust-ch-regulatory-posture.yml
  title: ''
  type: DataResidency
  url: regulatory/moltrust-ch-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/security/moltrust-ch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moltrust-ch-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moltrust-ch/refs/heads/main/security/moltrust-ch-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/moltrust-ch-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'CryptoKRI GmbH (Zurich, CHE-115.481.407) operates MolTrust, a trust registry for autonomous AI agents: W3C DID identity (did:moltrust, did:web), W3C Verifiable Credential issuance and verification, Agent Authorization Envelopes (AAE, an IETF Internet-Draft) with UCAN delegation and stateless mandate enforcement, behavioural trust scores signed with Ed25519, EU AI Act compliance endpoints (risk classification, Annex V declarations as VCs, Article 73 incidents), ERC-8004 on-chain registration and Merkle-batched evidence anchoring on Base L2. The MoltGuard sub-API adds wallet trust scoring, sybil detection, prediction-market integrity and vertical credentials (shopping, travel, skills, music, sports, brand provenance) paid per call in USDC via x402. Published surfaces: two OpenAPI 3.1 documents, a signed A2A agent card, a hosted MCP server with 53 tools, llms.txt on both hosts, JWKS / DID documents / x402 discovery under /.well-known, npm and PyPI SDKs, and an Upptime status page.'
image: https://moltrust.ch/img/moltrust-logo.png
layout: provider
mcp_servers:
- description: ''
  name: CryptoKRI GmbH MCP Server
  slug: cryptokri-gmbh-mcp-server
- description: ''
  name: Live endpoint
  slug: live-endpoint
modified: '2026-09-19'
name: CryptoKRI GmbH
nav: Providers
network: true
overview: 'CryptoKRI GmbH publishes 2 APIs on the [APIs.io](https://apis.io/) network: MolTrust API and MoltGuard API. Tagged areas include AI Agents, Agent Identity, Decentralized Identity, Verifiable Credentials, and Trust and Safety.


  The CryptoKRI GmbH catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CryptoKRI GmbH''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Moltrust Ch Plans Pricing
  plan_count: 5
  slug: moltrust-ch-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Moltrust Ch Rate Limits
  slug: moltrust-ch-rate-limits
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 54.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 44.7
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Moltrust Ch Authentication
  slug: moltrust-ch-authentication
  summary_line: apiKey/http-bearer (declared, not live)/x402-payment/admin-key (undeclared) · 6 schemes
- kind: domain-security
  name: Moltrust Ch Domain Security
  slug: moltrust-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Moltrust Ch Vulnerability Disclosure
  slug: moltrust-ch-vulnerability-disclosure
  summary_line: Hackerone
slug: moltrust-ch
tags:
- AI Agents
- Agent Identity
- Decentralized Identity
- Verifiable Credentials
- Trust and Safety
- Agent Authorization
- Compliance
- Blockchain
- A2A
- MCP
- x402
- agent-native
website: https://moltrust.ch/
---
