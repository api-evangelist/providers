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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'RESTful API for remotely configuring and controlling a Corelight Sensor and Fleet Manager. Device-local and account-gated (no public OpenAPI); driven by the official open-source corelight-client CLI. '
  name: Corelight Sensor API
  slug: corelight-sensor-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: http://www.corelight.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/corelight/corelight-client
- group: docs
  title: ''
  type: Documentation
  url: https://corelight.com/support/training
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/corelight
- group: company
  title: ''
  type: Blog
  url: https://corelight.com/blog
- group: operate
  title: ''
  type: Support
  url: https://corelight.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://corelight.com/products/open-ndr
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corelight.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corelight.com/legal/privacy
- group: build
  title: ''
  type: Packages
  url: packages/corelight-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/corelight-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/corelight-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/corelight-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corelight-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/corelight-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://corelight.com/support/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/corelight-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://corelight.com/trust-and-compliance
- group: design
  title: ''
  type: Conformance
  url: conformance/corelight-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corelight-llms.txt
created: '2026-07-17'
description: Corelight is a network detection and response (NDR) company founded by the creators of the open-source Zeek (formerly Bro) network security monitor. Its Open NDR Platform transforms network traffic into high-fidelity security evidence — logs, alerts, and metadata — powering threat detection, hunting, investigation, and incident response across on-premises and cloud environments. Corelight Sensors expose a comprehensive RESTful API for remote configuration and control, driven by the open-source corelight-client command-line client, with a Fleet Manager for centralized fleet management. Backed by Accel and General Catalyst, Corelight is listed on the FedRAMP Marketplace (In Process, Moderate).
image: https://corelight.com/hubfs/images/thumbs/Corelight_LinkShare_Thumbnail_V2.png
layout: provider
modified: '2026-07-18'
name: Corelight
nav: Providers
network: true
overview: 'Corelight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Network Detection and Response, NDR, and Network Security.


  Corelight''s developer surface includes documentation, engineering blog, support, pricing, CLI, authentication, and 14 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 30.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 30.2
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corelight/refs/heads/main/screenshots/corelight-2026-07-25T210426.png
security:
- kind: authentication
  name: Corelight Authentication
  slug: corelight-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Corelight Domain Security
  slug: corelight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Corelight Vulnerability Disclosure
  slug: corelight-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Corelight Trust Center
  slug: corelight-trust-center
  summary_line: FedRAMP, GDPR
slug: corelight
tags:
- Company
- Cybersecurity
- Network Detection and Response
- NDR
- Network Security
- Threat Detection
- Zeek
- Incident Response
- Security
website: http://www.corelight.com
---
