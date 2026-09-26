---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Zerotier Agentic Access
  operation_count: 38
  slug: zerotier-agentic-access
  summary_line: 38 operations · 16 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.zerotier.com/api/v1
  baseurl_source: declared
  description: The controller API from ZeroTier — 6 operation(s) for controller.
  name: ZeroTier Controller API
  slug: zerotier-controller-api
- baseURL: https://api.zerotier.com/api/v1
  baseurl_source: declared
  description: Network operations
  name: ZeroTier Network API
  slug: zerotier-network-api
- baseURL: https://api.zerotier.com/api/v1
  baseurl_source: declared
  description: Network member operations
  name: ZeroTier Network Member API
  slug: zerotier-network-member-api
- baseURL: https://api.zerotier.com/api/v1
  baseurl_source: declared
  description: 'Organization management. Note: Organizations require a paid account and cannot be created via the API'
  name: ZeroTier Organizations API
  slug: zerotier-organizations-api
- baseURL: https://api.zerotier.com/api/v1
  baseurl_source: declared
  description: peer status
  name: ZeroTier Peer API
  slug: zerotier-peer-api
- baseURL: https://api.zerotier.com/api/v1
  baseurl_source: declared
  description: status
  name: ZeroTier Status API
  slug: zerotier-status-api
- baseURL: https://api.zerotier.com/api/v1
  baseurl_source: declared
  description: User management operations
  name: ZeroTier User API
  slug: zerotier-user-api
- baseURL: https://api.zerotier.com/api/v1
  baseurl_source: declared
  description: Utility endpoints
  name: ZeroTier Util API
  slug: zerotier-util-api
artifact_total: 33
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/plans/zerotier-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zerotier-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/capabilities/zerotier-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zerotier-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/overlays/zerotier-central-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zerotier-central-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zerotier/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/agentic-access/zerotier-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zerotier-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/security/zerotier-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zerotier-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/security/zerotier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zerotier-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/authentication/zerotier-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/security/zerotier-vulnerability-disclosure.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/packages/zerotier-packages.yml
  title: ''
  type: Packages
  url: packages/zerotier-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/packages/zerotier-packages.yml
  title: ''
  type: SDKs
  url: packages/zerotier-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/cli/zerotier-cli.yml
  title: ''
  type: CLI
  url: cli/zerotier-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/mcp/zerotier-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zerotier-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/llms/zerotier-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zerotier-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/conformance/zerotier-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zerotier-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/errors/zerotier-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zerotier-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/lifecycle/zerotier-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zerotier-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/lifecycle/zerotier-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/zerotier-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/conventions/zerotier-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zerotier-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/data-model/zerotier-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zerotier-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/changelog/zerotier-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zerotier-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/asyncapi/zerotier-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/zerotier-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: ZeroTier, Inc. builds a software-defined networking (SDN) overlay that securely connects devices, servers, clouds, and networks anywhere in the world as if they were on the same local LAN, without the complexity of traditional VPNs, port forwarding, or firewall changes. The platform combines a peer-to-peer, end-to-end encrypted transport with a hosted control plane (ZeroTier Central) for network, member, organization, and access management. Developers automate ZeroTier through the hosted Central API (create and manage virtual networks, authorize members, set flow rules and IAM), the local ZeroTier One Service/Client API on each node, a Terraform provider, first-party client libraries, webhooks for real-time organization events, and a growing focus on post-quantum ("ZeroTier Quantum") secure networking.
image: https://avatars.githubusercontent.com/u/4173285?v=4
layout: provider
modified: '2026-07-21'
name: ZeroTier
nav: Providers
network: true
overview: 'ZeroTier publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Controller API, Network API, Network Member API, and 5 more. Tagged areas include Company, Networking, Software Defined Networking, SDN, and VPN.


  The ZeroTier catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZeroTier''s developer surface includes authentication, documentation, API reference, getting-started guide, quickstart, support, engineering blog, and 37 more developer resources.'
plans:
- name: Zerotier Plans Pricing
  plan_count: 5
  slug: zerotier-plans-pricing
- name: Zerotier Price Estimates
  plan_count: 0
  slug: zerotier-price-estimates
random_paper: 4
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 54.5
    developer_ergonomics: 74.4
    discoverability: 73.2
    operational_transparency: 52.6
  previous_composite: 63.3
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/zerotier/refs/heads/main/screenshots/zerotier-2026-08-17T083100.png
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
- Software Defined Networking
- SDN
- VPN
- Security
- Connectivity
- Overlay Network
- Zero Trust
- Infrastructure
website: https://www.zerotier.com/
---
