---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Subspace Agentic Access
  operation_count: 11
  slug: subspace-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 3
apis:
- description: The AcceleratorService API from Subspace — 2 operation(s) for acceleratorservice.
  name: Subspace AcceleratorService API
  slug: subspace-acceleratorservice-api
- description: The SipTeleportService API from Subspace — 2 operation(s) for sipteleportservice.
  name: Subspace SipTeleportService API
  slug: subspace-sipteleportservice-api
- description: The WebRtcCdnService API from Subspace — 1 operation(s) for webrtccdnservice.
  name: Subspace WebRtcCdnService API
  slug: subspace-webrtccdnservice-api
artifact_total: 9
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/subspace-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.subspace.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.subspace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://subspace.com/resources?category=documentation
- group: docs
  title: ''
  type: APIReference
  url: https://subspace.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://subspace.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.subspace.com/
- group: auth
  title: ''
  type: Security
  url: https://subspace.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/subspace-com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/subspace-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/subspace-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/subspace-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/subspace-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/subspace-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/subspace-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/subspace-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/subspace-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/subspace-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/subspace-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/subspace-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/subspace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/subspace-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/subspace-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/subspace-well-known.yml
created: '2026-07-17'
description: 'Subspace was a real-time network-as-a-service platform delivering a dedicated, performance-optimized global network for latency-sensitive applications — WebRTC, VoIP/SIP calling, video conferencing, multiplayer gaming, and fintech. Its Product API provisions three services: PacketAccelerator (no-code global internet acceleration), SIPTeleport (SIP/VoIP call-quality improvement), and WebRTC-CDN (instant global WebRTC acceleration with ICE server configuration). The REST API uses resource-oriented URLs and JSON responses, versioned at v1, authenticated with OAuth2 client-credentials issuing 24-hour JWT bearer tokens via Auth0, and ships six first-party OpenAPI client SDKs. The company was a Bloomberg Beta portfolio company; its marketing site remains live while the API, identity, and status hosts have wound down operationally.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/subspace.png
layout: provider
mcp_servers:
- description: ''
  name: subspace-mcp.yml
  slug: subspace-mcpyml
modified: '2026-07-21'
name: Subspace
nav: Providers
network: true
overview: 'Subspace publishes 3 APIs on the [APIs.io](https://apis.io/) network: AcceleratorService API, SipTeleportService API, and WebRtcCdnService API. Tagged areas include Company, Networking, Real-Time, WebRTC, and VoIP.


  Subspace''s developer surface includes documentation, API reference, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 42
scopes:
- name: Subspace Scopes
  scope_count: 9
  slug: subspace-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: thin
  composite: 38.4
  delta: -1.6
  facets:
    commercial_clarity: 23.7
    contract_quality: 52.2
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Subspace Authentication
  slug: subspace-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Subspace Domain Security
  slug: subspace-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Subspace Vulnerability Disclosure
  slug: subspace-vulnerability-disclosure
  summary_line: Bugcrowd
slug: subspace
tags:
- Company
- Networking
- Real-Time
- WebRTC
- VoIP
- SIP
- CDN
- Gaming
- Latency
- Infrastructure
website: https://www.subspace.com/
---
