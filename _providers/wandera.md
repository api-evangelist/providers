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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Query the risk states of enrolled devices and override device risk classifications. JWT bearer auth (15-minute tokens) obtained from Application ID/Secret via HTTP Basic. Base host https://api.wandera
  name: Wandera RADAR Risk API
  slug: wandera-radar-risk-api
- description: Obtain a bearer JWT from Application ID/Secret.
  name: Wandera Authentication API
  slug: wandera-authentication-api
artifact_total: 12
collections:
- collection_type: postman
  name: RADAR Risk API
  slug: postman-wandera-radar-risk-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wandera RADAR Risk Authentication API
  slug: open-wandera-authentication-api
- collection_type: open
  name: Wandera RADAR Authentication Risk API
  slug: open-wandera-risk-api
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
mcp_servers:
- description: ''
  name: wandera-mcp.yml
  slug: wandera-mcpyml
modified: '2026-07-21'
name: Wandera
nav: Providers
network: true
overview: 'Wandera publishes 2 APIs on the [APIs.io](https://apis.io/) network: RADAR Risk API and Authentication API. Tagged areas include Company, Cybersecurity, Mobile Security, Zero Trust, and Mobile Threat Defense.


  Wandera''s developer surface includes documentation, API reference, support, authentication, and 22 more developer resources.'
random_paper: 142
rate_limits:
- limit_count: 2
  name: Wandera Rate Limits
  slug: wandera-rate-limits
score:
  band: developing
  composite: 41.2
  delta: -2.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 16.7
    contract_quality: 58.0
    developer_ergonomics: 31.5
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 43.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wandera/refs/heads/main/screenshots/wandera-2026-08-17T082834.png
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
