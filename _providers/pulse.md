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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-01'
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
artifact_total: 20
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ivanti/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pulse-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pulse-security.txt
- group: auth
  title: ''
  type: Security
  url: security/pulse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pulse-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/pulse-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pulse-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pulse-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pulse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pulse-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/pulse-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pulse-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pulse-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pulse-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pulse-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pulse-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ivanti.com/support/api
- group: docs
  title: ''
  type: APIReference
  url: https://help.ivanti.com/ps/help/en_US/ICS/22.x/apig/rest_api_soln_guide/landingpage.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ivanti.com/ps/help/en_US/ICS/22.x/apig/rest_api_soln_guide/ovw.htm
- group: operate
  title: ''
  type: Support
  url: https://www.ivanti.com/support
- group: build
  title: ''
  type: Postman
  url: https://help.ivanti.com/ps/help/en_US/ICS/22.x/apig/rest_api_soln_guide/ics_postman_apis.htm
- group: start
  title: ''
  type: Login
  url: https://hub.ivanti.com/
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
description: 'Ivanti''s secure-access product family, formerly Pulse Secure, acquired by Ivanti in 2020. Three administrator-facing REST APIs configure and observe it: Ivanti Connect Secure for SSL VPN remote access, Ivanti Policy Secure for 802.1X and RADIUS/TACACS+ network access control, and Ivanti Neurons for Zero Trust Access for per-application ZTNA. Connect Secure and Policy Secure are customer-run appliances whose management API is reached at the customer''s own host; nZTA is a hosted tenant. All three are configuration and management interfaces rather than data-plane APIs — they change who can reach what on a corporate network. Ivanti publishes no OpenAPI and no SDK for any of them; the published contract is prose documentation with worked curl examples plus a customer-portal Postman collection.'
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
modified: '2026-08-29'
name: Pulse
nav: Providers
network: true
overview: 'Pulse publishes 1 API on the [APIs.io](https://apis.io/) network: Ivanti Connect Secure REST API. Tagged areas include Ivanti, Network Security, Secure Access, SSL VPN, and VPN.


  Pulse''s developer surface includes authentication, changelog, API reference, getting-started guide, support, documentation, engineering blog, and 24 more developer resources.'
plans:
- name: Pulse Plans Pricing
  plan_count: 0
  slug: pulse-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Pulse Rate Limits
  slug: pulse-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 37.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pulse/refs/heads/main/screenshots/pulse-2026-06-20T192251.png
security:
- kind: authentication
  name: Pulse Authentication
  slug: pulse-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pulse Domain Security
  slug: pulse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pulse Vulnerability Disclosure
  slug: pulse-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pulse Trust Center
  slug: pulse-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, FedRAMP, U.S. Federal Government Authorization to Operate (ATO), Common Criteria, IRAP, Cyber Essentials, SIG Lite, VPAT 2.4 / Section 508
slug: pulse
tags:
- Ivanti
- Network Security
- Secure Access
- SSL VPN
- VPN
- Zero Trust
- ZTNA
- Network Access Control
- Remote Access
- Identity and Access Management
- Security
- Pulse Secure
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
