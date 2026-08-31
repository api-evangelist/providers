---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Vpn Agentic Access
  operation_count: 8
  slug: vpn-agentic-access
  summary_line: 8 operations
api_count: 6
apis:
- description: Tailscale provides a REST API for managing tailnets (private mesh networks), devices, users, access control lists, and network configuration. Built on WireGuard, Tailscale enables zero-configuration V
  name: Tailscale API
  slug: tailscale-api
- description: AWS Site-to-Site VPN and AWS Client VPN provide managed VPN solutions on AWS infrastructure. Managed via the AWS EC2 API and AWS CLI for creating virtual private gateways, customer gateways, and VPN c
  name: AWS VPN API
  slug: aws-vpn
- description: Azure VPN Gateway provides managed site-to-site, point-to-site, and VNet-to-VNet VPN connections. Managed via Azure Resource Manager REST API and Azure CLI.
  name: Azure VPN Gateway API
  slug: azure-vpn
- description: The Catalog API from VPN — 3 operation(s) for catalog.
  name: VPN Catalog API
  slug: vpn-catalog-api
- description: The Servers API from VPN — 3 operation(s) for servers.
  name: VPN Servers API
  slug: vpn-servers-api
- description: The Stats API from VPN — 2 operation(s) for stats.
  name: VPN Stats API
  slug: vpn-stats-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NordVPN Public Catalog API
  slug: open-vpn-catalog-api
- collection_type: open
  name: NordVPN Public Catalog Servers API
  slug: open-vpn-servers-api
- collection_type: open
  name: NordVPN Public Catalog Stats API
  slug: open-vpn-stats-api
- collection_type: open
  name: NordVPN Public API
  slug: open-vpn
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vpn-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vpn-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vpn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vpn-domain-security.yml
- group: docs
  title: ''
  type: Reference
  url: https://en.wikipedia.org/wiki/Virtual_private_network
- group: other
  title: ''
  type: Standards
  url: https://www.wireguard.com/
- group: other
  title: ''
  type: Standards
  url: https://openvpn.net/
- group: start
  title: ''
  type: Portal
  url: https://tailscale.com/
- group: company
  title: ''
  type: Website
  url: https://www.nordvpn.com/
- group: company
  title: ''
  type: Website
  url: https://protonvpn.com/
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/qdm12/gluetun
created: '2025'
description: A VPN (Virtual Private Network) creates an encrypted tunnel between a user's device and a remote network, protecting data from interception and masking the user's IP address. VPN technology is widely used for secure remote access to corporate networks, protecting privacy on public Wi-Fi, and bypassing geographic content restrictions. This index documents VPN providers, protocols, and APIs relevant to the VPN technology landscape including NordVPN, OpenVPN, WireGuard, Tailscale, and cloud provider VPN services.
finops:
- name: Vpn Finops
  service_category: API
  slug: vpn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vpn.png
json_schemas:
- name: VPN Server
  property_count: 11
  slug: vpn-server
jsonld:
- class_count: 0
  name: Vpn Context
  property_count: 7
  slug: vpn-context
layout: provider
modified: '2026-05-19'
name: VPN
nav: Providers
network: true
overview: 'VPN publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API, Servers API, and Stats API. Tagged areas include Encryption, Networking, Privacy, Security, and VPN.


  The VPN catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  VPN''s developer surface includes developer portal and 10 more developer resources.'
plans:
- name: Vpn Plans Pricing
  plan_count: 3
  slug: vpn-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Vpn Rate Limits
  slug: vpn-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: VPN API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vpn-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 48.8
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.4
    commercial_clarity: 21.4
    contract_governance: 9.8
    contract_quality: 43.5
    developer_ergonomics: 26.2
    discoverability: 81.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vpn/refs/heads/main/screenshots/vpn-2026-06-20T201144.png
security:
- kind: domain-security
  name: Vpn Domain Security
  slug: vpn-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vpn Vulnerability Disclosure
  slug: vpn-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Vpn Trust Center
  slug: vpn-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: vpn
tags:
- Encryption
- Networking
- Privacy
- Security
- VPN
website: https://www.nordvpn.com/
---
