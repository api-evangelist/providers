---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: REST API for managing CloudConnexa Zero Trust networks, users, networks, connectors, DNS, routes, and access policies. Authentication uses OAuth 2.0 client credentials grant; API credentials are gener
  name: CloudConnexa Public API
  slug: cloudconnexa-api
- description: XML-RPC management API exposing hundreds of methods to control and monitor every aspect of an OpenVPN Access Server deployment, including user provisioning, permissions, configuration, and status. Req
  name: OpenVPN Access Server XML-RPC API
  slug: access-server-xmlrpc
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openvpn-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openvpn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openvpn
- group: company
  title: ''
  type: Website
  url: https://openvpn.net
- group: docs
  title: ''
  type: Documentation
  url: https://openvpn.net/as-docs/
- group: docs
  title: ''
  type: CloudConnexa Documentation
  url: https://openvpn.net/cloud-docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://openvpn.net/pricing/
- group: start
  title: ''
  type: Signup
  url: https://openvpn.net/cloudconnexa/
- group: operate
  title: ''
  type: Support
  url: https://support.openvpn.com/hc/en-us
- group: agent
  title: ''
  type: LlmsText
  url: https://openvpn.net/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.openvpn.net/rss.xml
created: '2026-05-11'
description: OpenVPN is a secure networking company providing VPN and Zero Trust network access solutions for over 20,000 organizations worldwide, offering both the self-hosted Access Server and the cloud-delivered CloudConnexa managed service. The platform supports encrypted tunnels, identity-based access policies, content filtering, IDS/IPS, and domain-based traffic rules across major cloud providers. OpenVPN exposes an XML-RPC management API for Access Server and an OAuth 2.0 protected REST API for CloudConnexa.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openvpn.png
layout: provider
modified: '2026-05-11'
name: OpenVPN
nav: Providers
network: true
overview: 'OpenVPN publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include VPN, Zero Trust, Network Security, Remote Access, and Identity.


  OpenVPN''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 12.7
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openvpn/refs/heads/main/screenshots/openvpn-2026-06-20T191051.png
security:
- kind: domain-security
  name: Openvpn Domain Security
  slug: openvpn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openvpn
tags:
- VPN
- Zero Trust
- Network Security
- Remote Access
- Identity
- Cloud Security
website: https://openvpn.net
---
