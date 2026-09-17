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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Subspace Agentic Access
  operation_count: 11
  slug: subspace-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.subspace.com/v1
  baseurl_source: declared
  description: The AcceleratorService API from Subspace — 2 operation(s) for acceleratorservice.
  name: Subspace AcceleratorService API
  slug: subspace-acceleratorservice-api
- baseURL: https://api.subspace.com/v1
  baseurl_source: declared
  description: The SipTeleportService API from Subspace — 2 operation(s) for sipteleportservice.
  name: Subspace SipTeleportService API
  slug: subspace-sipteleportservice-api
- baseURL: https://api.subspace.com/v1
  baseurl_source: declared
  description: The WebRtcCdnService API from Subspace — 1 operation(s) for webrtccdnservice.
  name: Subspace WebRtcCdnService API
  slug: subspace-webrtccdnservice-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Subspace Product AcceleratorService API
  slug: open-subspace-acceleratorservice-api
- collection_type: open
  name: Subspace Product AcceleratorService SipTeleportService API
  slug: open-subspace-sipteleportservice-api
- collection_type: open
  name: Subspace Product AcceleratorService WebRtcCdnService API
  slug: open-subspace-webrtccdnservice-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/overlays/subspace-openapi-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/llms/subspace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/subspace-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/packages/subspace-packages.yml
  title: ''
  type: Packages
  url: packages/subspace-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/packages/subspace-packages.yml
  title: ''
  type: SDKs
  url: packages/subspace-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/mcp/subspace-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/subspace-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/conventions/subspace-conventions.yml
  title: ''
  type: Conventions
  url: conventions/subspace-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/data-model/subspace-data-model.yml
  title: ''
  type: DataModel
  url: data-model/subspace-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/errors/subspace-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/subspace-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/lifecycle/subspace-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/subspace-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/conformance/subspace-conformance.yml
  title: ''
  type: Conformance
  url: conformance/subspace-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/authentication/subspace-authentication.yml
  title: ''
  type: Authentication
  url: authentication/subspace-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/scopes/subspace-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/subspace-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/agentic-access/subspace-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/subspace-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/security/subspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/subspace-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/security/subspace-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/subspace-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/well-known/subspace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/subspace-well-known.yml
created: '2026-07-17'
description: 'Subspace was a real-time network-as-a-service platform delivering a dedicated, performance-optimized global network for latency-sensitive applications — WebRTC, VoIP/SIP calling, video conferencing, multiplayer gaming, and fintech. Its Product API provisions three services: PacketAccelerator (no-code global internet acceleration), SIPTeleport (SIP/VoIP call-quality improvement), and WebRTC-CDN (instant global WebRTC acceleration with ICE server configuration). The REST API uses resource-oriented URLs and JSON responses, versioned at v1, authenticated with OAuth2 client-credentials issuing 24-hour JWT bearer tokens via Auth0, and ships six first-party OpenAPI client SDKs. The company was a Bloomberg Beta portfolio company; its marketing site remains live while the API, identity, and status hosts have wound down operationally.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/subspace.png
layout: provider
modified: '2026-07-21'
name: Subspace
nav: Providers
network: true
overview: 'Subspace publishes 3 APIs on the [APIs.io](https://apis.io/) network: AcceleratorService API, SipTeleportService API, and WebRtcCdnService API. Tagged areas include Company, Networking, Real-Time, WebRTC, and VoIP.


  Subspace''s developer surface includes documentation, API reference, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 18
scopes:
- name: Subspace Scopes
  scope_count: 9
  slug: subspace-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 42.3
    discoverability: 75.9
    operational_transparency: 13.2
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/subspace/refs/heads/main/screenshots/subspace-2026-09-02T161100.png
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
