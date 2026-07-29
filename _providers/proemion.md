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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Obtain and configure machine data from the DataPlatform, Proemion's API-first telematics cloud. Secured with OAuth2 client credentials (OpenID Connect / Keycloak).
  name: Proemion DataPlatform REST API
  slug: proemion-dataplatform-rest-api
- description: Export machine data from the DataPlatform according to the AEMP (ISO 15143-3) telematics data-exchange standard for mixed-fleet interoperability.
  name: Proemion AEMP API
  slug: proemion-aemp-api
- description: Integrate the CANlink mobile 10000 telematics control unit with other platforms over an HTTPS/WebSocket protobuf API (CLM10000 protocol).
  name: Proemion CANlink mobile 10000 API
  slug: proemion-canlink-mobile-10000-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/proemion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.proemion.com/docs/shared/pdf/proemion_vdp_v1.0.pdf
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proemion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.proemion.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.proemion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.proemion.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.proemion.com/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Proemion
- group: company
  title: ''
  type: Blog
  url: https://www.proemion.com/en/resources/knowledge/blog.html
- group: operate
  title: ''
  type: Support
  url: https://docs.proemion.com/#support
- group: start
  title: ''
  type: Login
  url: https://dataportal.proemion.com/#!/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proemion.com/en/privacy-policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.proemion.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.proemion.com/
- group: other
  title: ''
  type: Protobuf
  url: grpc/proemion-clmapi.proto
- group: build
  title: ''
  type: Packages
  url: packages/proemion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/proemion-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/proemion-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/proemion-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/proemion-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/proemion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/proemion-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/proemion-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/proemion-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/proemion-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/proemion-llms.txt
created: '2026-07-17'
description: Proemion is a telematics provider for off-highway and heavy equipment OEMs, embedding data collection directly into the machine down to the ECU across CAN and Ethernet networks. Its API-first DataPlatform telematics cloud, DataPortal web application, Machine Companion app, ProInsights analytics, and Mixed Fleet Telematics let manufacturers and fleet operators obtain, configure, and analyze machine data. Proemion also ships Telematics Control Units (CAN/Ethernet gateways), CANlink displays, and wired CAN interfaces, and exposes a REST API, an AEMP/ISO 15143-3 standard export, and the CANlink mobile 10000 protobuf device API. It serves construction, agriculture, material handling, municipal services, and ground-support-equipment markets.
image: https://avatars.githubusercontent.com/u/18528816?v=4
layout: provider
modified: '2026-07-20'
name: Proemion
nav: Providers
network: true
overview: 'Proemion publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telematics, IoT, Off-Highway Equipment, and CAN Bus.


  Proemion''s developer surface includes documentation, API reference, engineering blog, support, CLI, authentication, and 20 more developer resources.'
random_paper: 73
scopes:
- name: Proemion Scopes
  scope_count: 12
  slug: proemion-scopes
  summary_line: 12 scopes · clientCredentials
score:
  band: thin
  composite: 31.1
  delta: 1.1
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 30.0
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Proemion Authentication
  slug: proemion-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Proemion Domain Security
  slug: proemion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Proemion Vulnerability Disclosure
  slug: proemion-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: proemion
tags:
- Company
- Telematics
- IoT
- Off-Highway Equipment
- CAN Bus
- Fleet Management
- Machine Data
- OEM
- AEMP
- Construction
- Agriculture
website: https://www.proemion.com
---
