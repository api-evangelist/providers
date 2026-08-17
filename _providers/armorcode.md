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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: ArmorCode's REST API for programmatic access to findings, integrations, and remediation workflows across the unified exposure-management platform. Secured with bearer API tokens provisioned from the A
  name: ArmorCode API
  slug: armorcode-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.armorcode.com/
- group: start
  title: ''
  type: Portal
  url: https://app.armorcode.com/
- group: start
  title: ''
  type: Login
  url: https://app.armorcode.com/#/login
- group: company
  title: ''
  type: Blog
  url: https://www.armorcode.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.armorcode.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.armorcode.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.armorcode.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.armorcode.com/
- group: auth
  title: ''
  type: Security
  url: https://www.armorcode.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.armorcode.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/armorcode-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/armorcode-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/armorcode-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/armorcode-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/armorcode-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/armorcode-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/armorcode-llms.txt
created: '2026-07-17'
description: ArmorCode is a unified exposure and application security posture management (ASPM) platform that consolidates vulnerability and security findings from 350+ security tools and scanners into a single control plane. It uses a Context Risk Graph and agentic AI workflows (Anya agents) to prioritize risk and automate remediation across application, cloud, software supply-chain, and AI security. ArmorCode exposes a REST API on app.armorcode.com (US) and eu.armorcode.com (EU) for programmatic access to findings, integrations, and remediation workflows, secured with bearer API tokens. Originally surfaced as a Sierra Ventures portfolio company and enriched here from ArmorCode's public developer and trust surfaces.
image: https://www.armorcode.com/wp-content/uploads/2025/11/ArmorCode_default-thumb_R2_updated-11-11-25.png
layout: provider
modified: '2026-07-18'
name: ArmorCode
nav: Providers
network: true
overview: 'ArmorCode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Application Security, Vulnerability Management, and ASPM.


  ArmorCode''s developer surface includes developer portal, engineering blog, support, authentication, and 13 more developer resources.'
random_paper: 62
score:
  band: emerging
  composite: 27.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 27.7
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/armorcode/refs/heads/main/screenshots/armorcode-2026-07-25T201224.png
security:
- kind: authentication
  name: Armorcode Authentication
  slug: armorcode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Armorcode Domain Security
  slug: armorcode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Armorcode Vulnerability Disclosure
  slug: armorcode-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Armorcode Trust Center
  slug: armorcode-trust-center
  summary_line: SOC 2 Type 2
slug: armorcode
tags:
- Company
- Security
- Application Security
- Vulnerability Management
- ASPM
- Exposure Management
- DevSecOps
- Compliance
- API
website: https://www.armorcode.com/
---
