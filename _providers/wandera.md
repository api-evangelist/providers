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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 64.4
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Query the risk states of enrolled devices and override device risk classifications. JWT bearer auth (15-minute tokens) obtained from Application ID/Secret via HTTP Basic. Base host https://api.wandera
  name: Wandera RADAR Risk API
  slug: wandera-radar-risk-api
- description: Obtain a bearer JWT from Application ID/Secret.
  name: Wandera Authentication API
  slug: wandera-authentication-api
artifact_total: 8
collections:
- collection_type: postman
  name: RADAR Risk API
  slug: postman-wandera-radar-risk-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wandera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wandera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.jamf.com/jamf-security/docs/risk-api-2
- group: docs
  title: ''
  type: APIReference
  url: https://developer.jamf.com/jamf-security/docs/risk-api-2
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jamf
- group: build
  title: ''
  type: Postman
  url: https://github.com/jamf/RADAR_API_Postman_Collection
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jamf.com/
- group: operate
  title: ''
  type: Support
  url: https://www.jamf.com/support/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/wandera-risk-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wandera-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wandera-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wandera-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wandera-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wandera-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wandera-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.jamf.com/
- group: design
  title: ''
  type: DataModel
  url: data-model/wandera-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wandera-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wandera-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/wandera-risk-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wandera-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/wandera-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wandera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jamf.com/security/vulnerability-disclosure/
- group: auth
  title: ''
  type: TrustCenter
  url: security/wandera-trust-center.yml
created: '2026-07-17'
description: Wandera was a zero-trust mobile security company (backed by Bessemer Venture Partners and Sapphire Ventures) that Jamf acquired in July 2021 for approximately $400M. Its technology is now sold as Jamf Security Cloud (RADAR), providing mobile threat defense, Zero Trust Network Access (ZTNA), and data policy for mobile and desktop fleets. Wandera exposes a REST Risk API on the api.wandera.com host — documented on the Jamf Developer portal — that lets security integrations query the risk state of enrolled devices and override device risk classifications, using a short-lived JWT obtained from an Application ID/Secret pair.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wandera.png
layout: provider
modified: '2026-07-21'
name: Wandera
nav: Providers
network: true
overview: 'Wandera publishes 2 APIs on the [APIs.io](https://apis.io/) network: RADAR Risk API and Authentication API. Tagged areas include Company, Cybersecurity, Mobile Security, Zero Trust, and Mobile Threat Defense.


  Wandera''s developer surface includes documentation, API reference, support, authentication, and 22 more developer resources.'
random_paper: 24
rate_limits:
- limit_count: 0
  name: Wandera Rate Limits
  slug: wandera-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 60.2
    developer_ergonomics: 50.0
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Wandera Authentication
  slug: wandera-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Wandera Domain Security
  slug: wandera-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Wandera Vulnerability Disclosure
  slug: wandera-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Wandera Trust Center
  slug: wandera-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27701, PCI DSS, HIPAA, GDPR, CCPA, CPRA, CSA STAR, Cyber Essentials, EU-US DPF, NIST 800-53 Rev. 5
slug: wandera
tags:
- Company
- Cybersecurity
- Mobile Security
- Zero Trust
- Mobile Threat Defense
- Endpoint Security
- Device Risk
- Jamf
website: https://www.wandera.com/
---
