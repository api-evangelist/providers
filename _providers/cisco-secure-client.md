---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Cisco Secure Client Agentic Access
  operation_count: 15
  slug: cisco-secure-client-agentic-access
  summary_line: 15 operations · 9 acting
api_count: 11
apis:
- description: The Cisco Secure Firewall Management Center API configures remote-access VPN gateways, group policies, and Secure Client profiles distributed to endpoints. Authentication uses a token generated via th
  name: Cisco Secure Firewall Management Center API
  slug: secure-firewall-management-api
- description: The Cisco Identity Services Engine External RESTful Services (ERS) API manages the network access control plane that Secure Client integrates with for posture assessment and policy enforcement. Endpoi
  name: Cisco ISE ERS API
  slug: ise-ers-api
- description: 'The Cisco Umbrella API exposes the cloud-delivered DNS, secure web gateway, and roaming protection services that integrate with the Secure Client Umbrella module. Authentication uses OAuth 2.0 client '
  name: Cisco Umbrella API
  slug: umbrella-api
- description: The Duo Admin API configures multi-factor authentication policies, users, groups, and integrations used by Secure Client deployments for ZTNA and adaptive authentication. Authentication uses an HMAC s
  name: Cisco Duo Admin API
  slug: duo-admin-api
- description: The Cisco Secure Access API is the management interface for Cisco's converged SSE platform that Secure Client connects to as a SASE endpoint agent. Endpoints cover network tunnels, ZTNA application de
  name: Cisco Secure Access API
  slug: secure-access-api
- description: The AccessPolicies API from Cisco Secure Client — 1 operation(s) for accesspolicies.
  name: Cisco Secure Client AccessPolicies API
  slug: cisco-secure-client-accesspolicies-api
- description: The AccessRules API from Cisco Secure Client — 1 operation(s) for accessrules.
  name: Cisco Secure Client AccessRules API
  slug: cisco-secure-client-accessrules-api
- description: The Authentication API from Cisco Secure Client — 2 operation(s) for authentication.
  name: Cisco Secure Client Authentication API
  slug: cisco-secure-client-authentication-api
- description: The Devices API from Cisco Secure Client — 2 operation(s) for devices.
  name: Cisco Secure Client Devices API
  slug: cisco-secure-client-devices-api
- description: The Hosts API from Cisco Secure Client — 1 operation(s) for hosts.
  name: Cisco Secure Client Hosts API
  slug: cisco-secure-client-hosts-api
- description: The NetworkObjects API from Cisco Secure Client — 1 operation(s) for networkobjects.
  name: Cisco Secure Client NetworkObjects API
  slug: cisco-secure-client-networkobjects-api
artifact_total: 21
collections:
- collection_type: open
  name: Cisco Secure Firewall Management Center API (Secure Client management plane)
  slug: open-cisco-secure-client
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-secure-client-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-secure-client-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-secure-client-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-secure-client-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/anyconnect/feed
- group: docs
  title: ''
  type: Documentation
  url: https://www.cisco.com/c/en/us/support/security/secure-client-5/series.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/secure-client/getting-started/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cisco.com/c/en/us/td/docs/security/vpn_client/anyconnect/Cisco-Secure-Client-5/release/notes/release-notes-cisco-secure-client-5.html
- group: operate
  title: ''
  type: Support
  url: https://www.cisco.com/c/en/us/support/index.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cisco.com/
- group: operate
  title: ''
  type: Community
  url: https://community.cisco.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end-user-license-agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cisco-secure-client-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cisco-secure-client-rules.yml
created: '2024-01-01'
description: Cisco Secure Client (formerly AnyConnect) is the unified endpoint agent for Cisco security and connectivity, delivering VPN, Zero Trust Network Access, endpoint posture, network visibility, and secure web access from a single installer. Programmatic interfaces are exposed indirectly through Cisco Secure Firewall (ASA, FTD), Cisco Identity Services Engine (ISE), Cisco Secure Access, Umbrella, and Duo. There is no single public REST surface for the client itself; integration is achieved through profile XML packages, MDM-deployed configuration, and the management plane APIs exposed by these adjacent Cisco services.
finops:
- name: Cisco Secure Client Finops
  service_category: API
  slug: cisco-secure-client-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-secure-client.png
jsonld:
- class_count: 18
  name: Cisco Secure Client Context
  property_count: 0
  slug: cisco-secure-client-context
layout: provider
modified: '2026-04-23'
name: Cisco Secure Client
nav: Providers
network: true
overview: 'Cisco Secure Client publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AccessPolicies API, AccessRules API, Authentication API, and 3 more. Tagged areas include Endpoint Security, Remote Access, Security, VPN, and Zero Trust.


  The Cisco Secure Client catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cisco Secure Client''s developer surface includes authentication, developer portal, engineering blog, documentation, getting-started guide, changelog, support, and 9 more developer resources.'
plans:
- name: Cisco Secure Client Plans Pricing
  plan_count: 3
  slug: cisco-secure-client-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Cisco Secure Client Rate Limits
  slug: cisco-secure-client-rate-limits
rules:
- name: Cisco Secure Client API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: cisco-secure-client-rules
score:
  band: developing
  composite: 56.1
  delta: 2.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.0
    developer_ergonomics: 45.7
    discoverability: 87.5
    governance: 26.3
    operational_transparency: 63.2
  previous_composite: 54.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-secure-client/refs/heads/main/screenshots/cisco-secure-client-2026-06-20T174400.png
security:
- kind: authentication
  name: Cisco Secure Client Authentication
  slug: cisco-secure-client-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cisco Secure Client Domain Security
  slug: cisco-secure-client-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Secure Client Vulnerability Disclosure
  slug: cisco-secure-client-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cisco-secure-client
tags:
- Endpoint Security
- Remote Access
- Security
- VPN
- Zero Trust
website: https://developer.cisco.com/
---
