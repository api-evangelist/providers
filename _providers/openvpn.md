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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
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
random_paper: 18
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
