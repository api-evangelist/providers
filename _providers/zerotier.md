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
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Zerotier Agentic Access
  operation_count: 38
  slug: zerotier-agentic-access
  summary_line: 38 operations · 16 acting · 2 human-in-the-loop
api_count: 8
apis:
- description: The controller API from ZeroTier — 6 operation(s) for controller.
  name: ZeroTier controller API
  slug: zerotier-controller-api
- description: Network operations
  name: ZeroTier network API
  slug: zerotier-network-api
- description: Network member operations
  name: ZeroTier network-member API
  slug: zerotier-network-member-api
- description: 'Organization management. Note: Organizations require a paid account and cannot be created via the API'
  name: ZeroTier organizations API
  slug: zerotier-organizations-api
- description: peer status
  name: ZeroTier peer API
  slug: zerotier-peer-api
- description: status
  name: ZeroTier status API
  slug: zerotier-status-api
- description: User management operations
  name: ZeroTier user API
  slug: zerotier-user-api
- description: Utility endpoints
  name: ZeroTier util API
  slug: zerotier-util-api
artifact_total: 32
asyncapis:
- description: ''
  name: Zerotier Webhooks
  slug: zerotier-webhooks
collections:
- collection_type: postman
  name: ZeroTier Central controller API
  slug: postman-zerotier-controller-api
- collection_type: postman
  name: ZeroTier Central controller network API
  slug: postman-zerotier-network-api
- collection_type: postman
  name: ZeroTier Central controller network-member API
  slug: postman-zerotier-network-member-api
- collection_type: postman
  name: ZeroTier Central controller organizations API
  slug: postman-zerotier-organizations-api
- collection_type: postman
  name: ZeroTier Central controller peer API
  slug: postman-zerotier-peer-api
- collection_type: postman
  name: ZeroTier Central controller status API
  slug: postman-zerotier-status-api
- collection_type: postman
  name: ZeroTier Central controller user API
  slug: postman-zerotier-user-api
- collection_type: postman
  name: ZeroTier Central controller util API
  slug: postman-zerotier-util-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ZeroTier Central controller API
  slug: open-zerotier-controller-api
- collection_type: open
  name: ZeroTier Central controller network API
  slug: open-zerotier-network-api
- collection_type: open
  name: ZeroTier Central controller network-member API
  slug: open-zerotier-network-member-api
- collection_type: open
  name: ZeroTier Central controller organizations API
  slug: open-zerotier-organizations-api
- collection_type: open
  name: ZeroTier Central controller peer API
  slug: open-zerotier-peer-api
- collection_type: open
  name: ZeroTier Central controller status API
  slug: open-zerotier-status-api
- collection_type: open
  name: ZeroTier Central controller user API
  slug: open-zerotier-user-api
- collection_type: open
  name: ZeroTier Central controller util API
  slug: open-zerotier-util-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/zerotier-central-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zerotier/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zerotier-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zerotier-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zerotier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zerotier-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.zerotier.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zerotier.com/enterprise/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zerotier.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zerotier.com/api/central/new/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zerotier.com/start/
- group: start
  title: ''
  type: Quickstart
  url: https://docs.zerotier.com/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://www.zerotier.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.zerotier.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zerotier
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zerotier.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://my.zerotier.com/
- group: start
  title: ''
  type: Login
  url: https://my.zerotier.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zerotier.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zerotier.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zerotier.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.zerotier.com
- group: auth
  title: ''
  type: Compliance
  url: https://docs.zerotier.com/security/
- group: auth
  title: ''
  type: Security
  url: https://docs.zerotier.com/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zerotier-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.zerotier.com/changelog/
- group: operate
  title: ''
  type: SLA
  url: https://www.zerotier.com/sla/
- group: other
  title: ''
  type: Glossary
  url: https://www.zerotier.com/glossary/
- group: build
  title: ''
  type: Packages
  url: packages/zerotier-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zerotier-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/zerotier-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zerotier-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zerotier-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/zerotier-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zerotier-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zerotier-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/zerotier-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zerotier-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zerotier-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zerotier-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zerotier-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: ZeroTier, Inc. builds a software-defined networking (SDN) overlay that securely connects devices, servers, clouds, and networks anywhere in the world as if they were on the same local LAN, without the complexity of traditional VPNs, port forwarding, or firewall changes. The platform combines a peer-to-peer, end-to-end encrypted transport with a hosted control plane (ZeroTier Central) for network, member, organization, and access management. Developers automate ZeroTier through the hosted Central API (create and manage virtual networks, authorize members, set flow rules and IAM), the local ZeroTier One Service/Client API on each node, a Terraform provider, first-party client libraries, webhooks for real-time organization events, and a growing focus on post-quantum ("ZeroTier Quantum") secure networking.
image: https://avatars.githubusercontent.com/u/4173285?v=4
layout: provider
mcp_servers:
- description: ''
  name: zerotier-mcp.yml
  slug: zerotier-mcpyml
modified: '2026-07-21'
name: ZeroTier
nav: Providers
network: true
overview: 'ZeroTier publishes 8 APIs on the [APIs.io](https://apis.io/) network, including controller API, network API, network-member API, and 5 more. Tagged areas include Company, Networking, Software-Defined Networking, SDN, and VPN.


  The ZeroTier catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZeroTier''s developer surface includes authentication, documentation, API reference, getting-started guide, quickstart, support, engineering blog, and 35 more developer resources.'
random_paper: 139
score:
  band: strong
  composite: 60.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.4
    developer_ergonomics: 73.4
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Zerotier Authentication
  slug: zerotier-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Zerotier Domain Security
  slug: zerotier-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zerotier Vulnerability Disclosure
  slug: zerotier-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Zerotier Trust Center
  slug: zerotier-trust-center
  summary_line: SOC 2 Type II
slug: zerotier
tags:
- Company
- Networking
- Software-Defined Networking
- SDN
- VPN
- Security
- Connectivity
- Overlay Network
- Zero Trust
- Infrastructure
website: https://www.zerotier.com/
---
