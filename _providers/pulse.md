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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: 'REST API for managing Ivanti Connect Secure (formerly Pulse Connect Secure) VPN appliances. Provides endpoints for system configuration, user and role management, authentication server configuration, '
  name: Ivanti Connect Secure REST API
  slug: ivanti-connect-secure-rest-api
- description: REST API for managing Ivanti Policy Secure (formerly Pulse Policy Secure) network access control appliances.
  name: Ivanti Policy Secure REST API
  slug: ivanti-policy-secure-rest-api
- description: REST API for managing Ivanti Neurons for Zero Trust Access (nZTA), providing endpoints for managing zero trust access policies, gateways, and user access.
  name: Ivanti Neurons for Zero Trust Access REST API
  slug: ivanti-neurons-zero-trust-rest-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pulse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pulse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ivanti.com/products/connect-secure-vpn
- group: docs
  title: ''
  type: Documentation
  url: https://www.ivanti.com/support/product-documentation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ivanti.com/company/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ivanti.com/company/legal
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ivanticloud.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ivanti.com/blog
- group: operate
  title: ''
  type: Community
  url: https://forums.ivanti.com/s/welcome-pulse-secure?language=en_US
created: '2024-01-15'
description: APIs for Ivanti Pulse Secure (formerly Pulse Secure), providing secure remote access VPN, network access control, and zero trust access solutions.
features:
- description: Secure remote access to corporate resources through SSL VPN tunnels with granular access policies.
  name: SSL VPN Remote Access
- description: Identity-aware, application-level access control without exposing network resources.
  name: Zero Trust Network Access
- description: Enforce security policies on endpoints before granting network access with 802.1X and agent-based checks.
  name: Network Access Control
- description: Integrate with MFA providers for strong authentication on VPN and network access.
  name: Multi-Factor Authentication
- description: Validate endpoint compliance with security policies before granting access.
  name: Host Checker
- description: Define granular access policies based on user roles, device type, and compliance status.
  name: Role-Based Access Control
finops:
- name: Pulse Finops
  service_category: API
  slug: pulse-finops
image: /assets/icons/pulse.png
layout: provider
modified: '2026-04-18'
name: Pulse
nav: Providers
network: true
overview: 'Pulse publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Ivanti, Network Security, Secure Access, SSL VPN, and VPN.


  Pulse''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Pulse Plans Pricing
  plan_count: 3
  slug: pulse-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 5
  name: Pulse Rate Limits
  slug: pulse-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: -0.1
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 19.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pulse/refs/heads/main/screenshots/pulse-2026-06-20T192251.png
security:
- kind: domain-security
  name: Pulse Domain Security
  slug: pulse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pulse Vulnerability Disclosure
  slug: pulse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pulse
tags:
- Ivanti
- Network Security
- Secure Access
- SSL VPN
- VPN
- Zero Trust
use_cases:
- description: Provide secure remote access to corporate applications and resources for distributed teams.
  name: Remote Workforce Access
- description: Implement zero trust security with per-application access controls and continuous verification.
  name: Zero Trust Architecture
- description: Securely enable bring-your-own-device access with endpoint compliance checking.
  name: BYOD Management
- description: Grant controlled, time-limited access to third-party partners and contractors.
  name: Partner and Contractor Access
website: https://www.ivanti.com/products/connect-secure-vpn
---
