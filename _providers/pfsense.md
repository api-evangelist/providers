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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Pfsense Agentic Access
  operation_count: 12
  slug: pfsense-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 5
apis:
- description: Community-maintained REST and GraphQL API package for pfSense CE and pfSense Plus exposing 200+ endpoints under /api/v2 for firewall, interface, service, user, and system management. Authentication su
  name: pfSense REST API (pfSense-pkg-RESTAPI)
  slug: rest-api-package
- description: Obtain JWT bearer tokens.
  name: pfSense Authentication API
  slug: pfsense-authentication-api
- description: Manage firewall aliases.
  name: pfSense Firewall Aliases API
  slug: pfsense-firewall-aliases-api
- description: Apply pending firewall changes.
  name: pfSense Firewall Apply API
  slug: pfsense-firewall-apply-api
- description: Manage firewall rules.
  name: pfSense Firewall Rules API
  slug: pfsense-firewall-rules-api
artifact_total: 11
collections:
- collection_type: open
  name: pfSense REST API (pfSense-pkg-RESTAPI)
  slug: open-pfsense
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pfsense-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pfsense-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pfsense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pfsense-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pfsense.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netgate.com/pfsense/en/latest/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netgate.com/pfsense-plus-software
- group: other
  title: ''
  type: Download
  url: https://www.pfsense.org/download/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pfsense
- group: other
  title: ''
  type: Vendor
  url: https://www.netgate.com/
- group: company
  title: ''
  type: Blog
  url: https://www.netgate.com/blog/rss.xml
created: '2026-05-11'
description: pfSense is an open-source firewall and router operating system based on FreeBSD, developed and maintained by Netgate, providing stateful firewall, routing, VPN (IPsec, OpenVPN, WireGuard), captive portal, traffic shaping, and IDS/IPS capabilities for home and enterprise networks. It is available as pfSense Community Edition (CE) and pfSense Plus, both managed via a web UI. The unofficial pfSense-pkg-RESTAPI package adds a REST and GraphQL API with 200+ endpoints under /api/v2 for automating firewall management, authenticated via local users, API keys, or JWT.
graphqls:
- description: Community-maintained REST and GraphQL API package for pfSense CE and pfSense Plus exposing 200+ endpoints under /api/v2 for firewall, interface, service, user, and system management. Authentication su
  name: pfSense GraphQL API
  slug: pfsense-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pfsense.png
layout: provider
modified: '2026-05-11'
name: pfSense
nav: Providers
network: true
overview: 'pfSense publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Firewall Aliases API, Firewall Apply API, and 1 more. Tagged areas include Firewall, Network Security, Router, VPN, and Open Source.


  pfSense''s developer surface includes authentication, documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 78
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 55.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pfsense/refs/heads/main/screenshots/pfsense-2026-06-20T191628.png
security:
- kind: authentication
  name: Pfsense Authentication
  slug: pfsense-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Pfsense Domain Security
  slug: pfsense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pfsense Vulnerability Disclosure
  slug: pfsense-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pfsense
tags:
- Firewall
- Network Security
- Router
- VPN
- Open Source
- FreeBSD
- Netgate
website: https://www.pfsense.org/
---
