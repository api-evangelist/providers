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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-09-21'
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
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/security/proemion-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/proemion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.proemion.com/docs/shared/pdf/proemion_vdp_v1.0.pdf
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/security/proemion-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/grpc/proemion-clmapi.proto
  title: ''
  type: Protobuf
  url: grpc/proemion-clmapi.proto
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/packages/proemion-packages.yml
  title: ''
  type: Packages
  url: packages/proemion-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/packages/proemion-packages.yml
  title: ''
  type: SDKs
  url: packages/proemion-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/cli/proemion-cli.yml
  title: ''
  type: CLI
  url: cli/proemion-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/well-known/proemion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/proemion-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/well-known/proemion-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/proemion-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/authentication/proemion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/proemion-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/scopes/proemion-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/proemion-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/conformance/proemion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/proemion-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/conventions/proemion-conventions.yml
  title: ''
  type: Conventions
  url: conventions/proemion-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/lifecycle/proemion-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/proemion-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/llms/proemion-llms.txt
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
random_paper: 15
scopes:
- name: Proemion Scopes
  scope_count: 12
  slug: proemion-scopes
  summary_line: 12 scopes · clientCredentials
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 57.1
    discoverability: 72.2
    operational_transparency: 28.9
  previous_composite: 34.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/proemion/refs/heads/main/screenshots/proemion-2026-09-02T152122.png
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
