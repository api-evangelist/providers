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
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Tailscale Agentic Access
  operation_count: 45
  slug: tailscale-agentic-access
  summary_line: 45 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Devices API from Tailscale — 12 operation(s) for devices.
  name: Tailscale Devices API
  slug: tailscale-devices-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The DNS API from Tailscale — 3 operation(s) for dns.
  name: Tailscale DNS API
  slug: tailscale-dns-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Invites API from Tailscale — 7 operation(s) for invites.
  name: Tailscale Invites API
  slug: tailscale-invites-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Keys API from Tailscale — 2 operation(s) for keys.
  name: Tailscale Keys API
  slug: tailscale-keys-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Logging API from Tailscale — 4 operation(s) for logging.
  name: Tailscale Logging API
  slug: tailscale-logging-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Policy API from Tailscale — 2 operation(s) for policy.
  name: Tailscale Policy API
  slug: tailscale-policy-api
- baseURL: https://api.tailscale.com/api/v2
  baseurl_source: declared
  description: The Tailnet API from Tailscale — 2 operation(s) for tailnet.
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tailscale-capability-edges.yml
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


  Tailscale''s developer surface includes authentication, documentation, pricing, signup flow, GitHub presence, engineering blog, and 7 more developer resources.'
random_paper: 1
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
