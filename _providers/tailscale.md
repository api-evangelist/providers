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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Tailscale Agentic Access
  operation_count: 45
  slug: tailscale-agentic-access
  summary_line: 45 operations · 26 acting
api_count: 7
apis:
- description: The Devices API from Tailscale — 12 operation(s) for devices.
  name: Tailscale Devices API
  slug: tailscale-devices-api
- description: The DNS API from Tailscale — 3 operation(s) for dns.
  name: Tailscale DNS API
  slug: tailscale-dns-api
- description: The Invites API from Tailscale — 7 operation(s) for invites.
  name: Tailscale Invites API
  slug: tailscale-invites-api
- description: The Keys API from Tailscale — 2 operation(s) for keys.
  name: Tailscale Keys API
  slug: tailscale-keys-api
- description: The Logging API from Tailscale — 4 operation(s) for logging.
  name: Tailscale Logging API
  slug: tailscale-logging-api
- description: The Policy API from Tailscale — 2 operation(s) for policy.
  name: Tailscale Policy API
  slug: tailscale-policy-api
- description: The Tailnet API from Tailscale — 2 operation(s) for tailnet.
  name: Tailscale Tailnet API
  slug: tailscale-tailnet-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tailscale REST Devices API
  slug: open-tailscale-devices-api
- collection_type: open
  name: Tailscale REST Devices DNS API
  slug: open-tailscale-dns-api
- collection_type: open
  name: Tailscale REST Devices Invites API
  slug: open-tailscale-invites-api
- collection_type: open
  name: Tailscale REST Devices Keys API
  slug: open-tailscale-keys-api
- collection_type: open
  name: Tailscale REST Devices Logging API
  slug: open-tailscale-logging-api
- collection_type: open
  name: Tailscale REST Devices Policy API
  slug: open-tailscale-policy-api
- collection_type: open
  name: Tailscale REST Devices Tailnet API
  slug: open-tailscale-tailnet-api
- collection_type: open
  name: Tailscale REST API
  slug: open-tailscale
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tailscale-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tailscale-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tailscale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tailscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tailscale-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tailscale
- group: company
  title: ''
  type: Website
  url: https://tailscale.com
- group: docs
  title: ''
  type: Documentation
  url: https://tailscale.com/kb/
- group: commercial
  title: ''
  type: Pricing
  url: https://tailscale.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://login.tailscale.com/start
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tailscale/tailscale
- group: company
  title: ''
  type: Blog
  url: https://tailscale.com/blog/index.xml
created: '2026-05-11'
description: Tailscale is a zero-config mesh VPN built on WireGuard that creates secure private networks between devices, users, and services with identity-based access controls, Access Control Lists (ACLs), DNS, and device sharing. Tailscale eliminates traditional VPN complexity with peer-to-peer connectivity and SSO-based authentication. The Tailscale REST API provides programmatic control over tailnets, devices, users, ACLs, and keys using API tokens or OAuth client credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tailscale.png
layout: provider
modified: '2026-05-11'
name: Tailscale
nav: Providers
network: true
overview: 'Tailscale publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Devices API, DNS API, Invites API, and 4 more. Tagged areas include VPN, Mesh Networking, WireGuard, Zero Trust, and Networking.


  Tailscale''s developer surface includes authentication, documentation, pricing, signup flow, GitHub presence, engineering blog, and 6 more developer resources.'
random_paper: 52
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 55.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tailscale/refs/heads/main/screenshots/tailscale-2026-06-20T194858.png
security:
- kind: authentication
  name: Tailscale Authentication
  slug: tailscale-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Tailscale Domain Security
  slug: tailscale-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tailscale Vulnerability Disclosure
  slug: tailscale-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tailscale Trust Center
  slug: tailscale-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: tailscale
tags:
- VPN
- Mesh Networking
- WireGuard
- Zero Trust
- Networking
- Identity
website: https://tailscale.com
---
