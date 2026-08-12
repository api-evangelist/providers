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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Opnsense Agentic Access
  operation_count: 6
  slug: opnsense-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: REST API covering all core OPNsense modules including firewall, NAT, interfaces, VPN (IPsec, OpenVPN, WireGuard), routing, DHCP, DNS, users, and system administration. Authentication uses HTTP basic a
  name: OPNsense Core REST API
  slug: core-api
- description: Core OPNsense service controllers.
  name: OPNsense Core API
  slug: opnsense-core-api
- description: Interface and system diagnostics.
  name: OPNsense Diagnostics API
  slug: opnsense-diagnostics-api
- description: Firewall filter and aliases.
  name: OPNsense Firewall API
  slug: opnsense-firewall-api
artifact_total: 8
collections:
- collection_type: open
  name: OPNsense Core REST API
  slug: open-opnsense
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opnsense-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opnsense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opnsense-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/opnsense
- group: company
  title: ''
  type: Website
  url: https://opnsense.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opnsense.org
- group: other
  title: ''
  type: Download
  url: https://opnsense.org/download/
- group: operate
  title: ''
  type: Forums
  url: https://forum.opnsense.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opnsense
- group: other
  title: ''
  type: Business Edition
  url: https://shop.opnsense.com
created: '2026-05-11'
description: OPNsense is an open source FreeBSD-based firewall and routing platform providing stateful packet filtering, VPN (IPsec, OpenVPN, WireGuard), intrusion detection (Suricata), traffic shaping, captive portal, and high availability for home, enterprise, and managed service provider deployments. The platform features a web UI, plugin ecosystem, and a comprehensive Business Edition. OPNsense exposes a REST API for managing every core module and plugin, using HTTP basic authentication with an API key and secret.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opnsense.png
layout: provider
modified: '2026-05-11'
name: OPNsense
nav: Providers
network: true
overview: 'OPNsense publishes 3 APIs on the [APIs.io](https://apis.io/) network: Core API, Diagnostics API, and Firewall API. Tagged areas include Firewall, Networking, Security, VPN, and Routing.


  OPNsense''s developer surface includes authentication, documentation, and 8 more developer resources.'
random_paper: 63
score:
  band: emerging
  composite: 27.6
  delta: 0.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 59.0
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opnsense/refs/heads/main/screenshots/opnsense-2026-06-20T191103.png
security:
- kind: authentication
  name: Opnsense Authentication
  slug: opnsense-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opnsense Domain Security
  slug: opnsense-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: opnsense
tags:
- Firewall
- Networking
- Security
- VPN
- Routing
- Open Source
website: https://opnsense.org
---
