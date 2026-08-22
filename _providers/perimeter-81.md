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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 63
  human_in_the_loop: 14
  name: Perimeter 81 Agentic Access
  operation_count: 107
  slug: perimeter-81-agentic-access
  summary_line: 107 operations · 63 acting · 14 human-in-the-loop
api_count: 17
apis:
- description: The Application API from Perimeter 81 — 3 operation(s) for application.
  name: Perimeter 81 Application API
  slug: perimeter-81-application-api
- description: The Enhanced Network API allows you to manage and configure enhanced networks.
  name: Perimeter 81 Enhanced Networks API
  slug: perimeter-81-enhanced-networks-api
- description: The Enhanced Region API allows you to manage and configure enhanced regions, including scale units.
  name: Perimeter 81 Enhanced Regions API
  slug: perimeter-81-enhanced-regions-api
- description: The Enhanced Route Tables API allows you to manage and configure enhanced route tables of static and dynamic tunnels.
  name: Perimeter 81 Enhanced Route Tables API
  slug: perimeter-81-enhanced-route-tables-api
- description: The Enhanced Tunnel API allows you to manage and configure enhanced tunnels.
  name: Perimeter 81 Enhanced Tunnels API
  slug: perimeter-81-enhanced-tunnels-api
- description: The Firewall Policy API from Perimeter 81 — 1 operation(s) for firewall policy.
  name: Perimeter 81 Firewall Policy API
  slug: perimeter-81-firewall-policy-api
- description: The Gateways API from Perimeter 81 — 2 operation(s) for gateways.
  name: Perimeter 81 Gateways API
  slug: perimeter-81-gateways-api
- description: The IPSec-Redundant API from Perimeter 81 — 2 operation(s) for ipsec-redundant.
  name: Perimeter 81 IPSec-Redundant API
  slug: perimeter-81-ipsec-redundant-api
- description: The IPSec-Single API from Perimeter 81 — 2 operation(s) for ipsec-single.
  name: Perimeter 81 IPSec-Single API
  slug: perimeter-81-ipsec-single-api
- description: This API allows you to manage and configure standard networks using the old API and keep you BC.
  name: Perimeter 81 Networks API
  slug: perimeter-81-networks-api
- description: The Objects Addresses API from Perimeter 81 — 2 operation(s) for objects addresses.
  name: Perimeter 81 Objects Addresses API
  slug: perimeter-81-objects-addresses-api
- description: The Objects Services API from Perimeter 81 — 2 operation(s) for objects services.
  name: Perimeter 81 Objects Services API
  slug: perimeter-81-objects-services-api
- description: The OpenVPN API from Perimeter 81 — 2 operation(s) for openvpn.
  name: Perimeter 81 OpenVPN API
  slug: perimeter-81-openvpn-api
- description: The Regions API from Perimeter 81 — 3 operation(s) for regions.
  name: Perimeter 81 Regions API
  slug: perimeter-81-regions-api
- description: The Route Table API from Perimeter 81 — 1 operation(s) for route table.
  name: Perimeter 81 Route Table API
  slug: perimeter-81-route-table-api
- description: The Standard Network API allows you to manage and configure standard networks.
  name: Perimeter 81 Standard Networks API
  slug: perimeter-81-standard-networks-api
- description: The Wireguard API from Perimeter 81 — 2 operation(s) for wireguard.
  name: Perimeter 81 Wireguard API
  slug: perimeter-81-wireguard-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harmony SASE Public Application API
  slug: open-perimeter-81-application-api
- collection_type: open
  name: Harmony SASE Public Application Enhanced Networks API
  slug: open-perimeter-81-enhanced-networks-api
- collection_type: open
  name: Harmony SASE Public Application Enhanced Regions API
  slug: open-perimeter-81-enhanced-regions-api
- collection_type: open
  name: Harmony SASE Public Application Enhanced Route Tables API
  slug: open-perimeter-81-enhanced-route-tables-api
- collection_type: open
  name: Harmony SASE Public Application Enhanced Tunnels API
  slug: open-perimeter-81-enhanced-tunnels-api
- collection_type: open
  name: Harmony SASE Public Application Firewall Policy API
  slug: open-perimeter-81-firewall-policy-api
- collection_type: open
  name: Harmony SASE Public Application Gateways API
  slug: open-perimeter-81-gateways-api
- collection_type: open
  name: Harmony SASE Public Application IPSec-Redundant API
  slug: open-perimeter-81-ipsec-redundant-api
- collection_type: open
  name: Harmony SASE Public Application IPSec-Single API
  slug: open-perimeter-81-ipsec-single-api
- collection_type: open
  name: Harmony SASE Public Application Networks API
  slug: open-perimeter-81-networks-api
- collection_type: open
  name: Harmony SASE Public Application Objects Addresses API
  slug: open-perimeter-81-objects-addresses-api
- collection_type: open
  name: Harmony SASE Public Application Objects Services API
  slug: open-perimeter-81-objects-services-api
- collection_type: open
  name: Harmony SASE Public Application OpenVPN API
  slug: open-perimeter-81-openvpn-api
- collection_type: open
  name: Harmony SASE Public Application Regions API
  slug: open-perimeter-81-regions-api
- collection_type: open
  name: Harmony SASE Public Application Route Table API
  slug: open-perimeter-81-route-table-api
- collection_type: open
  name: Harmony SASE Public Application Standard Networks API
  slug: open-perimeter-81-standard-networks-api
- collection_type: open
  name: Harmony SASE Public Application Wireguard API
  slug: open-perimeter-81-wireguard-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/perimeter-81-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/perimeter-81-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perimeter-81-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.perimeter81.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.perimeter81.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://support.perimeter81.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis/Check-Point/Harmony-SASE-API
- group: start
  title: ''
  type: GettingStarted
  url: https://support.perimeter81.com/docs/api-getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.perimeter81.com/
- group: company
  title: ''
  type: Blog
  url: https://www.perimeter81.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.perimeter81.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perimeter81.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perimeter81.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/perimeter-81-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/perimeter-81-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/perimeter-81-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Perimeter 81 is a cloud-native Secure Access Service Edge (SASE) and Zero Trust Network Access (ZTNA) platform, now part of Check Point as Check Point Harmony SASE following its 2023 acquisition. It lets organizations build and manage secure, software-defined networks that connect a distributed workforce to on-premises resources, cloud infrastructure, and SaaS applications without legacy hardware appliances. The Harmony SASE Public API (v2.3) exposes programmatic control over networks, regions and points-of-presence, gateways, IPSec/WireGuard/OpenVPN tunnels, route tables, firewall policies, and network objects, using a two-step API-key-to-JWT access-token authentication model across US, EU, Australia, and India regional gateways.
image: https://www.perimeter81.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: perimeter-81-mcp.yml
  slug: perimeter-81-mcpyml
modified: '2026-07-20'
name: Perimeter 81
nav: Providers
network: true
overview: 'Perimeter 81 publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Application API, Enhanced Networks API, Enhanced Regions API, and 14 more. Tagged areas include Company, Cybersecurity, SASE, Zero Trust, and Networking.


  Perimeter 81''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 32.0
  delta: -8.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 60.0
    developer_ergonomics: 7.7
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: authentication
  name: Perimeter 81 Authentication
  slug: perimeter-81-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Perimeter 81 Domain Security
  slug: perimeter-81-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: perimeter-81
tags:
- Company
- Cybersecurity
- SASE
- Zero Trust
- Networking
- VPN
- ZTNA
- Security
- Cloud Security
website: https://www.perimeter81.com/
---
